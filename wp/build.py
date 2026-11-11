#!/usr/bin/env python3
"""Build the ThoxShield paper v1.1.2 (paper.src.html -> paper.html -> PDF).

Design: THOX Research Paper Template v1.0, built FROM the canonical
template files (THOX_Research_Paper_Template_v1.0)
— the stylesheet below is that template's own 5,160-char CSS, verbatim
(the /*__FONTS__*/ and /*__KATEX__*/ build slots are dropped: this paper
has no KaTeX content and fonts resolve to locally installed Inter /
JetBrains Mono). Every number comes from exp/results/summary.json (S).

Run: python3 wp/build.py   (writes wp/paper.src.html, dist/*.html, dist/*.pdf)
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
S = json.loads((ROOT / "exp" / "results" / "summary.json").read_text())
U = S["upstream_bla_agents_v3_2_4"]
T = S["thoxshield_v0_1_0"]
V12 = S["thoxshield_v0_1_2"]
F = T["fixtures"]
B = U["harden_bloat_measured"]
LAB = S["virtual_test_lab_v2"]["evidence"]
VERSION = "v1.1.2"
DATE = "2026-11-10"

def x(n): return f"{n:,}"

CSS = r""":root{--green:#047C3D;--green-dark:#05A451;--ink:#111827;--muted:#6B7280;--rule:#E5E7EB;--pale:#E6F4EC;--bg:#FFFFFF}
*{box-sizing:border-box}
html,body{margin:0;padding:0;background:var(--bg);color:var(--ink);font-family:Inter,system-ui,sans-serif;font-size:10.5pt;line-height:1.5}
.cover{background:#0B0F14;color:#F3F4F6;min-height:100vh;padding:0}
.cover-inner{max-width:7.1in;margin:0 auto;padding:0.9in 0.6in 0.6in}
.eyebrow{display:flex;justify-content:space-between;align-items:center;font-family:'JetBrains Mono',monospace;font-size:8pt;color:#9CA3AF;border-bottom:1px solid #1F2937;padding-bottom:8px}
.pill{border:1px solid var(--green-dark);color:var(--green-dark);border-radius:999px;padding:2px 10px}
.cover h1{font-size:21pt;line-height:1.2;font-weight:700;margin:22px 0 10px;color:#fff}
.deck{font-size:11pt;color:#D1D5DB;margin:0 0 10px}
.byline{font-size:8.5pt;color:#9CA3AF;margin:0 0 16px}
.abstract{border-left:3px solid var(--green-dark);padding:4px 0 4px 12px;margin:10px 0 14px}
.abstract p{font-size:9.2pt;line-height:1.45;color:#E5E7EB;margin:4px 0 0}
.ct{font-family:'JetBrains Mono',monospace;font-size:8pt;letter-spacing:.08em;text-transform:uppercase;color:var(--green-dark)}
.contents ol{columns:2;column-gap:28px;font-size:8.6pt;margin:6px 0 0;padding-left:0;list-style:none;color:#D1D5DB}
.contents a{color:#D1D5DB;text-decoration:none}
.cover-foot{margin-top:18px;font-size:8pt;color:#6B7280;border-top:1px solid #1F2937;padding-top:8px}
.paper-body{max-width:7.1in;margin:0 auto;padding:0.5in 0.6in 0.8in}
@media screen{.paper-body{padding-top:0.6in}}
h2{font-size:14pt;font-weight:700;margin:26px 0 8px;padding-bottom:4px;border-bottom:2px solid var(--green);break-after:avoid}
h2 .num{color:var(--green);margin-right:10px;font-family:'JetBrains Mono',monospace;font-size:11pt}
h3{font-size:11pt;font-weight:600;margin:16px 0 6px;break-after:avoid}
p{margin:0 0 8px;text-align:left}
.cite{color:var(--green);font-size:9pt}
table{width:100%;border-collapse:collapse;font-size:8.4pt;margin:8px 0 12px;break-inside:auto}
caption{caption-side:bottom;text-align:left;font-size:8.2pt;color:var(--muted);padding-top:5px}
th{background:var(--ink);color:#fff;text-align:left;padding:5px 6px;font-weight:600;font-size:8pt}
td{padding:4px 6px;border-bottom:1px solid var(--rule);vertical-align:top}
tr{break-inside:avoid}
figure{margin:12px 0 14px;break-inside:avoid}
.figwrap svg{width:100%;height:auto}
figcaption{font-size:8.4pt;color:var(--muted);margin-top:4px}
.eq{margin:6px 0 8px;text-align:center;font-size:10pt;overflow-x:auto}
.callout{border-left:3px solid var(--green);background:var(--pale);padding:8px 12px;margin:10px 0 12px;font-size:9.5pt;break-inside:avoid}
.callout .ct{margin-bottom:3px}
.kpis{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin:10px 0 12px}
.kpi{border:1px solid var(--rule);border-top:3px solid var(--green);padding:8px 9px;break-inside:avoid}
.kv{font-family:'JetBrains Mono',monospace;font-size:17pt;font-weight:700;color:var(--green);line-height:1.1}
.kl{font-size:8pt;color:var(--ink);margin-top:4px;line-height:1.3}
.kt{font-family:'JetBrains Mono',monospace;font-size:7pt;color:var(--muted);text-transform:uppercase;margin-top:5px;letter-spacing:.06em}
.algo{border:1px solid var(--rule);margin:8px 0 12px;break-inside:avoid}
.algo .at{background:var(--ink);color:#fff;font-size:8.4pt;font-weight:600;padding:4px 8px}
.algo pre,pre.small{font-family:'JetBrains Mono',monospace;font-size:7.8pt;line-height:1.4;margin:0;padding:8px;white-space:pre-wrap;overflow-x:auto}
pre.small{border:1px solid var(--rule)}
code{font-family:'JetBrains Mono',monospace;font-size:8pt;word-break:break-all}
ol,ul{margin:0 0 8px;padding-left:20px}
li{margin:0 0 4px}
.arch{border:1px solid var(--rule);padding:10px;margin:8px 0 2px;font-size:7.8pt;break-inside:avoid}
.arch-row{display:grid;gap:8px;margin:0}
.arch-row.three{grid-template-columns:1fr 1.3fr 1fr}.arch-row.four{grid-template-columns:repeat(4,1fr)}.arch-row.two{grid-template-columns:1fr 1fr}
.arch-arrow{text-align:center;color:var(--muted);font-family:'JetBrains Mono',monospace;font-size:7pt;padding:4px 0}
.box{border:1px solid var(--ink);border-radius:4px;padding:6px 8px;background:#fff}
.box b{display:block;font-size:8.2pt;margin-bottom:2px}.box span{color:#374151}
.box.hi{background:var(--pale);border-color:var(--green)}.box.ghost{background:#F3F4F6;border-color:#9CA3AF}.box.dim{border-style:dashed}
.refs{font-size:8.3pt;padding-left:0;list-style:none}
.refs li{margin:0 0 5px;padding-left:28px;text-indent:-28px}
.refs .rn{font-family:'JetBrains Mono',monospace;color:var(--green);margin-right:4px}
.refs a{color:var(--green);word-break:break-all;text-decoration:none}
@media print{.cover{min-height:11in;height:11in}h2{page-break-after:avoid}}
@media (max-width:600px){.paper-body,.cover-inner{padding:24px 16px}.cover h1{font-size:17pt}.kpis{grid-template-columns:1fr 1fr}.arch-row.three,.arch-row.four,.arch-row.two{grid-template-columns:1fr}.contents ol{columns:1}table{display:block;overflow-x:auto;white-space:normal}.eq{font-size:8.5pt}pre{font-size:7pt}.refs a{word-break:break-all}}
"""

PRINT_CSS = """
@page { size: A4; margin: 20mm 16mm 18mm 16mm;
  @bottom-left { content: "Your AI. Your Data. Your Rules.\\2122"; font-family: 'JetBrains Mono', monospace; font-size: 7.5pt; color: #6B7280; }
  @bottom-right { content: counter(page) " / " counter(pages); font-family: 'JetBrains Mono', monospace; font-size: 7.5pt; color: #6B7280; }
  @top-left { content: "ThoxShield: bloat-capped counter-REA defense"; font-size: 7.5pt; color: #6B7280; }
  @top-right { content: "THOX.ai Research \\00B7 preprint, not peer reviewed"; font-size: 7.5pt; color: #6B7280; } }
@page :first { margin: 12mm 16mm 10mm 16mm; @top-left { content: none; } @top-right { content: none; } }
@media print { .cover { min-height: 10.75in; height: auto; page-break-after: always; }
  .cover-inner { padding: 0.3in 0.6in 0.25in; }
  .cover h1 { font-size: 20pt; margin: 14px 0 8px; }
  .deck { margin: 0 0 8px; } .byline { margin: 0 0 10px; }
  .abstract { margin: 8px 0 10px; } .abstract p { font-size: 8.6pt; line-height: 1.4; }
  .contents ol { font-size: 8.2pt; } .contents li { margin: 0 0 2px; }
  .cover-foot { margin-top: 12px; } }
"""

OUT: list[str] = []
def raw(s): OUT.append(s)
def p(t): OUT.append(f"<p>{t}</p>")
def h2(num, text, anchor):
    n = f'<span class="num">{num}</span>' if num else ""
    OUT.append(f'<h2 id="{anchor}">{n}{text}</h2>')
def h3(t): OUT.append(f"<h3>{t}</h3>")
def kpi(kv, kl, kt="measured"):
    return f'<div class="kpi"><div class="kv">{kv}</div><div class="kl">{kl}</div><div class="kt">{kt}</div></div>'
def figure(svg_path, num, caption):
    svg = (ROOT / svg_path).read_text()
    OUT.append(f'<figure><div class="figwrap">{svg}</div><figcaption>Figure {num}. {caption}</figcaption></figure>')
def callout(title, body):
    OUT.append(f'<div class="callout"><div class="ct">{title}</div>{body}</div>')

TITLE = "ThoxShield: Bloat-Capped Counter-REA Defense for Local-First AI Artifacts"
DEK = ("A zero-dependency Rust tool and an agent-team loop harness that give independent developers and "
       "local-first AI products the highest-value protections against autonomous reverse-engineering "
       "agents — canary attribution, metadata-nesting breakers, and origin binding — at hundreds of bytes "
       "per artifact instead of megabytes, with every claim in this paper tied to a measurement.")
BYLINE = ("THOX.ai Research &middot; Authors: Craig Ross, Chief Executive Officer, and Tommy Xaypanya, "
          "CTO and Co-Founder (corresponding author), THOX.ai LLC &middot; ORCID iD: 0009-0000-4425-9565 (Xaypanya)")

ABSTRACT = f"""Autonomous reverse-engineering agents (REAs) — LLM-driven pipelines that unpack, index, and summarize shipped artifacts — have collapsed the cost of cloning unprotected software: a model file, a WebAssembly module, or an application bundle can be inventoried and reconstructed for cents. Counter-REA tools answer by poisoning, exhausting, and entangling artifacts, but their strongest settings exact a heavy toll on the defender: in our measurements, a current open-source counter-REA tool at its default intensity grows a 93-byte JavaScript fixture to {x(B['javascript']['hardened_bytes'])} bytes (1,440&times;) and an 8-byte WebAssembly fixture to {x(B['wasm']['hardened_bytes'])} bytes. For local-first products — applications and models that ship to user devices, where download size, storage, and update cost are user-facing — that toll is often unacceptable. We present ThoxShield, a bloat-capped subset of counter-REA defense implemented as a single zero-dependency Rust binary ({x(V12['binary_bytes'])} bytes). ThoxShield keeps the mechanisms whose analyzer cost is high and whose byte cost is low — self-identifying canary metadata, metadata-nesting breakers aimed at REA&rsquo;s published analyzer budgets, and a SHA-256 origin binding — and refuses, by construction, to add more than a configurable cap (default: the larger of 4 KiB or 5%) to any artifact. On reference fixtures it adds 736 bytes to a GGUF model, 578&ndash;619 bytes to a Safetensors model (fixture-dependent), and {F['core.wasm']['added_bytes']} bytes to a WASM module; and in an independent virtual test lab (Section 8) a production 380 MB GGUF with 290 tensors grew by 736 bytes and re-loaded in the reference GGUF reader with every tensor byte stream identical. Because modern releases are produced by teams of agents, ThoxShield also ships a lightweight loop harness in which five generic roles — coordinator, auditor, hardener, verifier, reporter — run the defense as an auditable loop with a hard separation between producing a shield and verifying it. One disclosure belongs next to every effectiveness statement in this paper, so we make it here as well: the lite shields have not yet been run against a live REA pipeline; the analyzer-budget evidence behind them is upstream-empirical (BLA, against REA) and, in our own lab, simulated and labeled as such. We release ThoxShield as open source under the MIT License so that the community whose software is exposed to REAs can apply the same protections, and we close with the limits of the approach, stated plainly."""

SECTIONS = [
    ("1", "Introduction", "intro"),
    ("2", "Background: the counter-REA mechanism set", "background"),
    ("3", "Threat model", "threat-model"),
    ("4", "The bloat problem, measured", "bloat"),
    ("5", "Design: defense under a byte budget", "design"),
    ("6", "The agent-team loop harness", "loop"),
    ("7", "Evaluation", "evaluation"),
    ("8", "Independent validation: the virtual test lab", "lab"),
    ("9", "What ThoxShield deliberately does not do", "exclusions"),
    ("10", "Limitations and future work", "limitations"),
    ("11", "Conclusion", "conclusion"),
    ("", "References", "references"),
    ("", "Artifact availability", "artifacts"),
]

def build_cover():
    items = "".join(
        f'<li><a href="#{a}">{(n + ". ") if n else ""}{t}</a></li>' for n, t, a in SECTIONS)
    return f"""<section class="cover">
  <div class="cover-inner">
    <div class="eyebrow"><span>THOX.ai Research &middot; Technical report {VERSION} &middot; {DATE}</span><span class="pill">Preprint, not peer reviewed</span></div>
    <h1>{TITLE}</h1>
    <p class="deck">{DEK}</p>
    <p class="byline">{BYLINE}</p>
    <div class="abstract"><div class="ct">Abstract</div><p>{ABSTRACT}</p></div>
    <div class="contents"><div class="ct">Contents</div><ol>{items}</ol></div>
    <div class="cover-foot">Your AI. Your Data. Your Rules.&trade; &middot; THOX&reg;, ThoxOS&trade;, MeshStack&trade; and ThoxWork&trade; are marks of THOX.ai LLC.</div>
  </div>
</section>"""

def body():
    raw('<div class="kpis">' +
        kpi("+736 B", "growth on a production 380 MB GGUF, 290 tensors, reader-verified") +
        kpi("+303 B", "bytes added to a WASM module (31 B fixture)") +
        kpi("0", "external dependencies in the shipped binary") +
        kpi("10.1 ms", "team loop to verified shields on the fixture tree (one loop)") +
        "</div>")

    h2("1", "Introduction", "intro")
    p("Local-first AI changes who ships valuable artifacts. Models, inference components, and application logic that once stayed on a server now sit on user devices, in public model repositories, and inside downloadable applications — exactly where an autonomous reverse-engineering agent can read them at machine speed. The defensive question is no longer whether an artifact <em>can</em> be inspected; it is what the inspection costs the inspector, and what raising that cost costs the defender.")
    p(f"Counter-REA research, most completely the open-source BLA project (Blind LLM Agents), answers with three mechanism families: <em>poison</em> (decoys and canaries that mislead summarization), <em>exhaust</em> (payloads that trip analyzer resource limits), and <em>entangle</em> (integrity bindings that punish stripping). BLA is a substantial system: {x(U['source_loc_typescript'])} lines of TypeScript with a {x(U['test_loc'])}-line test suite ({U['test_result']['passed']} tests passing in our run), a CLI and MCP server, and format shields for more than nineteen artifact types. We adopt its framing and credit it throughout; our contribution is different in kind: a measurement of what its strongest settings cost the defender, a re-implementation of its highest-value-per-byte mechanisms under an explicit byte budget, and a team-loop operating model for running those mechanisms in an agent-built release pipeline.")
    p("We claim exactly three things, and no more. (i) <em>Defender-side bloat as a hard, measured design constraint for model artifacts.</em> Scoring obfuscating transformations on a cost axis is 1997 prior art (Collberg, Thomborson and Low [7]); what is new here is applying an enforced byte cap to model-artifact metadata shields and measuring under it. (ii) <em>Producer &ne; verifier separation applied to release shielding</em>: agent loop harnesses are established practice [12], and obfuscation mechanisms are classified prior art [7][9]; the contribution is the application and the verification discipline, not the loop or the mechanisms. (iii) <em>Claims discipline on modeled multipliers</em>, stated as method in Section 4. That obfuscation already blunts LLM decompilers is demonstrated prior art [10], not a finding of this paper.")

    h2("2", "Background: the counter-REA mechanism set", "background")
    p("Three results published by BLA anchor the design; we attribute them inline because all three come from that one source, not from field consensus. First, the analyzer BLA targets — REA, an open-source MCP server and CLI [2] — enforces hard resource budgets that BLA names directly: <code>MODEL_JSON_NESTING</code> (Safetensors JSON nesting beyond 32 levels) and <code>MODEL_METADATA_NESTING</code> (GGUF metadata nesting beyond 32 array frames). These are REA&rsquo;s analyzer budgets, published by BLA, not properties of the formats and not an industry norm: the GGUF specification [4] defines no nesting limit, and the Safetensors format&rsquo;s documented anti-DoS limit is a 100 MB header cap, with <code>__metadata__</code> restricted to string-to-string values [5]. In BLA&rsquo;s empirical table, an artifact that crosses one of REA&rsquo;s budgets is downgraded from complete to limited examination or rejected outright. Second, the model-format trips are byte-cheap: in BLA&rsquo;s own empirical table, a GGUF file grows from 24 bytes to about 7.7 KB and a Safetensors file from 128 bytes to about 10.1 KB to trip their respective limits. Third, the exhaustion mechanisms for code artifacts are byte-expensive by design — BLA&rsquo;s stated rationale is that they work by flooding the analyzer&rsquo;s context, and the flood is stored in the artifact. A bloat-capped tool is therefore not a weaker version of the same tool; it is a selection of the mechanisms on the cheap side of that asymmetry.")
    p("The analyzer class is real and capable within limits, and the threat model in this paper is anchored to those published capability results rather than to REA alone: GPT-4 is proficient at understanding and explaining decompiled code, though weaker at detailed security analysis [11]; and in the LLM4Decompile study, both the LLM approach and Ghidra failed to effectively decompile obfuscated code [10]. REA [2] remains the one concrete, verified analyzer our breakers are designed against.")

    h2("3", "Threat model", "threat-model")
    p("<strong>Protected assets.</strong> The assets are the artifacts a local-first vendor ships — model files (GGUF, Safetensors), WebAssembly components, and application bundles — the development investment they embody, and the integrity of the release record (manifests and receipts) that describes them. The artifacts themselves sit on user devices and in public repositories, readable by anyone with the file; the confidentiality of their contents is not an asset this paper claims to protect.")
    p("<strong>Adversary class A: the budget-limited automated REA.</strong> An LLM-driven pipeline [2] that unpacks, indexes, and summarizes artifacts at machine speed and at scale, enforcing published resource budgets (32 nesting levels for GGUF metadata and Safetensors JSON, per BLA&rsquo;s empirical work). Its goal is a complete inventory and reconstruction of many artifacts at minimal cost per artifact. This is the adversary the lite shields are designed to tax: the nesting breakers trip its budgets, and the canaries pollute its summaries with self-identifying markers.")
    p("<strong>Adversary class B: the stripper-aware analyst.</strong> An analyst (human-guided or agent-guided) who knows the shields are present and works from the format specifications. Section 8 measures this adversary directly: a roughly 60-line spec-only stripper recovers the originals in under a millisecond. Against class B the shields provide no resistance; what survives is attribution, if the canaries are left in place, and the origin binding — which, stated plainly, also serves this adversary as a recovery oracle and a provenance fingerprint (Section 8).")
    p("<strong>Adversary class C: the determined human.</strong> An interactive analyst with time and tooling. Theory and survey evidence cap what any client-side shield can do here: virtual-black-box obfuscation is impossible in general [8], and interactive analysis defeats many obfuscations [9]. No claim in this paper is made against class C.")
    p("<strong>Defender assumptions.</strong> The defender owns the artifacts being shielded (ThoxShield&rsquo;s policy is own-artifacts-only); shields are applied before release, inside the release pipeline; verification is performed by a process independent of the one that produced the shield (Section 6); and the analyzer budgets the breakers target are as published by BLA&rsquo;s empirical work against REA — if those budgets change, the breakers&rsquo; visible +3 margin (Section 10) is the first thing to re-check.")
    p("<strong>Out of scope.</strong> Secrecy of artifact contents; tamper resistance; runtime adversaries on the device (including debugger deception, excluded by policy in Section 9); prompt-injection layers aimed at the analyzing agent (excluded in Section 9); and the protection of real secrets, which belong on trusted infrastructure, not inside shipped artifacts (Section 10).")

    h2("4", "The bloat problem, measured", "bloat")
    p(f"We built the upstream tool from source (Node v24.22.1), ran its full test suite (121 files, {U['test_result']['passed']} passed, {U['test_result']['skipped']} skipped, {U['test_result']['duration_s']} s), and hardened a fixture directory at its default <em>bankrupt</em> intensity. Table 1 records the growth. We also record a claims-discipline finding: the tool&rsquo;s showcase benchmark reports aggregate token amplification of {U['benchmark_aggregate_token_amplification']['readme_claim']}&times; in its README and {U['benchmark_aggregate_token_amplification']['state_md_claim']}&times; in its state document, and printed {U['benchmark_aggregate_token_amplification']['this_run']}&times; in our run. These are modeled estimates from a token estimator, not measurements of an analyzer process — BLA itself labels them &ldquo;modeled,&rdquo; under a README benchmark section headed &ldquo;Internal Estimates&rdquo; — and their disagreement across versions is precisely why this paper reports no amplification figure as a result. We also state a gap our literature survey found rather than papering over it: no independent, non-BLA measurement of agent cost amplification against model artifacts was found; the only figures in this space are BLA&rsquo;s, split as above into an empirical REA-outcome table and modeled estimates.")
    rows = "".join([
        f"<tr><td>JavaScript</td><td>{B['javascript']['original_bytes']} B</td><td>{x(B['javascript']['hardened_bytes'])} B</td><td>1,440&times;</td></tr>",
        f"<tr><td>Python</td><td>{B['python']['original_bytes']} B</td><td>{x(B['python']['hardened_bytes'])} B</td><td>904&times;</td></tr>",
        f"<tr><td>GGUF model</td><td>{B['gguf']['original_bytes']} B</td><td>{x(B['gguf']['hardened_bytes'])} B</td><td>73&times;</td></tr>",
        f"<tr><td>WebAssembly</td><td>{B['wasm']['original_bytes']} B</td><td>{x(B['wasm']['hardened_bytes'])} B</td><td>484,146&times;</td></tr>"])
    raw(f"<table><tr><th>Fixture</th><th>Original</th><th>After upstream harden (bankrupt)</th><th>Growth</th></tr>{rows}<caption>Table 1. Measured defender-side cost of full-intensity counter-REA hardening on small fixtures (evidence class: MEASURED). Small fixtures exaggerate ratios; the absolute bytes are the load-bearing figures — a multi-megabyte addition to a WASM component is a product decision, not a detail.</caption></table>")

    h2("5", "Design: defense under a byte budget", "design")
    p("ThoxShield is a single Rust binary with zero external crates (SHA-256 and the JSON parser are implemented in-tree), organized as four verbs and a harness. <strong>Audit</strong> walks a release tree, detects formats by magic bytes, hashes every artifact, and lints for plaintext secrets and shipped source maps. <strong>Harden</strong> applies light shields to the three formats whose trips are byte-cheap: GGUF (canary key-values plus a 35-deep nested ARRAY metadata entry, original key-values preserved verbatim and in order), Safetensors (canary <code>__metadata__</code> strings — the format allows string-to-string metadata only [5] — plus a nesting breaker carried on the first tensor descriptor, tensor payload untouched), and WASM (an inert custom section carrying a canary and the original file&rsquo;s SHA-256; the original bytes remain a strict prefix). The WASM shield&rsquo;s payload preservation rests on the specification itself: for custom sections, &sect;5.5.3 of the WebAssembly Core Specification provides that errors in that data &ldquo;must not invalidate the module&rdquo; [6]. <strong>Verify</strong> re-derives the preservation properties from the bytes, not from the hardener&rsquo;s report. <strong>Manifest</strong> emits the SHA-256 inventory a release record needs. The bloat cap is enforced inside <em>harden</em>: an artifact whose shield would exceed the cap is refused, not trimmed silently. Canaries are synthetic and self-identifying; the enclave-manifest canary states in its own text that no enclave is present, because a privacy-first tool must not lie to the humans who later audit the artifact.")
    raw("""<div class="arch"><div class="arch-row four">
<div class="box hi"><b>audit</b><span>inventory, hashes, secret lint, source-map lint</span></div>
<div class="box hi"><b>harden</b><span>lite shields under the byte cap; refuses overflow</span></div>
<div class="box hi"><b>verify</b><span>preservation re-derived from bytes, independently</span></div>
<div class="box hi"><b>manifest</b><span>SHA-256 release inventory for the record</span></div>
</div><div class="arch-arrow">the four verbs, run directly or by the team loop of Section 6</div></div>""")

    h2("6", "The agent-team loop harness", "loop")
    p("Agent-built pipelines need the defense to run the way the pipeline runs: as a team, in a loop, with receipts. The harness (<code>thoxshield team</code>) defines five generic roles — coordinator, auditor, hardener, verifier, reporter — and no personas, frameworks, or model calls: each role is one of the CLI verbs run as a separate process, coordinated through a workorder and a state file that any agent can resume. The loop runs audit &rarr; lint gate &rarr; harden &rarr; verify &rarr; report, hardening from the original inputs on every iteration, and stops on exactly three conditions: all artifacts verified, a blocking lint finding (a plaintext secret is not a shielding problem and must stop a release), or exhaustion of the iteration budget, reported as failure. Iterative LM-agent tool-use loops are mature prior art (SWE-agent [12]); this harness claims no novelty as a loop. Its contribution is the application: producer &ne; verifier separation as a release gate for shields. The verifier&rsquo;s verdict, never the hardener&rsquo;s, closes the loop. The same protocol is published in prose (<code>harness/WORKORDER.md</code>) so an external agent — a coding assistant, a CI system, a human — can run the identical loop without the harness binary.")
    figure("wp/figures/fig-loop.svg", 1, "The team loop. The verifier is a separate process from the hardener; its verdict, never the hardener&rsquo;s report, closes the loop.")

    h2("7", "Evaluation", "evaluation")
    p(f"All figures are from <code>exp/results/summary.json</code>, the single evidence source. The ThoxShield fixture, preservation, and loop figures are re-derived from this paper&rsquo;s artifact pack by <code>exp/run_experiments.py</code>; the upstream figures and the 232-file audit timing are recorded measurements from the same session, with their commands noted in <code>summary.json</code>. On the reference fixtures, hardening added 736 B (GGUF, current fixture; the v0.1.0 fixture measured 746 B of inserted metadata before the alignment fix of Section 8), 578&ndash;619 B (Safetensors, fixture-dependent), and {F['core.wasm']['added_bytes']} B (WASM) — two to four orders of magnitude below the full-intensity figures of Table 1 on comparable fixtures. Preservation was checked independently of the tool&rsquo;s own verifier: a Python parser confirmed GGUF key preservation, tensor-count stability, byte-identical post-metadata content, and a nesting depth of 35; a Python JSON parse confirmed Safetensors header validity, byte-identical tensor payload, and a topology nesting depth of 36; Node&rsquo;s <code>WebAssembly.validate</code> accepted the WASM module before and after, and the hardened module compiles with its exports unchanged. The audit verb inventoried a 232-file tree in {T['audit_232_file_tree_ms']} ms. For production scale: hardening the 380 MB production GGUF of Section 8 took 4.7 s wall time (lab item HRD-02, Section 8). GGUF growth is 746 B of inserted metadata adjusted by alignment re-padding (Section 8), an observed band of &plusmn;31 B; Safetensors additions are fixture-dependent (578&ndash;619 B observed) because the header is rewritten. On byte-identical fixtures, the same-fixture comparison is direct: a 1,328 B spec-correct GGUF grows to 8,875 B under upstream bankrupt and 2,096 B under ThoxShield lite; a 36 B WASM module grows to 6,880,103 B under upstream bankrupt and 339 B under ThoxShield lite. The team loop reached verified shields on a clean three-artifact tree in one loop ({T['team_loop']['wall_ms']} ms in the reference run; 10&ndash;50 ms across lab runs), and, on a tree seeded with a planted flag marker and a shipped source map, stopped before hardening, named both artifacts, wrote its report, and exited non-zero — the gate behaving as designed. The tool&rsquo;s own unit tests cover SHA-256 against published vectors and JSON round-tripping.")
    figure("wp/figures/fig-bloat.svg", 2, "Same-fixture hardened sizes (lab item COMP-01, MEASURED) and the production-scale lite delta. Upstream&rsquo;s full-intensity settings grow the WASM fixture by five orders of magnitude; the lite shields stay in hundreds of bytes.")
    callout("Product implications", "For a local-first vendor, the practical consequence is that counter-REA defense can move from a specialist, per-release decision to a default pipeline step: audit in CI on every candidate, light shields on every published model and WASM component, independent verification in the release record. The cost line moves from megabytes and a Node toolchain to hundreds of bytes and one static binary — small enough to protect community and open-source releases with the same pipeline used for commercial ones.")

    h2("8", "Independent validation: the virtual test lab", "lab")
    p("The v1.0.0 edition of this paper rested on the authors&rsquo; own parsers. For v1.1.0 the THOX Research Team reviewed an independently produced test lab and its claims (the v1.1.x editions carry that rebuilt evidence forward; v1.1.2&rsquo;s changes are presentational and packaging — the template rebuild, the threat-model consolidation of Section 3, and the reproducibility scoping of Section 7 — not new measurements); the review found eight defects in that lab&rsquo;s evidence (invalid GGUF fixtures without tensor-info records, a hardcoded pass, a simulated analyzer that compared depths instead of enforcing its budget, self-verification labeled as independence, and a bundled binary that matched no recorded build). We rebuilt the lab to the review&rsquo;s standard: spec-correct fixtures, computed passes only, a budget enforced <em>during</em> traversal, self-checks labeled as self-checks, and the canonical binary&rsquo;s SHA-256 recorded in the evidence pack. The rebuilt lab runs twelve evidence items; ThoxShield&rsquo;s own <code>verify</code> is labeled SELF-CHECK throughout, and independence is claimed only where the reference implementations provide it: gguf-py, the safetensors library, and Node. The lab code ships in this pack (<code>exp/vlab.py</code>).")
    p("<strong>The lab earned its keep immediately: it caught a critical defect in ThoxShield v0.1.0.</strong> The first hardener copied the post-metadata bytes verbatim, which shifts a GGUF file&rsquo;s tensor data section off its alignment boundary (<code>general.alignment</code>, default 32); reference readers locate tensor data on that boundary, so on a production 380 MB GGUF all 290 tensors read misaligned through gguf-py. The v1.0.0 checks could not see this because they compared raw tail bytes, not reader-visible tensors. ThoxShield v0.1.1 re-pads after the tensor-info region, and its <code>verify</code> now checks tensor-info identity, data-section identity, and data-start alignment. Post-fix, the production GGUF grows by 736 B and gguf-py loads it with every tensor byte stream identical; hardening it twice is byte-identical; a 1.7 MB vocab GGUF grows by 777 B. The hardened Safetensors loads in the reference library with all tensors numerically identical. The simulated analyzer, now enforcing REA&rsquo;s 32-level budget (<code>MODEL_METADATA_NESTING</code>) during the walk, aborts on the nesting breaker at depth 33 (SIMULATED; a live REA run remains future work). Depth figures in this paper use stated roots: GGUF breaker depth is 35 nested ARRAY frames; the Safetensors header measures 38 by whole-header JSON depth (root = 1) and 36 for the topology value alone — the two conventions behind the inconsistent figures in earlier drafts.")
    p("<strong>Strip test.</strong> The lab also measures removal: a roughly 60-line stripper written from the format specifications, with no ThoxShield code, recovers the GGUF and WASM originals byte-exactly and the Safetensors payload exactly, in under a millisecond per artifact. We report this as a headline limitation, not a footnote: the lite shields are tripwires for budget-limited automated analyzers and carriers of attribution canaries. They are not, and are not sold as, tamper resistance. The origin binding cuts both ways: the embedded SHA-256 of the original tells a stripper exactly when a recovery is correct, and lets anyone match a shielded file against public unshielded models — the attribution mechanism and the fingerprint are the same bytes.")

    h2("9", "What ThoxShield deliberately does not do", "exclusions")
    p("Three exclusions are policy, not backlog. (1) <strong>No prompt-injection layers.</strong> Some counter-REA systems plant instructions aimed at the analyzing agent, including imitations of legal and regulatory notices. The mechanism is a known attack class, not a gray area: retrieved content blurs the data/instruction boundary for LLM-integrated applications (indirect prompt injection [13]). A transparency-first vendor does not ship fake regulatory text inside user artifacts. (2) <strong>No runtime deception of users.</strong> Shields that detect a debugger and serve synthetic telemetry deceive the artifact&rsquo;s owner as readily as its adversary; they belong, if anywhere, in sealed training challenges, not in shipped products. (3) <strong>No exhaustion flooding.</strong> Flooding is the mechanism whose cost lands on the user&rsquo;s disk, bandwidth, and battery; the cap exists so it cannot be enabled by accident. Each exclusion narrows the tool; we consider the narrowing a feature and record it so adopters can make their own judgment with open eyes. Underlying all three: ThoxShield claims cost and attribution, never secrecy — a ceiling set by theory, not modesty, since virtual-black-box obfuscation is impossible in general [8] and the standard survey concludes that interactive analysis defeats many obfuscations, so protection by obfuscation &ldquo;remains highly challenging&rdquo; [9].")

    h2("10", "Limitations and future work", "limitations")
    p("First, the lite shields&rsquo; nesting breakers are aimed at analyzer limits that upstream work verified empirically against a live REA pipeline; a live REA run against ThoxShield&rsquo;s own output has not yet been performed and is the first item of future work, together with a sealed-vs-unsealed exposure study. Production-scale <em>integrity</em> evidence is no longer future work: Section 8 covers a 380 MB production model. Second, coverage is intentionally narrow: JavaScript, Python, SQLite, and archive formats are audit-only in this tool, and teams needing AST-level weaving should use the upstream system; likewise, only the GGUF evidence is production-sourced — the Safetensors and WASM results rest on spec-correct fixtures, not real-world artifacts of those formats. Third, manifests are unsigned in this version; Ed25519 signing of the manifest is designed and scheduled. Fourth, removal is cheap and now measured: the strip test of Section 8 recovers originals in under a millisecond, so any deployment must assume the shields can be removed by an analyst who knows they are present; what they tax is the <em>unmodified, budget-limited automated pass</em>, plus they carry attribution if left in place. The breaker&rsquo;s margin over REA&rsquo;s published analyzer budget (+3 levels) is visible in every shipped artifact, so analyzer authors can raise their budgets at zero cost; open-sourcing accepts that bounded half-life deliberately. Fifth, the tool loads artifacts fully in memory: measured peak RSS is about twice the artifact size (1,026 MiB on a 512 MiB GGUF across audit, harden, and verify), so multi-GB models need matching RAM until a streaming implementation lands. Sixth, no client-side shield, including this one, creates secrecy against a determined human analyst [8][9]; ThoxShield buys cost and attribution, and real secrets belong on trusted infrastructure.")

    h2("11", "Conclusion", "conclusion")
    p("Counter-REA defense does not have to be heavy to be real. Measured carefully, its most efficient mechanisms cost hundreds of bytes; capped honestly, they fit the products and communities that need them most; and run as a verified team loop, they become a release habit rather than a specialist event. ThoxShield is our attempt at that habit, released openly so others can adopt, audit, and improve it. Your AI. Your Data. Your Rules.&trade;")

    h2("", "References", "references")
    refs = [
        "BLA Contributors. <em>BLA: Blind LLM Agents (bla-agents v3.2.4)</em>. Open-source counter-REA toolkit, MIT License. https://github.com/qybaihe/bla",
        "Morluto. <em>REA: Reverse Engineer Anything</em>. Open-source MCP server and CLI (npm: rea-agents), MIT License. https://github.com/morluto/rea",
        "National Institute of Standards and Technology. <em>Secure Hash Standard (SHS)</em>, FIPS PUB 180-4, 2012 (reissued 2015; the reissue changed only the Applicability Clause).",
        "ggml-org. <em>GGUF Format Specification</em>, docs/gguf.md, format version 3. https://github.com/ggml-org/ggml/blob/master/docs/gguf.md",
        "Hugging Face. <em>Safetensors format specification</em>. https://github.com/huggingface/safetensors (documented limits: 100 MB header cap; <code>__metadata__</code> is a string-to-string map only)",
        "W3C WebAssembly Community Group. <em>WebAssembly Core Specification</em>, &sect;5.5.3 (Custom Sections): errors in custom-section data &ldquo;must not invalidate the module.&rdquo;",
        "Collberg, C., Thomborson, C., and Low, D. <em>A Taxonomy of Obfuscating Transformations</em>. Technical Report 148, Department of Computer Science, University of Auckland, 1997. https://hdl.handle.net/2292/3491",
        "Barak, B., Goldreich, O., Impagliazzo, R., Rudich, S., Sahai, A., Vadhan, S., and Yang, K. <em>On the (Im)possibility of Obfuscating Programs</em>. CRYPTO 2001; journal version: J. ACM 59(2), Article 6, 2012. DOI 10.1145/2160158.2160159",
        "Schrittwieser, S., Katzenbeisser, S., Kinder, J., Merzdovnik, G., and Weippl, E. <em>Protecting Software through Obfuscation: Can It Keep Pace with Progress in Code Analysis?</em> ACM Computing Surveys 49(1), 1&ndash;37, 2016. DOI 10.1145/2886012",
        "Tan, H., Luo, Q., Li, J., and Zhang, Y. <em>LLM4Decompile: Decompiling Binary Code with Large Language Models</em>. arXiv:2403.05286, 2024.",
        "Pordanesh, S. and Tan, B. <em>Exploring the Efficacy of Large Language Models (GPT-4) in Binary Reverse Engineering</em>. arXiv:2406.06637, 2024.",
        "Yang, J., Jimenez, C., Wettig, A., Lieret, K., Yao, S., Narasimhan, K., and Press, O. <em>SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering</em>. arXiv:2405.15793, 2024 (NeurIPS 2024).",
        "Greshake, K., Abdelnabi, S., Mishra, S., Endres, C., Holz, T., and Fritz, M. <em>Not What You&rsquo;ve Signed Up For: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection</em>. arXiv:2302.12173, 2023 (AISec &rsquo;23).",
    ]
    raw('<ol class="refs">' + "".join(
        f'<li><span class="rn">[{i}]</span>{r}</li>' for i, r in enumerate(refs, 1)) + "</ol>")

    h2("", "Artifact availability", "artifacts")
    p("Ross, C. and Xaypanya, T. <em>ThoxShield: Bloat-Capped Counter-REA Defense for Local-First AI Artifacts</em>, v1.1.2 — experiment code and evidence ship in the artifact pack: <code>exp/run_experiments.py</code> re-derives the ThoxShield fixture, preservation, and loop figures from the pack (a thoxshield binary is the one prerequisite); <code>exp/vlab.py</code> is the virtual test lab of Section 8; <code>exp/results/summary.json</code> is the single evidence source for every number in this paper. The ThoxShield tool (v0.1.2) is open source under the MIT License; this paper is licensed CC BY 4.0.")

def main():
    raw(build_cover())
    raw('<div class="paper-body">')
    body()
    raw("</div>")
    src = ("<!doctype html>\n<html lang=\"en\"><head><meta charset=\"utf-8\">"
           "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">\n"
           f"<title>{TITLE}</title>\n"
           f"<meta name=\"description\" content=\"THOX.ai Research technical report {VERSION}\">\n"
           f"<style>{CSS}</style></head>\n<body data-version=\"{VERSION}\">\n" + "\n".join(OUT) + "\n</body></html>")
    (ROOT / "wp" / "paper.src.html").write_text(src)
    dist = ROOT / "dist"; dist.mkdir(exist_ok=True)
    html = src.replace("</style>", PRINT_CSS + "</style>", 1) if "</style>" in src else src
    html = html.replace("<style>", f"<style>", 1)
    (dist / "THOX_ThoxShield_Research_Paper_v1.1.2.html").write_text(html)
    from weasyprint import HTML
    HTML(string=html, base_url=str(ROOT)).write_pdf(str(dist / "THOX_ThoxShield_Research_Paper_v1.1.2.pdf"))
    print("wrote wp/paper.src.html, dist/THOX_ThoxShield_Research_Paper_v1.1.2.html/.pdf")

if __name__ == "__main__":
    main()
