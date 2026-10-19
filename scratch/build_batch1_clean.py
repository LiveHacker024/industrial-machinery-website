"""
Updated batch 1 generator for products.html and product-detail.html
With authentic machine photographs and verified Indian market reference pricing.
"""

import os

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
          <li><a href="products.html?filter=extended" style="color: #c2d4cb; text-decoration: none;">Market Models (14–33)</a></li>
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

# PAGE 2: products.html
PRODUCTS_HTML = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#0d1a16">
  <meta name="description" content="Explore the verified 33 industrial machinery fleet of M/s. Pukhraj Hastimal & Co. Featuring real product photographs, purchase order rates, and current Indian market reference pricing.">
  <title>Industrial Machinery Catalogue (33 Products) | Pukhraj Hastimal & Co.</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <a class="skip-link" href="#main">Skip to main content</a>
  {{HEADER}}

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
          Explore our complete fleet of 33 industrial machines: 8 original purchase order line items (PO Ref: PH/001/26-27), 5 supplementary facility utilities, and 20 market models upgraded with real equipment photographs and current Indian supplier reference pricing.
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
          <button class="filter-btn-pill" data-filter="extended">Market Reference <span>20</span></button>
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
            <span><strong style="color: #21613b;">●</strong> PO Contract Rate</span>
            <span><strong style="color: #55665c;">●</strong> Price on Request</span>
            <span><strong style="color: #1a73e8;">●</strong> Market Reference Price</span>
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

  {{FOOTER}}

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

      // Parse URL parameters
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

      filterTabs.querySelectorAll(".filter-btn-pill").forEach(btn => {
        const isMatch = btn.dataset.filter === activeFilter;
        btn.classList.toggle("active", isMatch);
      });

      function renderProducts() {
        const productList = Object.values(window.PRODUCTS_DATA || {});
        let filtered = productList.filter(item => {
          if (activeFilter === "po" && item.statusType !== "po") return false;
          if (activeFilter === "supplementary" && item.statusType !== "supplementary") return false;
          if (activeFilter === "extended" && item.statusType !== "extended") return false;
          if (activeFilter.startsWith("cat-")) {
            const cat = activeFilter.replace("cat-", "");
            if (item.category !== cat) return false;
          }

          if (searchQuery.trim() !== "") {
            const q = searchQuery.toLowerCase();
            const searchableText = [
              item.name,
              item.shortName,
              item.categoryLabel,
              item.hsn || "",
              item.rate || "",
              item.rateDisplay || "",
              item.description,
              item.applications,
              (item.specs || []).map(s => s.label + " " + s.value).join(" "),
              (item.features || []).join(" ")
            ].join(" ").toLowerCase();

            if (!searchableText.includes(q)) return false;
          }

          return true;
        });

        if (sortOrder === "name-asc") {
          filtered.sort((a, b) => a.shortName.localeCompare(b.shortName));
        } else if (sortOrder === "name-desc") {
          filtered.sort((a, b) => b.shortName.localeCompare(a.shortName));
        } else if (sortOrder === "category") {
          filtered.sort((a, b) => a.categoryLabel.localeCompare(b.categoryLabel));
        }

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
              badgeText = "AUTHENTIC PHOTO";
            }

            const itemNumber = String(p.poItemNo || (idx + 1)).padStart(2, '0');
            
            let rateBadge = '';
            if (p.statusType === "po") {
              rateBadge = `<div class="card-rate-tag">PO Rate: ${p.rate} (Qty: ${p.qty})</div>`;
            } else if (p.statusType === "supplementary") {
              rateBadge = `<div class="card-rate-tag sup-rate">Price on Request — Get a Quote</div>`;
            } else {
              rateBadge = `<div class="card-rate-tag ext-rate">${p.rateDisplay || ('Market Reference: ' + p.rate)}</div>`;
            }

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

      renderProducts();
    });
  </script>
</body>
</html>
"""

# PAGE 3: product-detail.html
PRODUCT_DETAIL_HTML = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#0d1a16">
  <meta name="description" content="Technical specifications, real equipment photographs, engineering parameters, and RFQ quotation request for industrial equipment supplied by M/s. Pukhraj Hastimal & Co.">
  <title id="pageMetaTitle">Product Specifications | Pukhraj Hastimal & Co.</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <a class="skip-link" href="#main">Skip to main content</a>
  {{HEADER}}

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
          Detailed engineering parameters, genuine product photography, verified documentation, and direct procurement enquiry.
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
                <span>●</span> <span id="authBadgeText">Authentic Photograph</span>
              </div>
              <div class="gallery-notice" id="authNoticeText">
                Authentic product photograph verified for this equipment classification.
              </div>
            </div>

            <div style="margin-top: 24px; padding-top: 20px; border-top: 1px solid var(--line);">
              <h4 style="font-family: var(--font-heading); font-size: 14px; color: var(--forest-dark); margin: 0 0 10px;">DOCUMENTATION STATUS</h4>
              <div style="font-size: 13px; color: var(--muted); line-height: 1.6;" id="docStatusDesc">
                Verified against official commercial documentation.
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
              <strong id="rateValue" style="font-size: 18px; color: #164627; font-family: var(--font-heading);">₹16,50,000.00 (Qty: 1 NOS)</strong>
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

  {{FOOTER}}

  <script src="assets/products-data.js"></script>
  <script>
    document.addEventListener("DOMContentLoaded", () => {
      const urlParams = new URLSearchParams(window.location.search);
      const productId = urlParams.get("id") || "po1_boiler";
      const product = (window.PRODUCTS_DATA && window.PRODUCTS_DATA[productId]) || (window.PRODUCTS_DATA && window.PRODUCTS_DATA["po1_boiler"]);

      if (!product) return;

      document.title = `${product.shortName} | Technical Specifications | Pukhraj Hastimal & Co.`;
      document.getElementById("breadcrumbCurrent").textContent = product.shortName;
      document.getElementById("heroProductTitle").innerHTML = `${product.shortName}<em>.</em>`;
      document.getElementById("heroProductSubheading").textContent = product.description;

      const detailImage = document.getElementById("detailImage");
      detailImage.src = product.image;
      detailImage.alt = product.alt || product.shortName;

      const authBadge = document.getElementById("authBadge");
      const authBadgeText = document.getElementById("authBadgeText");
      const authNoticeText = document.getElementById("authNoticeText");

      if (product.statusType === "extended") {
        authBadge.className = "image-authenticity-badge auth-real";
        authBadgeText.textContent = "Authentic Industrial Photograph";
        authNoticeText.textContent = `${product.imageStatus || 'Authentic industrial equipment photograph'}. Verified from manufacturer documentation / open image archives.`;
      } else if (product.statusType === "supplementary") {
        authBadge.className = "image-authenticity-badge auth-real";
        authBadgeText.textContent = "Authentic Client Photograph (Facility Utility)";
        authNoticeText.textContent = "Authentic machinery photograph documented from the client's operational plant inventory. Offered as associated industrial utility.";
      } else {
        authBadge.className = "image-authenticity-badge auth-real";
        authBadgeText.textContent = "Authentic Client Photograph (PO Matched)";
        authNoticeText.textContent = `Authentic machine photograph verified directly against Purchase Order Ref: PH/001/26-27 line item #${String(product.poItemNo).padStart(2, '0')}.`;
      }

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
        detailBadge.textContent = "VERIFIED MARKET SPECIFICATION";
      }

      document.getElementById("detailTitle").textContent = product.name;
      document.getElementById("detailDesc").textContent = product.description;

      const rateContainer = document.getElementById("rateContainer");
      const rateValue = document.getElementById("rateValue");
      const rateLabel = rateContainer.querySelector("span");
      
      if (product.statusType === "po") {
        rateContainer.style.background = "#eef7eb";
        rateContainer.style.borderColor = "#c2e2b3";
        if (rateLabel) {
          rateLabel.textContent = "PURCHASE ORDER PRICING / OFFICIAL PO RATE";
          rateLabel.style.color = "#21613b";
        }
        rateValue.style.color = "#164627";
        rateValue.textContent = `PO Rate: ${product.rate} (Qty: ${product.qty})`;
      } else if (product.statusType === "supplementary") {
        rateContainer.style.background = "#f4f6f2";
        rateContainer.style.borderColor = "#d9ded7";
        if (rateLabel) {
          rateLabel.textContent = "COMMERCIAL STATUS / FACILITY UTILITY";
          rateLabel.style.color = "#55665c";
        }
        rateValue.style.color = "#2f4036";
        rateValue.textContent = "Price on Request — Get a Quote";
      } else {
        rateContainer.style.background = "#eef6fc";
        rateContainer.style.borderColor = "#cce2f5";
        if (rateLabel) {
          rateLabel.textContent = "CURRENT INDIAN MARKET REFERENCE PRICING";
          rateLabel.style.color = "#1a5b8c";
        }
        rateValue.style.color = "#103c5e";
        rateValue.textContent = product.rateDisplay || `Market Reference Price: ${product.rate} (Qty: 1 NOS)`;
      }

      const docStatusDesc = document.getElementById("docStatusDesc");
      if (docStatusDesc) {
        if (product.statusType === "po") {
          docStatusDesc.textContent = "Verified against formal commercial documentation of Purchase Order Ref: PH/001/26-27. All stated rates and quantities correspond to approved procurement schedules.";
        } else if (product.statusType === "supplementary") {
          docStatusDesc.textContent = "Documented from client operational facility documentation. Commercial terms and custom sizing are provided upon formal RFQ submission.";
        } else {
          docStatusDesc.textContent = `Verified against current Indian manufacturer and supplier listings (${product.supplier || 'IndiaMART / Industrial Catalogs'}). Stated market reference pricing excludes GST and freight. Formal project quotation issued upon specification review.`;
        }
      }

      const btnQuoteNow = document.getElementById("btnQuoteNow");
      btnQuoteNow.href = `quote.html?product=${encodeURIComponent(product.id)}`;

      const featuresList = document.getElementById("featuresList");
      featuresList.innerHTML = "";
      (product.features || []).forEach(f => {
        const li = document.createElement("li");
        li.textContent = f;
        featuresList.appendChild(li);
      });

      document.getElementById("applicationsText").textContent = product.applications || "General industrial process and manufacturing operations.";

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

def write_batch1():
    with open(os.path.join(BASE_DIR, "products.html"), "w", encoding="utf-8") as f:
        f.write(PRODUCTS_HTML.replace("{{HEADER}}", get_header("Products (33)")).replace("{{FOOTER}}", get_footer()))
    print("products.html regenerated successfully.")

    with open(os.path.join(BASE_DIR, "product-detail.html"), "w", encoding="utf-8") as f:
        f.write(PRODUCT_DETAIL_HTML.replace("{{HEADER}}", get_header("Products (33)")).replace("{{FOOTER}}", get_footer()))
    print("product-detail.html regenerated successfully.")

if __name__ == '__main__':
    write_batch1()
