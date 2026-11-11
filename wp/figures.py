#!/usr/bin/env python3
"""Generate the paper's figures from exp/results/summary.json only.
Run: python3 wp/figures.py  ->  wp/figures/fig-bloat.svg, wp/figures/fig-loop.svg
Figure 1: same-fixture hardened sizes (lab COMP-01) + lite added bytes.
Figure 2: the team loop (five roles, three stop conditions)."""
import json, math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
S = json.loads((ROOT / "exp" / "results" / "summary.json").read_text())
OUT = ROOT / "wp" / "figures"; OUT.mkdir(parents=True, exist_ok=True)
C = S["virtual_test_lab_v2"]["evidence"]["COMP-01"]
GREEN, INK, MUT = "#047C3D", "#111827", "#6B7280"

def fig_bloat():
    pairs = [("GGUF (1,328 B fixture)", C["spec.gguf"]["upstream_hardened_bytes"], C["spec.gguf"]["thoxshield_hardened_bytes"]),
             ("WASM (36 B fixture)", C["core.wasm"]["upstream_hardened_bytes"], C["core.wasm"]["thoxshield_hardened_bytes"])]
    W, H = 680, 300; x0, x1 = 150, 640; top = 30; rowh = 52
    def X(v): return x0 + (math.log10(max(v, 1)) / 7.0) * (x1 - x0)
    el = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="Inter,sans-serif">']
    el.append(f'<text x="0" y="16" font-size="12" font-weight="700" fill="{INK}">Hardened size, same fixtures (log scale)</text>')
    for g in range(0, 8):
        gx = x0 + (g / 7.0) * (x1 - x0)
        el.append(f'<line x1="{gx:.0f}" y1="{top}" x2="{gx:.0f}" y2="{top + 2 * rowh + 30}" stroke="#E5E7EB"/><text x="{gx:.0f}" y="{top + 2 * rowh + 44}" font-size="8" fill="{MUT}" text-anchor="middle">10^{g}</text>')
    y = top
    for label, up, lite in pairs:
        el.append(f'<text x="0" y="{y + 12}" font-size="10" fill="{INK}">{label}</text>')
        if X(up) > 470:
            el.append(f'<rect x="{x0}" y="{y}" width="{X(up) - x0:.0f}" height="13" fill="{INK}"/><text x="{X(up) - 5:.0f}" y="{y + 11}" font-size="9" fill="#FFFFFF" text-anchor="end">upstream bankrupt {up:,} B</text>')
        else:
            el.append(f'<rect x="{x0}" y="{y}" width="{X(up) - x0:.0f}" height="13" fill="{INK}"/><text x="{X(up) + 5:.0f}" y="{y + 11}" font-size="9" fill="{INK}">upstream bankrupt {up:,} B</text>')
        el.append(f'<rect x="{x0}" y="{y + 18}" width="{X(lite) - x0:.0f}" height="13" fill="{GREEN}"/><text x="{X(lite) + 5:.0f}" y="{y + 29}" font-size="9" fill="{GREEN}">ThoxShield lite {lite:,} B</text>')
        y += rowh
    prod = S["virtual_test_lab_v2"]["evidence"]["REAL-prod"]
    el.append(f'<text x="0" y="{y + 16}" font-size="10" fill="{INK}">Production GGUF (397,808,032 B, 290 tensors): lite adds +{prod["added_bytes"]} B — a bar at this scale would be invisible; that is the point.</text>')
    el.append("</svg>")
    (OUT / "fig-bloat.svg").write_text("".join(el))

def fig_loop():
    roles = [("coordinator", "workorder + state"), ("auditor", "audit + lint gate"),
             ("hardener", "harden from originals"), ("verifier", "independent verify"),
             ("reporter", "report + receipts")]
    W, H = 680, 170; bw, bh, gap, x0, y0 = 118, 56, 14, 6, 26
    el = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="Inter,sans-serif">']
    el.append(f'<text x="0" y="16" font-size="12" font-weight="700" fill="{INK}">The team loop: five roles, producer &#8800; verifier</text>')
    for i, (r, sub) in enumerate(roles):
        x = x0 + i * (bw + gap)
        fill = "#E6F4EC" if r in ("verifier",) else "#FFFFFF"
        el.append(f'<rect x="{x}" y="{y0}" width="{bw}" height="{bh}" rx="5" fill="{fill}" stroke="{GREEN if r=="verifier" else INK}"/>')
        el.append(f'<text x="{x + bw/2}" y="{y0 + 24}" font-size="11" font-weight="700" fill="{INK}" text-anchor="middle">{r}</text>')
        el.append(f'<text x="{x + bw/2}" y="{y0 + 42}" font-size="8" fill="{MUT}" text-anchor="middle">{sub}</text>')
        if i < 4:
            el.append(f'<text x="{x + bw + 2}" y="{y0 + 34}" font-size="13" fill="{MUT}">&#8594;</text>')
    el.append(f'<path d="M {x0 + 4 * (bw + gap) + bw/2} {y0 + bh} V {y0 + bh + 26} H {x0 + bw/2} V {y0 + bh + 4}" fill="none" stroke="{MUT}" stroke-dasharray="3 3"/>')
    el.append(f'<text x="{W/2}" y="{y0 + bh + 44}" font-size="9" fill="{MUT}" text-anchor="middle">iterate until: all artifacts verified &#183; a blocking lint finding stops the release &#183; iteration budget exhausted (reported as failure)</text>')
    el.append("</svg>")
    (OUT / "fig-loop.svg").write_text("".join(el))

if __name__ == "__main__":
    fig_bloat(); fig_loop(); print("figures written to", OUT)
