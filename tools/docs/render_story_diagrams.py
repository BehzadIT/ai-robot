#!/usr/bin/env python3
"""Render or freshness-check canonical Mermaid sources with pinned local mmdc."""
import argparse,hashlib,json,subprocess,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; MMDC=ROOT/"node_modules/.bin/mmdc"; BASE=ROOT/"docs/backlog"
def sources(): return sorted(BASE.glob("**/diagrams/*.mmd"))
def render(src,out):
 seed=hashlib.sha256(src.relative_to(ROOT).as_posix().encode()).hexdigest()[:16]
 cfg={"deterministicIds":True,"deterministicIDSeed":seed,"theme":"neutral","fontFamily":"Arial"}
 with tempfile.TemporaryDirectory() as td:
  cp=Path(td)/"config.json";cp.write_text(json.dumps(cfg,sort_keys=True))
  pp=Path(td)/"puppeteer.json";pp.write_text(json.dumps({"args":["--no-sandbox","--disable-setuid-sandbox"]}))
  subprocess.run([str(MMDC),"-i",str(src),"-o",str(out),"-c",str(cp),"-p",str(pp),"-b","transparent"],check=True)
def main():
 ap=argparse.ArgumentParser();g=ap.add_mutually_exclusive_group(required=True);g.add_argument("--write",action="store_true");g.add_argument("--check",action="store_true");a=ap.parse_args()
 if not MMDC.exists():raise SystemExit("local mmdc missing; run npm ci")
 srcs=sources();expected={p.with_suffix(".svg") for p in srcs};orphans=set(BASE.glob("**/diagrams/*.svg"))-expected
 if orphans:raise SystemExit("orphan SVGs: "+", ".join(map(str,sorted(orphans))))
 for src in srcs:
  dst=src.with_suffix(".svg")
  if a.write:render(src,dst)
  else:
   with tempfile.TemporaryDirectory() as td:
    candidate=Path(td)/dst.name;render(src,candidate)
    if not dst.exists() or candidate.read_bytes()!=dst.read_bytes():raise SystemExit(f"stale or missing diagram: {dst.relative_to(ROOT)}")
 print(f"Diagram check passed: {len(srcs)} sources.")
if __name__=="__main__":main()
