"""
Process all 20 industrial machinery photographs to premium 1600x1200 (4:3) standard.
Consistent studio lighting, neutral framing, realistic textures, and sharp focus.
"""

import os
from PIL import Image, ImageEnhance, ImageOps

BASE_DIR = r"D:\Client Websites"
DEST_DIR = os.path.join(BASE_DIR, "assets", "machines", "additional")
os.makedirs(DEST_DIR, exist_ok=True)

TARGET_W, TARGET_H = 1600, 1200

# Map of index to source image
sources = {
    1: (r"C:\Users\liveh\.gemini\antigravity-ide\brain\efce830e-6dea-4524-9d6c-e2cb41ce4741\ext_vacuum_pump_1792398882980.jpg", "ext-01-vacuum-pump.jpg", "crop"),
    2: (r"C:\Users\liveh\.gemini\antigravity-ide\brain\efce830e-6dea-4524-9d6c-e2cb41ce4741\ext_gear_pump_1792399039941.jpg", "ext-02-gear-pump.jpg", "crop"),
    3: (r"C:\Users\liveh\.gemini\antigravity-ide\brain\efce830e-6dea-4524-9d6c-e2cb41ce4741\ext_dosing_pump_1792399060867.jpg", "ext-03-dosing-pump.jpg", "crop"),
    4: (r"C:\Users\liveh\.gemini\antigravity-ide\brain\efce830e-6dea-4524-9d6c-e2cb41ce4741\ext_circulation_pump_1792399085516.jpg", "ext-04-circulation-pump.jpg", "crop"),
    5: (r"C:\Users\liveh\.gemini\antigravity-ide\brain\efce830e-6dea-4524-9d6c-e2cb41ce4741\ext_plate_exchanger_1792399107668.jpg", "ext-05-plate-exchanger.jpg", "crop"),
    6: (r"C:\Users\liveh\.gemini\antigravity-ide\brain\efce830e-6dea-4524-9d6c-e2cb41ce4741\ext_refrig_condenser_1792399127106.jpg", "ext-06-refrig-condenser.jpg", "crop"),
    7: (r"C:\Users\liveh\.gemini\antigravity-ide\brain\efce830e-6dea-4524-9d6c-e2cb41ce4741\ext_evaporator_1792399184393.jpg", "ext-07-evaporator.jpg", "crop"),
    8: (r"C:\Users\liveh\.gemini\antigravity-ide\brain\efce830e-6dea-4524-9d6c-e2cb41ce4741\ext_storage_tank_1792399206345.jpg", "ext-08-storage-tank.jpg", "crop"),
    9: (r"C:\Users\liveh\.gemini\antigravity-ide\brain\efce830e-6dea-4524-9d6c-e2cb41ce4741\ext_mixing_tank_1792399225560.jpg", "ext-09-mixing-tank.jpg", "crop"),
    10: (r"C:\Users\liveh\.gemini\antigravity-ide\brain\efce830e-6dea-4524-9d6c-e2cb41ce4741\ext_air_receiver_1792399252426.jpg", "ext-10-air-receiver.jpg", "crop"),
    11: (r"C:\Users\liveh\.gemini\antigravity-ide\brain\efce830e-6dea-4524-9d6c-e2cb41ce4741\ext_centrifugal_blower_1792399270545.jpg", "ext-11-centrifugal-blower.jpg", "crop"),
    12: (r"C:\Users\liveh\.gemini\antigravity-ide\brain\efce830e-6dea-4524-9d6c-e2cb41ce4741\ext_air_dryer_1792399289790.jpg", "ext-12-air-dryer.jpg", "crop"),
    13: (r"C:\Users\liveh\.gemini\antigravity-ide\brain\efce830e-6dea-4524-9d6c-e2cb41ce4741\ext_filtration_system_1792399314321.jpg", "ext-13-filtration-system.jpg", "crop"),
    14: (os.path.join(BASE_DIR, "scratch", "highres_raw", "14_bag_filter.jpg"), "ext-14-bag-filter.jpg", "crop"),
    15: (os.path.join(BASE_DIR, "scratch", "highres_raw", "15_cartridge.jpg"), "ext-15-cartridge-filter.jpg", "fit_canvas"),
    16: (os.path.join(BASE_DIR, "scratch", "highres_raw", "16_ro.jpg"), "ext-16-ro-system.jpg", "crop"),
    17: (os.path.join(BASE_DIR, "scratch", "highres_raw", "17_softener.jpg"), "ext-17-water-softener.jpg", "crop"),
    18: (os.path.join(BASE_DIR, "scratch", "highres_raw", "18_dg.jpg"), "ext-18-diesel-generator.jpg", "crop"),
    19: (os.path.join(BASE_DIR, "scratch", "highres_raw", "19_motor.jpg"), "ext-19-electric-motor.jpg", "crop"),
    20: (os.path.join(BASE_DIR, "scratch", "highres_raw", "20_mcc.jpg"), "ext-20-mcc-panel.jpg", "crop"),
}

for idx in range(1, 21):
    src_path, filename, mode = sources[idx]
    dest_path = os.path.join(DEST_DIR, filename)
    
    assert os.path.exists(src_path), f"Missing source: {src_path}"
    im = Image.open(src_path)
    if im.mode != "RGB":
        im = im.convert("RGB")
        
    w, h = im.size
    target_aspect = 4.0 / 3.0
    current_aspect = w / h
    
    if mode == "fit_canvas":
        # Fit vertically or horizontally into 1600x1200 on clean studio grey canvas
        scale = min(TARGET_W / w, TARGET_H / h) * 0.90
        nw, nh = int(w * scale), int(h * scale)
        im_resized = im.resize((nw, nh), Image.Resampling.LANCZOS)
        
        # Studio canvas matching the other images (#e8ebea)
        canvas = Image.new("RGB", (TARGET_W, TARGET_H), (235, 238, 237))
        pos_x = (TARGET_W - nw) // 2
        pos_y = (TARGET_H - nh) // 2
        canvas.paste(im_resized, (pos_x, pos_y))
        out = canvas
    else:
        if abs(current_aspect - target_aspect) < 0.02:
            out = im.resize((TARGET_W, TARGET_H), Image.Resampling.LANCZOS)
        elif current_aspect > target_aspect:
            # Wider than 4:3 -> center crop sides
            new_w = int(h * target_aspect)
            left = (w - new_w) // 2
            im_cropped = im.crop((left, 0, left + new_w, h))
            out = im_cropped.resize((TARGET_W, TARGET_H), Image.Resampling.LANCZOS)
        else:
            # Taller than 4:3 -> center crop top/bottom
            new_h = int(w / target_aspect)
            top = (h - new_h) // 2
            im_cropped = im.crop((0, top, w, top + new_h))
            out = im_cropped.resize((TARGET_W, TARGET_H), Image.Resampling.LANCZOS)
            
    # Subtle enhancement: slight contrast and sharpness for crisp B2B industrial look
    enhancer = ImageEnhance.Sharpness(out)
    out = enhancer.enhance(1.08)
    
    out.save(dest_path, "JPEG", quality=92, optimize=True)
    size_kb = os.path.getsize(dest_path) // 1024
    print(f"[{idx:02d}/20] {filename} saved: {out.size[0]}x{out.size[1]} ({size_kb} KB)")

print("\nAll 20 industrial machinery photographs processed to 1600x1200 4:3 successfully!")
