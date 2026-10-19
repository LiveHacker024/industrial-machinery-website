"""
Polite search script for Wikimedia Commons images
"""

import urllib.request
import urllib.parse
import json
import time

queries = [
    ("ext2_gear_pump", "Zahnradpumpe OR \"gear pump\""),
    ("ext3_dosing_pump", "\"metering pump\" OR \"dosing pump\""),
    ("ext4_circulation_pump", "\"inline pump\" OR \"centrifugal pump\" OR \"circulating pump\""),
    ("ext5_plate_exchanger", "\"plate heat exchanger\""),
    ("ext6_refrig_condenser", "\"air cooled condenser\" OR \"condenser\" refrigeration"),
    ("ext7_evaporator", "evaporator chemical OR \"falling film\" OR \"industrial evaporator\""),
    ("ext8_storage_tank", "\"storage tank\" stainless OR \"chemical tank\""),
    ("ext9_mixing_tank", "\"stirred tank\" OR \"mixing tank\" OR \"agitator\""),
    ("ext10_air_receiver", "\"air receiver\" OR \"pressure vessel\""),
    ("ext11_centrifugal_blower", "\"centrifugal fan\" OR \"centrifugal blower\""),
    ("ext12_air_dryer", "\"air dryer\" OR \"compressed air\" dryer"),
    ("ext13_filtration_system", "\"sand filter\" OR \"water filter\" industrial"),
    ("ext14_bag_filter", "\"bag filter\""),
    ("ext15_cartridge_filter", "\"cartridge filter\" OR \"filter housing\""),
    ("ext16_ro_system", "\"reverse osmosis\" plant OR \"reverse osmosis\" industrial"),
    ("ext17_water_softener", "\"water softener\" OR \"ion exchange\" water"),
    ("ext18_diesel_generator", "\"diesel generator\" OR \"generating set\""),
    ("ext19_electric_motor", "\"electric motor\" induction OR tefc"),
    ("ext20_mcc_panel", "\"motor control center\" OR \"switchgear\" OR \"distribution board\"")
]

results = {}

for key, q in queries:
    time.sleep(1.2)  # be polite
    encoded_q = urllib.parse.quote(q)
    url = f"https://commons.wikimedia.org/w/api.php?action=query&list=search&srsearch={encoded_q}&srnamespace=6&srlimit=6&format=json"
    req = urllib.request.Request(url, headers={'User-Agent': 'AntigravityMachineryBot/1.0 (contact@clientwebsites.local)'})
    try:
        with urllib.request.urlopen(req, timeout=10) as res:
            data = json.loads(res.read().decode('utf-8'))
            items = data.get('query', {}).get('search', [])
            candidates = [it['title'] for it in items if not it['title'].endswith('.svg') and not it['title'].endswith('.pdf')]
            results[key] = candidates
            print(f"[{key}] Found {len(candidates)} candidates: {candidates[:3]}")
    except Exception as e:
        print(f"[{key}] Error: {e}")

with open("scratch/search_results.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)

print("\nDone searching. Results saved to scratch/search_results.json")
