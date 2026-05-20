#!/usr/bin/env python3
from __future__ import annotations
import argparse, datetime as dt, re, sys
from dataclasses import dataclass
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
WIKI_DIR = ROOT / 'wiki'
INDEX_PATH = WIKI_DIR / 'index.md'
SECTIONS = {'entities':'entity','concepts':'concept','sources':'source','syntheses':'synthesis'}
DATE_RE = re.compile(r'^\d{4}-\d{2}-\d{2}$')

@dataclass(frozen=True)
class Page:
    path: Path; category:str; page_name:str; updated:str; source_count:int; summary:str

def parse_value(v:str):
    v=v.strip()
    if v.startswith('[') and v.endswith(']'):
        inner=v[1:-1].strip()
        if not inner: return []
        parts=[x.strip() for x in inner.split(',')]
        return [p.strip('"\' ') for p in parts]
    if v.isdigit(): return int(v)
    return v.strip('"\' ')

def parse_frontmatter(path:Path)->dict:
    lines=path.read_text(encoding='utf-8').splitlines()
    if not lines or lines[0].strip()!='---': raise ValueError(f"{path}: missing YAML frontmatter opening '---'")
    end=None
    for i in range(1,len(lines)):
        if lines[i].strip()=='---': end=i; break
    if end is None: raise ValueError(f"{path}: missing YAML frontmatter closing '---'")
    d={}
    for raw in lines[1:end]:
        s=raw.strip()
        if not s or s.startswith('#'): continue
        if ':' not in s: raise ValueError(f"{path}: malformed frontmatter line: {raw}")
        k,v=s.split(':',1)
        d[k.strip()]=parse_value(v)
    return d

def validate_date(path,key,v):
    if not isinstance(v,str) or not DATE_RE.match(v): raise ValueError(f"{path}: frontmatter '{key}' must be YYYY-MM-DD, got {v!r}")

def first_h1(path:Path)->str:
    for l in path.read_text(encoding='utf-8').splitlines():
        if l.startswith('# '): return l[2:].strip()
    return path.stem

def summary_line(path:Path)->str:
    lines=path.read_text(encoding='utf-8').splitlines(); in_fm=False
    for l in lines:
        if l.strip()=='---': in_fm=not in_fm; continue
        s=l.strip()
        if in_fm or not s or s.startswith('#') or s.startswith('>'): continue
        return s.replace('|','\\|')
    return '—'

def load_pages(sort_by):
    pages=[]
    for folder,typ in SECTIONS.items():
        for p in sorted((WIKI_DIR/folder).glob('*.md')):
            fm=parse_frontmatter(p)
            if fm.get('type')!=typ: raise ValueError(f"{p}: type/path mismatch (expected type '{typ}' in wiki/{folder}/)")
            created=str(fm.get('created',''))
            if not created: raise ValueError(f"{p}: missing required frontmatter field 'created'")
            validate_date(p,'created',created)
            updated=str(fm.get('updated',created)); validate_date(p,'updated',updated)
            sc=fm.get('source_count',0)
            if isinstance(sc,bool) or not isinstance(sc,int) or sc<0: raise ValueError(f"{p}: frontmatter 'source_count' must be a non-negative integer")
            pages.append(Page(p,folder,first_h1(p),updated,sc,summary_line(p)))
    pages.sort(key=(lambda x:(x.category,x.updated,x.page_name.lower(),x.path.name)) if sort_by=='updated' else (lambda x:(x.category,x.page_name.lower(),x.path.name)))
    return pages

def table(rows):
    return ['| Page | Summary | Sources | Status | Updated |','|------|---------|---------|--------|---------|',* [f"| [[{r.page_name}]] | {r.summary} | {r.source_count} | active | {r.updated} |" for r in rows]]

def render(pages):
    by={k:[] for k in SECTIONS}
    for p in pages: by[p.category].append(p)
    last=max((p.updated for p in pages), default=dt.date.today().isoformat())
    return '\n'.join(['# Wiki Index','','> Content catalog. Updated after every ingest, query, or lint operation.','','## Entities','',*table(by['entities']),'','## Concepts','',*table(by['concepts']),'','## Sources','',*table(by['sources']),'','## Syntheses','',*table(by['syntheses']),'','## Statistics','','- **Total pages**: '+str(len(pages)),'- **Total sources**: '+str(len(by['sources'])),'- **Last updated**: '+last,''])

def main():
    ap=argparse.ArgumentParser(description='Rebuild wiki/index.md from wiki page frontmatter')
    ap.add_argument('--sort-by',choices=['name','updated'],default='name'); ap.add_argument('--check',action='store_true')
    a=ap.parse_args()
    try: out=render(load_pages(a.sort_by))
    except ValueError as e: print(f'ERROR: {e}',file=sys.stderr); return 1
    if a.check:
        cur=INDEX_PATH.read_text(encoding='utf-8') if INDEX_PATH.exists() else ''
        if cur!=out: print('ERROR: wiki/index.md is out of date. Run scripts/rebuild_index.py',file=sys.stderr); return 1
        print('wiki/index.md is up to date.'); return 0
    INDEX_PATH.write_text(out,encoding='utf-8'); print('Rebuilt wiki/index.md'); return 0
if __name__=='__main__': raise SystemExit(main())
