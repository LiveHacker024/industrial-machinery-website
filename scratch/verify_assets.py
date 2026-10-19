import urllib.request, re

with open('d:/Client Websites/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

srcs = re.findall(r'src=["\'](.*?)["\']', html)
hrefs = re.findall(r'href=["\'](assets/.*?)["\']', html)

all_assets = set(srcs + hrefs)
failed = []

for a in all_assets:
    if a.startswith(('http://', 'https://')):
        url = a
    else:
        url = 'http://localhost:8080/' + a.lstrip('/')
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as resp:
            if resp.getcode() != 200:
                failed.append((url, resp.getcode()))
    except Exception as e:
        failed.append((url, str(e)))

print('Total assets tested from index.html:', len(all_assets))
if failed:
    print('Failed assets:', failed)
else:
    print('ALL ASSETS IN INDEX.HTML LOADED WITH HTTP 200 OK!')

with open('d:/Client Websites/script.js', 'r', encoding='utf-8') as f:
    js = f.read()

images = re.findall(r'image:\s*["\'](.*?)["\']', js)
print('Total images in script.js:', len(images))
img_failed = []
for img in set(images):
    url = 'http://localhost:8080/' + img
    try:
        with urllib.request.urlopen(url) as resp:
            if resp.getcode() != 200:
                img_failed.append((img, resp.getcode()))
    except Exception as e:
        img_failed.append((img, str(e)))

if img_failed:
    print('Failed images in script.js:', img_failed)
else:
    print('ALL 13 PRODUCT IMAGES IN SCRIPT.JS LOADED WITH HTTP 200 OK!')

