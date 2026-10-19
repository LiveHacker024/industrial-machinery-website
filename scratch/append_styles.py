# Append extended styles to styles.css
styles_to_append = """
/* ==========================================================================
   EXTENDED MULTI-PAGE DESIGN SYSTEM STYLES
   M/s. PUKHRAJ HASTIMAL & CO.
   ========================================================================== */

/* Subpage Hero Header */
.subpage-hero {
  background: radial-gradient(circle at 85% 20%, rgba(200, 231, 122, 0.08) 0%, transparent 60%),
              linear-gradient(180deg, #0d1a16 0%, #16362d 100%);
  color: var(--white);
  padding: 56px 0 44px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  position: relative;
}

.breadcrumbs {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 8px;
  font-size: 12.5px;
  font-family: var(--font-mono);
  color: #9cb5aa;
  margin-bottom: 16px;
  letter-spacing: 0.3px;
}

.breadcrumbs a {
  color: #cddcd4;
  transition: color 0.2s ease;
  text-decoration: none;
}

.breadcrumbs a:hover {
  color: var(--lime);
}

.breadcrumbs .sep {
  opacity: 0.5;
}

.breadcrumbs .current {
  color: var(--lime);
  font-weight: 600;
}

.page-title {
  font-family: var(--font-heading);
  font-size: clamp(28px, 4vw, 42px);
  font-weight: 800;
  line-height: 1.15;
  letter-spacing: -0.8px;
  color: var(--white);
  margin: 0 0 12px;
}

.page-title em {
  font-style: normal;
  color: var(--lime);
}

.hero-subheading {
  font-size: 16px;
  line-height: 1.6;
  color: #c8dad1;
  max-width: 800px;
  margin: 0;
}

/* Category & Badge Extensions */
.card-badge.badge-ext,
.badge-ext {
  background: #e6f4ea;
  color: #137333;
  border: 1px solid #ceead6;
  font-weight: 700;
}

.card-badge.badge-tech,
.badge-tech {
  background: #e8f0fe;
  color: #1a73e8;
  border: 1px solid #d2e3fc;
  font-weight: 700;
}

.dialog-po-tag.po-extended {
  background: #f0f7f4;
  color: #1e5942;
  border: 1px solid #c8e1d5;
}

.dialog-po-tag.po-tech {
  background: #eef5fc;
  color: #1a5b8c;
  border: 1px solid #cce2f5;
}

/* Authentic vs Reference Image Notice Badge */
.image-authenticity-badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 6px 12px;
  border-radius: 4px;
  font-family: var(--font-mono);
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.5px;
}

.image-authenticity-badge.auth-real {
  background: #eef7eb;
  color: #21613b;
  border: 1px solid #c2e2b3;
}

.image-authenticity-badge.auth-schematic {
  background: #f1f7fd;
  color: #1b5b88;
  border: 1px solid #cce2f5;
}

/* Multi-category Filtering Tabs */
.filter-tabs-wrap {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 14px;
}

.filter-btn-pill {
  padding: 8px 16px;
  border-radius: 30px;
  border: 1px solid #d7e0d9;
  background: var(--paper-card);
  color: #3b4e45;
  font-size: 12.5px;
  font-weight: 600;
  transition: all 0.2s ease;
  display: inline-flex;
  align-items: center;
  gap: 6px;
}

.filter-btn-pill span {
  font-family: var(--font-mono);
  font-size: 11px;
  background: #eef2ee;
  color: #55665c;
  padding: 1px 7px;
  border-radius: 12px;
}

.filter-btn-pill:hover {
  background: #eef4ee;
  border-color: #bccbc0;
  color: var(--forest);
}

.filter-btn-pill.active {
  background: var(--forest);
  border-color: var(--forest);
  color: var(--white);
}

.filter-btn-pill.active span {
  background: rgba(200, 231, 122, 0.25);
  color: var(--lime);
}

/* Product Detail Page Specifics */
.product-detail-layout {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 48px;
  align-items: start;
}

.product-detail-gallery {
  background: var(--white);
  border: 1px solid var(--line);
  border-radius: var(--radius-md);
  padding: 24px;
  box-shadow: var(--shadow-sm);
  position: sticky;
  top: 104px;
}

.main-image-frame {
  width: 100%;
  aspect-ratio: 4 / 3;
  background: #f7f9f7;
  border: 1px solid #e5ebe6;
  border-radius: var(--radius-sm);
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  position: relative;
}

.main-image-frame img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  transition: transform 0.3s ease;
}

.main-image-frame:hover img {
  transform: scale(1.02);
}

.gallery-notice {
  margin-top: 14px;
  font-size: 12px;
  color: var(--muted);
  line-height: 1.5;
  padding: 10px 14px;
  background: #f9faf8;
  border: 1px solid #e6eae7;
  border-radius: 6px;
}

.product-detail-info {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.product-detail-meta {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  align-items: center;
}

.product-detail-title {
  font-family: var(--font-heading);
  font-size: clamp(24px, 3vw, 34px);
  font-weight: 800;
  line-height: 1.25;
  color: var(--forest-dark);
  margin: 0;
}

.product-detail-desc {
  font-size: 15px;
  line-height: 1.7;
  color: #384d43;
}

.features-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.features-list li {
  display: flex;
  align-items: flex-start;
  gap: 10px;
  font-size: 14px;
  color: #2b4036;
}

.features-list li::before {
  content: "✓";
  color: #1e7041;
  font-weight: 800;
  margin-top: 1px;
}

.product-actions-bar {
  display: flex;
  flex-wrap: wrap;
  gap: 14px;
  padding: 20px 0;
  border-top: 1px solid var(--line);
  border-bottom: 1px solid var(--line);
  margin: 8px 0;
}

/* Category Index Page Layout */
.categories-showcase-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
  gap: 28px;
}

.cat-card {
  background: var(--white);
  border: 1px solid var(--line);
  border-radius: var(--radius-md);
  padding: 28px;
  display: flex;
  flex-direction: column;
  gap: 16px;
  box-shadow: var(--shadow-sm);
  transition: transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease;
  position: relative;
  overflow: hidden;
}

.cat-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 4px;
  height: 100%;
  background: var(--forest);
  opacity: 0;
  transition: opacity 0.25s ease;
}

.cat-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-md);
  border-color: #c4d4c8;
}

.cat-card:hover::before {
  opacity: 1;
}

.cat-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.cat-icon-badge {
  width: 48px;
  height: 48px;
  border-radius: 10px;
  background: #edf5f0;
  border: 1px solid #d3e5d8;
  display: grid;
  place-items: center;
  font-size: 22px;
}

.cat-count {
  font-family: var(--font-mono);
  font-size: 11.5px;
  font-weight: 700;
  color: var(--forest);
  background: #f0f7f3;
  padding: 4px 10px;
  border-radius: 20px;
  border: 1px solid #d3e5d8;
}

.cat-card h3 {
  font-family: var(--font-heading);
  font-size: 20px;
  font-weight: 700;
  color: var(--forest-dark);
  margin: 0;
}

.cat-card p {
  font-size: 14px;
  color: #4b6055;
  line-height: 1.6;
  margin: 0;
  flex-grow: 1;
}

.cat-machine-preview {
  display: flex;
  flex-direction: column;
  gap: 6px;
  padding: 12px 14px;
  background: #f8faf8;
  border-radius: 8px;
  font-size: 12.5px;
  color: #3b5045;
  border: 1px solid #e9ede9;
}

.cat-machine-preview span {
  display: flex;
  align-items: center;
  gap: 6px;
}

.cat-machine-preview span::before {
  content: "•";
  color: var(--forest-light);
}

.cat-link {
  font-size: 13.5px;
  font-weight: 700;
  color: var(--forest);
  display: inline-flex;
  align-items: center;
  gap: 6px;
  margin-top: 4px;
  transition: color 0.2s ease, gap 0.2s ease;
}

.cat-link:hover {
  color: #0b8043;
  gap: 10px;
}

/* Downloads & Resources Page */
.downloads-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 24px;
}

.download-card {
  background: var(--white);
  border: 1px solid var(--line);
  border-radius: var(--radius-md);
  padding: 24px;
  display: flex;
  flex-direction: column;
  gap: 14px;
  box-shadow: var(--shadow-sm);
  transition: transform 0.2s, box-shadow 0.2s;
}

.download-card:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}

.file-header {
  display: flex;
  align-items: center;
  gap: 12px;
}

.file-icon {
  width: 40px;
  height: 40px;
  background: #fdf2f2;
  border: 1px solid #f9d6d6;
  color: #c53030;
  font-weight: 800;
  font-size: 12px;
  font-family: var(--font-mono);
  display: grid;
  place-items: center;
  border-radius: 6px;
}

.file-title {
  font-weight: 700;
  font-size: 16px;
  color: var(--forest-dark);
}

.file-meta-tag {
  font-family: var(--font-mono);
  font-size: 11px;
  color: var(--muted);
}

/* Industries & Applications Grid */
.industry-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
  gap: 28px;
}

.industry-card {
  background: var(--white);
  border: 1px solid var(--line);
  border-radius: var(--radius-md);
  padding: 28px;
  box-shadow: var(--shadow-sm);
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.industry-card h3 {
  font-family: var(--font-heading);
  font-size: 20px;
  font-weight: 700;
  color: var(--forest-dark);
  margin: 0;
}

.industry-equipment-list {
  background: #f8faf8;
  border: 1px solid #e7ebe7;
  border-radius: 8px;
  padding: 12px 14px;
  font-size: 12.5px;
  line-height: 1.6;
  color: #3b5045;
}

/* Legal & Policy Pages */
.legal-card {
  background: var(--white);
  border: 1px solid var(--line);
  border-radius: var(--radius-md);
  padding: clamp(24px, 4vw, 48px);
  box-shadow: var(--shadow-sm);
  max-width: 900px;
  margin-inline: auto;
}

.legal-notice-box {
  background: #fdfae8;
  border: 1px solid #e8deb0;
  border-radius: 8px;
  padding: 16px 20px;
  font-size: 13.5px;
  color: #63531b;
  margin-bottom: 28px;
  line-height: 1.6;
}

.legal-section {
  margin-bottom: 32px;
}

.legal-section h2 {
  font-family: var(--font-heading);
  font-size: 20px;
  font-weight: 700;
  color: var(--forest-dark);
  margin: 0 0 12px;
  border-bottom: 1px solid var(--line);
  padding-bottom: 8px;
}

.legal-section p, .legal-section ul {
  font-size: 14.5px;
  line-height: 1.7;
  color: #384d43;
}

/* 404 Error Page */
.error-hero-card {
  text-align: center;
  padding: 80px 24px;
  max-width: 680px;
  margin-inline: auto;
}

.error-code {
  font-family: var(--font-heading);
  font-size: clamp(64px, 10vw, 110px);
  font-weight: 800;
  line-height: 1;
  color: var(--forest);
  margin-bottom: 12px;
  letter-spacing: -2px;
}

/* Related Products Slider / Grid */
.related-products-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  gap: 20px;
  margin-top: 24px;
}

/* Responsive adjustments */
@media (max-width: 900px) {
  .product-detail-layout {
    grid-template-columns: 1fr;
    gap: 32px;
  }
  .product-detail-gallery {
    position: static;
  }
  .categories-showcase-grid,
  .industry-grid,
  .downloads-grid {
    grid-template-columns: 1fr;
  }
}
"""

with open("D:/Client Websites/styles.css", "a", encoding="utf-8") as f:
    f.write(styles_to_append)

print("Extended styles successfully appended to styles.css")
