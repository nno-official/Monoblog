import os, json, email.utils, datetime
from pathlib import Path

def xml_escape(s: str) -> str:
    s = s or ""
    return (s.replace("&", "&amp;")
             .replace("<", "&lt;")
             .replace(">", "&gt;")
             .replace('"', "&quot;")
             .replace("'", "&apos;"))

REPO = os.environ.get('GITHUB_REPOSITORY','')  # e.g. user/repo
if '/' in REPO:
    user, repo = REPO.split('/')
else:
    user, repo = 'username', 'repo'
SITE_URL = f'https://{user}.github.io/{repo}'

posts = json.loads(Path('posts/index.json').read_text(encoding='utf-8'))
now_rfc = email.utils.format_datetime(datetime.datetime.utcnow())

items_xml = []
for p in posts:
    link = f"{SITE_URL}/#/post/{p['slug']}"
    if p.get('date'):
        try:
            dt = datetime.datetime.strptime(p['date'], '%Y-%m-%d')
        except ValueError:
            dt = datetime.datetime.utcnow()
    else:
        dt = datetime.datetime.utcnow()
    pubdate = email.utils.format_datetime(dt)
    title = xml_escape(p.get('title',''))
    desc  = xml_escape(p.get('summary',''))
    items_xml.append(f"""
    <item>
      <title>{title}</title>
      <link>{link}</link>
      <guid>{link}</guid>
      <pubDate>{pubdate}</pubDate>
      <description>{desc}</description>
    </item>
    """)

rss = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>MonoBlog</title>
    <link>{SITE_URL}</link>
    <description>{xml_escape('Zero‑build blog feed')}</description>
    <lastBuildDate>{now_rfc}</lastBuildDate>
    {''.join(items_xml)}
  </channel>
</rss>
"""

Path('feed.xml').write_text(rss, encoding='utf-8')
print('Wrote feed.xml with', len(posts), 'items')