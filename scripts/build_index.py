import os, re, json, datetime, glob
from pathlib import Path
POSTS_DIR = Path('posts')
OUTPUT = POSTS_DIR / 'index.json'
FRONT_RE = re.compile(r'^---\n([\s\S]*?)\n---\n', re.M)
def parse_front(text):
    m = FRONT_RE.match(text); meta = {}
    if not m: return meta
    raw = m.group(1)
    for line in raw.splitlines():
        if ':' not in line: continue
        k,v = line.split(':',1); k=k.strip(); v=v.strip()
        if k=='tags':
            v=v.strip('[]'); meta['tags']=[t.strip().strip('\"\'') for t in v.split(',') if t.strip()]
        else: meta[k]=v.strip('\"\'')
    return meta
def first_h1(text):
    for line in text.splitlines():
        if line.lstrip().startswith('# '): return line.lstrip()[2:].strip()
    return None
def first_paragraph(text):
    text = FRONT_RE.sub('', text, count=1)
    paras=[p.strip() for p in text.split('\n\n') if p.strip()]
    return re.sub(r'\s+',' ',paras[0])[:300] if paras else ''
def build():
    items=[]
    for md in sorted(glob.glob(str(POSTS_DIR/'*.md'))):
        name=os.path.basename(md)
        if name=='README.md': continue
        with open(md,'r',encoding='utf-8') as f: text=f.read()
        meta=parse_front(text)
        from datetime import datetime as dt
        title=meta.get('title') or first_h1(text) or Path(md).stem.replace('-',' ').title()
        date=meta.get('date') or dt.fromtimestamp(os.path.getmtime(md)).strftime('%Y-%m-%d')
        slug=meta.get('slug') or Path(md).stem
        summary=meta.get('summary') or first_paragraph(text)
        tags=meta.get('tags') or []
        cover=meta.get('cover') or ''
        items.append({'slug':slug,'title':title,'date':date,'tags':tags,'summary':summary,'file':f'posts/{name}','cover':cover})
    items.sort(key=lambda x: x['date'], reverse=True)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT,'w',encoding='utf-8') as f: json.dump(items,f,indent=2,ensure_ascii=False)
if __name__=='__main__': build()
