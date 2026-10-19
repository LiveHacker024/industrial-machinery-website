"""
Batch 2 generator for categories.html, about.html, quote.html, contact.html
"""

import os

BASE_DIR = r"D:\Client Websites"

from build_batch1_clean import get_header, get_footer

CATEGORIES_HTML = """<!doctype html>
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
  {{HEADER}}

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

  {{FOOTER}}
</body>
</html>
"""

ABOUT_HTML = """<!doctype html>
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
  {{HEADER}}

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

  {{FOOTER}}
</body>
</html>
"""

QUOTE_HTML = """<!doctype html>
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
  {{HEADER}}

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

  {{FOOTER}}

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

CONTACT_HTML = """<!doctype html>
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
  {{HEADER}}

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

  {{FOOTER}}

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

def write_batch2():
    with open(os.path.join(BASE_DIR, "categories.html"), "w", encoding="utf-8") as f:
        f.write(CATEGORIES_HTML.replace("{{HEADER}}", get_header("Categories")).replace("{{FOOTER}}", get_footer()))
    print("categories.html generated.")

    with open(os.path.join(BASE_DIR, "about.html"), "w", encoding="utf-8") as f:
        f.write(ABOUT_HTML.replace("{{HEADER}}", get_header("About Us")).replace("{{FOOTER}}", get_footer()))
    print("about.html generated.")

    with open(os.path.join(BASE_DIR, "quote.html"), "w", encoding="utf-8") as f:
        f.write(QUOTE_HTML.replace("{{HEADER}}", get_header("Request a Quote")).replace("{{FOOTER}}", get_footer()))
    print("quote.html generated.")

    with open(os.path.join(BASE_DIR, "contact.html"), "w", encoding="utf-8") as f:
        f.write(CONTACT_HTML.replace("{{HEADER}}", get_header("Contact")).replace("{{FOOTER}}", get_footer()))
    print("contact.html generated.")

write_batch2()
