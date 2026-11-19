"""Build the single-file prototype: inlines images, SVGs and the Logo lab data.

    python3 src/build.py      # writes index.html at the repo root
"""
import base64, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
t = open(os.path.join(HERE, 'prototype.html'), encoding='utf-8').read()

def img(m):
    n = m.group(1); mime = 'image/png' if n.endswith('.png') else 'image/jpeg'
    data = open(os.path.join(HERE, 'assets', n), 'rb').read()
    return 'data:%s;base64,%s' % (mime, base64.b64encode(data).decode())

def svg(m):
    s = open(os.path.join(HERE, 'svg', m.group(1) + '.svg'), encoding='utf-8').read().strip()
    return re.sub(r'\s+', ' ', s).replace('`', '')

t = t.replace('{{json:lab}}', open(os.path.join(HERE, 'lab.json'), encoding='utf-8').read())
t = re.sub(r'\{\{img:([^}]+)\}\}', img, t)
t = re.sub(r'\{\{svg:([^}]+)\}\}', svg, t)
assert not re.search(r'\{\{(img|svg|json):', t), 'unreplaced placeholder'
open(os.path.join(ROOT, 'index.html'), 'w', encoding='utf-8').write(t)
print('index.html', len(t) // 1024, 'KB')
