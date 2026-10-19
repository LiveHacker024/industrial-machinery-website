import urllib.request
import urllib.parse
import json

queries = [
    'gear pump industrial',
    'electric motor TEFC',
    'bag filter housing',
    'inline pump industrial'
]

for q in queries:
    enc = urllib.parse.quote(q)
    url = f"https://commons.wikimedia.org/w/api.php?action=query&list=search&srsearch={enc}&srnamespace=6&srlimit=6&format=json"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    try:
        with urllib.request.urlopen(req, timeout=10) as res:
            d = json.loads(res.read().decode('utf-8'))
            print("=== " + q + " ===")
            for h in d.get('query', {}).get('search', []):
                t = h['title']
                if any(t.lower().endswith(x) for x in ['.jpg', '.jpeg', '.png']):
                    print("  " + t)
    except Exception as e:
        print("Error:", e)
