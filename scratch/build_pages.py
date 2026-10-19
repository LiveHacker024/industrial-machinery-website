"""
Builder script to generate all 14 multi-page HTML documents for
M/s. PUKHRAJ HASTIMAL & CO. Industrial Machinery Website.
"""

import json
import os

# Common Navigation Generator
def get_header(active_page=""):
    pages = [
        ("Home", "index.html"),
        ("About Us", "about.html"),
        ("Products (33)", "products.html"),
        ("Categories", "categories.html"),
        ("Industries", "industries.html"),
        ("Downloads", "downloads.html"),
        ("Contact", "contact.html"),
    ]
    nav_links = []
    for label, url in pages:
        is_active = ' class="active" aria-current="page"' if active_page == label else ''
        nav_links.append(f'<a href="{url}"{is_active}>{label}</a>')
    
    quote_active = ' class="nav-cta active"' if active_page == "Request a Quote" else ' class="nav-cta"'

    return f"""  <!-- SITE HEADER & NAVIGATION -->
  <header class="site-header">
    <div class="container nav-wrap">
      <a class="brand" href="index.html" aria-label="Pukhraj Hastimal & Co. Homepage">
        <span class="brand-mark">PH</span>
        <span class="brand-copy">
          <strong>PUKHRAJ HASTIMAL & CO.</strong>
          <small>Industrial Equipment · Solutions · Trust</small>
        </span>
      </a>

      <button class="menu-toggle" id="menuToggle" aria-expanded="false" aria-controls="primaryNav" aria-label="Open navigation menu">
        <span></span><span></span><span></span>
      </button>

      <nav id="primaryNav" class="primary-nav" aria-label="Main navigation">
        {' '.join(nav_links)}
        <a href="quote.html"{quote_active}>Request a Quote <span aria-hidden="true">↗</span></a>
      </nav>
    </div>
  </header>"""

def get_footer():
    return """  <!-- SITE FOOTER -->
  <footer class="site-footer">
    <div class="container footer-main">
      <div class="footer-col-brand">
        <a class="brand footer-brand" href="index.html">
          <span class="brand-mark">PH</span>
          <span class="brand-copy">
            <strong>PUKHRAJ HASTIMAL & CO.</strong>
            <small>Precision Engineering · Powerful Performance</small>
          </span>
        </a>
        <p style="margin-top: 14px; font-size: 13.5px; color: #a4b8af; line-height: 1.6; max-width: 380px;">
          Supplier and contractor for industrial machinery, process thermal systems, plant utilities, and power distribution infrastructure.
        </p>
        <div style="margin-top: 14px; font-size: 12.5px; color: #879c93; font-family: var(--font-mono);">
          GSTIN: 27AFMPJ3478A1ZG<br>
          PO REF: PH/001/26-27
        </div>
      </div>

      <div class="footer-col">
        <h4 style="font-family: var(--font-heading); color: var(--white); font-size: 14px; margin-bottom: 12px; letter-spacing: 0.5px;">EQUIPMENT FLEET</h4>
        <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 8px; font-size: 13px;">
          <li><a href="products.html" style="color: #c2d4cb; text-decoration: none;">All 33 Machines</a></li>
          <li><a href="products.html?filter=po" style="color: #c2d4cb; text-decoration: none;">Original PO Items (01–08)</a></li>
          <li><a href="products.html?filter=supplementary" style="color: #c2d4cb; text-decoration: none;">Plant Utilities (09–13)</a></li>
          <li><a href="products.html?filter=extended" style="color: #c2d4cb; text-decoration: none;">Technical Specifications (14–33)</a></li>
          <li><a href="categories.html" style="color: #c2d4cb; text-decoration: none;">All 7 Product Categories</a></li>
        </ul>
      </div>

      <div class="footer-col">
        <h4 style="font-family: var(--font-heading); color: var(--white); font-size: 14px; margin-bottom: 12px; letter-spacing: 0.5px;">COMPANY & RESOURCES</h4>
        <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 8px; font-size: 13px;">
          <li><a href="about.html" style="color: #c2d4cb; text-decoration: none;">About Our Company</a></li>
          <li><a href="industries.html" style="color: #c2d4cb; text-decoration: none;">Industries & Applications</a></li>
          <li><a href="downloads.html" style="color: #c2d4cb; text-decoration: none;">Downloads & Datasheets</a></li>
          <li><a href="faq.html" style="color: #c2d4cb; text-decoration: none;">Frequently Asked Questions</a></li>
          <li><a href="contact.html" style="color: #c2d4cb; text-decoration: none;">Contact Procurement</a></li>
        </ul>
      </div>

      <div class="footer-col">
        <h4 style="font-family: var(--font-heading); color: var(--white); font-size: 14px; margin-bottom: 12px; letter-spacing: 0.5px;">LEGAL & COMPLIANCE</h4>
        <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 8px; font-size: 13px;">
          <li><a href="privacy.html" style="color: #c2d4cb; text-decoration: none;">Privacy Policy</a></li>
          <li><a href="terms.html" style="color: #c2d4cb; text-decoration: none;">Terms & Conditions</a></li>
          <li><a href="shipping.html" style="color: #c2d4cb; text-decoration: none;">Shipping & Delivery</a></li>
          <li><a href="search.html" style="color: #c2d4cb; text-decoration: none;">Catalogue Search</a></li>
          <li><a href="quote.html" style="color: var(--lime); font-weight: 700; text-decoration: none;">Request Quotation ↗</a></li>
        </ul>
      </div>
    </div>

    <div class="container footer-bottom" style="margin-top: 36px; padding-top: 20px; border-top: 1px solid rgba(255,255,255,0.08); display: flex; flex-wrap: wrap; justify-content: space-between; gap: 12px; font-size: 12px; color: #7f958a;">
      <span>© 2026 M/s. Pukhraj Hastimal & Co. · Registered Office: Office No 03, 2nd Floor, 7 Kika Bhai Mansion, Gulalwadi, Mumbai - 400004</span>
      <span>Official Contact: <a href="mailto:pukhrajhastimal@gmail.com" style="color: var(--lime);">pukhrajhastimal@gmail.com</a></span>
    </div>
  </footer>

  <!-- Global Mobile Nav Toggle Script -->
  <script>
    const menuToggle = document.getElementById('menuToggle');
    const primaryNav = document.getElementById('primaryNav');
    if (menuToggle && primaryNav) {
      menuToggle.addEventListener('click', () => {
        const isOpen = primaryNav.classList.toggle('open');
        menuToggle.setAttribute('aria-expanded', String(isOpen));
      });
    }
  </script>"""

print("Helper functions ready.")
