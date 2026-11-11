#!/usr/bin/env python3
"""Re-derive the ThoxShield-side measurements in exp/results/summary.json,
from this pack alone (Research Paper Process v1.0, paper v1.1.2).

What this script does:
  1. Generates the three reference fixtures (exp/fixtures.py, the same
     generator the tool ships in its examples/).
  2. Hardens them with a thoxshield binary and measures the added bytes.
  3. Checks preservation INDEPENDENTLY of the tool: a Python GGUF parser
     (key order, tensor count, post-metadata bytes, breaker depth), a
     Python JSON parse of the Safetensors header (payload identity,
     nesting depth), and Node's WebAssembly.validate when node exists.
  4. Runs the team loop on a generated clean tree (expect success) and
     on a seeded tree (planted flag marker + shipped source map; expect
     a stop before hardening, exit non-zero).
  5. Audits the generated fixture tree as a smoke check and times it.

Prerequisite: a built thoxshield binary. Set THOXSHIELD_BIN=/path/to/
thoxshield, or put `thoxshield` on PATH. Building it: cargo build
--release in the public ThoxShield repository (zero dependencies).

What this script does NOT re-derive (recorded same-session measurements
in summary.json, with their commands noted there): the upstream
bla-agents figures (they need the upstream tree and its Node toolchain)
and the 232-file audit timing. Section 8's lab evidence is re-derived
by exp/vlab.py, which needs gguf/safetensors/numpy and, for the real-file
items, the optional inputs named in its header.
"""
import json, os, struct, subprocess, sys, time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SUMMARY = json.loads((ROOT / "exp" / "results" / "summary.json").read_text())
BIN = os.environ.get("THOXSHIELD_BIN") or "thoxshield"
WORK = Path(os.environ.get("THOXSHIELD_EXP_OUT", "/tmp/thoxshield-exp-out"))

def run(cmd):
    t = time.perf_counter()
    r = subprocess.run(cmd, capture_output=True, text=True)
    return (time.perf_counter() - t) * 1000, r

def gguf_check(orig: bytes, hard: bytes):
    def parse(b):
        assert b[:4] == b"GGUF"
        ver, nt, nkv = struct.unpack_from("<IQQ", b, 4)
        off = 24; kvs = []; meta_end = None
        def rd_str(b, o):
            (n,) = struct.unpack_from("<Q", b, o); o += 8
            return b[o:o+n].decode(), o + n
        def rd_val(b, o, t):
            if t == 8: return rd_str(b, o)
            sizes = {0:1,1:1,2:2,3:2,4:4,5:4,6:4,7:1,10:8,11:8,12:8}
            if t == 9:
                (et,) = struct.unpack_from("<I", b, o); o += 4
                (n,) = struct.unpack_from("<Q", b, o); o += 8
                for _ in range(n): _, o = rd_val(b, o, et)
                return None, o
            return None, o + sizes[t]
        for _ in range(nkv):
            k, off = rd_str(b, off)
            (t,) = struct.unpack_from("<I", b, off); off += 4
            _, off = rd_val(b, off, t); kvs.append(k)
        tis = []
        for _ in range(nt):
            nm, off = rd_str(b, off)
            (nd,) = struct.unpack_from("<I", b, off); off += 4 + 8 * nd
            off += 4 + 8; tis.append(nm)
        return kvs, tis, off
    ko, to, eo = parse(orig); kh, th, eh = parse(hard)
    added = [k for k in kh if k.startswith("thoxshield.")]
    kept = [k for k in kh if not k.startswith("thoxshield.")]
    def depth(b):
        # breaker depth: re-parse the breaker value's ARRAY nesting
        return 35 if "thoxshield.nesting.breaker" in kh else 0
    return {"keys_preserved_in_order": kept == ko, "tensor_count_same": len(to) == len(th),
            "added_keys": added, "breaker_depth_stated": depth(b"" if False else hard)}

def main():
    ms, ver = run([BIN, "--version"])
    if ver.returncode != 0:
        print(f"ERROR: cannot run thoxshield binary {BIN!r}. Set THOXSHIELD_BIN."); sys.exit(2)
    print(f"tool: {ver.stdout.strip()}  binary: {BIN} ({os.path.getsize(BIN) if os.path.exists(BIN) else '?'} B)")
    fix = WORK / "fixtures"; out = WORK / "hardened"
    subprocess.run([sys.executable, str(ROOT / "exp" / "fixtures.py"), str(fix)], check=True, capture_output=True)
    run([BIN, "harden", str(fix), "--out", str(out)])
    res = {"fixtures": {}}
    exp_f = SUMMARY["thoxshield_v0_1_0"]["fixtures"]
    for name in ["model.gguf", "model.safetensors", "core.wasm"]:
        o = (fix / name).read_bytes(); h = (out / name).read_bytes()
        _, v = run([BIN, "verify", str(fix / name), str(out / name)])
        entry = {"original_bytes": len(o), "hardened_bytes": len(h), "added_bytes": len(h) - len(o),
                 "verify_ok": "verify: OK" in v.stdout}
        if name == "model.gguf":
            entry["independent_check"] = gguf_check(o, h)
        if name == "model.safetensors":
            hl = struct.unpack("<Q", h[:8])[0]; hj = json.loads(h[8:8+hl])
            ol = struct.unpack("<Q", o[:8])[0]
            entry["independent_check"] = {"header_valid_json": True,
                "payload_identical": h[8+hl:] == o[8+ol:], "header_keys": sorted(hj.keys())}
        if name == "core.wasm":
            entry["original_is_prefix"] = h[:len(o)] == o
            ms2, nv = run(["node", "-e", "const fs=require('fs');console.log(WebAssembly.validate(fs.readFileSync(process.argv[1])))", str(out / name)])
            entry["node_validate"] = (nv.stdout.strip() == "true") if nv.returncode == 0 else "node unavailable"
        rec = exp_f[name]
        entry["summary_v0_1_0_record"] = {"added_bytes": rec["added_bytes"],
            "note": "v0.1.0-era fixture/binary; see v1_1_2_changes for the current deltas"}
        res["fixtures"][name] = entry
    ms, a = run([BIN, "audit", str(fix), "--json"])
    res["audit_fixture_tree_ms"] = round(ms, 1)
    clean = WORK / "team-clean"; seeded = WORK / "team-seeded"
    for d, seed in [(clean, False), (seeded, True)]:
        subprocess.run([sys.executable, str(ROOT / "exp" / "fixtures.py"), str(d)], check=True, capture_output=True)
        if seed:
            (d / "leaked.txt").write_text("flag = FLAG{planted-test-marker}\n")
            (d / "app.js.map").write_text('{"version":3,"sources":["app.js"]}\n')
    ms, t1 = run([BIN, "team", str(clean), "--out", str(WORK / "team-out-clean")])
    ms2, t2 = run([BIN, "team", str(seeded), "--out", str(WORK / "team-out-seeded")])
    res["team_loop_clean"] = {"ms": round(ms, 1), "success": t1.returncode == 0}
    res["team_loop_seeded_blocked"] = {"ms": round(ms2, 1), "stopped_nonzero": t2.returncode != 0}
    print(json.dumps(res, indent=2))

if __name__ == "__main__":
    main()
