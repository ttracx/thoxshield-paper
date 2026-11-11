# ThoxShield — Research Paper Artifact Bundle v1.1.2

**Paper:** *ThoxShield: Bloat-Capped Counter-REA Defense for Local-First
AI Artifacts* — THOX.ai Research, technical report v1.1.2, 2026-11-10.
Authors: Craig Ross (Chief Executive Officer) and Tommy Xaypanya (CTO
and Co-Founder, corresponding author, ORCID 0009-0000-4425-9565),
THOX.ai LLC. Paper license: CC BY 4.0. Tool license: MIT.
Status: preprint, not peer reviewed. Published 2026-11-11.
Version of record: DOI 10.5281/zenodo.24146345 (concept DOI 10.5281/zenodo.24146344).
The deposited edition is these exact bytes: the Zenodo file md5 matches
`dist/THOX_ThoxShield_Research_Paper_v1.1.2.pdf` (f73530943cf3f8e45f4ebdcbd8af5c3b).
The ThoxShield tool is MIT-licensed and lives at
https://github.com/ttracx/thoxshield; this paper is CC BY 4.0.

## Contents

- `dist/` — the shipped paper (PDF + single-file HTML) and the
  interactive demo HTML.
- `exp/results/summary.json` — the single evidence source: every
  number in the paper traces to this file.
- `exp/run_experiments.py` — re-derives the ThoxShield fixture,
  preservation, and team-loop figures from this bundle (see below).
- `exp/vlab.py` — the virtual test lab v2 behind Section 8 (needs
  `gguf`, `safetensors`, `numpy`, and Node; real-file items are
  env-configured and skip cleanly when unset).
- `exp/fixtures.py` — the reference-fixture generator.
- `wp/` — the paper build: `build.py` (source of truth; generates
  `paper.src.html`, the HTML, and the PDF), `figures.py` + `figures/`,
  `demo_template.html` + `build_demo.py`, and `wp/qa/` (QA report,
  contact sheet, side-by-side and viewport screenshots).
- `CITATION.cff` / `paper.bib` — the citation set.
- `HANDOFF.md` — the publication record.

## Rebuild

```
python3 wp/figures.py     # regenerates wp/figures/*.svg from summary.json
python3 wp/build.py       # paper.src.html -> dist paper HTML + PDF (WeasyPrint)
python3 wp/build_demo.py  # dist demo HTML from wp/demo_template.html
```

## Re-verify the evidence

```
# prerequisite: a built thoxshield binary (cargo build --release in the
# public ThoxShield repository; zero dependencies)
THOXSHIELD_BIN=/path/to/thoxshield python3 exp/run_experiments.py
```

That re-derives the fixture added-bytes, the independent preservation
checks, and the team-loop behavior (clean tree succeeds; seeded tree
stops before hardening). The upstream comparison figures and the
232-file audit timing in `summary.json` are recorded same-session
measurements with their commands noted in the file; Section 8's lab
items re-derive via `exp/vlab.py` where their inputs are available.
