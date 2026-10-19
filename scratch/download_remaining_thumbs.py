"""
Download remaining 13 machine photos via Wikimedia thumbnail API
"""

import urllib.request
import urllib.parse
import json
import os
import time
from PIL import Image

TARGET_DIR = r"D:\Client Websites\assets\machines\additional"

REMAINING_MAP = {
    "ext3_dosing_pump": {
        "file": "File:Milton Roy's Primeroyal N Triplex Metering Pump.jpg",
        "output": "ext-03-dosing-pump.jpg",
        "name": "Milton Roy Primeroyal Industrial Dosing & Metering Pump",
        "source_label": "Wikimedia Commons (Milton Roy Primeroyal)"
    },
    "ext4_circulation_pump": {
        "file": "File:Centrifugal Pump.jpg",
        "output": "ext-04-circulation-pump.jpg",
        "name": "Industrial Inline Centrifugal Circulation Pump",
        "source_label": "Wikimedia Commons (Hydronic Centrifugal Circulation)"
    },
    "ext6_refrig_condenser": {
        "file": "File:Industrial Refrigeration Condensers.jpg",
        "output": "ext-06-refrig-condenser.jpg",
        "name": "Industrial Finned-Tube Refrigeration Condenser Bank",
        "source_label": "Wikimedia Commons (Industrial Refrigeration Condensers)"
    },
    "ext7_evaporator": {
        "file": "File:The single effect climbing falling film evaporator.jpg",
        "output": "ext-07-evaporator.jpg",
        "name": "Industrial Single Effect Climbing & Falling Film Evaporator",
        "source_label": "Wikimedia Commons (Falling Film Evaporator)"
    },
    "ext9_mixing_tank": {
        "file": "File:Pueblo Chemical Agent - Agitated reactor (motor).jpg",
        "output": "ext-09-mixing-tank.jpg",
        "name": "Industrial Motorized Agitated Reaction Mixing Vessel",
        "source_label": "Wikimedia Commons (US Army Agitated Reactor)"
    },
    "ext11_centrifugal_blower": {
        "file": "File:High Pressure Centrifugal Fan.jpg",
        "output": "ext-11-centrifugal-blower.jpg",
        "name": "High-Pressure Industrial Centrifugal Blower Fan",
        "source_label": "Wikimedia Commons (High Pressure Centrifugal Fan)"
    },
    "ext12_air_dryer": {
        "file": "File:Dryer-CFC Dryer.jpg",
        "output": "ext-12-air-dryer.jpg",
        "name": "Industrial Refrigerated Compressed Air Dryer System",
        "source_label": "Wikimedia Commons (Refrigerated Air Dryer Unit)"
    },
    "ext13_filtration_system": {
        "file": "File:Industrial Water Treatment Plants.jpg",
        "output": "ext-13-filtration-system.jpg",
        "name": "Multi-Grade Sand & Media Water Filtration Tank Skid",
        "source_label": "Wikimedia Commons (Industrial Water Treatment Plants)"
    },
    "ext14_bag_filter": {
        "file": "File:Schlauchfilter im Deutschen Museum.jpg",
        "output": "ext-14-bag-filter.jpg",
        "name": "Industrial Fabric Bag Filter Multi-Chamber Housing",
        "source_label": "Wikimedia Commons (Deutsches Museum Bag Filter)"
    },
    "ext16_ro_system": {
        "file": "File:Reverse Osmosis System.jpg",
        "output": "ext-16-ro-system.jpg",
        "name": "Industrial Skid-Mounted Reverse Osmosis (RO) Plant",
        "source_label": "Wikimedia Commons (Reverse Osmosis Skid Unit)"
    },
    "ext17_water_softener": {
        "file": "File:Water softener.jpg",
        "output": "ext-17-water-softener.jpg",
        "name": "Automated Cation-Exchange Water Softener Plant",
        "source_label": "Wikimedia Commons (Water Softener Unit)"
    },
    "ext18_diesel_generator": {
        "file": "File:Caterpillar (Olympian) Generator Set.jpg",
        "output": "ext-18-diesel-generator.jpg",
        "name": "Industrial Acoustic Canopy Diesel Generator Set",
        "source_label": "Wikimedia Commons (Caterpillar Olympian DG Set)"
    },
    "ext19_electric_motor": {
        "file": "File:Three Phase Induction Motor.jpg",
        "output": "ext-19-electric-motor.jpg",
        "name": "Heavy-Duty Cast Iron TEFC Three-Phase Induction Motor",
        "source_label": "Wikimedia Commons (Three Phase Induction Motor)"
    }
}

info_file = "scratch/downloaded_photos.json"
downloaded_info = {}
if os.path.exists(info_file):
    with open(info_file, "r", encoding="utf-8") as f:
        downloaded_info = json.load(f)

for pid, meta in REMAINING_MAP.items():
    time.sleep(2.0)
    filename = meta["file"]
    enc_name = urllib.parse.quote(filename)
    api_url = f"https://commons.wikimedia.org/w/api.php?action=query&titles={enc_name}&prop=imageinfo&iiprop=url|size|extmetadata&iiurlwidth=960&format=json"
    req = urllib.request.Request(api_url, headers={'User-Agent': 'AntigravityMachineryBot/3.0 (info@pukhrajhastimal.com)'})
    
    try:
        with urllib.request.urlopen(req, timeout=15) as res:
            data = json.loads(res.read().decode('utf-8'))
            pages = data['query']['pages']
            img_info = None
            for p in pages.values():
                if 'imageinfo' in p and len(p['imageinfo']) > 0:
                    img_info = p['imageinfo'][0]
                    break
            
            if not img_info:
                print(f"[{pid}] Could not get imageinfo for {filename}")
                continue
            
            thumb_url = img_info.get('thumburl') or img_info.get('url')
            desc_url = img_info.get('descriptionurl', f"https://commons.wikimedia.org/wiki/{filename}")
            extmeta = img_info.get('extmetadata', {})
            author = extmeta.get('Artist', {}).get('value', 'Wikimedia Commons Contributor')
            license_name = extmeta.get('LicenseShortName', {}).get('value', 'CC-BY-SA / Public Domain')
            
            print(f"[{pid}] Downloading {meta['name']} thumb...")
            
            img_req = urllib.request.Request(thumb_url, headers={'User-Agent': 'AntigravityMachineryBot/3.0 (info@pukhrajhastimal.com)'})
            with urllib.request.urlopen(img_req, timeout=30) as img_res:
                raw_data = img_res.read()
            
            temp_path = os.path.join(TARGET_DIR, "temp_" + meta["output"])
            final_path = os.path.join(TARGET_DIR, meta["output"])
            
            with open(temp_path, "wb") as f:
                f.write(raw_data)
            
            with Image.open(temp_path) as im:
                im = im.convert("RGB")
                im.thumbnail((1200, 1200), Image.Resampling.LANCZOS)
                im.save(final_path, "JPEG", quality=88, optimize=True)
            
            os.remove(temp_path)
            
            file_size_kb = round(os.path.getsize(final_path) / 1024, 1)
            print(f"  -> Saved {meta['output']} ({file_size_kb} KB)")
            
            downloaded_info[pid] = {
                "id": pid,
                "name": meta["name"],
                "file_path": f"assets/machines/additional/{meta['output']}",
                "source_url": desc_url,
                "source_label": meta["source_label"],
                "author": author,
                "license": license_name
            }
            
    except Exception as e:
        print(f"[{pid}] Error downloading {filename}: {e}")

with open(info_file, "w", encoding="utf-8") as f:
    json.dump(downloaded_info, f, indent=2)

print(f"\nRemaining download complete! Total in downloaded_info: {len(downloaded_info)}")
