"""
Find specific Wikimedia images for the remaining items
"""

import urllib.request
import urllib.parse
import json
import time

items = [
    ("ext2_gear_pump", "File:Zahnradpumpe"),
    ("ext2_gear_pump_alt", "gear pump"),
    ("ext4_circulation_pump", "circulating pump OR inline pump"),
    ("ext7_evaporator", "falling film evaporator OR industrial evaporator"),
    ("ext9_mixing_tank", "chemical reactor OR mixing tank stainless OR industrial agitator"),
    ("ext10_air_receiver", "air receiver OR compressed air tank OR pressure vessel"),
    ("ext14_bag_filter", "bag filter OR liquid bag filter"),
    ("ext15_cartridge_filter", "cartridge filter OR cartridge housing OR water filter housing"),
    ("ext16_ro_system", "reverse osmosis skid OR reverse osmosis system OR desalination plant"),
    ("ext17_water_softener", "water softener OR ion exchange resin vessel"),
    ("ext19_electric_motor", "electric motor cast iron OR TEFC motor OR induction motor industrial")
]

for tag, term in items:
    time.sleep(1.0)
    enc = urllib.parse.quote(term)
    url = f"https://commons.wikimedia.org/w/api.php?action=query&list=search&srsearch={enc}&srnamespace=6&srlimit=8&format=json"
    req = urllib.request.Request(url, headers={'User-Agent': 'AntigravityAudit/2.0'})
    try:
        with urllib.request.urlopen(req, timeout=10) as res:
            data = json.loads(res.read().decode('utf-8'))
            hits = [h['title'] for h in data.get('query', {}).get('search', []) if any(h['title'].lower().endswith(ext) for ext in ['.jpg', '.jpeg', '.png'])]
            print(f"=== {tag} ({term}) ===")
            for h in hits[:5]:
                print(f"  {h}")
    except Exception as e:
        print(f"Error {tag}: {e}")
