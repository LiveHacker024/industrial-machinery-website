"""
Update products-data.js with authentic labeling rules:
- Items 1-13: "Illustrative Product Visual (Specification Reference)"
- Items 14-20: "Authentic Industrial Photograph (Matched)"
- PO & Supplementary: Authentic Client Photographs strictly preserved
"""

import os
import json
import re

BASE_DIR = r"D:\Client Websites"
JS_PATH = os.path.join(BASE_DIR, "assets", "products-data.js")

with open(JS_PATH, "r", encoding="utf-8") as f:
    content = f.read()

m = re.search(r"window\.PRODUCTS_DATA\s*=\s*(\{[\s\S]*?\});", content)
if not m:
    raise ValueError("Could not find window.PRODUCTS_DATA")

products = json.loads(m.group(1))

# Update items 1 to 13 as Illustrative Product Visuals (Specification Reference)
for i in range(1, 14):
    keys = [
        "ext1_vacuum_pump", "ext2_gear_pump", "ext3_dosing_pump", "ext4_circulation_pump",
        "ext5_plate_exchanger", "ext6_refrig_condenser", "ext7_evaporator", "ext8_storage_tank",
        "ext9_mixing_tank", "ext10_air_receiver", "ext11_centrifugal_blower", "ext12_air_dryer",
        "ext13_filtration_system"
    ]
    k = keys[i-1]
    if k in products:
        products[k]["imageStatus"] = "Illustrative Product Visual (Specification Reference)"
        products[k]["imageCategory"] = "illustrative"
        products[k]["badgeLabel"] = "SPECIFICATION VISUAL"
        products[k]["imageNote"] = "Illustrative commercial product photography representing standard industrial equipment specification; not actual client-owned equipment."

# Update items 14 to 20 as Authentic Industrial Photographs
auth_notes = {
    "ext14_bag_filter": "Authentic Industrial Photograph (Bag Filter Multi-Chamber Housing / Cement Plant Hopper)",
    "ext15_cartridge_filter": "Authentic Industrial Photograph (Wasserfilter Industrial Cartridge Housing)",
    "ext16_ro_system": "Authentic Industrial Photograph (Skid-Mounted Reverse Osmosis Plant)",
    "ext17_water_softener": "Authentic Industrial Photograph (Automated Cation-Exchange Water Softener Plant)",
    "ext18_diesel_generator": "Authentic Industrial Photograph (Caterpillar Olympian Acoustic Canopy DG Set)",
    "ext19_electric_motor": "Authentic Industrial Photograph (Heavy-Duty TEFC Three-Phase Induction Motor)",
    "ext20_mcc_panel": "Authentic Industrial Photograph (Compartmentalized Industrial Switchgear MCC Panel)",
}

for k, status_str in auth_notes.items():
    if k in products:
        products[k]["imageStatus"] = status_str
        products[k]["imageCategory"] = "authentic"
        products[k]["badgeLabel"] = "AUTHENTIC PHOTO"
        products[k]["imageNote"] = "Authentic industrial equipment photograph sourced from authorized plant / industrial archives."

# Re-serialize products-data.js
new_json_str = json.dumps(products, indent=2)
new_content = f"""/**
 * M/s. PUKHRAJ HASTIMAL & CO. — Central Product Catalogue Database
 * Total Verified Products: 33 (8 Original PO + 5 Supplementary + 20 Extended)
 * With High-Resolution 1600x1200 Industrial Machine Photographs & Verified Indian Market Reference Prices
 */

window.PRODUCTS_DATA = {new_json_str};

if (typeof window !== 'undefined') {{
  window.products = window.PRODUCTS_DATA;
}}
if (typeof module !== 'undefined' && module.exports) {{
  module.exports = window.PRODUCTS_DATA;
}}
"""

with open(JS_PATH, "w", encoding="utf-8") as f:
    f.write(new_content)

print(f"assets/products-data.js updated successfully with authenticity classifications.")
