import React, { useMemo } from 'react';
import PropTypes from 'prop-types';

/**
 * Reusable Dynamic Product Detail Page Component for Pukhraj Hastimal & Co.
 *
 * Implements the dark charcoal (#0b0d10) aesthetic, golden-yellow pricing highlight,
 * dynamic breadcrumbs, 2-column image/spec layout, 3 action buttons, 2x2 perks grid,
 * and the "HEAVY-DUTY SPECIFICATIONS" parameter/value table.
 *
 * @param {Object} props
 * @param {string} [props.productId] - The unique product identifier (e.g., "po1_boiler")
 * @param {Object} [props.product] - Optional product data object. If not provided, fallback/database is used.
 * @param {Function} [props.onSendEnquiry] - Optional handler when user clicks Send Enquiry
 * @param {Function} [props.onCallSales] - Optional handler for Call Sales Desk
 * @param {Function} [props.onDownloadSpec] - Optional handler for Spec Sheet download
 */
export default function ProductDetail({
  productId = 'po1_boiler',
  product: initialProduct,
  onSendEnquiry,
  onCallSales,
  onDownloadSpec,
}) {
  // If running in browser where window.PRODUCTS_DATA is available, or fallback to passed prop
  const product = useMemo(() => {
    if (initialProduct) return initialProduct;
    if (typeof window !== 'undefined' && window.PRODUCTS_DATA) {
      return window.PRODUCTS_DATA[productId] || window.PRODUCTS_DATA['po1_boiler'];
    }
    return null;
  }, [productId, initialProduct]);

  if (!product) {
    return (
      <div style={{ padding: '80px 20px', textAlign: 'center', background: '#0b0d10', color: '#e5ede8' }}>
        <h2>Product Specification Loading...</h2>
        <p style={{ color: '#8fa69a' }}>Querying industrial database for item: {productId}</p>
      </div>
    );
  }

  const categoryName = (product.categoryLabel || 'Industrial Equipment').toUpperCase();
  const productName = product.name || 'Industrial Machine';
  const shortName = (product.shortName || productName).toUpperCase();

  // Price formatting
  const formattedPrice = useMemo(() => {
    if (product.statusType === 'po') {
      return {
        label: 'PURCHASE ORDER PRICING / OFFICIAL PO RATE',
        amount: product.rate,
        badge: `Official PO Rate (Qty: ${product.qty})`,
      };
    }
    if (product.statusType === 'supplementary') {
      return {
        label: 'COMMERCIAL PRICING / BASIC RATE',
        amount: 'Price on Request',
        badge: 'Plant Stock / Custom Sizing',
      };
    }
    return {
      label: 'ESTIMATED INDIAN MARKET BASIC RATE',
      amount: product.rateDisplay || product.rate || 'Price on Request',
      badge: 'Indicative Market Price',
    };
  }, [product]);

  return (
    <div className="product-detail-template-wrapper" style={{ background: '#0b0d10', color: '#e5ede8', minHeight: '100vh', fontFamily: "var(--font-sans, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif)" }}>

      {/* 1. TOP BREADCRUMB NAVIGATION */}
      <nav aria-label="Breadcrumb" style={{ background: '#080a0c', borderBottom: '1px solid rgba(255,255,255,0.08)', padding: '14px 0', fontSize: '12px', letterSpacing: '1px' }}>
        <div style={{ maxWidth: '1240px', margin: '0 auto', padding: '0 20px', display: 'flex', alignItems: 'center', gap: '10px', flexWrap: 'wrap' }}>
          <a href="products.html" style={{ color: '#8ea699', textDecoration: 'none', fontWeight: 600 }}>CATALOGUE</a>
          <span style={{ color: '#4a6255' }}>&gt;</span>
          <a href={`products.html?filter=${encodeURIComponent(product.category || 'all')}`} style={{ color: '#8ea699', textDecoration: 'none', fontWeight: 600 }}>{categoryName}</a>
          <span style={{ color: '#4a6255' }}>&gt;</span>
          <span style={{ color: '#f1c75b', fontWeight: 700 }}>{shortName}</span>
        </div>
      </nav>

      {/* 2. MAIN TWO-COLUMN PRODUCT SECTION */}
      <section style={{ padding: '48px 0 60px' }}>
        <div style={{ maxWidth: '1240px', margin: '0 auto', padding: '0 20px' }}>
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(360px, 1fr))', gap: '48px', alignItems: 'start' }}>

            {/* LEFT COLUMN: Product Image Container */}
            <div style={{ background: '#111514', border: '1px solid rgba(255, 255, 255, 0.08)', borderRadius: '12px', overflow: 'hidden', boxShadow: '0 12px 40px rgba(0,0,0,0.45)', position: 'sticky', top: '90px' }}>
              <div style={{ padding: '36px 28px', display: 'flex', alignItems: 'center', justifyContent: 'center', minHeight: '380px', background: 'radial-gradient(ellipse at 50% 50%, rgba(255,255,255,0.03) 0%, rgba(0,0,0,0.5) 100%)' }}>
                <img
                  src={product.image}
                  alt={product.alt || productName}
                  style={{ maxWidth: '100%', maxHeight: '340px', objectFit: 'contain', filter: 'drop-shadow(0 14px 28px rgba(0,0,0,0.5))' }}
                  loading="eager"
                />
              </div>

              <div style={{ padding: '20px 24px', background: '#0c0f0e', borderTop: '1px solid rgba(255,255,255,0.08)' }}>
                <div style={{ display: 'inline-flex', alignItems: 'center', gap: '8px', padding: '5px 12px', borderRadius: '4px', fontSize: '11px', fontFamily: 'monospace', fontWeight: 700, textTransform: 'uppercase', background: 'rgba(92, 230, 150, 0.12)', color: '#5ce696', border: '1px solid rgba(92, 230, 150, 0.3)' }}>
                  <span>●</span> <span>{product.statusType === 'po' ? 'Authentic Client Photograph (PO Matched)' : 'Authentic Industrial Photograph'}</span>
                </div>
                <p style={{ margin: '10px 0 0', fontSize: '12.5px', color: '#95ada0', lineHeight: 1.5 }}>
                  {product.statusType === 'po'
                    ? `Authentic machine photograph verified directly against Purchase Order Ref: PH/001/26-27 line item #${String(product.poItemNo).padStart(2, '0')}.`
                    : 'Authentic industrial equipment photograph verified from engineering documentation and manufacturer catalogs.'}
                </p>
              </div>
            </div>

            {/* RIGHT COLUMN: Product Info & CTAs */}
            <div>
              {/* Category Tag */}
              <div style={{ display: 'flex', alignItems: 'center', gap: '10px', marginBottom: '14px', flexWrap: 'wrap' }}>
                <span style={{ display: 'inline-block', padding: '6px 14px', background: 'rgba(92, 230, 150, 0.12)', border: '1px solid rgba(92, 230, 150, 0.3)', borderRadius: '4px', color: '#5ce696', fontFamily: 'monospace', fontSize: '11px', fontWeight: 700, letterSpacing: '1.2px', textTransform: 'uppercase' }}>
                  {categoryName}
                </span>
                {product.statusType === 'po' && (
                  <span style={{ display: 'inline-block', padding: '6px 12px', background: 'rgba(241, 199, 91, 0.12)', border: '1px solid rgba(241, 199, 91, 0.3)', borderRadius: '4px', color: '#f1c75b', fontFamily: 'monospace', fontSize: '11px', fontWeight: 700 }}>
                    PO ITEM #{String(product.poItemNo).padStart(2, '0')}
                  </span>
                )}
              </div>

              {/* Product Title */}
              <h1 style={{ fontFamily: "var(--font-heading, 'Inter', sans-serif)", fontSize: 'clamp(28px, 3.2vw, 38px)', fontWeight: 800, lineHeight: 1.18, letterSpacing: '-0.8px', color: '#ffffff', margin: '0 0 18px' }}>
                {productName}
              </h1>

              {/* Pricing Highlighted in Golden-Yellow */}
              <div style={{ padding: '16px 20px', background: 'rgba(241, 199, 91, 0.08)', border: '1px solid rgba(241, 199, 91, 0.28)', borderRadius: '8px', marginBottom: '22px' }}>
                <span style={{ display: 'block', fontSize: '11px', fontFamily: 'monospace', fontWeight: 700, letterSpacing: '1.2px', color: '#d3ae4a', marginBottom: '6px', textTransform: 'uppercase' }}>
                  {formattedPrice.label}
                </span>
                <div style={{ display: 'flex', alignItems: 'baseline', gap: '12px', flexWrap: 'wrap' }}>
                  <span style={{ fontSize: 'clamp(24px, 2.5vw, 32px)', fontWeight: 800, color: '#f1c75b', fontFamily: "var(--font-heading, 'Inter', sans-serif)", letterSpacing: '-0.5px' }}>
                    {formattedPrice.amount}
                  </span>
                  <span style={{ fontSize: '12px', padding: '3px 8px', borderRadius: '4px', background: 'rgba(241, 199, 91, 0.18)', color: '#f8d986', fontFamily: 'monospace', fontWeight: 600 }}>
                    {formattedPrice.badge}
                  </span>
                </div>
              </div>

              {/* Description */}
              <p style={{ fontSize: '15px', lineHeight: 1.65, color: '#b2c7bc', margin: '0 0 28px' }}>
                {product.description}
              </p>

              {/* Action Buttons Trio */}
              <div style={{ display: 'flex', gap: '12px', flexWrap: 'wrap', marginBottom: '32px' }}>
                {/* Primary Yellow Button: Send Enquiry */}
                <a
                  href={`quote.html?product=${encodeURIComponent(product.id)}`}
                  onClick={onSendEnquiry}
                  style={{ display: 'inline-flex', alignItems: 'center', gap: '8px', padding: '13px 24px', background: '#f1c75b', color: '#0b0d10', borderRadius: '6px', fontWeight: 700, fontSize: '13.5px', textDecoration: 'none', border: 'none', cursor: 'pointer', transition: 'all 0.2s ease', boxShadow: '0 4px 16px rgba(241, 199, 91, 0.3)' }}
                >
                  <span>Send Enquiry</span>
                  <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                </a>

                {/* Secondary Button: Call Sales Desk */}
                <a
                  href="tel:+912223880000"
                  onClick={onCallSales}
                  style={{ display: 'inline-flex', alignItems: 'center', gap: '8px', padding: '13px 22px', background: 'rgba(255,255,255,0.05)', color: '#ffffff', borderRadius: '6px', fontWeight: 600, fontSize: '13.5px', textDecoration: 'none', border: '1px solid rgba(255,255,255,0.14)', cursor: 'pointer', transition: 'all 0.2s ease' }}
                >
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
                  <span>Call Sales Desk</span>
                </a>

                {/* Tertiary Button: Spec Sheet */}
                <a
                  href={`downloads.html?product=${encodeURIComponent(product.id)}`}
                  onClick={onDownloadSpec}
                  style={{ display: 'inline-flex', alignItems: 'center', gap: '8px', padding: '13px 20px', background: 'transparent', color: '#5ce696', borderRadius: '6px', fontWeight: 600, fontSize: '13.5px', textDecoration: 'none', border: '1px solid rgba(92, 230, 150, 0.4)', cursor: 'pointer', transition: 'all 0.2s ease' }}
                >
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4M7 10l5 5 5-5M12 15V3"/></svg>
                  <span>Spec Sheet</span>
                </a>
              </div>

              {/* 2x2 Feature Highlights Grid */}
              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(2, 1fr)', gap: '14px', marginBottom: '28px' }}>
                <div style={{ background: '#111514', border: '1px solid rgba(255,255,255,0.06)', borderRadius: '8px', padding: '14px 16px', display: 'flex', gap: '12px', alignItems: 'flex-start' }}>
                  <div style={{ color: '#5ce696', flexShrink: 0, marginTop: '2px' }}>
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/></svg>
                  </div>
                  <div>
                    <strong style={{ display: 'block', fontSize: '12px', color: '#ffffff', letterSpacing: '0.4px', textTransform: 'uppercase' }}>1-YEAR STANDARD WARRANTY</strong>
                    <span style={{ fontSize: '11.5px', color: '#8fa69a' }}>OEM structural & operational coverage</span>
                  </div>
                </div>

                <div style={{ background: '#111514', border: '1px solid rgba(255,255,255,0.06)', borderRadius: '8px', padding: '14px 16px', display: 'flex', gap: '12px', alignItems: 'flex-start' }}>
                  <div style={{ color: '#5ce696', flexShrink: 0, marginTop: '2px' }}>
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><rect x="1" y="3" width="15" height="13"/><polygon points="16 8 20 8 23 11 23 16 16 16 16 8"/><circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/></svg>
                  </div>
                  <div>
                    <strong style={{ display: 'block', fontSize: '12px', color: '#ffffff', letterSpacing: '0.4px', textTransform: 'uppercase' }}>PAN-INDIA DELIVERY</strong>
                    <span style={{ fontSize: '11.5px', color: '#8fa69a' }}>Direct transit to MIDC & industrial hubs</span>
                  </div>
                </div>

                <div style={{ background: '#111514', border: '1px solid rgba(255,255,255,0.06)', borderRadius: '8px', padding: '14px 16px', display: 'flex', gap: '12px', alignItems: 'flex-start' }}>
                  <div style={{ color: '#5ce696', flexShrink: 0, marginTop: '2px' }}>
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><rect x="2" y="5" width="20" height="14" rx="2"/><line x1="2" y1="10" x2="22" y2="10"/></svg>
                  </div>
                  <div>
                    <strong style={{ display: 'block', fontSize: '12px', color: '#ffffff', letterSpacing: '0.4px', textTransform: 'uppercase' }}>FINANCING AVAILABLE</strong>
                    <span style={{ fontSize: '11.5px', color: '#8fa69a' }}>Flexible equipment procurement & CAPEX terms</span>
                  </div>
                </div>

                <div style={{ background: '#111514', border: '1px solid rgba(255,255,255,0.06)', borderRadius: '8px', padding: '14px 16px', display: 'flex', gap: '12px', alignItems: 'flex-start' }}>
                  <div style={{ color: '#5ce696', flexShrink: 0, marginTop: '2px' }}>
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>
                  </div>
                  <div>
                    <strong style={{ display: 'block', fontSize: '12px', color: '#ffffff', letterSpacing: '0.4px', textTransform: 'uppercase' }}>INSTALLATION SUPPORT</strong>
                    <span style={{ fontSize: '11.5px', color: '#8fa69a' }}>On-site technical commissioning & trial testing</span>
                  </div>
                </div>
              </div>

              {/* Engineering Highlights List */}
              {product.features && product.features.length > 0 && (
                <div style={{ borderTop: '1px solid rgba(255,255,255,0.08)', paddingTop: '20px' }}>
                  <h4 style={{ fontSize: '14px', color: '#ffffff', margin: '0 0 10px', letterSpacing: '0.4px' }}>Engineering Highlights</h4>
                  <ul style={{ margin: 0, padding: '0 0 0 18px', color: '#cbdcd1', fontSize: '13.5px', lineHeight: 1.7 }}>
                    {product.features.map((feat, idx) => (
                      <li key={idx}>{feat}</li>
                    ))}
                  </ul>
                </div>
              )}
            </div>

          </div>
        </div>
      </section>

      {/* 3. BOTTOM SPECIFICATIONS SECTION ("HEAVY-DUTY SPECIFICATIONS") */}
      <section style={{ padding: '60px 0 80px', background: '#080a0c', borderTop: '1px solid rgba(255, 255, 255, 0.08)' }}>
        <div style={{ maxWidth: '1240px', margin: '0 auto', padding: '0 20px' }}>
          <div style={{ marginBottom: '28px' }}>
            <span style={{ display: 'block', fontFamily: 'monospace', fontSize: '11px', letterSpacing: '2px', color: '#5ce696', fontWeight: 700, textTransform: 'uppercase', marginBottom: '6px' }}>
              TECHNICAL ARCHITECTURE
            </span>
            <h2 style={{ fontFamily: "var(--font-heading, 'Inter', sans-serif)", fontSize: 'clamp(24px, 3vw, 32px)', fontWeight: 800, color: '#ffffff', margin: '0 0 8px', letterSpacing: '-0.5px' }}>
              HEAVY-DUTY SPECIFICATIONS
            </h2>
            <p style={{ margin: 0, fontSize: '14px', color: '#92a89c' }}>
              Comprehensive verified engineering attributes, operating tolerances, design parameters, and compliance codes.
            </p>
          </div>

          {/* Full-Width Two-Column Key-Value Table */}
          <div style={{ background: '#111514', border: '1px solid rgba(255, 255, 255, 0.08)', borderRadius: '10px', overflowX: 'auto', boxShadow: '0 10px 30px rgba(0,0,0,0.35)' }}>
            <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: '13.5px', minWidth: '500px' }}>
              <thead>
                <tr style={{ background: '#161c18', borderBottom: '1px solid rgba(255, 255, 255, 0.1)' }}>
                  <th style={{ width: '38%', padding: '16px 24px', textAlign: 'left', color: '#5ce696', fontFamily: 'monospace', fontSize: '11px', letterSpacing: '1.5px', fontWeight: 700 }}>PARAMETER</th>
                  <th style={{ width: '62%', padding: '16px 24px', textAlign: 'left', color: '#5ce696', fontFamily: 'monospace', fontSize: '11px', letterSpacing: '1.5px', fontWeight: 700 }}>VALUE</th>
                </tr>
              </thead>
              <tbody>
                {product.specs && product.specs.map((s, idx) => (
                  <tr key={idx} style={{ borderBottom: '1px solid rgba(255, 255, 255, 0.06)' }}>
                    <td style={{ padding: '14px 24px', fontFamily: 'monospace', fontSize: '11.5px', color: '#9eb5aa', fontWeight: 700, textTransform: 'uppercase', background: 'rgba(255, 255, 255, 0.015)', borderRight: '1px solid rgba(255, 255, 255, 0.06)' }}>
                      {s.label}
                    </td>
                    <td style={{ padding: '14px 24px', color: '#e5ede8', fontWeight: 500 }}>
                      {s.value}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </section>

    </div>
  );
}

ProductDetail.propTypes = {
  productId: PropTypes.string,
  product: PropTypes.shape({
    id: PropTypes.string,
    name: PropTypes.string,
    shortName: PropTypes.string,
    categoryLabel: PropTypes.string,
    category: PropTypes.string,
    rate: PropTypes.string,
    rateDisplay: PropTypes.string,
    qty: PropTypes.oneOfType([PropTypes.string, PropTypes.number]),
    description: PropTypes.string,
    image: PropTypes.string,
    alt: PropTypes.string,
    statusType: PropTypes.string,
    poItemNo: PropTypes.oneOfType([PropTypes.string, PropTypes.number]),
    features: PropTypes.arrayOf(PropTypes.string),
    applications: PropTypes.string,
    specs: PropTypes.arrayOf(
      PropTypes.shape({
        label: PropTypes.string,
        value: PropTypes.oneOfType([PropTypes.string, PropTypes.number]),
      })
    ),
  }),
  onSendEnquiry: PropTypes.func,
  onCallSales: PropTypes.func,
  onDownloadSpec: PropTypes.func,
};
