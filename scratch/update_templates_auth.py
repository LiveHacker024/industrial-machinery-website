"""
Update build_batch1_clean.py and build_batch3.py with exact authenticity rules
and regenerate products.html, product-detail.html, and search.html.
"""

import os
import re

BASE_DIR = r"D:\Client Websites"

# 1. Update build_batch1_clean.py
b1_path = os.path.join(BASE_DIR, "scratch", "build_batch1_clean.py")
with open(b1_path, "r", encoding="utf-8") as f:
    b1_code = f.read()

# Replace card badge logic in products.html
old_card_badge = '''            let badgeClass = "badge-po";
            let badgeText = p.badgeLabel || "VERIFIED PO";
            if (p.statusType === "supplementary") {
              badgeClass = "badge-sup";
            } else if (p.statusType === "extended") {
              badgeClass = "badge-tech";
              badgeText = "AUTHENTIC PHOTO";
            }'''

new_card_badge = '''            let badgeClass = "badge-po";
            let badgeText = p.badgeLabel || "VERIFIED PO";
            if (p.statusType === "supplementary") {
              badgeClass = "badge-sup";
              badgeText = "SUPPLEMENTARY";
            } else if (p.statusType === "extended") {
              badgeClass = "badge-tech";
              badgeText = p.badgeLabel || (p.imageCategory === "illustrative" ? "SPECIFICATION VISUAL" : "AUTHENTIC PHOTO");
            }'''

if old_card_badge in b1_code:
    b1_code = b1_code.replace(old_card_badge, new_card_badge)

# Replace authBadge in product-detail.html
old_detail_auth = '''      if (product.statusType === "extended") {
        authBadge.className = "image-authenticity-badge auth-real";
        authBadgeText.textContent = "Authentic Industrial Photograph";
        authNoticeText.textContent = `${product.imageStatus || 'Authentic industrial equipment photograph'}. Verified from manufacturer documentation / open image archives.`;
      }'''

new_detail_auth = '''      if (product.statusType === "extended") {
        if (product.imageCategory === "illustrative") {
          authBadge.className = "image-authenticity-badge auth-illustrative";
          authBadgeText.textContent = "Illustrative Product Visual (Specification Reference)";
          authNoticeText.textContent = product.imageNote || "Illustrative commercial product photography representing standard industrial model specification and appearance; not actual client-owned equipment.";
        } else {
          authBadge.className = "image-authenticity-badge auth-real";
          authBadgeText.textContent = "Authentic Industrial Photograph";
          authNoticeText.textContent = `${product.imageStatus || 'Authentic industrial equipment photograph'}. Verified from manufacturer documentation / open image archives.`;
        }
      }'''

if old_detail_auth in b1_code:
    b1_code = b1_code.replace(old_detail_auth, new_detail_auth)

with open(b1_path, "w", encoding="utf-8") as f:
    f.write(b1_code)

print("build_batch1_clean.py updated.")

# 2. Update build_batch3.py
b3_path = os.path.join(BASE_DIR, "scratch", "build_batch3.py")
with open(b3_path, "r", encoding="utf-8") as f:
    b3_code = f.read()

old_b3_badge = '''            let badgeClass = "badge-po";
            let badgeText = p.badgeLabel || "VERIFIED PO";
            if (p.statusType === "supplementary") {
              badgeClass = "badge-sup";
              badgeText = "SUPPLEMENTARY";
            } else if (p.statusType === "extended") {
              badgeClass = "badge-tech";
              badgeText = "AUTHENTIC PHOTO";
            }'''

new_b3_badge = '''            let badgeClass = "badge-po";
            let badgeText = p.badgeLabel || "VERIFIED PO";
            if (p.statusType === "supplementary") {
              badgeClass = "badge-sup";
              badgeText = "SUPPLEMENTARY";
            } else if (p.statusType === "extended") {
              badgeClass = "badge-tech";
              badgeText = p.badgeLabel || (p.imageCategory === "illustrative" ? "SPECIFICATION VISUAL" : "AUTHENTIC PHOTO");
            }'''

if old_b3_badge in b3_code:
    b3_code = b3_code.replace(old_b3_badge, new_b3_badge)

with open(b3_path, "w", encoding="utf-8") as f:
    f.write(b3_code)

print("build_batch3.py updated.")
