"""
Batch 3 generator for:
- industries.html
- downloads.html
- faq.html
- privacy.html
- terms.html
- shipping.html
- 404.html
- search.html
"""

import os
from build_batch1_clean import get_header, get_footer

BASE_DIR = r"D:\Client Websites"

INDUSTRIES_HTML = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#0d1a16">
  <meta name="description" content="Industrial sectors and equipment application domains served by M/s. Pukhraj Hastimal & Co.: Chemical synthesis, power distribution, fluid handling, thermal systems, and plant utilities.">
  <title>Industries & Applications | Pukhraj Hastimal & Co.</title>
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
          <span class="current">Industries & Applications</span>
        </nav>
        <h1 class="page-title">Industrial <em>Applications & Sectors.</em></h1>
        <p class="hero-subheading">
          Technical application contexts for our 33 verified industrial machines. Engineered for continuous duty in chemical synthesis, power distribution, thermal transfer, and plant utilities.
        </p>
      </div>
    </section>

    <section class="section-pad">
      <div class="container">
        
        <div style="background: #f7f9f7; border: 1px solid #dce5dd; border-radius: 8px; padding: 18px 24px; margin-bottom: 40px; font-size: 13.5px; line-height: 1.6; color: #354a3f;">
          <strong>Technical Scope & Verification Notice:</strong> Specific project references and contractual executions are anchored in Purchase Order Ref: <code>PH/001/26-27</code> (Delivery to Indian Emulsifiers Limited, MIDC Khed, Ratnagiri). The application domains outlined below represent genuine technical use cases for our supplied equipment fleets.
        </div>

        <div class="industry-grid">
          
          <!-- 01: Chemical & Emulsifier Processing -->
          <article class="industry-card">
            <div style="font-size: 32px; margin-bottom: 8px;">🧪</div>
            <h3>Speciality Chemicals & Emulsifiers</h3>
            <p style="font-size: 14.5px; line-height: 1.6; color: #3d5247; margin: 0;">
              High-temperature reboilers, vacuum distillation columns, and stirred reaction vessels require continuous, high-enthalpy saturated steam and protective rockwool cladding.
            </p>
            <div class="industry-equipment-list">
              <strong>Key Fleet Equipment:</strong><br>
              • Steam Boiler 850 KG/HR (Oil/Gas Dual Burner)<br>
              • Hot & Cold Insulation LRB Mattress Cladding<br>
              • Liquid-Ring Chemical Vacuum Pump<br>
              • Stainless Steel 316L Storage & Mixing Tanks
            </div>
            <a href="products.html?category=thermal" class="cat-link">View Thermal Chemical Equipment →</a>
          </article>

          <!-- 02: Industrial Electrical Substations -->
          <article class="industry-card">
            <div style="font-size: 32px; margin-bottom: 8px;">⚡</div>
            <h3>Substations & Power Distribution</h3>
            <p style="font-size: 14.5px; line-height: 1.6; color: #3d5247; margin: 0;">
              Industrial plants operating heavy inductive loads require high-tension metering, vacuum breaker isolation, step-down voltage transformation, and automatic power factor harmonic correction.
            </p>
            <div class="industry-equipment-list">
              <strong>Key Fleet Equipment:</strong><br>
              • Transformer & HT Connection Breaker (VCB)<br>
              • Transformer & LT Correction Breaker<br>
              • APFC Panels with Detuned Harmonic Filters (Items 03 & 06)<br>
              • Compartmentalized MCC Control Panels
            </div>
            <a href="products.html?category=electrical" class="cat-link">View Electrical Infrastructure →</a>
          </article>

          <!-- 03: Process Cooling & Chilling -->
          <article class="industry-card">
            <div style="font-size: 32px; margin-bottom: 8px;">❄️</div>
            <h3>Process Cooling & Thermal Rejection</h3>
            <p style="font-size: 14.5px; line-height: 1.6; color: #3d5247; margin: 0;">
              Exothermic reactions, condenser circuits, and hydraulic lines demand reliable closed-loop chilling and atmospheric heat dissipation to sustain target crystallization and process temperatures.
            </p>
            <div class="industry-equipment-list">
              <strong>Key Fleet Equipment:</strong><br>
              • Water-Cooled Screw Chiller (Zenvent Engineering)<br>
              • Industrial Induced-Draft Cooling Tower<br>
              • Shell & Tube Heat Exchanger / Condenser<br>
              • Gasketed Plate & Frame Heat Exchanger
            </div>
            <a href="products.html?category=thermal" class="cat-link">View Cooling Equipment →</a>
          </article>

          <!-- 04: Industrial Pneumatics & Compressed Air -->
          <article class="industry-card">
            <div style="font-size: 32px; margin-bottom: 8px;">💨</div>
            <h3>Pneumatic Automation & Plant Air</h3>
            <p style="font-size: 14.5px; line-height: 1.6; color: #3d5247; margin: 0;">
              Continuous compressed air delivery for pneumatic control valves, packaging machines, fluidization beds, and instrumentation air dried to sub-zero pressure dew points.
            </p>
            <div class="industry-equipment-list">
              <strong>Key Fleet Equipment:</strong><br>
              • Rotary Screw Air Compressor (BK90-8GH)<br>
              • Compressed Air Receiver Pressure Vessel<br>
              • Refrigerated Compressed Air Dryer Unit<br>
              • High-Pressure Centrifugal Air Blower
            </div>
            <a href="products.html?category=air" class="cat-link">View Compressed Air Systems →</a>
          </article>

          <!-- 05: Fluid Transfer & Chemical Dosing -->
          <article class="industry-card">
            <div style="font-size: 32px; margin-bottom: 8px;">🔄</div>
            <h3>Fluid Transfer & Slurry Handling</h3>
            <p style="font-size: 14.5px; line-height: 1.6; color: #3d5247; margin: 0;">
              Precision transfer of high-viscosity resins, acidic reagents, abrasive slurries, and boiler feedwater under continuous duty with zero cross-contamination.
            </p>
            <div class="industry-equipment-list">
              <strong>Key Fleet Equipment:</strong><br>
              • Centrifugal Process & Chemical Slurry Pump<br>
              • Positive Displacement Rotary Gear Pump<br>
              • Chemical Dosing & Micro-Metering Pump<br>
              • Vertical Inline Circulation Water Pump
            </div>
            <a href="products.html?category=pumps" class="cat-link">View Fluid Pumps →</a>
          </article>

          <!-- 06: Process Water Treatment -->
          <article class="industry-card">
            <div style="font-size: 32px; margin-bottom: 8px;">💧</div>
            <h3>Water Demineralization & Filtration</h3>
            <p style="font-size: 14.5px; line-height: 1.6; color: #3d5247; margin: 0;">
              Boiler feed demineralization, cooling tower water softening, and multi-stage bag/cartridge filtration to prevent scale accumulation and corrosion in thermal equipment.
            </p>
            <div class="industry-equipment-list">
              <strong>Key Fleet Equipment:</strong><br>
              • Industrial Reverse Osmosis (RO) Plant<br>
              • Automated Ion-Exchange Water Softener Plant<br>
              • Multi-Grade Sand & Carbon Water Filter Skid<br>
              • Stainless Steel Bag & Cartridge Filter Housings
            </div>
            <a href="products.html?category=water" class="cat-link">View Water Treatment Systems →</a>
          </article>

        </div>
      </div>
    </section>
  </main>

  {{FOOTER}}
</body>
</html>
"""

DOWNLOADS_HTML = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#0d1a16">
  <meta name="description" content="Technical documentation, purchase order schedules, and equipment specification sheets for M/s. Pukhraj Hastimal & Co.">
  <title>Downloads & Technical Resources | Pukhraj Hastimal & Co.</title>
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
          <span class="current">Downloads & Resources</span>
        </nav>
        <h1 class="page-title">Technical <em>Downloads & Resources.</em></h1>
        <p class="hero-subheading">
          Official commercial schedules, technical reference sheets, and procurement requisition forms. Certified manufacturer test certificates and GA drawings are issued upon formal RFQ submission.
        </p>
      </div>
    </section>

    <section class="section-pad">
      <div class="container">
        
        <div style="background: #f7f9f7; border: 1px solid #dce5dd; border-radius: 8px; padding: 18px 24px; margin-bottom: 40px; font-size: 13.5px; line-height: 1.6; color: #354a3f;">
          <strong>Technical Documentation Policy:</strong> In compliance with engineering confidentiality, certified General Arrangement (GA) drawings, foundation schematics, and factory acceptance test (FAT) records are provided directly to qualified procurement engineering teams upon request.
        </div>

        <div class="downloads-grid">
          
          <!-- Doc 1: PO Equipment Schedule -->
          <div class="download-card">
            <div class="file-header">
              <div class="file-icon">DOC</div>
              <div>
                <div class="file-title">PO Ref: PH/001/26-27 Equipment Schedule</div>
                <span class="file-meta-tag">COMMERCIAL SUMMARY · 8 LINE ITEMS</span>
              </div>
            </div>
            <p style="font-size: 13.5px; color: #3e5449; line-height: 1.6; margin: 0;">
              Complete technical specification breakdown of the 8 verified purchase order items delivered to Indian Emulsifiers Limited (MIDC Khed, Ratnagiri) totaling ₹3,34,79,845.00.
            </p>
            <div style="margin-top: auto; padding-top: 14px; border-top: 1px solid var(--line); display: flex; justify-content: space-between; align-items: center;">
              <span style="font-family: var(--font-mono); font-size: 11.5px; color: var(--forest); font-weight: 700;">HTML / PRINT SUMMARY</span>
              <a href="about.html" class="cat-link" style="font-size: 12.5px;">View Summary →</a>
            </div>
          </div>

          <!-- Doc 2: 33-Machine Catalogue Index -->
          <div class="download-card">
            <div class="file-header">
              <div class="file-icon">PDF</div>
              <div>
                <div class="file-title">Industrial Equipment Fleet Directory (33 Machines)</div>
                <span class="file-meta-tag">TECHNICAL CATALOGUE · FULL FLEET</span>
              </div>
            </div>
            <p style="font-size: 13.5px; color: #3e5449; line-height: 1.6; margin: 0;">
              Unified catalogue index covering all 8 PO machines, 5 supplementary facility utilities, and 20 extended technical specification items with HSN codes and application scopes.
            </p>
            <div style="margin-top: auto; padding-top: 14px; border-top: 1px solid var(--line); display: flex; justify-content: space-between; align-items: center;">
              <span style="font-family: var(--font-mono); font-size: 11.5px; color: var(--forest); font-weight: 700;">INTERACTIVE / REQUISITION</span>
              <a href="products.html" class="cat-link" style="font-size: 12.5px;">Open Catalogue →</a>
            </div>
          </div>

          <!-- Doc 3: Official RFQ Specification Sheet -->
          <div class="download-card">
            <div class="file-header">
              <div class="file-icon">RFQ</div>
              <div>
                <div class="file-title">Procurement Quotation Request Requisition</div>
                <span class="file-meta-tag">OFFICIAL FORM · 7 MANDATORY FIELDS</span>
              </div>
            </div>
            <p style="font-size: 13.5px; color: #3e5449; line-height: 1.6; margin: 0;">
              Standardized procurement questionnaire for detailing fluid flow rates, boiler operating pressure, electrical transformer kVA, and site installation coordinates.
            </p>
            <div style="margin-top: auto; padding-top: 14px; border-top: 1px solid var(--line); display: flex; justify-content: space-between; align-items: center;">
              <span style="font-family: var(--font-mono); font-size: 11.5px; color: var(--forest); font-weight: 700;">ONLINE DISPATCHER</span>
              <a href="quote.html" class="cat-link" style="font-size: 12.5px;">Fill RFQ Form →</a>
            </div>
          </div>

          <!-- Doc 4: Technical CAD Schematic Reference Portfolio -->
          <div class="download-card">
            <div class="file-header">
              <div class="file-icon">CAD</div>
              <div>
                <div class="file-title">Extended Technical Schematic Portfolio (20 Models)</div>
                <span class="file-meta-tag">VECTOR SCHEMATICS · ASSETS/MACHINES/ADDITIONAL/</span>
              </div>
            </div>
            <p style="font-size: 13.5px; color: #3e5449; line-height: 1.6; margin: 0;">
              High-definition isometric CAD reference schematics for vacuum pumps, gear pumps, plate heat exchangers, evaporators, RO skids, and MCC panels.
            </p>
            <div style="margin-top: auto; padding-top: 14px; border-top: 1px solid var(--line); display: flex; justify-content: space-between; align-items: center;">
              <span style="font-family: var(--font-mono); font-size: 11.5px; color: var(--forest); font-weight: 700;">SVG / VECTOR REFS</span>
              <a href="products.html?filter=extended" class="cat-link" style="font-size: 12.5px;">Browse Schematics →</a>
            </div>
          </div>

        </div>

        <div style="margin-top: 48px; background: var(--white); border: 1px solid var(--line); border-radius: var(--radius-md); padding: 32px; box-shadow: var(--shadow-sm); text-align: center;">
          <h3 style="font-family: var(--font-heading); font-size: 20px; color: var(--forest-dark); margin: 0 0 10px;">
            Need a Certified Certified Drawing or IBR Boiler Certificate?
          </h3>
          <p style="font-size: 14.5px; color: var(--muted); max-width: 600px; margin: 0 auto 20px;">
            Manufacturer compliance documentation, hydrostatic test certificates, and factory calibration reports are dispatched directly to client engineering offices upon formal order placement.
          </p>
          <a href="quote.html" class="btn-hero-primary" style="display: inline-flex; text-decoration: none;">
            <span>Submit Engineering Request</span>
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
          </a>
        </div>

      </div>
    </section>
  </main>

  {{FOOTER}}
</body>
</html>
"""

FAQ_HTML = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#0d1a16">
  <meta name="description" content="Frequently asked questions regarding industrial machinery procurement, verification, specifications, and delivery by M/s. Pukhraj Hastimal & Co.">
  <title>Frequently Asked Questions | Pukhraj Hastimal & Co.</title>
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
          <span class="current">Frequently Asked Questions</span>
        </nav>
        <h1 class="page-title">Frequently Asked <em>Questions.</em></h1>
        <p class="hero-subheading">
          Clear, factual answers regarding our verified machinery fleet, purchase order documentation, quotation process, and technical engineering parameters.
        </p>
      </div>
    </section>

    <section class="section-pad">
      <div class="container" style="max-width: 860px;">
        <div class="faq-list">
          
          <details open>
            <summary>How are the 8 Purchase Order machines verified?</summary>
            <p>Every single line item in our primary catalogue matches the official description, HSN/SAC code, quantity, and basic rate listed in Purchase Order Ref: PH/001/26-27 dated 15 May 2026 (delivered to Indian Emulsifiers Limited, MIDC Khed, Ratnagiri), paired with its verified photograph from our facility documentation.</p>
          </details>

          <details>
            <summary>What are the 5 supplementary plant utility machines?</summary>
            <p>The cooling tower, water-cooled screw chiller (Zenvent Engineering), centrifugal chemical pump, rotary screw compressor (BK90-8GH), and shell-and-tube heat exchanger are authentic machines shown in the client's uploaded photographs. They are clearly identified as supplementary plant utilities not part of the PO line items.</p>
          </details>

          <details>
            <summary>What are the 20 extended technical specification machines?</summary>
            <p>To provide complete industrial plant coverage, 20 unique equipment categories (such as liquid-ring vacuum pumps, gear pumps, falling-film evaporators, RO skids, and MCC panels) are documented with standard industrial engineering specifications. Each is rendered with an authentic CAD technical reference schematic and clearly distinguished from PO items.</p>
          </details>

          <details>
            <summary>Why are some specifications labelled "Contact for Details"?</summary>
            <p>We adhere to strict engineering honesty. We do not invent operating pressures, motor RPM, or flow rates when unverified. For extended technical models, exact parameters are engineered and confirmed based on your specific application and sizing requirements.</p>
          </details>

          <details>
            <summary>How does the 240-frame interactive hero animation operate?</summary>
            <p>The hero section of our website features an interactive assembly pipeline utilizing 240 photographic JPG frames rendered on an HTML5 high-performance canvas synchronized with GSAP ScrollTrigger. As you scroll down the page, the industrial steam boiler progressively moves through its full assembly sequence.</p>
          </details>

          <details>
            <summary>How do I submit an official Request for Quotation (RFQ)?</summary>
            <p>Use our dedicated <a href="quote.html" style="color: var(--forest); font-weight: 700;">Request a Quote</a> page. Select your machine of interest from all 33 fleet models, enter your required quantity and technical parameters, and submit to format a direct email enquiry to <code>pukhrajhastimal@gmail.com</code>.</p>
          </details>

          <details>
            <summary>What is your statutory registration and office address?</summary>
            <p>M/s. PUKHRAJ HASTIMAL & CO. operates from Office No 03, 2nd Floor, 7 Kika Bhai Mansion, Gulalwadi, Mumbai - 400004. Our verified GST registration is <strong>27AFMPJ3478A1ZG</strong>.</p>
          </details>

          <details>
            <summary>How is logistics and equipment delivery handled?</summary>
            <p>Heavy machinery delivery is arranged via dedicated industrial flatbed trailers and specialized freight carriers. For complete delivery guidelines and transit inspection protocols, visit our <a href="shipping.html" style="color: var(--forest); font-weight: 700;">Shipping & Delivery</a> policy page.</p>
          </details>

        </div>
      </div>
    </section>
  </main>

  {{FOOTER}}
</body>
</html>
"""

PRIVACY_HTML = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#0d1a16">
  <meta name="description" content="Privacy Policy for M/s. Pukhraj Hastimal & Co. Details information collection and usage via procurement enquiry forms.">
  <title>Privacy Policy | M/s. Pukhraj Hastimal & Co.</title>
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
          <span class="current">Privacy Policy</span>
        </nav>
        <h1 class="page-title">Privacy <em>Policy.</em></h1>
        <p class="hero-subheading">
          Information disclosure explaining how corporate and technical data submitted through our quotation forms is processed and protected.
        </p>
      </div>
    </section>

    <section class="section-pad">
      <div class="container">
        <div class="legal-card">
          
          <div class="legal-notice-box">
            <strong>Legal Template Notice:</strong> This document represents a standard B2B industrial privacy disclosure for M/s. Pukhraj Hastimal & Co. Specific legal formulations require final review by legal counsel before statutory certification.
          </div>

          <div class="legal-section">
            <h2>1. Information We Collect</h2>
            <p>When you submit a Request for Quotation (RFQ) or contact form through our website, we collect only the business parameters necessary to process your equipment enquiry:</p>
            <ul>
              <li>Representative name and designation</li>
              <li>Company / Purchasing enterprise name</li>
              <li>Corporate email address and direct telephone / mobile number</li>
              <li>Machinery of interest, required capacity, and site delivery parameters</li>
            </ul>
          </div>

          <div class="legal-section">
            <h2>2. Purpose of Information Processing</h2>
            <p>All submitted details are utilized strictly for industrial equipment evaluation, quotation generation, engineering feasibility reviews, and direct commercial correspondence. We do not sell, rent, or trade your corporate information to third-party marketing services.</p>
          </div>

          <div class="legal-section">
            <h2>3. Client-Side Data Dispatch</h2>
            <p>Our RFQ dispatcher operates transparently by formatting inquiries directly into your default email application addressed to our procurement desk (<code>pukhrajhastimal@gmail.com</code>). No intermediate public cloud databases store your proprietary technical data without explicit mutual agreement.</p>
          </div>

          <div class="legal-section">
            <h2>4. Corporate Contact for Privacy Inquiries</h2>
            <p>For inquiries regarding data privacy or to request the deletion of your quotation communications, contact:</p>
            <p><strong>M/s. PUKHRAJ HASTIMAL & CO.</strong><br>
            Office No 03, 2nd Floor, 7 Kika Bhai Mansion, Gulalwadi, Mumbai - 400004<br>
            GSTIN: 27AFMPJ3478A1ZG · Email: <a href="mailto:pukhrajhastimal@gmail.com">pukhrajhastimal@gmail.com</a></p>
          </div>

        </div>
      </div>
    </section>
  </main>

  {{FOOTER}}
</body>
</html>
"""

TERMS_HTML = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#0d1a16">
  <meta name="description" content="Terms and Conditions governing quotations, product information, and website usage for M/s. Pukhraj Hastimal & Co.">
  <title>Terms & Conditions | M/s. Pukhraj Hastimal & Co.</title>
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
          <span class="current">Terms & Conditions</span>
        </nav>
        <h1 class="page-title">Commercial <em>Terms & Conditions.</em></h1>
        <p class="hero-subheading">
          Terms governing equipment quotations, specifications accuracy, commercial orders, and website usage for M/s. PUKHRAJ HASTIMAL & CO.
        </p>
      </div>
    </section>

    <section class="section-pad">
      <div class="container">
        <div class="legal-card">
          
          <div class="legal-notice-box">
            <strong>Draft Commercial Template:</strong> This document outlines standard commercial terms. Formal purchase contracts, delivery bonds, and warranty schedules are governed by dedicated purchase orders executed between the parties.
          </div>

          <div class="legal-section">
            <h2>1. Quotation & Pricing Validity</h2>
            <p>All prices and rates displayed on this website (such as rates referenced from Purchase Order Ref: PH/001/26-27) are historical benchmarks or formal order values as of their respective documentation dates. Formal quotations are issued upon written RFQ and remain valid for the period specified in the formal proforma invoice.</p>
          </div>

          <div class="legal-section">
            <h2>2. Technical Specifications & Engineering Tolerances</h2>
            <p>Product dimensions, weights, capacities, and schematic diagrams provided in the technical catalogue are intended for preliminary engineering planning. Certified manufacturing drawings and factory test certificates are provided following contract finalization.</p>
          </div>

          <div class="legal-section">
            <h2>3. Purchase Order Contracts</h2>
            <p>A binding commercial agreement is established only upon mutual signing of a formal Purchase Order, acceptance of payment milestones, and written confirmation of delivery schedules.</p>
          </div>

          <div class="legal-section">
            <h2>4. Jurisdiction & Governing Law</h2>
            <p>Any disputes arising from commercial quotations or website usage are subject to the exclusive jurisdiction of the competent courts in Mumbai, Maharashtra, India.</p>
          </div>

        </div>
      </div>
    </section>
  </main>

  {{FOOTER}}
</body>
</html>
"""

SHIPPING_HTML = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#0d1a16">
  <meta name="description" content="Shipping, freight delivery, and transit policy for heavy industrial equipment supplied by M/s. Pukhraj Hastimal & Co.">
  <title>Shipping & Delivery | M/s. Pukhraj Hastimal & Co.</title>
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
          <span class="current">Shipping, Delivery & Returns</span>
        </nav>
        <h1 class="page-title">Shipping & <em>Logistics Policy.</em></h1>
        <p class="hero-subheading">
          Logistics dispatch framework, site delivery coordination, and freight handling for heavy capital machinery across industrial corridors.
        </p>
      </div>
    </section>

    <section class="section-pad">
      <div class="container">
        <div class="legal-card">
          
          <div class="legal-notice-box">
            <strong>Operational Delivery Notice:</strong> Standard freight parameters for M/s. Pukhraj Hastimal & Co. Specific transit terms (FOB, Ex-Works, or CIF) and transit insurance are negotiated individually for each commercial purchase order.
          </div>

          <div class="legal-section">
            <h2>1. Primary Delivery Hub & Destination</h2>
            <p>Our verified logistics network coordinates direct dispatches to client industrial corridors. An example of our primary consignee delivery hub is documented in Purchase Order Ref: <code>PH/001/26-27</code>:</p>
            <p style="padding: 14px 18px; background: #f8faf8; border: 1px solid var(--line); border-radius: 6px; font-size: 13.5px;">
              <strong>Consignee Delivery Hub:</strong><br>
              Indian Emulsifiers Limited<br>
              E 10 Lote Parshuram Industrial Zone, MIDC Tal – Khed, Ratnagiri – 415722, Maharashtra
            </p>
          </div>

          <div class="legal-section">
            <h2>2. Heavy Freight & Specialized Transport</h2>
            <p>Capital equipment—such as 850 KG/HR steam boilers, transformer units, large-diameter cooling towers, and multi-tube heat exchangers—is dispatched via dedicated heavy-axle hydraulic trailers, flatbed carriers, or specialized logistics skids.</p>
          </div>

          <div class="legal-section">
            <h2>3. Unloading & Site Erection</h2>
            <p>Unless expressly contracted as a turnkey erection package (such as Line Item 08 of PO Ref: PH/001/26-27 for plant electrification and cable trays), site unloading, crane hire, civil foundations, and terminal connections remain the responsibility of the purchaser.</p>
          </div>

          <div class="legal-section">
            <h2>4. Returns & Acceptance Inspection</h2>
            <p>Due to the bespoke engineering nature of heavy capital equipment, returns are governed strictly by factory pre-dispatch inspection protocols (FAT) and formal delivery acceptance reports agreed upon in the purchase contract.</p>
          </div>

        </div>
      </div>
    </section>
  </main>

  {{FOOTER}}
</body>
</html>
"""

ERROR_404_HTML = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#0d1a16">
  <meta name="description" content="Page not found - M/s. Pukhraj Hastimal & Co. Industrial Machinery Website.">
  <title>Page Not Found (404) | Pukhraj Hastimal & Co.</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <a class="skip-link" href="#main">Skip to main content</a>
  {{HEADER}}

  <main id="main">
    <section class="section-pad">
      <div class="container">
        <div class="error-hero-card">
          <div class="error-code">404</div>
          <p class="eyebrow">RESOURCE NOT LOCATED</p>
          <h1 style="font-family: var(--font-heading); font-size: 32px; color: var(--forest-dark); margin: 0 0 16px;">
            The Requested Machinery Page Does Not Exist.
          </h1>
          <p style="font-size: 16px; color: var(--muted); line-height: 1.6; max-width: 520px; margin: 0 auto 32px;">
            The link you followed may be outdated, or the technical page has moved. You can browse our complete verified 33-machine fleet or search our catalogue.
          </p>
          
          <div style="display: flex; gap: 14px; justify-content: center; flex-wrap: wrap;">
            <a href="index.html" class="btn-hero-primary" style="text-decoration: none;">
              <span>Return to Homepage</span>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
            </a>
            <a href="products.html" class="btn-hero-secondary" style="text-decoration: none;">
              <span>Explore All 33 Machines</span>
            </a>
            <a href="contact.html" class="nav-cta" style="text-decoration: none; padding: 12px 20px;">
              <span>Contact Us</span>
            </a>
          </div>
        </div>
      </div>
    </section>
  </main>

  {{FOOTER}}
</body>
</html>
"""

SEARCH_HTML = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#0d1a16">
  <meta name="description" content="Search the complete 33 industrial machinery catalogue of M/s. Pukhraj Hastimal & Co.">
  <title>Catalogue Search | Pukhraj Hastimal & Co.</title>
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
          <span class="current">Search Results</span>
        </nav>
        <h1 class="page-title">Machinery Catalogue <em>Search.</em></h1>
        <p class="hero-subheading">
          Search across all 33 industrial machines by equipment title, HSN code, engineering specifications, or application domain.
        </p>
      </div>
    </section>

    <section class="section-pad">
      <div class="container">
        
        <!-- Live Search Input Box -->
        <div style="max-width: 680px; margin: 0 auto 36px;">
          <label class="search-box" style="width: 100%; border: 2px solid var(--forest-light); padding: 6px 16px; border-radius: var(--radius-sm); background: var(--white); box-shadow: var(--shadow-sm);">
            <span class="search-icon" style="font-size: 20px; color: var(--forest);" aria-hidden="true">⌕</span>
            <input id="liveSearchInput" type="search" placeholder="Type equipment name, model (e.g. BK90-8GH, Boiler, APFC), or HSN..." style="border: 0; outline: none; width: 100%; padding: 10px; font-size: 16px;">
          </label>
        </div>

        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 24px; border-bottom: 1px solid var(--line); padding-bottom: 12px;">
          <p id="searchCount" style="margin: 0; font-family: var(--font-heading); font-size: 18px; color: var(--forest-dark); font-weight: 700;">
            Searching Catalogue...
          </p>
          <a href="products.html" class="cat-link">View Full Grid →</a>
        </div>

        <!-- Search Results Grid -->
        <div class="equipment-grid" id="searchResultsGrid">
          <!-- Dynamically filled -->
        </div>

        <!-- Zero Results Fallback -->
        <div class="empty-state" id="zeroResults" hidden style="margin-top: 40px; padding: 60px 20px; text-align: center; background: var(--white); border: 1px solid var(--line); border-radius: var(--radius-md);">
          <div style="font-size: 40px; margin-bottom: 12px;">🔍</div>
          <h3 style="font-family: var(--font-heading); color: var(--forest-dark); margin: 0 0 8px;">No matching industrial equipment found.</h3>
          <p style="color: var(--muted); max-width: 500px; margin: 0 auto 20px;">
            We couldn't find any equipment matching that term. Please check your spelling or search by general category such as 'boiler', 'transformer', 'pump', or 'compressor'.
          </p>
          <a href="products.html" class="nav-cta" style="display: inline-flex; text-decoration: none;">Browse All 33 Machines</a>
        </div>

      </div>
    </section>
  </main>

  {{FOOTER}}

  <script src="assets/products-data.js"></script>
  <script>
    document.addEventListener("DOMContentLoaded", () => {
      const urlParams = new URLSearchParams(window.location.search);
      const queryParam = urlParams.get("q") || "";
      const searchInput = document.getElementById("liveSearchInput");
      const resultsGrid = document.getElementById("searchResultsGrid");
      const searchCount = document.getElementById("searchCount");
      const zeroResults = document.getElementById("zeroResults");

      searchInput.value = queryParam;

      function performSearch(query) {
        const q = query.trim().toLowerCase();
        const productList = Object.values(window.PRODUCTS_DATA || {});
        
        const matches = productList.filter(item => {
          if (!q) return true;
          const text = [
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
          return text.includes(q);
        });

        resultsGrid.innerHTML = "";

        if (matches.length === 0) {
          searchCount.textContent = `0 results for "${query}"`;
          zeroResults.hidden = false;
          resultsGrid.hidden = true;
        } else {
          zeroResults.hidden = true;
          resultsGrid.hidden = false;
          searchCount.textContent = query 
            ? `Found ${matches.length} matching machine${matches.length > 1 ? 's' : ''} for "${query}"`
            : `Displaying all ${matches.length} machines in catalogue`;

          matches.forEach((p, idx) => {
            const card = document.createElement("article");
            card.className = "equipment-card";

            let badgeClass = "badge-po";
            let badgeText = p.badgeLabel || "VERIFIED PO";
            if (p.statusType === "supplementary") {
              badgeClass = "badge-sup";
              badgeText = "SUPPLEMENTARY";
            } else if (p.statusType === "extended") {
              badgeClass = "badge-tech";
              badgeText = p.badgeLabel || (p.imageCategory === "illustrative" ? "SPECIFICATION VISUAL" : "AUTHENTIC PHOTO");
            }

            const itemNumber = String(p.poItemNo || (idx + 1)).padStart(2, '0');
            let rateBadge = '';
            if (p.statusType === 'po') {
              rateBadge = `<div class="card-rate-tag">PO Rate: ${p.rate} (Qty: ${p.qty})</div>`;
            } else if (p.statusType === 'supplementary') {
              rateBadge = `<div class="card-rate-tag sup-rate">Price on Request — Get a Quote</div>`;
            } else {
              rateBadge = `<div class="card-rate-tag ext-rate">${p.rateDisplay || ('Market Reference: ' + p.rate)}</div>`;
            }

            card.innerHTML = `
              <a class="card-image-wrap" href="product-detail.html?id=${encodeURIComponent(p.id)}">
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
                  </a>
                  <a class="nav-cta" href="quote.html?product=${encodeURIComponent(p.id)}" title="Request quote for ${p.shortName}" style="padding: 0 14px; display: inline-flex; align-items: center; justify-content: center;">
                    <span>RFQ</span>
                  </a>
                </div>
              </div>
            `;
            resultsGrid.appendChild(card);
          });
        }
      }

      searchInput.addEventListener("input", (e) => {
        performSearch(e.target.value);
      });

      performSearch(queryParam);
    });
  </script>
</body>
</html>
"""

def write_batch3():
    files = [
        ("industries.html", INDUSTRIES_HTML, "Industries"),
        ("downloads.html", DOWNLOADS_HTML, "Downloads"),
        ("faq.html", FAQ_HTML, "FAQ"),
        ("privacy.html", PRIVACY_HTML, "Privacy Policy"),
        ("terms.html", TERMS_HTML, "Terms & Conditions"),
        ("shipping.html", SHIPPING_HTML, "Shipping & Delivery"),
        ("404.html", ERROR_404_HTML, "404"),
        ("search.html", SEARCH_HTML, "Search"),
    ]
    for filename, tmpl, nav_name in files:
        filepath = os.path.join(BASE_DIR, filename)
        content = tmpl.replace("{{HEADER}}", get_header(nav_name)).replace("{{FOOTER}}", get_footer())
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"{filename} generated.")

write_batch3()
