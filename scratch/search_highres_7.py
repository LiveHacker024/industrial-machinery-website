import urllib.request
import urllib.parse
import json

def search_commons(query):
    url = f"https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrsearch={urllib.parse.quote(query)}&gsrnamespace=6&gsrlimit=10&prop=imageinfo&iiprop=url|size|extmetadata&format=json"
    req = urllib.request.Request(url, headers={'User-Agent': 'PHMachineryBot/2.0 (industrial-catalogue; contact@example.com)'})
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            data = json.loads(r.read().decode())
            pages = data.get('query', {}).get('pages', {})
            results = []
            for k, v in pages.items():
                title = v.get('title', '')
                ii = v.get('imageinfo', [{}])[0]
                img_url = ii.get('url', '')
                w = ii.get('width', 0)
                h = ii.get('height', 0)
                if img_url.lower().endswith(('.jpg', '.jpeg', '.png')) and w >= 800:
                    results.append({'title': title, 'url': img_url, 'w': w, 'h': h})
            return results
    except Exception as e:
        print('Error:', e)
        return []

queries = [
    ('ext14_bag_filter', ['bag filter vessel', 'industrial bag filter', 'dust collector filter bag', 'filtration vessel']),
    ('ext15_cartridge_filter', ['cartridge filter housing', 'industrial cartridge filter', 'filter housing stainless', 'water filter housing']),
    ('ext16_ro_system', ['reverse osmosis skid', 'reverse osmosis plant', 'desalination plant skid', 'RO membrane skid']),
    ('ext17_water_softener', ['water softener resin tank', 'ion exchange water softener', 'demineralisation plant', 'water softener plant']),
    ('ext18_diesel_generator', ['diesel generator canopy', 'caterpillar generator set', 'soundproof diesel generator', 'diesel genset']),
    ('ext19_electric_motor', ['electric motor TEFC', 'three phase electric induction motor', 'industrial induction motor']),
    ('ext20_mcc_panel', ['motor control center switchgear', 'MCC panel switchgear', 'low voltage switchgear cabinet', 'electrical control panel switchgear'])
]

for key, q_list in queries:
    print(f"\n=================== {key} ===================")
    found = False
    for q in q_list:
        res = search_commons(q)
        if res:
            print(f"Query '{q}' found {len(res)}:")
            for r in res[:4]:
                print(f"  {r['title']} ({r['w']}x{r['h']})\n    {r['url']}")
            found = True
            break
        import time
        time.sleep(1)
