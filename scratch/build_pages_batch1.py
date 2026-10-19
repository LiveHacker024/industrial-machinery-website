"""
Script to build all 14 multi-page HTML documents for M/s. PUKHRAJ HASTIMAL & CO.
"""

import os
import json

BASE_DIR = r"D:\Client Websites"

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

# -----------------------------------------------------------------------------
# PAGE 2: products.html (ALL PRODUCTS)
# -----------------------------------------------------------------------------
def build_products_page():
    content = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#0d1a16">
  <meta name="description" content="Explore the verified 33 industrial machinery fleet of M/s. Pukhraj Hastimal & Co. Including 8 original purchase order items, 5 supplementary utilities, and 20 extended industrial machines.">
  <title>Industrial Machinery Catalogue (33 Products) | Pukhraj Hastimal & Co.</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <a class="skip-link" href="#main">Skip to main content</a>
  {get_header("Products (33)")}

  <main id="main">
    <section class="subpage-hero">
      <div class="container">
        <nav class="breadcrumbs" aria-label="Breadcrumb">
          <a href="index.html">Home</a>
          <span class="sep">/</span>
          <span class="current">All Products Catalogue</span>
        </nav>
        <h1 class="page-title">Industrial Machinery <em>Catalogue (33).</em></h1>
        <p class="hero-subheading">
          Explore our complete verified fleet of 33 heavy-duty industrial equipment units: 8 original purchase order line items (PO Ref: PH/001/26-27), 5 supplementary facility utilities, and 20 extended process machines.
        </p>
      </div>
    </section>

    <section class="section-pad">
      <div class="container">
        <!-- Search and Filter Toolbar -->
        <div class="catalogue-controls" style="margin-bottom: 24px;">
          <label class="search-box">
            <span class="search-icon" aria-hidden="true">⌕</span>
            <input id="searchInput" type="search" placeholder="Search by machine name, HSN code, capacity, or specifications..." aria-label="Search industrial machinery catalogue">
          </label>
          <div style="display: flex; gap: 12px; align-items: center; flex-wrap: wrap;">
            <label for="sortSelect" style="font-size: 13px; font-weight: 600; color: #43584e;">Sort By:</label>
            <select id="sortSelect" style="padding: 10px 16px; border-radius: var(--radius-sm); border: 1px solid var(--line); background: var(--white); font-size: 13px; font-weight: 600; color: var(--forest);">
              <option value="default">Catalogue Order (PO First)</option>
              <option value="name-asc">Product Name (A – Z)</option>
              <option value="name-desc">Product Name (Z – A)</option>
              <option value="category">Category</option>
            </select>
          </div>
        </div>

        <!-- Category & Group Filter Tabs -->
        <div class="filter-tabs-wrap" id="filterTabs" role="group" aria-label="Filter equipment categories">
          <button class="filter-btn-pill active" data-filter="all">All Equipment <span>33</span></button>
          <button class="filter-btn-pill" data-filter="po">Verified PO Items <span>8</span></button>
          <button class="filter-btn-pill" data-filter="supplementary">Plant Utilities <span>5</span></button>
          <button class="filter-btn-pill" data-filter="extended">Technical Reference <span>20</span></button>
          <button class="filter-btn-pill" data-filter="cat-thermal">Thermal & Heat <span>5</span></button>
          <button class="filter-btn-pill" data-filter="cat-pumps">Pumps & Handling <span>4</span></button>
          <button class="filter-btn-pill" data-filter="cat-air">Air & Gas <span>3</span></button>
          <button class="filter-btn-pill" data-filter="cat-water">Water & Filtration <span>5</span></button>
          <button class="filter-btn-pill" data-filter="cat-vessels">Vessels & Tanks <span>3</span></button>
          <button class="filter-btn-pill" data-filter="cat-electrical">Electrical & Power <span>5</span></button>
        </div>

        <div style="display: flex; justify-content: space-between; align-items: center; margin: 24px 0 16px; flex-wrap: wrap; gap: 10px;">
          <p class="results-count" id="resultsCount" style="margin: 0;" aria-live="polite">Showing 33 Verified Industrial Machines</p>
          <div style="font-size: 12.5px; color: var(--muted); display: flex; align-items: center; gap: 16px;">
            <span><strong style="color: #21613b;">●</strong> Authentic Photo</span>
            <span><strong style="color: #1a73e8;">●</strong> Technical Schematic</span>
          </div>
        </div>

        <!-- Product Cards Grid -->
        <div class="equipment-grid" id="equipmentGrid">
          <!-- Dynamically populated from assets/products-data.js -->
        </div>

        <!-- Empty Search State -->
        <div class="empty-state" id="emptyState" hidden style="margin-top: 40px; padding: 60px 20px; text-align: center; background: var(--white); border: 1px solid var(--line); border-radius: var(--radius-md);">
          <div style="font-size: 40px; margin-bottom: 12px;">🔍</div>
          <h3 style="font-family: var(--font-heading); color: var(--forest-dark); margin: 0 0 8px;">No matching industrial equipment found.</h3>
          <p style="color: var(--muted); max-width: 500px; margin: 0 auto 20px;">We could not find any machines matching your filter. Try searching for terms like 'boiler', 'pump', 'transformer', 'filter', or 'chiller'.</p>
          <button id="resetSearchBtn" class="nav-cta" style="cursor: pointer;">Reset All Filters</button>
        </div>
      </div>
    </section>
  </main>

  {get_footer()}

  <script src="assets/products-data.js"></script>
  <script>
    document.addEventListener("DOMContentLoaded", () => {
      const grid = document.getElementById("equipmentGrid");
      const searchInput = document.getElementById("searchInput");
      const sortSelect = document.getElementById("sortSelect");
      const filterTabs = document.getElementById("filterTabs");
      const resultsCount = document.getElementById("resultsCount");
      const emptyState = document.getElementById("emptyState");
      const resetSearchBtn = document.getElementById("resetSearchBtn");

      let activeFilter = "all";
      let searchQuery = "";
      let sortOrder = "default";

      // Parse URL parameters (e.g., products.html?filter=po or ?category=thermal)
      const urlParams = new URLSearchParams(window.location.search);
      if (urlParams.has("filter")) {
        activeFilter = urlParams.get("filter");
      } else if (urlParams.has("category")) {
        activeFilter = "cat-" + urlParams.get("category");
      }
      if (urlParams.has("q")) {
        searchQuery = urlParams.get("q");
        searchInput.value = searchQuery;
      }

      // Update active pill button
      filterTabs.querySelectorAll(".filter-btn-pill").forEach(btn => {
        const isMatch = btn.dataset.filter === activeFilter;
        btn.classList.toggle("active", isMatch);
      });

      function renderProducts() {
        const productList = Object.values(window.PRODUCTS_DATA || {});
        let filtered = productList.filter(item => {
          // Category / Group Filter
          if (activeFilter === "po" && item.statusType !== "po") return false;
          if (activeFilter === "supplementary" && item.statusType !== "supplementary") return false;
          if (activeFilter === "extended" && item.statusType !== "extended") return false;
          if (activeFilter.startsWith("cat-")) {
            const cat = activeFilter.replace("cat-", "");
            if (item.category !== cat) return false;
          }

          // Search Filter
          if (searchQuery.trim() !== "") {
            const q = searchQuery.toLowerCase();
            const searchableText = [
              item.name,
              item.shortName,
              item.categoryLabel,
              item.hsn || "",
              item.rate || "",
              item.description,
              item.applications,
              (item.specs || []).map(s => s.label + " " + s.value).join(" "),
              (item.features || []).join(" ")
            ].join(" ").toLowerCase();

            if (!searchableText.includes(q)) return false;
          }

          return true;
        });

        // Sorting
        if (sortOrder === "name-asc") {
          filtered.sort((a, b) => a.shortName.localeCompare(b.shortName));
        } else if (sortOrder === "name-desc") {
          filtered.sort((a, b) => b.shortName.localeCompare(a.shortName));
        } else if (sortOrder === "category") {
          filtered.sort((a, b) => a.categoryLabel.localeCompare(b.categoryLabel));
        }

        // Render Cards
        grid.innerHTML = "";
        if (filtered.length === 0) {
          emptyState.hidden = false;
          grid.hidden = true;
          resultsCount.textContent = "0 Products matching current criteria";
        } else {
          emptyState.hidden = true;
          grid.hidden = false;
          resultsCount.textContent = `Showing ${filtered.length} of ${productList.length} Verified Industrial Machines`;

          filtered.forEach((p, idx) => {
            const card = document.createElement("article");
            card.className = "equipment-card";
            
            let badgeClass = "badge-po";
            let badgeText = p.badgeLabel || "VERIFIED PO";
            if (p.statusType === "supplementary") {
              badgeClass = "badge-sup";
            } else if (p.statusType === "extended") {
              badgeClass = "badge-tech";
              badgeText = "SPECIFICATION REFERENCE";
            }

            const itemNumber = String(p.poItemNo || (idx + 1)).padStart(2, '0');
            const rateBadge = p.rate && p.rate.includes("₹")
              ? `<div class="card-rate-tag">PO Rate: ${p.rate} (Qty: ${p.qty})</div>`
              : `<div class="card-rate-tag sup-rate">Status: Contact for Quotation</div>`;

            card.innerHTML = `
              <a class="card-image-wrap" href="product-detail.html?id=${encodeURIComponent(p.id)}" aria-label="View specifications for ${p.shortName}">
                <img src="${p.image}" alt="${p.alt}" loading="lazy">
                <span class="card-number">${itemNumber}</span>
                <span class="card-badge ${badgeClass}">${badgeText}</span>
                <span class="card-arrow" aria-hidden="true">↗</span>
              </a>
              <div class="card-body">
                <div class="card-meta">
                  <span>${p.categoryLabel.toUpperCase()}</span>
                  <span>${p.hsn ? 'HSN: ' + p.hsn : 'CODE: ' + p.id.toUpperCase()}</span>
                </div>
                <h3><a href="product-detail.html?id=${encodeURIComponent(p.id)}" style="color: inherit; text-decoration: none;">${p.shortName}</a></h3>
                <p>${p.description}</p>
                ${rateBadge}
                <div style="display: flex; gap: 10px; margin-top: 16px;">
                  <a class="card-view-btn" href="product-detail.html?id=${encodeURIComponent(p.id)}" style="flex: 1; text-align: center; text-decoration: none; justify-content: center;">
                    <span>View Specifications</span>
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                  </a>
                  <a class="nav-cta" href="quote.html?product=${encodeURIComponent(p.id)}" title="Request quote for ${p.shortName}" style="padding: 0 14px; display: inline-flex; align-items: center; justify-content: center;">
                    <span>RFQ</span>
                  </a>
                </div>
              </div>
            `;
            grid.appendChild(card);
          });
        }
      }

      // Event Listeners
      filterTabs.querySelectorAll(".filter-btn-pill").forEach(btn => {
        btn.addEventListener("click", () => {
          activeFilter = btn.dataset.filter;
          filterTabs.querySelectorAll(".filter-btn-pill").forEach(b => b.classList.toggle("active", b === btn));
          renderProducts();
        });
      });

      searchInput.addEventListener("input", (e) => {
        searchQuery = e.target.value;
        renderProducts();
      });

      sortSelect.addEventListener("change", (e) => {
        sortOrder = e.target.value;
        renderProducts();
      });

      resetSearchBtn.addEventListener("click", () => {
        searchInput.value = "";
        searchQuery = "";
        activeFilter = "all";
        filterTabs.querySelectorAll(".filter-btn-pill").forEach(b => b.classList.toggle("active", b.dataset.filter === "all"));
        renderProducts();
      });

      // Initial Render
      renderProducts();
    });
  </script>
</body>
</html>
"""
    with open(os.path.join(BASE_DIR, "products.html"), "w", encoding="utf-8") as f:
        f.write(content)
    print("products.html built.")

# -----------------------------------------------------------------------------
# PAGE 3: product-detail.html (DEDICATED PRODUCT DETAIL ROUTE)
# -----------------------------------------------------------------------------
def build_product_detail_page():
    content = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#0d1a16">
  <meta name="description" content="Technical specifications, engineering parameters, applications, and RFQ request for industrial equipment supplied by M/s. Pukhraj Hastimal & Co.">
  <title id="pageMetaTitle">Product Specifications | Pukhraj Hastimal & Co.</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <a class="skip-link" href="#main">Skip to main content</a>
  {get_header("Products (33)")}

  <main id="main">
    <section class="subpage-hero">
      <div class="container">
        <nav class="breadcrumbs" aria-label="Breadcrumb">
          <a href="index.html">Home</a>
          <span class="sep">/</span>
          <a href="products.html">Products Catalogue</a>
          <span class="sep">/</span>
          <span class="current" id="breadcrumbCurrent">Equipment Details</span>
        </nav>
        <h1 class="page-title" id="heroProductTitle">Technical <em>Equipment Profile.</em></h1>
        <p class="hero-subheading" id="heroProductSubheading">
          Detailed engineering parameters, verified documentation, applications, and direct procurement enquiry.
        </p>
      </div>
    </section>

    <section class="section-pad">
      <div class="container">
        <div class="product-detail-layout" id="productDetailLayout">
          
          <!-- Left Column: Gallery & Authenticity Notice -->
          <div class="product-detail-gallery">
            <div class="main-image-frame">
              <img id="detailImage" src="assets/machines/po-01-boiler.png" alt="Industrial machinery photograph">
            </div>

            <div style="margin-top: 18px; display: flex; flex-direction: column; gap: 10px;">
              <div id="authBadge" class="image-authenticity-badge auth-real">
                <span>●</span> <span id="authBadgeText">Authentic Client Photograph</span>
              </div>
              <div class="gallery-notice" id="authNoticeText">
                This image represents authentic operational machinery documented from the official project delivery records of Purchase Order Ref: PH/001/26-27.
              </div>
            </div>

            <div style="margin-top: 24px; padding-top: 20px; border-top: 1px solid var(--line);">
              <h4 style="font-family: var(--font-heading); font-size: 14px; color: var(--forest-dark); margin: 0 0 10px;">DOCUMENTATION STATUS</h4>
              <div style="font-size: 13px; color: var(--muted); line-height: 1.6;" id="docStatusDesc">
                Verified against official commercial documentation. All stated rates and quantities correspond to approved procurement schedules.
              </div>
            </div>
          </div>

          <!-- Right Column: Details, Specifications & RFQ -->
          <div class="product-detail-info">
            <div class="product-detail-meta">
              <span id="detailBadge" class="dialog-po-tag po-verified">VERIFIED PO LINE ITEM</span>
              <span id="detailCat" style="font-family: var(--font-mono); font-size: 11px; font-weight: 700; color: var(--forest-light); background: #f0f4f1; padding: 6px 12px; border-radius: 4px;">THERMAL & HEAT</span>
            </div>

            <h2 class="product-detail-title" id="detailTitle">BOILER 850 KG/HR CAPACITY WITH OIL & GAS BURNER DUAL</h2>
            
            <p class="product-detail-desc" id="detailDesc">
              Industrial high-pressure steam boiler with a rated capacity of 850 kg/hr, equipped with an automated dual-fuel burner firing light oil and natural gas.
            </p>

            <div id="rateContainer" style="padding: 14px 18px; background: #eef7eb; border: 1px solid #c2e2b3; border-radius: 8px;">
              <span style="font-size: 11.5px; font-family: var(--font-mono); font-weight: 700; color: #21613b; display: block; margin-bottom: 4px;">PURCHASE ORDER PRICING / COMMERCIAL STATUS</span>
              <strong id="rateValue" style="font-size: 20px; color: #164627; font-family: var(--font-heading);">₹16,50,000.00 (Qty: 1 NOS)</strong>
            </div>

            <div class="product-actions-bar">
              <a class="btn-hero-primary" id="btnQuoteNow" href="quote.html" style="text-decoration: none;">
                <span>Request a Quote for this Machine</span>
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
              </a>
              <a class="nav-cta" href="downloads.html" style="text-decoration: none;">
                <span>Datasheet Requisition ↗</span>
              </a>
            </div>

            <div>
              <h3 style="font-family: var(--font-heading); font-size: 18px; color: var(--forest-dark); margin: 0 0 12px;">Key Engineering Features</h3>
              <ul class="features-list" id="featuresList">
                <!-- Dynamically generated features -->
              </ul>
            </div>

            <div style="margin-top: 10px;">
              <h3 style="font-family: var(--font-heading); font-size: 18px; color: var(--forest-dark); margin: 0 0 8px;">Industrial Applications</h3>
              <p id="applicationsText" style="font-size: 14px; line-height: 1.6; color: #3b5045; margin: 0;">
                Chemical reboilers, reaction vessels, pharmaceutical heating, food processing, and distillation columns.
              </p>
            </div>

            <div style="margin-top: 14px;">
              <h3 style="font-family: var(--font-heading); font-size: 18px; color: var(--forest-dark); margin: 0 0 12px;">Full Technical Specifications</h3>
              <table class="specs-table" style="width: 100%;">
                <tbody id="specsTableBody">
                  <!-- Dynamically populated spec rows -->
                </tbody>
              </table>
            </div>

          </div>

        </div>

        <!-- Related Industrial Equipment -->
        <div style="margin-top: 64px; padding-top: 40px; border-top: 1px solid var(--line);">
          <div style="display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 24px; flex-wrap: wrap; gap: 12px;">
            <div>
              <p class="eyebrow" style="margin-bottom: 4px;">ASSOCIATED MACHINERY</p>
              <h3 style="font-family: var(--font-heading); font-size: 24px; color: var(--forest-dark); margin: 0;">Related Plant Equipment.</h3>
            </div>
            <a href="products.html" class="cat-link">View Full 33-Machine Fleet <span>→</span></a>
          </div>

          <div class="related-products-grid" id="relatedGrid">
            <!-- Dynamically populated related items -->
          </div>
        </div>

      </div>
    </section>
  </main>

  {get_footer()}

  <script src="assets/products-data.js"></script>
  <script>
    document.addEventListener("DOMContentLoaded", () => {
      const urlParams = new URLSearchParams(window.location.search);
      const productId = urlParams.get("id") || "po1_boiler";
      const product = (window.PRODUCTS_DATA && window.PRODUCTS_DATA[productId]) || (window.PRODUCTS_DATA && window.PRODUCTS_DATA["po1_boiler"]);

      if (!product) return;

      // Title & Meta
      document.title = `${product.shortName} | Technical Specifications | Pukhraj Hastimal & Co.`;
      document.getElementById("breadcrumbCurrent").textContent = product.shortName;
      document.getElementById("heroProductTitle").innerHTML = `${product.shortName}<em>.</em>`;
      document.getElementById("heroProductSubheading").textContent = product.description;

      // Image & Authenticity
      const detailImage = document.getElementById("detailImage");
      detailImage.src = product.image;
      detailImage.alt = product.alt || product.shortName;

      const authBadge = document.getElementById("authBadge");
      const authBadgeText = document.getElementById("authBadgeText");
      const authNoticeText = document.getElementById("authNoticeText");

      if (product.statusType === "extended") {
        authBadge.className = "image-authenticity-badge auth-schematic";
        authBadgeText.textContent = "Technical Reference Schematic (CAD Layout)";
        authNoticeText.textContent = "This technical schematic depicts standard engineering parameters. Authentic certified machinery photographs and manufacturer drawings are issued upon formal RFQ enquiry.";
      } else if (product.statusType === "supplementary") {
        authBadge.className = "image-authenticity-badge auth-real";
        authBadgeText.textContent = "Authentic Client Photograph (Facility Utility)";
        authNoticeText.textContent = "Authentic machinery photograph documented from the client's operational plant inventory. Offered as associated industrial utility.";
      } else {
        authBadge.className = "image-authenticity-badge auth-real";
        authBadgeText.textContent = "Authentic Client Photograph (PO Matched)";
        authNoticeText.textContent = "Authentic machine photograph verified directly against Purchase Order Ref: PH/001/26-27 line items.";
      }

      // Details
      document.getElementById("detailCat").textContent = product.categoryLabel.toUpperCase();
      const detailBadge = document.getElementById("detailBadge");
      if (product.statusType === "po") {
        detailBadge.className = "dialog-po-tag po-verified";
        detailBadge.textContent = `VERIFIED PO LINE ITEM · ITEM #${String(product.poItemNo).padStart(2, '0')}`;
      } else if (product.statusType === "supplementary") {
        detailBadge.className = "dialog-po-tag po-supplementary";
        detailBadge.textContent = "SUPPLEMENTARY PLANT UTILITY (NOT IN PO)";
      } else {
        detailBadge.className = "dialog-po-tag po-extended";
        detailBadge.textContent = "TECHNICAL SPECIFICATION CATALOGUE";
      }

      document.getElementById("detailTitle").textContent = product.name;
      document.getElementById("detailDesc").textContent = product.description;

      // Pricing / Commercial container
      const rateContainer = document.getElementById("rateContainer");
      const rateValue = document.getElementById("rateValue");
      if (product.rate && product.rate.includes("₹")) {
        rateContainer.style.background = "#eef7eb";
        rateContainer.style.borderColor = "#c2e2b3";
        rateValue.textContent = `${product.rate} (Document Qty: ${product.qty})`;
      } else {
        rateContainer.style.background = "#f4f6f2";
        rateContainer.style.borderColor = "#d9ded7";
        rateValue.textContent = "Contact for Quotation & Custom Sizing";
      }

      // RFQ button prefill link
      const btnQuoteNow = document.getElementById("btnQuoteNow");
      btnQuoteNow.href = `quote.html?product=${encodeURIComponent(product.id)}`;

      // Features list
      const featuresList = document.getElementById("featuresList");
      featuresList.innerHTML = "";
      (product.features || []).forEach(f => {
        const li = document.createElement("li");
        li.textContent = f;
        featuresList.appendChild(li);
      });

      // Applications
      document.getElementById("applicationsText").textContent = product.applications || "General industrial process and manufacturing operations.";

      // Specs table
      const specsTableBody = document.getElementById("specsTableBody");
      specsTableBody.innerHTML = "";
      (product.specs || []).forEach(s => {
        const tr = document.createElement("tr");
        tr.innerHTML = `
          <td class="spec-label">${s.label}</td>
          <td class="spec-value">${s.value}</td>
        `;
        specsTableBody.appendChild(tr);
      });

      // Related Products
      const relatedGrid = document.getElementById("relatedGrid");
      relatedGrid.innerHTML = "";
      const relatedIds = product.related || [];
      relatedIds.forEach(relId => {
        const rel = window.PRODUCTS_DATA[relId];
        if (!rel) return;
        const card = document.createElement("div");
        card.className = "equipment-card";
        card.style.background = "var(--white)";
        card.innerHTML = `
          <a class="card-image-wrap" href="product-detail.html?id=${encodeURIComponent(rel.id)}" style="aspect-ratio: 16/10;">
            <img src="${rel.image}" alt="${rel.shortName}" loading="lazy">
          </a>
          <div class="card-body" style="padding: 16px;">
            <div class="card-meta" style="font-size: 11px;"><span>${rel.categoryLabel.toUpperCase()}</span></div>
            <h4 style="font-size: 15px; margin: 4px 0 8px; font-family: var(--font-heading);"><a href="product-detail.html?id=${encodeURIComponent(rel.id)}" style="color: inherit; text-decoration: none;">${rel.shortName}</a></h4>
            <a class="cat-link" href="product-detail.html?id=${encodeURIComponent(rel.id)}" style="font-size: 12.5px;">View Specs →</a>
          </div>
        `;
        relatedGrid.appendChild(card);
      });
    });
  </script>
</body>
</html>
"""
    with open(os.path.join(BASE_DIR, "product-detail.html"), "w", encoding="utf-8") as f:
        f.write(content)
    print("product-detail.html built.")

# -----------------------------------------------------------------------------
# PAGE 4: categories.html (PRODUCT CATEGORIES)
# -----------------------------------------------------------------------------
def build_categories_page():
    content = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#0d1a16">
  <meta name="description" content="Explore equipment categories offered by M/s. Pukhraj Hastimal & Co.: Thermal systems, pumps, compressors, water treatment, electrical substations, and process vessels.">
  <title>Industrial Equipment Categories | Pukhraj Hastimal & Co.</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <a class="skip-link" href="#main">Skip to main content</a>
  {get_header("Categories")}

  <main id="main">
    <section class="subpage-hero">
      <div class="container">
        <nav class="breadcrumbs" aria-label="Breadcrumb">
          <a href="index.html">Home</a>
          <span class="sep">/</span>
          <span class="current">Product Categories</span>
        </nav>
        <h1 class="page-title">Industrial Equipment <em>Categories.</em></h1>
        <p class="hero-subheading">
          Browse our catalogue across 7 major industrial sectors. Each division features verified purchase order machinery, certified plant utilities, and technical specification models.
        </p>
      </div>
    </section>

    <section class="section-pad">
      <div class="container">
        <div class="categories-showcase-grid">

          <!-- 01: Thermal & Heat Transfer -->
          <article class="cat-card">
            <div class="cat-header">
              <div class="cat-icon-badge">🔥</div>
              <span class="cat-count">5 Machines</span>
            </div>
            <h3>Thermal & Heat Transfer</h3>
            <p>High-efficiency steam boilers, multi-tube heat exchangers, plate coolers, and falling-film chemical evaporators engineered for severe industrial thermal cycles.</p>
            <div class="cat-machine-preview">
              <span>Steam Boiler 850 KG/HR (Dual Burner) · [PO 01]</span>
              <span>Shell & Tube Heat Exchanger · [Supplementary]</span>
              <span>Gasketed Plate Heat Exchanger · [Technical]</span>
              <span>Falling-Film Chemical Evaporator · [Technical]</span>
              <span>Air-Cooled Refrigeration Condenser · [Technical]</span>
            </div>
            <a class="cat-link" href="products.html?category=thermal">Explore Thermal Equipment <span>→</span></a>
          </article>

          <!-- 02: Electrical & Power Infrastructure -->
          <article class="cat-card">
            <div class="cat-header">
              <div class="cat-icon-badge">⚡</div>
              <span class="cat-count">5 Machines</span>
            </div>
            <h3>Electrical & Power Infrastructure</h3>
            <p>Turn-key high-tension and low-tension distribution equipment, automatic power factor correction (APFC) panels with harmonic inductors, and motor control centers.</p>
            <div class="cat-machine-preview">
              <span>APFC Panels with Harmonic Filters (Items 03 & 06) · [PO]</span>
              <span>Transformer & LT Correction Breaker · [PO 04]</span>
              <span>Transformer & HT Connection Breaker (VCB) · [PO 05]</span>
              <span>Industrial Diesel Generator Set (DG Set) · [Technical]</span>
              <span>Compartmentalized MCC Control Panel · [Technical]</span>
            </div>
            <a class="cat-link" href="products.html?category=electrical">Explore Electrical Infrastructure <span>→</span></a>
          </article>

          <!-- 03: Pumps & Fluid Handling -->
          <article class="cat-card">
            <div class="cat-header">
              <div class="cat-icon-badge">🔄</div>
              <span class="cat-count">4 Machines</span>
            </div>
            <h3>Pumps & Fluid Handling Systems</h3>
            <p>Heavy-duty fluid transfer solutions for viscous chemicals, aggressive slurries, process vacuum, dosing reagents, and closed-loop water recirculation circuits.</p>
            <div class="cat-machine-preview">
              <span>Centrifugal Process Slurry Pump · [Supplementary]</span>
              <span>Liquid-Ring Industrial Vacuum Pump · [Technical]</span>
              <span>Positive Displacement Rotary Gear Pump · [Technical]</span>
              <span>Micro-Metering Chemical Dosing Pump · [Technical]</span>
            </div>
            <a class="cat-link" href="products.html?category=pumps">Explore Fluid Handling <span>→</span></a>
          </article>

          <!-- 04: Industrial Air & Gas Systems -->
          <article class="cat-card">
            <div class="cat-header">
              <div class="cat-icon-badge">💨</div>
              <span class="cat-count">3 Machines</span>
            </div>
            <h3>Air & Gas Systems</h3>
            <p>Rotary screw air compressors, pressure receiver surge vessels, high-static centrifugal draft blowers, and refrigerated compressed air moisture dryers.</p>
            <div class="cat-machine-preview">
              <span>Rotary Screw Compressor (BK90-8GH) · [Supplementary]</span>
              <span>High-Pressure Centrifugal Air Blower · [Technical]</span>
              <span>Refrigerated Air Dryer & Moisture Separator · [Technical]</span>
            </div>
            <a class="cat-link" href="products.html?category=air">Explore Air & Gas Systems <span>→</span></a>
          </article>

          <!-- 05: Water Treatment & Filtration -->
          <article class="cat-card">
            <div class="cat-header">
              <div class="cat-icon-badge">💧</div>
              <span class="cat-count">5 Machines</span>
            </div>
            <h3>Water Treatment & Filtration</h3>
            <p>Comprehensive plant utilities for process water softening, reverse osmosis demineralization, cooling water dissipation, and multi-bag/cartridge micro-filtration.</p>
            <div class="cat-machine-preview">
              <span>Induced Draft Cooling Tower · [Supplementary]</span>
              <span>Multi-Grade Sand & Carbon Filter Skid · [Technical]</span>
              <span>Stainless Steel Bag Filter Housing · [Technical]</span>
              <span>Industrial Reverse Osmosis (RO) Plant · [Technical]</span>
              <span>Automated Ion-Exchange Softener Plant · [Technical]</span>
            </div>
            <a class="cat-link" href="products.html?category=water">Explore Water Treatment <span>→</span></a>
          </article>

          <!-- 06: Process Vessels & Tanks -->
          <article class="cat-card">
            <div class="cat-header">
              <div class="cat-icon-badge">🏗️</div>
              <span class="cat-count">3 Machines</span>
            </div>
            <h3>Process Vessels & Agitated Tanks</h3>
            <p>ASME & IS standard pressure vessels, stainless steel chemical storage reservoirs, and motorized jacketed reaction tanks engineered for sanitary or chemical duty.</p>
            <div class="cat-machine-preview">
              <span>SS316L Chemical Storage Tank · [Technical]</span>
              <span>Jacketed Mixing Tank with Motorized Agitator · [Technical]</span>
              <span>Compressed Air Receiver Pressure Vessel · [Technical]</span>
            </div>
            <a class="cat-link" href="products.html?category=vessels">Explore Process Vessels <span>→</span></a>
          </article>

          <!-- 07: Thermal Insulation & Plant Services -->
          <article class="cat-card">
            <div class="cat-header">
              <div class="cat-icon-badge">🛡️</div>
              <span class="cat-count">3 Scope Packages</span>
            </div>
            <h3>Thermal Insulation & Electrification</h3>
            <p>Turn-key industrial insulation cladding for steam/chilled lines, perforated steel cable tray infrastructure, motor starters, and statutory liaison permissions.</p>
            <div class="cat-machine-preview">
              <span>LRB Mattress Insulation & Aluminium Cladding · [PO 02]</span>
              <span>Plant Electrification, Cable Trays & Starters · [PO 08]</span>
              <span>LT Switchgear Plant Networking · [PO 07]</span>
            </div>
            <a class="cat-link" href="products.html?filter=po">Explore PO Scope Packages <span>→</span></a>
          </article>

        </div>
      </div>
    </section>
  </main>

  {get_footer()}
</body>
</html>
"""
    with open(os.path.join(BASE_DIR, "categories.html"), "w", encoding="utf-8") as f:
        f.write(content)
    print("categories.html built.")

# -----------------------------------------------------------------------------
# PAGE 5: about.html (ABOUT US)
# -----------------------------------------------------------------------------
def build_about_page():
    content = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#0d1a16">
  <meta name="description" content="About M/s. Pukhraj Hastimal & Co. — Industrial equipment supplier, thermal machinery, and turnkey electrical contractor based in Mumbai, Maharashtra. Verified facts only.">
  <title>About Us | M/s. Pukhraj Hastimal & Co.</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <a class="skip-link" href="#main">Skip to main content</a>
  {get_header("About Us")}

  <main id="main">
    <section class="subpage-hero">
      <div class="container">
        <nav class="breadcrumbs" aria-label="Breadcrumb">
          <a href="index.html">Home</a>
          <span class="sep">/</span>
          <span class="current">About Our Company</span>
        </nav>
        <h1 class="page-title">Engineering Infrastructure. <em>Real Delivery.</em></h1>
        <p class="hero-subheading">
          Official business profile of M/s. PUKHRAJ HASTIMAL & CO. Founded on authentic engineering documentation, verified purchase orders, and heavy industrial execution.
        </p>
      </div>
    </section>

    <section class="section-pad">
      <div class="container" style="max-width: 960px;">
        
        <div style="background: var(--white); border: 1px solid var(--line); border-radius: var(--radius-md); padding: clamp(24px, 4vw, 44px); box-shadow: var(--shadow-sm);">
          <p class="eyebrow">COMPANY BACKGROUND & PROFILE</p>
          <h2 style="font-family: var(--font-heading); font-size: 26px; color: var(--forest-dark); margin: 0 0 16px;">
            M/s. PUKHRAJ HASTIMAL & CO.
          </h2>
          
          <p style="font-size: 15.5px; line-height: 1.8; color: #2e4338;">
            <strong>M/s. Pukhraj Hastimal & Co.</strong> is an established industrial equipment supplier, thermal engineering provider, and electrical distribution contractor operating from Mumbai, Maharashtra. We coordinate the supply, technical verification, and on-site delivery of heavy industrial assets for manufacturing and chemical facilities across India.
          </p>

          <p style="font-size: 15.5px; line-height: 1.8; color: #2e4338;">
            Our business specializes in multi-discipline industrial scopes: steam generation boilers, thermal insulation with aluminium weather cladding, high-tension (HT) vacuum circuit breaker substations, step-down transformers, automatic power factor correction (APFC) panels, process chillers, cooling towers, and rotary compressed air systems.
          </p>

          <div style="margin: 32px 0; padding: 24px; background: #f8faf8; border: 1px solid #dce4dd; border-radius: 8px;">
            <h3 style="font-family: var(--font-heading); font-size: 18px; color: var(--forest-dark); margin: 0 0 14px;">
              Verified Corporate & Statutory Credentials
            </h3>
            <dl style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 16px; margin: 0;">
              <div>
                <dt style="font-family: var(--font-mono); font-size: 11px; color: var(--muted); text-transform: uppercase;">Company Name</dt>
                <dd style="margin: 4px 0 0; font-size: 14.5px; font-weight: 700; color: var(--forest);">M/s. PUKHRAJ HASTIMAL & CO.</dd>
              </div>
              <div>
                <dt style="font-family: var(--font-mono); font-size: 11px; color: var(--muted); text-transform: uppercase;">GSTIN / Registration</dt>
                <dd style="margin: 4px 0 0; font-size: 14.5px; font-weight: 700; color: var(--forest); font-family: var(--font-mono);">27AFMPJ3478A1ZG</dd>
              </div>
              <div>
                <dt style="font-family: var(--font-mono); font-size: 11px; color: var(--muted); text-transform: uppercase;">Registered Office</dt>
                <dd style="margin: 4px 0 0; font-size: 13.5px; color: #354a3f;">Office No 03, 2nd Floor, 7 Kika Bhai Mansion, Gulalwadi, Mumbai - 400004</dd>
              </div>
              <div>
                <dt style="font-family: var(--font-mono); font-size: 11px; color: var(--muted); text-transform: uppercase;">Official Procurement Email</dt>
                <dd style="margin: 4px 0 0; font-size: 13.5px; font-weight: 600;"><a href="mailto:pukhrajhastimal@gmail.com" style="color: #1e663a;">pukhrajhastimal@gmail.com</a></dd>
              </div>
            </dl>
          </div>

          <h3 style="font-family: var(--font-heading); font-size: 20px; color: var(--forest-dark); margin: 32px 0 12px;">
            Major Purchase Order Reference: PH/001/26-27
          </h3>
          <p style="font-size: 15px; line-height: 1.7; color: #354a3f;">
            Our primary product fleet is anchored in the verified commercial execution of Purchase Order Ref: <strong>PH/001/26-27</strong> dated 15 May 2026. This comprehensive contract encompassed eight heavy capital equipment line items delivered to <strong>Indian Emulsifiers Limited</strong> at the MIDC Tal–Khed industrial corridor in Ratnagiri:
          </p>

          <div style="background: #ffffff; border: 1px solid var(--line); border-radius: 8px; overflow-x: auto; margin: 20px 0;">
            <table class="specs-table" style="width: 100%;">
              <thead>
                <tr style="background: #edf3ee; text-align: left; font-size: 12px; font-family: var(--font-mono);">
                  <th style="padding: 10px 14px;">Item</th>
                  <th style="padding: 10px 14px;">Equipment Description</th>
                  <th style="padding: 10px 14px;">HSN/SAC</th>
                  <th style="padding: 10px 14px;">Quantity</th>
                  <th style="padding: 10px 14px;">Basic PO Rate</th>
                </tr>
              </thead>
              <tbody style="font-size: 13px;">
                <tr><td>01</td><td>Steam Boiler 850 KG/HR (Dual Burner)</td><td>84029090</td><td>1 NOS</td><td>₹16,50,000.00</td></tr>
                <tr><td>02</td><td>Hot & Cold Insulation LRB Mattress Cladding</td><td>87089900</td><td>1 NOS</td><td>₹45,38,500.00</td></tr>
                <tr><td>03</td><td>APFC Panels with Harmonic Filters (Item 03)</td><td>85321000</td><td>1 NOS</td><td>₹17,15,000.00</td></tr>
                <tr><td>04</td><td>Transformer & LT Correction Breaker</td><td>85043100</td><td>1 NOS</td><td>₹26,10,000.00</td></tr>
                <tr><td>05</td><td>Transformer & HT Connection Breaker (VCB)</td><td>85043100</td><td>1 NOS</td><td>₹46,00,000.00</td></tr>
                <tr><td>06</td><td>APFC Panels with Harmonic Filters (Item 06)</td><td>85321000</td><td>1 NOS</td><td>₹34,30,000.00</td></tr>
                <tr><td>07</td><td>LT Networking in Plant & Switchgear</td><td>85372000</td><td>1 NOS</td><td>₹33,79,250.00</td></tr>
                <tr><td>08</td><td>Plant Electrification, Cable Trays & Starters</td><td>995461</td><td>1 NOS</td><td>₹64,50,000.00</td></tr>
              </tbody>
            </table>
          </div>

          <div style="padding: 14px 18px; background: #eef7eb; border: 1px solid #c2e2b3; border-radius: 6px; font-size: 13px; color: #215d38; line-height: 1.6;">
            <strong>Order Financial Total:</strong> Total basic amount: ₹2,83,72,750.00 | CGST (9%): ₹25,53,547.50 | SGST (9%): ₹25,53,547.50 | <strong>Total Order Value: ₹3,34,79,845.00</strong> (Three Crores Thirty-Four Lakhs Seventy-Nine Thousand Eight Hundred Forty-Five Only).
          </div>

          <div style="margin-top: 40px; text-align: center;">
            <a href="quote.html" class="btn-hero-primary" style="text-decoration: none; display: inline-flex;">
              <span>Initiate Equipment Procurement RFQ</span>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
            </a>
          </div>

        </div>

      </div>
    </section>
  </main>

  {get_footer()}
</body>
</html>
"""
    with open(os.path.join(BASE_DIR, "about.html"), "w", encoding="utf-8") as f:
        f.write(content)
    print("about.html built.")

# -----------------------------------------------------------------------------
# PAGE 6: quote.html (REQUEST A QUOTE - 7 FORM FIELDS)
# -----------------------------------------------------------------------------
def build_quote_page():
    content = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#0d1a16">
  <meta name="description" content="Request a formal procurement quotation from M/s. Pukhraj Hastimal & Co. for verified industrial boilers, electrical infrastructure, pumps, compressors, and plant equipment.">
  <title>Request a Quotation | Pukhraj Hastimal & Co.</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <a class="skip-link" href="#main">Skip to main content</a>
  {get_header("Request a Quote")}

  <main id="main">
    <section class="subpage-hero">
      <div class="container">
        <nav class="breadcrumbs" aria-label="Breadcrumb">
          <a href="index.html">Home</a>
          <span class="sep">/</span>
          <span class="current">Request a Quote (RFQ)</span>
        </nav>
        <h1 class="page-title">Procurement Quotation <em>Request.</em></h1>
        <p class="hero-subheading">
          Submit your technical specifications, required capacity, and organization parameters. Our engineering team prepares formal price quotations and delivery schedules.
        </p>
      </div>
    </section>

    <section class="section-pad">
      <div class="container">
        <div style="display: grid; grid-template-columns: 2fr 1fr; gap: 40px; align-items: start;">
          
          <!-- Quotation Form (7 Required Fields) -->
          <form class="contact-form" id="rfqForm" style="margin: 0; box-shadow: var(--shadow-sm); border: 1px solid var(--line); border-radius: var(--radius-md); padding: clamp(24px, 4vw, 40px); background: var(--white);">
            <div class="form-heading">
              <h2 style="font-family: var(--font-heading); font-size: 22px; margin: 0; color: var(--forest-dark);">Official Machinery RFQ Form</h2>
              <span style="font-size: 12.5px; color: var(--muted);">* All fields mandatory for formal pricing</span>
            </div>

            <!-- Field 1 & 2: Customer Name & Company Name -->
            <div class="form-grid-2">
              <div class="form-row">
                <label for="name">1. Customer Name / Authorized Representative *</label>
                <input id="name" name="name" autocomplete="name" required maxlength="100" placeholder="e.g. Rajesh Sharma, Head of Engineering">
              </div>
              <div class="form-row">
                <label for="company">2. Company Name / Purchasing Enterprise *</label>
                <input id="company" name="company" autocomplete="organization" required maxlength="120" placeholder="e.g. Apex Speciality Chemicals Pvt Ltd">
              </div>
            </div>

            <!-- Field 3 & 4: Email Address & Phone Number -->
            <div class="form-grid-2">
              <div class="form-row">
                <label for="email">3. Official Corporate Email Address *</label>
                <input id="email" name="email" type="email" autocomplete="email" required maxlength="150" placeholder="e.g. procurement@company.com">
              </div>
              <div class="form-row">
                <label for="phone">4. Direct Phone / Mobile Number *</label>
                <input id="phone" name="phone" type="tel" autocomplete="tel" required maxlength="30" placeholder="e.g. +91 98200 XXXXX">
              </div>
            </div>

            <!-- Field 5 & 6: Machine of Interest & Quantity -->
            <div class="form-grid-2">
              <div class="form-row">
                <label for="equipment">5. Machine of Interest (Select from 33 Items) *</label>
                <select id="equipment" name="equipment" required style="width: 100%;">
                  <option value="">Select machinery model...</option>
                  
                  <optgroup label="--- 8 Original Purchase Order Machines (PO Ref: PH/001/26-27) ---">
                    <option value="po1_boiler">BOILER 850 KG/HR CAPACITY (Dual Burner) — Item 01</option>
                    <option value="po2_insulation">HOT & COLD INSULATION LRB MATTRESS & CLADDING — Item 02</option>
                    <option value="po3_apfc1">APFC PANELS WITH HARMONIC FILTERS — Item 03</option>
                    <option value="po4_ltbreaker">TRANSFORMER & LT ORRECTION BREAKER — Item 04</option>
                    <option value="po5_htbreaker">TRANSFORMER & HT CONNECTION BREAKER (VCB) — Item 05</option>
                    <option value="po6_apfc2">APFC PANNELS WITH HARMONIC FILTERS — Item 06</option>
                    <option value="po7_network">LT NETWORKING IN PLANT & SWITCHGEAR — Item 07</option>
                    <option value="po8_electrification">ELECTRIFICATION, CABLE TRAYS & STARTERS — Item 08</option>
                  </optgroup>

                  <optgroup label="--- 5 Supplementary Plant Utilities (From Client Facility Photos) ---">
                    <option value="sup1_cooling">INDUSTRIAL COOLING TOWER (INDUCED DRAFT)</option>
                    <option value="sup2_chiller">WATER-COOLED SCREW CHILLER (ZENVENT ENGINEERING)</option>
                    <option value="sup3_pump">CENTRIFUGAL PROCESS & CHEMICAL SLURRY PUMP</option>
                    <option value="sup4_compressor">ROTARY SCREW AIR COMPRESSOR BK90-8GH</option>
                    <option value="sup5_exchanger">SHELL & TUBE HEAT EXCHANGER / INDUSTRIAL CONDENSER</option>
                  </optgroup>

                  <optgroup label="--- 20 Extended Technical Specification Models ---">
                    <option value="ext1_vacuum_pump">LIQUID-RING INDUSTRIAL VACUUM PUMP</option>
                    <option value="ext2_gear_pump">POSITIVE DISPLACEMENT ROTARY GEAR PUMP</option>
                    <option value="ext3_dosing_pump">CHEMICAL DOSING & METERING PUMP</option>
                    <option value="ext4_circulation_pump">VERTICAL INLINE WATER CIRCULATION PUMP</option>
                    <option value="ext5_plate_exchanger">GASKETED PLATE & FRAME HEAT EXCHANGER</option>
                    <option value="ext6_refrig_condenser">AIR-COOLED FINNED-TUBE REFRIGERATION CONDENSER</option>
                    <option value="ext7_evaporator">INDUSTRIAL FALLING-FILM CHEMICAL EVAPORATOR</option>
                    <option value="ext8_storage_tank">STAINLESS STEEL CHEMICAL STORAGE TANK</option>
                    <option value="ext9_mixing_tank">JACKETED MIXING TANK WITH MOTORIZED AGITATOR</option>
                    <option value="ext10_air_receiver">COMPRESSED AIR RECEIVER PRESSURE VESSEL</option>
                    <option value="ext11_centrifugal_blower">HIGH-PRESSURE CENTRIFUGAL AIR BLOWER</option>
                    <option value="ext12_air_dryer">REFRIGERATED COMPRESSED AIR DRYER UNIT</option>
                    <option value="ext13_filtration_system">MULTI-GRADE SAND & CARBON WATER FILTRATION SKID</option>
                    <option value="ext14_bag_filter">STAINLESS STEEL BAG FILTER HOUSING</option>
                    <option value="ext15_cartridge_filter">MULTI-ELEMENT CARTRIDGE FILTER HOUSING</option>
                    <option value="ext16_ro_system">INDUSTRIAL REVERSE OSMOSIS (RO) PLANT</option>
                    <option value="ext17_water_softener">AUTOMATED ION-EXCHANGE WATER SOFTENER PLANT</option>
                    <option value="ext18_diesel_generator">INDUSTRIAL DIESEL GENERATOR SET (DG SET)</option>
                    <option value="ext19_electric_motor">HEAVY-DUTY IE3 EFFICIENCY ELECTRIC MOTOR</option>
                    <option value="ext20_mcc_panel">COMPARTMENTALIZED MOTOR CONTROL CENTRE (MCC PANEL)</option>
                  </optgroup>
                </select>
              </div>
              <div class="form-row">
                <label for="quantity">6. Quantity Required *</label>
                <input id="quantity" name="quantity" type="number" min="1" max="500" value="1" required>
              </div>
            </div>

            <!-- Field 7: Technical Specifications / Message -->
            <div class="form-row">
              <label for="message">7. Technical Requirements, Operating Parameters & Delivery Location *</label>
              <textarea id="message" name="message" required minlength="15" maxlength="2500" rows="5" placeholder="Detail your process requirements, required capacity, design pressure, fluid medium, operating temperature, installation state/city, and required project delivery timeline..."></textarea>
            </div>

            <button class="submit-button" type="submit" style="margin-top: 10px;">
              <span>Format & Dispatch Quotation RFQ</span>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
            </button>
            
            <p class="form-feedback" id="formFeedback" role="status" aria-live="polite"></p>

            <div style="margin-top: 20px; padding: 14px 16px; background: #f8faf8; border: 1px solid #e1e7e2; border-radius: 6px; font-size: 12.5px; color: var(--muted); line-height: 1.6;">
              <strong>Procurement Dispatch Notice:</strong> This secure form client-side formats your full RFQ inquiry and launches your registered email client addressed directly to <code>pukhrajhastimal@gmail.com</code>. No intermediate cloud database stores or exposes your confidential engineering data.
            </div>
          </form>

          <!-- Sidebar Information Card -->
          <div style="background: var(--white); border: 1px solid var(--line); border-radius: var(--radius-md); padding: 28px; box-shadow: var(--shadow-sm);">
            <h3 style="font-family: var(--font-heading); font-size: 18px; color: var(--forest-dark); margin: 0 0 16px;">
              Official Procurement Desk
            </h3>

            <div style="display: flex; flex-direction: column; gap: 16px; font-size: 13.5px;">
              <div>
                <strong style="color: var(--forest); display: block; font-size: 12px; font-family: var(--font-mono);">BUYER / CONTRACTOR:</strong>
                <span>M/s. PUKHRAJ HASTIMAL & CO.</span>
              </div>

              <div>
                <strong style="color: var(--forest); display: block; font-size: 12px; font-family: var(--font-mono);">REGISTERED OFFICE:</strong>
                <span>Office No 03, 2nd Floor, 7 Kika Bhai Mansion, Gulalwadi, Mumbai - 400004</span>
              </div>

              <div>
                <strong style="color: var(--forest); display: block; font-size: 12px; font-family: var(--font-mono);">GST REGISTRATION:</strong>
                <span style="font-family: var(--font-mono); font-weight: 700; color: #1e5938;">27AFMPJ3478A1ZG</span>
              </div>

              <div>
                <strong style="color: var(--forest); display: block; font-size: 12px; font-family: var(--font-mono);">DIRECT RFQ EMAIL:</strong>
                <a href="mailto:pukhrajhastimal@gmail.com" style="color: #1e663a; font-weight: 600;">pukhrajhastimal@gmail.com</a>
              </div>

              <div style="margin-top: 12px; padding: 14px; background: #eef6ec; border: 1px solid #c9e3c4; border-radius: 6px;">
                <strong style="display: block; font-size: 12px; color: #1e5938; margin-bottom: 4px;">PURCHASE ORDER REFERENCE:</strong>
                <span style="font-size: 12.5px; color: #2e4d3a;">
                  PO Ref: PH/001/26-27<br>
                  Consignee: Indian Emulsifiers Limited, MIDC Khed, Ratnagiri
                </span>
              </div>
            </div>
          </div>

        </div>
      </div>
    </section>
  </main>

  {get_footer()}

  <script src="assets/products-data.js"></script>
  <script>
    document.addEventListener("DOMContentLoaded", () => {
      const urlParams = new URLSearchParams(window.location.search);
      const equipmentSelect = document.getElementById("equipment");
      const preselectId = urlParams.get("product") || "";

      if (preselectId && equipmentSelect) {
        for (let opt of equipmentSelect.options) {
          if (opt.value === preselectId) {
            equipmentSelect.value = preselectId;
            break;
          }
        }
      }

      const rfqForm = document.getElementById("rfqForm");
      const formFeedback = document.getElementById("formFeedback");

      rfqForm.addEventListener("submit", (e) => {
        e.preventDefault();
        if (!rfqForm.reportValidity()) return;

        const formData = new FormData(rfqForm);
        const customerName = formData.get("name") || "";
        const companyName = formData.get("company") || "";
        const email = formData.get("email") || "";
        const phone = formData.get("phone") || "";
        const selectedMachineId = formData.get("equipment") || "";
        const quantity = formData.get("quantity") || "1";
        const message = formData.get("message") || "";

        const productObj = window.PRODUCTS_DATA ? window.PRODUCTS_DATA[selectedMachineId] : null;
        const machineTitle = productObj ? productObj.name : selectedMachineId;
        const poStatus = productObj && productObj.statusType === "po"
          ? `Verified PO Line Item #${productObj.poItemNo} (HSN: ${productObj.hsn})`
          : (productObj && productObj.statusType === "supplementary" ? "Supplementary Plant Utility" : "Extended Technical Model");

        const subject = `Official RFQ: ${machineTitle} — [${companyName}]`;
        const body = [
          `FORMAL INDUSTRIAL PROCUREMENT ENQUIRY (RFQ)`,
          `============================================================`,
          `Authorized Representative: ${customerName}`,
          `Company Name:              ${companyName}`,
          `Corporate Email:           ${email}`,
          `Direct Phone:              ${phone}`,
          `Date of Request:           ${new Date().toLocaleDateString("en-IN")}`,
          `------------------------------------------------------------`,
          `Machine of Interest:       ${machineTitle}`,
          `Catalogue Classification:  ${poStatus}`,
          `Required Quantity:         ${quantity} NOS`,
          `------------------------------------------------------------`,
          `Engineering Parameters & Scope:`,
          message,
          `============================================================`,
          `To: M/s. PUKHRAJ HASTIMAL & CO.`,
          `Registered Office: Office No 03, 2nd Floor, 7 Kika Bhai Mansion, Gulalwadi, Mumbai - 400004`,
          `GST NO: 27AFMPJ3478A1ZG | Email: pukhrajhastimal@gmail.com`
        ].join("\\n");

        if (formFeedback) {
          formFeedback.textContent = "Formatting RFQ parameters and opening your email application...";
          formFeedback.className = "form-feedback feedback-active";
        }

        setTimeout(() => {
          window.location.href = `mailto:pukhrajhastimal@gmail.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
          if (formFeedback) {
            formFeedback.textContent = "Your email application has been launched with the complete quotation enquiry draft.";
          }
        }, 350);
      });
    });
  </script>
</body>
</html>
"""
    with open(os.path.join(BASE_DIR, "quote.html"), "w", encoding="utf-8") as f:
        f.write(content)
    print("quote.html built.")

# -----------------------------------------------------------------------------
# PAGE 7: contact.html (CONTACT US)
# -----------------------------------------------------------------------------
def build_contact_page():
    content = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#0d1a16">
  <meta name="description" content="Contact M/s. Pukhraj Hastimal & Co. — Industrial equipment supply and engineering contracting office in Mumbai, Maharashtra. Official email, registered office address, and GSTIN.">
  <title>Contact Us | M/s. Pukhraj Hastimal & Co.</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <a class="skip-link" href="#main">Skip to main content</a>
  {get_header("Contact")}

  <main id="main">
    <section class="subpage-hero">
      <div class="container">
        <nav class="breadcrumbs" aria-label="Breadcrumb">
          <a href="index.html">Home</a>
          <span class="sep">/</span>
          <span class="current">Contact Procurement</span>
        </nav>
        <h1 class="page-title">Direct Procurement <em>Contact.</em></h1>
        <p class="hero-subheading">
          Official communication channels for M/s. PUKHRAJ HASTIMAL & CO. Connect directly with our industrial equipment procurement team in Mumbai.
        </p>
      </div>
    </section>

    <section class="section-pad">
      <div class="container">
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 48px; align-items: start;">
          
          <!-- Contact Details Cards -->
          <div>
            <p class="eyebrow">VERIFIED CORPORATE CREDENTIALS</p>
            <h2 style="font-family: var(--font-heading); font-size: 26px; color: var(--forest-dark); margin: 0 0 20px;">
              Get in Touch with our Engineering Team.
            </h2>
            <p style="font-size: 15px; line-height: 1.7; color: #354a3f; margin-bottom: 28px;">
              For equipment sizing inquiries, purchase order verification, proforma invoices, and site installation schedules, contact our registered office in Gulalwadi, Mumbai.
            </p>

            <div style="display: flex; flex-direction: column; gap: 20px;">
              <div style="display: flex; gap: 16px; padding: 20px; background: var(--white); border: 1px solid var(--line); border-radius: var(--radius-sm); box-shadow: var(--shadow-sm);">
                <div style="width: 44px; height: 44px; background: #eef6ec; border: 1px solid #c8e4c2; color: #1e5e3b; display: grid; place-items: center; border-radius: 8px; font-size: 20px;">✉️</div>
                <div>
                  <small style="font-family: var(--font-mono); font-size: 11px; color: var(--muted); text-transform: uppercase;">Direct Procurement Email</small>
                  <div style="font-size: 16px; font-weight: 700; margin-top: 2px;">
                    <a href="mailto:pukhrajhastimal@gmail.com" style="color: var(--forest); text-decoration: none;">pukhrajhastimal@gmail.com</a>
                  </div>
                  <span style="font-size: 12px; color: var(--muted); margin-top: 2px; display: block;">Official channel for formal RFQs and documentation.</span>
                </div>
              </div>

              <div style="display: flex; gap: 16px; padding: 20px; background: var(--white); border: 1px solid var(--line); border-radius: var(--radius-sm); box-shadow: var(--shadow-sm);">
                <div style="width: 44px; height: 44px; background: #eef6ec; border: 1px solid #c8e4c2; color: #1e5e3b; display: grid; place-items: center; border-radius: 8px; font-size: 20px;">📍</div>
                <div>
                  <small style="font-family: var(--font-mono); font-size: 11px; color: var(--muted); text-transform: uppercase;">Registered Mumbai Office</small>
                  <div style="font-size: 14.5px; font-weight: 700; color: var(--forest-dark); margin-top: 2px; line-height: 1.5;">
                    Office No 03, 2nd Floor, 7 Kika Bhai Mansion, Gulalwadi, Mumbai - 400004, Maharashtra, India
                  </div>
                </div>
              </div>

              <div style="display: flex; gap: 16px; padding: 20px; background: var(--white); border: 1px solid var(--line); border-radius: var(--radius-sm); box-shadow: var(--shadow-sm);">
                <div style="width: 44px; height: 44px; background: #eef6ec; border: 1px solid #c8e4c2; color: #1e5e3b; display: grid; place-items: center; border-radius: 8px; font-size: 20px;">🏛️</div>
                <div>
                  <small style="font-family: var(--font-mono); font-size: 11px; color: var(--muted); text-transform: uppercase;">GSTIN / Statutory Reference</small>
                  <div style="font-size: 16px; font-weight: 800; color: #1e5e3b; font-family: var(--font-mono); margin-top: 2px;">
                    27AFMPJ3478A1ZG
                  </div>
                  <span style="font-size: 12px; color: var(--muted); margin-top: 2px; display: block;">PO Reference: PH/001/26-27</span>
                </div>
              </div>

              <div style="display: flex; gap: 16px; padding: 20px; background: var(--white); border: 1px solid var(--line); border-radius: var(--radius-sm); box-shadow: var(--shadow-sm);">
                <div style="width: 44px; height: 44px; background: #eef6ec; border: 1px solid #c8e4c2; color: #1e5e3b; display: grid; place-items: center; border-radius: 8px; font-size: 20px;">🏭</div>
                <div>
                  <small style="font-family: var(--font-mono); font-size: 11px; color: var(--muted); text-transform: uppercase;">PO Consignee Delivery Destination</small>
                  <div style="font-size: 14px; font-weight: 700; color: var(--forest-dark); margin-top: 2px; line-height: 1.5;">
                    Indian Emulsifiers Limited, E 10 Lote Parshuram Industrial Zone, MIDC Tal – Khed, Ratnagiri – 415722
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- General Enquiry Form -->
          <div style="background: var(--white); border: 1px solid var(--line); border-radius: var(--radius-md); padding: clamp(24px, 4vw, 36px); box-shadow: var(--shadow-sm);">
            <h3 style="font-family: var(--font-heading); font-size: 20px; color: var(--forest-dark); margin: 0 0 8px;">
              Send a General Enquiry
            </h3>
            <p style="font-size: 13.5px; color: var(--muted); margin: 0 0 24px;">
              For immediate machinery pricing, please use the <a href="quote.html" style="color: var(--forest); font-weight: 700;">Request a Quote</a> page.
            </p>

            <form id="generalContactForm">
              <div class="form-row">
                <label for="c_name">Your Name *</label>
                <input id="c_name" name="c_name" required placeholder="Full name">
              </div>
              <div class="form-row">
                <label for="c_email">Official Email *</label>
                <input id="c_email" name="c_email" type="email" required placeholder="name@company.com">
              </div>
              <div class="form-row">
                <label for="c_subject">Subject *</label>
                <input id="c_subject" name="c_subject" required placeholder="Enquiry regarding machinery supply / site delivery">
              </div>
              <div class="form-row">
                <label for="c_message">Message *</label>
                <textarea id="c_message" name="c_message" rows="4" required placeholder="Your message or question..."></textarea>
              </div>

              <button class="submit-button" type="submit" style="width: 100%; justify-content: center;">
                <span>Send Message</span>
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
              </button>
              <p id="contactFeedback" class="form-feedback" role="status" aria-live="polite" style="margin-top: 14px;"></p>
            </form>
          </div>

        </div>
      </div>
    </section>
  </main>

  {get_footer()}

  <script>
    const form = document.getElementById("generalContactForm");
    const feedback = document.getElementById("contactFeedback");
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      if (!form.reportValidity()) return;
      const name = document.getElementById("c_name").value;
      const email = document.getElementById("c_email").value;
      const subject = document.getElementById("c_subject").value;
      const msg = document.getElementById("c_message").value;

      feedback.textContent = "Launching your email client to dispatch message...";
      feedback.className = "form-feedback feedback-active";

      setTimeout(() => {
        const body = `NAME: ${name}\\nEMAIL: ${email}\\n\\nMESSAGE:\\n${msg}`;
        window.location.href = `mailto:pukhrajhastimal@gmail.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
      }, 350);
    });
  </script>
</body>
</html>
"""
    with open(os.path.join(BASE_DIR, "contact.html"), "w", encoding="utf-8") as f:
        f.write(content)
    print("contact.html built.")

# -----------------------------------------------------------------------------
# Run the first batch of builders
# -----------------------------------------------------------------------------
build_products_page()
build_product_detail_page()
build_categories_page()
build_about_page()
build_quote_page()
build_contact_page()
print("Batch 1 (products, product-detail, categories, about, quote, contact) generated.")
