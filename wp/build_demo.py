#!/usr/bin/env python3
"""Build dist/ThoxShield_Demo_v1.1.2.html from wp/demo_template.html with
exp/results/summary.json embedded at the /*__SUMMARY__*/ slot."""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
tpl = (ROOT / "wp" / "demo_template.html").read_text()
S = (ROOT / "exp" / "results" / "summary.json").read_text()
html = tpl.replace("/*__SUMMARY__*/", S.replace("</", "<\\/"))
out = ROOT / "dist" / "ThoxShield_Demo_v1.1.2.html"
out.write_text(html)
print("wrote", out)
