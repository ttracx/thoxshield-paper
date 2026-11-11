# HANDOFF — ThoxShield paper v1.1.2 (publication record)

Status: PUBLISHED 2026-11-11. Founder consent to these exact bytes was given
2026-11-11 15:08 CT (labeled supplement consent, per the THOX Research Paper
Process v1.0 §2, because v1.1.2 supersedes the v1.1.1 bytes after an
independent standards audit).

Publication record, each leg verified rather than assumed:
- Zenodo: version DOI 10.5281/zenodo.24146345, concept DOI
  10.5281/zenodo.24146344, published 2026-11-11. The anonymous
  return-download PDF hash matched the consented bytes; re-verified
  2026-11-11 17:58 CST against the Zenodo file md5
  (f73530943cf3f8e45f4ebdcbd8af5c3b = the local dist PDF).
- Hugging Face whitepapers: landed under thoxshield/ (commit d7da0e89),
  read-back hash matched.
- GitHub tool repo: https://github.com/ttracx/thoxshield public, release
  v0.1.2 with the Linux x86_64 binary and manifest.
- GitHub paper repo: this repository, release v1.1.2 with the shipped PDF,
  HTML, demo and the artifact bundle.
- LinkedIn: draft updated to v1.1.2, not posted (posting is the founders' call).

Still open: the Model Factory revision bump and the thox.ai paper page. Both
touch website surfaces and are held for the lane owner; the paper's DOI,
Hugging Face card and both GitHub repos carry the association already.

## Edition hashes (SHA-256)
- dist/THOX_ThoxShield_Research_Paper_v1.1.2.pdf
  dcd188093864252c26daf49f1388ddc4a0c73e1bd6e2e1ce1e2afa54feb3b38b
- dist/THOX_ThoxShield_Research_Paper_v1.1.2.html
  c5de7cbc169dac423cd2c000007c2e9ae590d4edecb4a5fa30fa51b817e92183
- dist/ThoxShield_Demo_v1.1.2.html
  1a09ef4bfaec9d7e42d8c5195b73c348acbe8bf32c94c520785fc21d728baab9
(PDF bytes carry a build timestamp; the hash above is of the shipped
file in this bundle.)

## What v1.1.2 is
The v1.1.1 content and evidence, rebuilt to standard after the
independent standards audit of v1.1.1 (3 blockers, 5 majors, 8 minors):
- Paper rebuilt FROM the canonical THOX Research Paper Template v1.0
  files (dark cover + marks footer, Inter/JetBrains Mono, green
  KPI cards, numbered two-column contents, black table headers,
  green section numbers). Rendered inspection: BUILD_RECORD.md and
  wp/qa/QA-REPORT.md. At 390 px the template's own responsive rules
  collapse the contents and KPI grid; verified by browser screenshot
  (wp/qa/). (Correction of the v1.1.1 record: that edition's 390 px
  overflow was caused by its own hand-rolled CSS, which had no media
  queries — not by the template's CSS.)
- Abstract binary size corrected to the released tool: v0.1.2,
  486,808 B (v1.1.1 printed the superseded v0.1.0 figure).
- New Section 3, Threat model, consolidated from Sections 2/8/9/10
  material; no new experiments or claims.
- Production GGUF harden wall time (4.7 s) added to Section 7.
- Demo rebuilt from the template's demo_template.html with real
  in-browser computation; canonical evidence labels only.
- Bundle assembled to Process §1.3 (this README, named dist files,
  exp/ incl. the virtual test lab code, wp/qa/); internal review
  material removed from all shipped files.
- CITATION.cff license corrected to CC-BY-4.0 (the paper's license).

## Evidence
- Single source: exp/results/summary.json (v1.1.2), including the
  virtual test lab v2 evidence map, the ALIGN-1 defect record, and
  per-version change records. All six THOX Research Team reviews
  (economics, evidence, redteam, security, systems, literature)
  returned and are folded.
- Reproducibility: exp/run_experiments.py re-derives the ThoxShield
  fixture/preservation/loop figures from this bundle (run recorded
  in wp/qa/QA-REPORT.md); upstream figures are recorded measurements.
- A separate SHA-256 receipt utility (THOX Release Verify
  v0.1.0-rc.1, reviewed from a founder-supplied archive, 2026-11-10)
  is adopted as the receipt format for ThoxShield release manifests;
  it remains its own tool with its own paper.

## Gates remaining before any public step
1. Founder consent to the EXACT v1.1.2 bytes above (supplement
   consent; v1.1.1 and earlier bytes are superseded).
2. Zenodo deposit FIRST (DOI), then the public ThoxShield repo push
   at tool v0.1.2, then the one-pass association. Social is the
   founders' call.
3. Nothing has been published, deposited, or pushed.
