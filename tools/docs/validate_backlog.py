#!/usr/bin/env python3
"""Validate directory story dossiers and the generated backlog index block."""
from __future__ import annotations
import argparse,json,re,sys
from pathlib import Path
import jsonschema,yaml
ROOT=Path(__file__).resolve().parents[2];BACKLOG=ROOT/"docs/backlog";ITEMS=BACKLOG/"items";INDEX=BACKLOG/"README.md"
SS=ROOT/"docs/reference/schemas/story-frontmatter.schema.json";PS=ROOT/"docs/reference/schemas/implementation-plan-frontmatter.schema.json"
BEGIN="<!-- BEGIN GENERATED STORY INDEX -->";END="<!-- END GENERATED STORY INDEX -->";ORDER=("draft","ready","in-progress","blocked","deferred","done")
def parse(p):
 t=p.read_text();
 if not t.startswith("---\n"):raise ValueError("missing YAML front matter")
 raw,body=t[4:].split("\n---\n",1);m=yaml.safe_load(raw)
 if not isinstance(m,dict):raise ValueError("front matter must be a mapping")
 return m,body
def check_schema(m,p,s,errors):
 v=jsonschema.Draft202012Validator(json.loads(s.read_text()),format_checker=jsonschema.FormatChecker())
 for e in sorted(v.iter_errors(m),key=lambda x:list(x.absolute_path)): errors.append(f"{p.relative_to(ROOT)}:{'.'.join(map(str,e.absolute_path)) or '<root>'}: {e.message}")
def find_cycle(g):
 seen=set();stack=[]
 def visit(n):
  if n in stack:return stack[stack.index(n):]+[n]
  if n in seen:return None
  stack.append(n)
  for d in g.get(n,[]):
   c=visit(d)
   if c:return c
  stack.pop();seen.add(n)
 for n in g:
  c=visit(n)
  if c:return c
def block(records):
 out=[]
 for status in ORDER:
  rows=sorted(((p,m) for p,m in records if m.get("status")==status),key=lambda x:x[1].get("id",""))
  if not rows:continue
  out += [f"### {status.replace('-',' ').title()}","","| ID | Title | Priority | Dependencies |","| --- | --- | --- | --- |"]
  for p,m in rows:
   deps=", ".join(f"{d['id']} ({d['kind']})" for d in m.get("dependencies",[])) or "—"
   out.append(f"| `{m['id']}` | [{m['title']}]({p.relative_to(BACKLOG).as_posix()}) | {m['priority']} | {deps} |")
  out.append("")
 return "\n".join(out).rstrip()
def replace(text,new):
 if text.count(BEGIN)!=1 or text.count(END)!=1:raise ValueError("index markers must occur exactly once")
 a,r=text.split(BEGIN);_,b=r.split(END);return f"{a}{BEGIN}\n{new}\n{END}{b}"
def validate(write=False):
 errors=[];records=[];stories={};plans={}
 for d in sorted(ITEMS.glob("US-[0-9][0-9][0-9]-*")):
  if not d.is_dir():continue
  p=d/"README.md"
  try:m,b=parse(p)
  except Exception as e:errors.append(f"{p.relative_to(ROOT)}: {e}");continue
  check_schema(m,p,SS,errors);sid=m.get("id","");acs=set(re.findall(r"\bAC-[0-9]{3}\b",b))
  if not d.name.startswith(f"{sid}-"):errors.append(f"{p.relative_to(ROOT)}: directory must start with {sid}-")
  if f"# {sid}: {m.get('title','')}" not in b:errors.append(f"{p.relative_to(ROOT)}: H1 must match metadata")
  if m.get("status")!="draft" and not acs:errors.append(f"{p.relative_to(ROOT)}: non-draft story needs acceptance IDs")
  for dg in m.get("diagrams",[]):
   src=d/dg["path"]
   if not src.is_file() or not src.with_suffix(".svg").is_file():errors.append(f"{p.relative_to(ROOT)}: diagram pair missing for {dg['path']}")
  plan=d/"implementation-plan.md"
  if m.get("status")!="draft" and not plan.is_file():errors.append(f"{p.relative_to(ROOT)}: {m.get('status')} story requires implementation-plan.md")
  if plan.is_file():
   try:pm,pb=parse(plan);check_schema(pm,plan,PS,errors);plans[sid]=(pm,pb,acs,plan)
   except Exception as e:errors.append(f"{plan.relative_to(ROOT)}: {e}")
  stories[sid]=m;records.append((p,m))
 for sid,m in stories.items():
  for dep in m.get("dependencies",[]):
   if dep["id"] not in stories:errors.append(f"{sid}: unknown dependency {dep['id']}")
 c=find_cycle({s:[d["id"] for d in m.get("dependencies",[]) if d["kind"]=="blocks"] for s,m in stories.items()})
 if c:errors.append("blocking dependency cycle: "+" -> ".join(c))
 for sid,(pm,pb,acs,path) in plans.items():
  if pm.get("story_id")!=sid:errors.append(f"{path.relative_to(ROOT)}: story_id mismatch")
  tasks=pm.get("tasks",[]);ids=[t.get("id") for t in tasks];g={t.get("id"):t.get("depends_on",[]) for t in tasks}
  if len(ids)!=len(set(ids)):errors.append(f"{path.relative_to(ROOT)}: duplicate task ID")
  for t in tasks:
   for d in t.get("depends_on",[]):
    if d not in g:errors.append(f"{path.relative_to(ROOT)}: {t.get('id')} unknown dependency {d}")
   for a in t.get("acceptance",[]):
    if a not in acs:errors.append(f"{path.relative_to(ROOT)}: {t.get('id')} unknown acceptance {a}")
  tc=find_cycle(g)
  if tc:errors.append(f"{path.relative_to(ROOT)}: task cycle {' -> '.join(tc)}")
  covered={a for t in tasks for a in t.get("acceptance",[])}
  if stories[sid].get("status")!="draft" and acs-covered:errors.append(f"{path.relative_to(ROOT)}: uncovered acceptance IDs {sorted(acs-covered)}")
  if stories[sid].get("status")=="done" and any(t.get("status") not in {"done","skipped"} for t in tasks):errors.append(f"{path.relative_to(ROOT)}: done story has open tasks")
  for h in ("Architecture And Boundaries","Pattern Analysis","Change Map","Diagram Index","Test Strategy And Doubles","Task Graph","Detailed Tasks","Physical Gates","Traceability","Plan Change Log"):
   if f"## {h}" not in pb:errors.append(f"{path.relative_to(ROOT)}: missing ## {h}")
 if not records:errors.append("no backlog stories found")
 try:
  current=INDEX.read_text();expected=replace(current,block(records))
  if write and not errors:INDEX.write_text(expected)
  elif current!=expected:errors.append("docs/backlog/README.md: generated index block is stale; run --write-index")
 except Exception as e:errors.append(f"docs/backlog/README.md: {e}")
 return errors
def main():
 ap=argparse.ArgumentParser();ap.add_argument("--write-index",action="store_true");a=ap.parse_args();es=validate(a.write_index)
 if es:
  for e in es:print("ERROR:",e,file=sys.stderr)
  return 1
 print(f"Backlog valid: {len(list(ITEMS.glob('US-*/README.md')))} stories.");return 0
if __name__=="__main__":raise SystemExit(main())
