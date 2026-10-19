"""
Script to search Wikimedia Commons API for authentic machinery photographs
"""

import urllib.request
import urllib.parse
import json

queries = {
    "ext1_vacuum_pump": "liquid ring vacuum pump",
    "ext2_gear_pump": "rotary gear pump industrial",
    "ext3_dosing_pump": "metering pump industrial",
    "ext4_circulation_pump": "vertical inline pump centrifugal",
    "ext5_plate_exchanger": "plate heat exchanger",
    "ext6_refrig_condenser": "air cooled condenser industrial",
    "ext7_evaporator": "evaporator industrial chemical",
    "ext8_storage_tank": "stainless steel storage tank industrial",
    "ext9_mixing_tank": "mixing tank agitator industrial",
    "ext10_air_receiver": "air receiver pressure vessel",
    "ext11_centrifugal_blower": "centrifugal fan industrial blower",
    "ext12_air_dryer": "refrigerated air dryer compressed",
    "ext13_filtration_system": "sand filter industrial water",
    "ext14_bag_filter": "bag filter industrial",
    "ext15_cartridge_filter": "cartridge filter industrial housing",
    "ext16_ro_system": "reverse osmosis industrial plant",
    "ext17_water_softener": "water softener industrial ion exchange",
    "ext18_diesel_generator": "diesel generator set industrial",
    "ext19_electric_motor": "electric motor three phase induction tefc",
    "ext20_mcc_panel": "motor control center panel industrial"
}

for key, q in queries.items():
    encoded_q = urllib.parse.quote(q)
    url = f"https://commons.wikimedia.org/w/api.php?action=query&list=search&srsearch={encoded_q}&srnamespace=6&srlimit=5&format=json"
    req = urllib.request.Request(url, headers={'User-Agent': 'AntigravityAuditBot/1.0'})
    try:
        res = urllib.request.urlopen(req, timeout=10)
        data = json.loads(res.read().decode('utf-8'))
        results = data.get('query', {}).get('search', [])
        print(f"\n=== {key} ({q}) ===")
        for r in results:
            title = r['title']
            if not title.endswith('.svg'):  # prefer raster photos
                print(f" - {title}")
    except Exception as e:
        print(f"Error searching for {key}: {e}")
