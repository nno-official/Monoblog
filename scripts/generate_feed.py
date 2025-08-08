import os, json, email.utils, datetime
from pathlib import Path
REPO = os.environ.get('GITHUB_REPOSITORY','')
if '/' in REPO: user, repo = REPO.split('/')
else: user, repo = 'username', 'repo'
SITE_URL = f'https://{user}.github.io/{repo}'
posts = json.loads(Path('posts/index.json').read_text(encoding='utf-8'))
now_rfc = email.utils.format_datetime(datetime.datetime.utcnow())
items_xml = []
for p in posts:
    link = f"{SITE_URL}/#/post/{p['slug']}"
    pubdate = email.utils.format_datetime(datetime.datetime.strptime(p['date'], '%Y-%m-%d')) if p.get('date') else now_rfc
    desc = (p.get('summary') or '').replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
    items_xml.append(f'''<item>
  <title>{p['title']}</title>
  <link>{link}</link>
  <guid>{link}</guid>
  <pubDate>{pubdate}</pubDate>
  <description>{desc}</description>
</item>
''')
rss = f'''<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>MonoBlog</title>
    <link>{SITE_URL}</link>
    <description>Zero‑build blog feed</description>
    <lastBuildDate>{now_rfc}</lastBuildDate>
    {''.join(items_xml)}
  </channel>
</rss>
'''
Path('feed.xml').write_text(rss, encoding='utf-8')
print('Wrote feed.xml with', len(posts), 'items')
