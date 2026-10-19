import json

products = {
  # =========================================================================
  # 1. THE 8 VERIFIED ORIGINAL PURCHASE ORDER MACHINES
  # =========================================================================
  "po1_boiler": {
    "id": "po1_boiler",
    "poItemNo": 1,
    "name": "BOILER 850 KG/HR CAPACITY WITH OIL & GAS BURNER DUAL",
    "shortName": "Steam Boiler 850 KG/HR (Dual Burner)",
    "category": "thermal",
    "categoryLabel": "Thermal & Heat Transfer",
    "statusType": "po",
    "badgeLabel": "VERIFIED PO ITEM 01",
    "hsn": "84029090",
    "qty": "1 NOS",
    "rate": "₹16,50,000.00",
    "image": "assets/machines/po-01-boiler.png",
    "imageStatus": "Authentic Client Photograph (Matched)",
    "alt": "Industrial Steam Boiler 850 kg/hr with dual fuel burner",
    "description": "High-pressure industrial steam boiler featuring 850 kg/hr steam generation capacity, integrated with dual-fuel oil and natural gas burner assembly for continuous thermal processing.",
    "applications": "Chemical reboilers, reaction vessels, pharmaceutical heating, food processing, distillation columns.",
    "features": [
      "850 kg/hr steam generation capacity",
      "Automated dual-fuel burner for light oil and natural gas",
      "Integrated control panel and flame monitoring safety sensor",
      "Compliant with Indian Boiler Regulations (IBR) safety design"
    ],
    "specs": [
      { "label": "Document Reference", "value": "Purchase Order Ref: PH/001/26-27 · Line Item 01" },
      { "label": "HSN / SAC Code", "value": "84029090" },
      { "label": "Document Quantity", "value": "1 NOS" },
      { "label": "Stated Basic Rate", "value": "₹16,50,000.00" },
      { "label": "Steam Capacity", "value": "850 kg/hr" },
      { "label": "Burner Assembly", "value": "Dual Fuel (Light Oil & Natural Gas compatible)" },
      { "label": "Delivery Consignee", "value": "Indian Emulsifiers Limited, MIDC Tal–Khed, Ratnagiri" }
    ],
    "related": ["po2_insulation", "sup5_exchanger", "ext5_plate_exchanger", "ext7_evaporator"]
  },

  "po2_insulation": {
    "id": "po2_insulation",
    "poItemNo": 2,
    "name": "HOT & COLD INSULATION LRB MATTRESS WITH ALUMINIUM CLADDING",
    "shortName": "Thermal Insulation & Aluminium Cladding",
    "category": "process",
    "categoryLabel": "Process Equipment",
    "statusType": "po",
    "badgeLabel": "VERIFIED PO ITEM 02",
    "hsn": "87089900",
    "qty": "1 NOS (Full Scope)",
    "rate": "₹45,38,500.00",
    "image": "assets/machines/po-02-insulation.png",
    "imageStatus": "Authentic Client Photograph (Matched)",
    "alt": "Hot and cold insulation LRB mattress with aluminium cladding",
    "description": "Complete thermal insulation execution using Light Resin Bonded (LRB) rockwool mattresses clad with protective aluminium sheets across process reactors, reboiler columns, vessels, steam hot lines, and chilled water cold lines.",
    "applications": "Chemical reaction columns, distillation vessels, hot steam headers, cryogenic chilled fluid piping.",
    "features": [
      "High-density Light Resin Bonded (LRB) rockwool mattress",
      "Corrugated and plain aluminium sheet cladding",
      "Hot line thermal retention and cold line anti-condensation protection",
      "Turnkey installation across reactors, columns, and plant piping"
    ],
    "specs": [
      { "label": "Document Reference", "value": "Purchase Order Ref: PH/001/26-27 · Line Item 02" },
      { "label": "HSN / SAC Code", "value": "87089900" },
      { "label": "Document Quantity", "value": "1 NOS (Complete Plant Scope)" },
      { "label": "Stated Basic Rate", "value": "₹45,38,500.00" },
      { "label": "Insulation Material", "value": "LRB Rockwool Mattress as per required thickness & density" },
      { "label": "Cladding Sheet", "value": "Heavy-gauge aluminium protective cladding" },
      { "label": "Delivery Consignee", "value": "Indian Emulsifiers Limited, MIDC Tal–Khed, Ratnagiri" }
    ],
    "related": ["po1_boiler", "ext8_storage_tank", "ext9_mixing_tank", "sup5_exchanger"]
  },

  "po3_apfc1": {
    "id": "po3_apfc1",
    "poItemNo": 3,
    "name": "APFC PANELS WITH HARMONIC FILTERS (ITEM 03)",
    "shortName": "APFC Panel with Harmonic Filters",
    "category": "electrical",
    "categoryLabel": "Electrical Equipment",
    "statusType": "po",
    "badgeLabel": "VERIFIED PO ITEM 03",
    "hsn": "85321000",
    "qty": "1 NOS",
    "rate": "₹17,15,000.00",
    "image": "assets/machines/po-03-apfc-panel.png",
    "imageStatus": "Authentic Client Photograph (Matched)",
    "alt": "APFC panel with harmonic filters",
    "description": "Automatic Power Factor Correction (APFC) panel enclosure equipped with capacitor banks and detuned copper-wound harmonic suppression filter inductors.",
    "applications": "Industrial substations, chemical plant power distribution, motor control centres, utility power factor management.",
    "features": [
      "Heavy-duty cylindrical dry-type capacitor cells",
      "7% detuned copper-wound harmonic suppression reactors",
      "Microprocessor-based intelligent power factor relay controller",
      "IP54/55 compartmentalized sheet metal enclosure"
    ],
    "specs": [
      { "label": "Document Reference", "value": "Purchase Order Ref: PH/001/26-27 · Line Item 03" },
      { "label": "HSN / SAC Code", "value": "85321000" },
      { "label": "Document Quantity", "value": "1 NOS" },
      { "label": "Stated Basic Rate", "value": "₹17,15,000.00" },
      { "label": "Operating Voltage", "value": "415V, 3-Phase, 50 Hz" },
      { "label": "Harmonic Suppression", "value": "Detuned series reactors preventing harmonic resonance" },
      { "label": "Delivery Consignee", "value": "Indian Emulsifiers Limited, MIDC Tal–Khed, Ratnagiri" }
    ],
    "related": ["po4_ltbreaker", "po5_htbreaker", "po6_apfc2", "ext20_mcc_panel"]
  },

  "po4_ltbreaker": {
    "id": "po4_ltbreaker",
    "poItemNo": 4,
    "name": "TRANSFORMER & LT ORRECTION BREAKER",
    "shortName": "Transformer & LT Breaker Panel",
    "category": "electrical",
    "categoryLabel": "Electrical Equipment",
    "statusType": "po",
    "badgeLabel": "VERIFIED PO ITEM 04",
    "hsn": "995461",
    "qty": "1 NOS",
    "rate": "₹38,36,250.00",
    "image": "assets/machines/po-04-transformer-lt.png",
    "imageStatus": "Authentic Client Photograph (Matched)",
    "alt": "Transformer & LT breaker panel substation installation",
    "description": "Substation step-down distribution transformer coupled with low-tension (LT) main circuit breaker and power distribution cubicle.",
    "applications": "Main plant electrical intake, primary step-down substation, low-voltage distribution.",
    "features": [
      "Heavy-duty industrial step-down transformer",
      "Four-pole motorized draw-out Air Circuit Breaker (ACB)",
      "High short-circuit withstand busbar chamber",
      "Comprehensive digital metering and overcurrent trip unit"
    ],
    "specs": [
      { "label": "Document Reference", "value": "Purchase Order Ref: PH/001/26-27 · Line Item 04" },
      { "label": "HSN / SAC Code", "value": "995461" },
      { "label": "Document Quantity", "value": "1 NOS" },
      { "label": "Stated Basic Rate", "value": "₹38,36,250.00" },
      { "label": "Equipment Role", "value": "Power transformation & low-tension feeder protection" },
      { "label": "Delivery Consignee", "value": "Indian Emulsifiers Limited, MIDC Tal–Khed, Ratnagiri" }
    ],
    "related": ["po3_apfc1", "po5_htbreaker", "po7_network", "ext18_diesel_generator"]
  },

  "po5_htbreaker": {
    "id": "po5_htbreaker",
    "poItemNo": 5,
    "name": "TRANSFORMER & HT CONNECTION BREAKER",
    "shortName": "Transformer & HT Breaker (VCB)",
    "category": "electrical",
    "categoryLabel": "Electrical Equipment",
    "statusType": "po",
    "badgeLabel": "VERIFIED PO ITEM 05",
    "hsn": "85042100",
    "qty": "1 NOS",
    "rate": "₹37,48,000.00",
    "image": "assets/machines/po-05-transformer-ht.png",
    "imageStatus": "Authentic Client Photograph (Matched)",
    "alt": "Transformer & HT Connection Vacuum Circuit Breaker (VCB)",
    "description": "High-tension 11kV connection switchgear featuring Vacuum Circuit Breakers (VCB), Current Transformers (CTs), Potential Transformers (PT), digital protection relay, busbars, and metering section.",
    "applications": "High-tension incoming utility substation, grid switching, transformer protection.",
    "features": [
      "11kV / 12kV Vacuum Circuit Breaker (VCB) interrupters",
      "Current Transformers (CTs) and Potential Transformers (PT)",
      "Digital numerical overcurrent, earth-fault & differential protection relay",
      "Spring-charge motorized operating mechanism with trip/close coils"
    ],
    "specs": [
      { "label": "Document Reference", "value": "Purchase Order Ref: PH/001/26-27 · Line Item 05" },
      { "label": "HSN / SAC Code", "value": "85042100" },
      { "label": "Document Quantity", "value": "1 NOS" },
      { "label": "Stated Basic Rate", "value": "₹37,48,000.00" },
      { "label": "Breaker Type", "value": "VCB (Vacuum Circuit Breaker)" },
      { "label": "Delivery Consignee", "value": "Indian Emulsifiers Limited, MIDC Tal–Khed, Ratnagiri" }
    ],
    "related": ["po4_ltbreaker", "po7_network", "ext18_diesel_generator", "ext20_mcc_panel"]
  },

  "po6_apfc2": {
    "id": "po6_apfc2",
    "poItemNo": 6,
    "name": "APFC PANNELS WITH HARMONIC FILTERS (LINE ITEM 06)",
    "shortName": "Secondary APFC Filter Panel",
    "category": "electrical",
    "categoryLabel": "Electrical Equipment",
    "statusType": "po",
    "badgeLabel": "VERIFIED PO ITEM 06",
    "hsn": "85321000",
    "qty": "1 NOS",
    "rate": "₹17,35,000.00",
    "image": "assets/machines/po-06-apfc-panel-2.png",
    "imageStatus": "Authentic Client Photograph (Matched)",
    "alt": "Secondary APFC panel with harmonic filters",
    "description": "Second distinct APFC harmonic filter panel line item in the purchase order, designated for secondary plant bus power factor correction.",
    "applications": "Secondary motor control feeders, heavy inductive utility clusters, process expansion bus.",
    "features": [
      "Modular stepped power factor correction",
      "Series iron-core harmonic detuned reactors",
      "Independent microprocessor telemetry",
      "Thermal overheat cutouts and fast-acting HRC fuses"
    ],
    "specs": [
      { "label": "Document Reference", "value": "Purchase Order Ref: PH/001/26-27 · Line Item 06" },
      { "label": "HSN / SAC Code", "value": "85321000" },
      { "label": "Document Quantity", "value": "1 NOS" },
      { "label": "Stated Basic Rate", "value": "₹17,35,000.00" },
      { "label": "Delivery Consignee", "value": "Indian Emulsifiers Limited, MIDC Tal–Khed, Ratnagiri" }
    ],
    "related": ["po3_apfc1", "po7_network", "ext20_mcc_panel"]
  },

  "po7_network": {
    "id": "po7_network",
    "poItemNo": 7,
    "name": "LT NETWORKING IN PLANT SUPPLYING OF METERING KIOSKS & SWITCHGEAR",
    "shortName": "LT Plant Networking & Main Switchgear",
    "category": "electrical",
    "categoryLabel": "Electrical Equipment",
    "statusType": "po",
    "badgeLabel": "VERIFIED PO ITEM 07",
    "hsn": "84734090",
    "qty": "1 NOS (Complete Plant Scope)",
    "rate": "₹47,00,000.00",
    "image": "assets/machines/po-07-lt-networking.png",
    "imageStatus": "Authentic Client Photograph (Matched)",
    "alt": "LT Networking in plant supplying metering kiosks and switchgear",
    "description": "Full plant low-tension electrical distribution infrastructure including metering kiosks, multi-tier switchgear cubicles, coloured busbar runs (R-Y-B-N), circuit breakers, cable termination joints, copper earthing strips, and plant lighting fixtures.",
    "applications": "Plant-wide electrical reticulation, distribution substations, factory lighting, MCC feeds.",
    "features": [
      "Weatherproof outdoor metering kiosks",
      "Multi-tier compartmentalized main LT switchgear",
      "High-conductivity copper busbars with insulation shrouds",
      "Earthing grid with chemical earthing pits and copper bonding tapes"
    ],
    "specs": [
      { "label": "Document Reference", "value": "Purchase Order Ref: PH/001/26-27 · Line Item 07" },
      { "label": "HSN / SAC Code", "value": "84734090" },
      { "label": "Document Quantity", "value": "1 NOS (Turnkey Plant Scope)" },
      { "label": "Stated Basic Rate", "value": "₹47,00,000.00" },
      { "label": "Delivery Consignee", "value": "Indian Emulsifiers Limited, MIDC Tal–Khed, Ratnagiri" }
    ],
    "related": ["po8_electrification", "ext20_mcc_panel", "ext19_electric_motor"]
  },

  "po8_electrification": {
    "id": "po8_electrification",
    "poItemNo": 8,
    "name": "CHARGES FOR ELECTRIFICATION, CABLE TRAYS, STARTERS & APPROVALS",
    "shortName": "Plant Electrification, Trays & Starters",
    "category": "electrical",
    "categoryLabel": "Electrical Equipment",
    "statusType": "po",
    "badgeLabel": "VERIFIED PO ITEM 08",
    "hsn": "995461",
    "qty": "1 NOS (Complete Execution)",
    "rate": "₹64,50,000.00",
    "image": "assets/machines/po-08-electrification.png",
    "imageStatus": "Authentic Client Photograph (Matched)",
    "alt": "Plant Electrification cable tray starters and push buttons",
    "description": "Execution of turnkey plant equipment electrification, perforated steel cable trays, heavy motor drive connections, local push-button emergency stations (LPBS), engineering drawings, and statutory permissions.",
    "applications": "Field motor connections, cable containment systems, operator safety stations, liaison compliance.",
    "features": [
      "Hot-dip galvanized perforated and ladder type cable trays",
      "Local control push-button stations (LPBS) with mushroom head e-stops",
      "DOL and Star-Delta starter integrations for plant drives",
      "CAD single-line diagrams, engineering approvals & statutory clearances"
    ],
    "specs": [
      { "label": "Document Reference", "value": "Purchase Order Ref: PH/001/26-27 · Line Item 08" },
      { "label": "HSN / SAC Code", "value": "995461" },
      { "label": "Document Quantity", "value": "1 NOS (Complete Execution)" },
      { "label": "Stated Basic Rate", "value": "₹64,50,000.00" },
      { "label": "Delivery Consignee", "value": "Indian Emulsifiers Limited, MIDC Tal–Khed, Ratnagiri" }
    ],
    "related": ["po7_network", "ext19_electric_motor", "ext20_mcc_panel"]
  },

  # =========================================================================
  # 2. THE 5 SUPPLEMENTARY PLANT UTILITIES (FROM CLIENT PHOTOGRAPHS)
  # =========================================================================
  "sup1_cooling": {
    "id": "sup1_cooling",
    "name": "INDUSTRIAL COOLING TOWER (INDUCED DRAFT)",
    "shortName": "Industrial Induced-Draft Cooling Tower",
    "category": "utilities",
    "categoryLabel": "Plant Utilities",
    "statusType": "supplementary",
    "badgeLabel": "SUPPLEMENTARY UTILITY",
    "hsn": "Contact for Details",
    "qty": "Contact for Details",
    "rate": "Contact for Details",
    "image": "assets/machines/sup-01-cooling-tower.png",
    "imageStatus": "Authentic Client Photograph (Matched)",
    "alt": "Industrial Induced-Draft Cooling Tower Plant",
    "description": "Multi-cell induced-draft industrial cooling tower structure complete with galvanized steel maintenance staircase, overhead walkway, upper fan stacks, and process water piping headers.",
    "applications": "Condenser water cooling, chemical reactor jacket heat rejection, air compressor cooling loops.",
    "features": [
      "Corrosion-resistant UV-stabilized FRP composite casing",
      "High-efficiency virgin PVC honeycomb fills with drift eliminators",
      "Heavy-duty cast aluminium / FRP fan blades with TEFC motor",
      "Complete external structural staircase and inspection walkways"
    ],
    "specs": [
      { "label": "Catalogue Classification", "value": "Supplementary Plant Utility (From Uploaded Photos)" },
      { "label": "PO Status", "value": "Not in PO Ref: PH/001/26-27 (Offered as Auxiliary Equipment)" },
      { "label": "Verified Photograph", "value": "Screenshot 2026-10-19 110351.png" },
      { "label": "Draft Type", "value": "Induced Draft Counter-Flow / Cross-Flow" },
      { "label": "Cooling Role", "value": "Heat rejection from circulating plant water circuits" },
      { "label": "Capacity & Pricing", "value": "Contact for Details" }
    ],
    "related": ["sup2_chiller", "sup3_pump", "sup5_exchanger", "ext4_circulation_pump"]
  },

  "sup2_chiller": {
    "id": "sup2_chiller",
    "name": "WATER-COOLED SCREW CHILLER (ZENVENT ENGINEERING)",
    "shortName": "Water-Cooled Screw Chiller",
    "category": "utilities",
    "categoryLabel": "Plant Utilities",
    "statusType": "supplementary",
    "badgeLabel": "SUPPLEMENTARY UTILITY",
    "hsn": "Contact for Details",
    "qty": "Contact for Details",
    "rate": "Contact for Details",
    "image": "assets/machines/sup-02-screw-chiller.png",
    "imageStatus": "Authentic Client Photograph (Matched)",
    "alt": "Water-Cooled Screw Chiller Zenvent Engineering",
    "description": "Heavy-duty industrial water-cooled screw chiller featuring horizontal shell-and-tube heat exchange vessel, twin screw compressor assembly, and dedicated PLC electrical control cabinet labeled 'Zenvent Engineering'.",
    "applications": "Precision reactor cooling, low-temperature batch distillation, pharmaceutical process refrigeration.",
    "features": [
      "Twin-screw refrigeration compressor with infinite slide valve modulation",
      "Cleanable water-cooled shell-and-tube condenser",
      "Direct PLC electronic control cabinet (Zenvent Engineering visible branding)",
      "High efficiency thermodynamic cycle with eco-friendly refrigerant"
    ],
    "specs": [
      { "label": "Catalogue Classification", "value": "Supplementary Plant Utility (From Uploaded Photos)" },
      { "label": "PO Status", "value": "Not in PO Ref: PH/001/26-27 (Offered as Auxiliary Equipment)" },
      { "label": "Verified Photographs", "value": "Screenshot 2026-10-19 110405.png & 110421.png" },
      { "label": "Visible Branding", "value": "Zenvent Engineering (control cabinet)" },
      { "label": "Chiller Type", "value": "Water-Cooled Screw Chiller Unit" },
      { "label": "Capacity & Pricing", "value": "Contact for Details" }
    ],
    "related": ["sup1_cooling", "sup3_pump", "ext6_refrig_condenser", "ext4_circulation_pump"]
  },

  "sup3_pump": {
    "id": "sup3_pump",
    "name": "CENTRIFUGAL PROCESS & CHEMICAL SLURRY PUMP",
    "shortName": "Centrifugal Chemical Process Pump",
    "category": "pumps",
    "categoryLabel": "Pumps & Fluid Handling",
    "statusType": "supplementary",
    "badgeLabel": "SUPPLEMENTARY UTILITY",
    "hsn": "Contact for Details",
    "qty": "Contact for Details",
    "rate": "Contact for Details",
    "image": "assets/machines/sup-03-centrifugal-pump.png",
    "imageStatus": "Authentic Client Photograph (Matched)",
    "alt": "Centrifugal Process & Chemical Slurry Pump",
    "description": "Base-mounted industrial centrifugal process pump with flanged radial discharge, high-torque TEFC induction motor, and rigid steel skid.",
    "applications": "Industrial water circulation, chemical slurry transfer, boiler feedwater circulation, heat exchanger delivery.",
    "features": [
      "Single-stage end-suction centrifugal design",
      "Robust baseplate mounting with vibration isolation",
      "Cartridge mechanical seal for leak-free chemical duty",
      "Heavy-duty cast volute casing with flanged connections"
    ],
    "specs": [
      { "label": "Catalogue Classification", "value": "Supplementary Plant Utility (From Uploaded Photos)" },
      { "label": "PO Status", "value": "Not in PO Ref: PH/001/26-27" },
      { "label": "Verified Photograph", "value": "Screenshot 2026-10-19 110434.png" },
      { "label": "Pump Type", "value": "End-suction centrifugal process pump" },
      { "label": "Capacity & Head", "value": "Contact for Details" }
    ],
    "related": ["ext1_vacuum_pump", "ext2_gear_pump", "ext4_circulation_pump", "sup1_cooling"]
  },

  "sup4_compressor": {
    "id": "sup4_compressor",
    "name": "ROTARY SCREW AIR COMPRESSOR BK90-8GH",
    "shortName": "Rotary Screw Air Compressor BK90-8GH",
    "category": "air",
    "categoryLabel": "Air & Compressed-Air",
    "statusType": "supplementary",
    "badgeLabel": "SUPPLEMENTARY UTILITY",
    "hsn": "Contact for Details",
    "qty": "Contact for Details",
    "rate": "Contact for Details",
    "image": "assets/machines/sup-04-screw-compressor.png",
    "imageStatus": "Authentic Client Photograph (Matched)",
    "alt": "Rotary Screw Air Compressor Model BK90-8GH",
    "description": "Cabinet-enclosed rotary screw compressor marked 'BK90-8GH' with integrated digital controller and emergency trip.",
    "applications": "Plant pneumatic control valves, air cylinder actuation, powder transport, workshop instrument air.",
    "features": [
      "Direct-coupled asymmetric rotary screw air-end",
      "Acoustically insulated weather-resistant canopy",
      "Intelligent microprocessor controller with pressure transducer feedback",
      "High-efficiency air-oil separation system"
    ],
    "specs": [
      { "label": "Catalogue Classification", "value": "Supplementary Plant Utility (From Uploaded Photos)" },
      { "label": "PO Status", "value": "Not in PO Ref: PH/001/26-27" },
      { "label": "Verified Photograph", "value": "Screenshot 2026-10-19 110443.png" },
      { "label": "Visible Model Number", "value": "BK90-8GH (printed on unit door)" },
      { "label": "Air Delivery & Rating", "value": "Contact for Details" }
    ],
    "related": ["ext10_air_receiver", "ext11_centrifugal_blower", "ext12_air_dryer"]
  },

  "sup5_exchanger": {
    "id": "sup5_exchanger",
    "name": "SHELL & TUBE HEAT EXCHANGER / INDUSTRIAL CONDENSER",
    "shortName": "Shell & Tube Industrial Heat Exchanger",
    "category": "thermal",
    "categoryLabel": "Thermal & Heat Transfer",
    "statusType": "supplementary",
    "badgeLabel": "SUPPLEMENTARY UTILITY",
    "hsn": "Contact for Details",
    "qty": "Contact for Details",
    "rate": "Contact for Details",
    "image": "assets/machines/sup-05-heat-exchanger.png",
    "imageStatus": "Authentic Client Photograph (Matched)",
    "alt": "Shell and Tube Heat Exchanger and Industrial Condenser",
    "description": "Twin stacked industrial shell-and-tube heat exchangers with bolted flanged tube sheets in workshop fabrication bay.",
    "applications": "Distillation overhead condensation, process liquid heating/cooling, boiler blowdown heat recovery.",
    "features": [
      "High thermal transfer multi-pass shell and seamless tube bundle",
      "Precision-machined circular tube sheets with expansion joints",
      "Heavy bolted flange end-bonnets for cleanable tube access",
      "Fabricated to ASME Section VIII / TEMA standards"
    ],
    "specs": [
      { "label": "Catalogue Classification", "value": "Supplementary Plant Utility (From Uploaded Photos)" },
      { "label": "PO Status", "value": "Not in PO Ref: PH/001/26-27" },
      { "label": "Verified Photograph", "value": "Screenshot 2026-10-19 110452.png" },
      { "label": "Design Type", "value": "Fixed / U-tube / Floating Head Shell-and-Tube Exchanger" },
      { "label": "Surface Area & Rating", "value": "Contact for Details" }
    ],
    "related": ["po1_boiler", "po2_insulation", "ext5_plate_exchanger", "sup1_cooling"]
  },

  # =========================================================================
  # 3. EXACTLY 20 NEW UNIQUE INDUSTRIAL MACHINES (EXTENDED CATALOGUE)
  # =========================================================================
  "ext1_vacuum_pump": {
    "id": "ext1_vacuum_pump",
    "name": "INDUSTRIAL LIQUID-RING VACUUM PUMP SYSTEM",
    "shortName": "Liquid-Ring Vacuum Pump",
    "category": "pumps",
    "categoryLabel": "Pumps & Fluid Handling",
    "statusType": "extended",
    "badgeLabel": "EXTENDED CATALOGUE",
    "hsn": "Contact for Details",
    "qty": "As per requirement",
    "rate": "Contact for Quotation",
    "image": "assets/machines/additional/ext-01-vacuum-pump.svg",
    "imageStatus": "Technical Blueprint Schematic (Specification on RFQ)",
    "alt": "Industrial Liquid-Ring Vacuum Pump System schematic",
    "description": "Heavy-duty single and two-stage liquid-ring vacuum pump unit engineered for handling condensable vapours, moist gases, and industrial chemical process evacuations.",
    "applications": "Vacuum distillation, reactor degassing, vacuum drying ovens, chemical solvent recovery.",
    "features": [
      "Non-contacting impeller design with liquid seal",
      "Isothermal compression suitable for explosive/flammable vapours",
      "Available in SS304, SS316, and Cast Iron metallurgy",
      "Complete skid with seal-water recirculation heat exchanger"
    ],
    "specs": [
      { "label": "Classification", "value": "Extended Catalogue (Technical Reference)" },
      { "label": "Vacuum Level", "value": "Down to 33 mbar (with water seal) or lower with air ejector" },
      { "label": "Shaft Sealing", "value": "Mechanical seal / Gland packing options" },
      { "label": "Commercial Status", "value": "Contact for Quotation & Sizing" }
    ],
    "related": ["sup3_pump", "ext2_gear_pump", "ext3_dosing_pump"]
  },

  "ext2_gear_pump": {
    "id": "ext2_gear_pump",
    "name": "POSITIVE DISPLACEMENT ROTARY GEAR PUMP",
    "shortName": "Positive Displacement Gear Pump",
    "category": "pumps",
    "categoryLabel": "Pumps & Fluid Handling",
    "statusType": "extended",
    "badgeLabel": "EXTENDED CATALOGUE",
    "hsn": "Contact for Details",
    "qty": "As per requirement",
    "rate": "Contact for Quotation",
    "image": "assets/machines/additional/ext-02-gear-pump.svg",
    "imageStatus": "Technical Blueprint Schematic (Specification on RFQ)",
    "alt": "Positive Displacement Rotary Gear Pump schematic",
    "description": "Precision external rotary gear pump designed for the pulse-free transfer of high-viscosity chemicals, polymers, resins, fuel oils, and industrial emulsions.",
    "applications": "Fuel oil transfer to boiler burners, viscous chemical pumping, resin dosing, lube oil systems.",
    "features": [
      "Hardened alloy steel / stainless steel precision gears",
      "Self-priming positive displacement pumping mechanism",
      "Integrated internal or external pressure relief bypass valve",
      "High mechanical efficiency under continuous duty"
    ],
    "specs": [
      { "label": "Classification", "value": "Extended Catalogue (Technical Reference)" },
      { "label": "Viscosity Range", "value": "Up to 100,000 cSt" },
      { "label": "Pressure Rating", "value": "Up to 16 Bar (g)" },
      { "label": "Commercial Status", "value": "Contact for Quotation & Sizing" }
    ],
    "related": ["po1_boiler", "ext1_vacuum_pump", "sup3_pump"]
  },

  "ext3_dosing_pump": {
    "id": "ext3_dosing_pump",
    "name": "PRECISION CHEMICAL METERING & DOSING PUMP",
    "shortName": "Chemical Dosing & Metering Pump",
    "category": "pumps",
    "categoryLabel": "Pumps & Fluid Handling",
    "statusType": "extended",
    "badgeLabel": "EXTENDED CATALOGUE",
    "hsn": "Contact for Details",
    "qty": "As per requirement",
    "rate": "Contact for Quotation",
    "image": "assets/machines/additional/ext-03-dosing-pump.svg",
    "imageStatus": "Technical Blueprint Schematic (Specification on RFQ)",
    "alt": "Chemical Dosing and Metering Pump schematic",
    "description": "Electromechanically driven diaphragm chemical metering pump designed for exact, repeatable dosing of corrosion inhibitors, biocides, acids, and process additives.",
    "applications": "Boiler feedwater chemical dosing, cooling tower biocide treatment, effluent treatment pH control.",
    "features": [
      "PTFE diaphragm with zero leakage wetted-end construction",
      "Manual and 4-20mA automated stroke length regulation",
      "Chemical-resistant liquid ends in PVDF, PP, and SS316",
      "Built-in relief and back-pressure valve coordination"
    ],
    "specs": [
      { "label": "Classification", "value": "Extended Catalogue (Technical Reference)" },
      { "label": "Dosing Accuracy", "value": "±1% steady-state metering tolerance" },
      { "label": "Stroke Control", "value": "Micrometer dial & optional 4-20 mA analog input" },
      { "label": "Commercial Status", "value": "Contact for Quotation & Sizing" }
    ],
    "related": ["po1_boiler", "sup1_cooling", "ext16_ro_system", "ext17_water_softener"]
  },

  "ext4_circulation_pump": {
    "id": "ext4_circulation_pump",
    "name": "VERTICAL INLINE WATER CIRCULATION PUMP",
    "shortName": "Vertical Inline Circulation Pump",
    "category": "pumps",
    "categoryLabel": "Pumps & Fluid Handling",
    "statusType": "extended",
    "badgeLabel": "EXTENDED CATALOGUE",
    "hsn": "Contact for Details",
    "qty": "As per requirement",
    "rate": "Contact for Quotation",
    "image": "assets/machines/additional/ext-04-circulation-pump.svg",
    "imageStatus": "Technical Blueprint Schematic (Specification on RFQ)",
    "alt": "Vertical Inline Water Circulation Pump schematic",
    "description": "Close-coupled vertical inline centrifugal booster pump designed for compact space-saving installation in heating, chiller circulation, and cooling tower water loops.",
    "applications": "Chilled water circulation, HVAC utility loops, boiler secondary heating loops, condenser water boosting.",
    "features": [
      "Inline suction and discharge ports directly into pipework",
      "Space-saving vertical orientation with rigid motor stool",
      "Balanced silicon carbide mechanical seal",
      "Low noise IE3 premium efficiency electric motor"
    ],
    "specs": [
      { "label": "Classification", "value": "Extended Catalogue (Technical Reference)" },
      { "label": "Pipe Connection", "value": "Flanged PN16 / ANSI 150#" },
      { "label": "Temperature Range", "value": "-15°C to +120°C" },
      { "label": "Commercial Status", "value": "Contact for Quotation & Sizing" }
    ],
    "related": ["sup1_cooling", "sup2_chiller", "sup3_pump"]
  },

  "ext5_plate_exchanger": {
    "id": "ext5_plate_exchanger",
    "name": "GASKETED PLATE & FRAME HEAT EXCHANGER",
    "shortName": "Plate & Frame Heat Exchanger",
    "category": "thermal",
    "categoryLabel": "Thermal & Heat Transfer",
    "statusType": "extended",
    "badgeLabel": "EXTENDED CATALOGUE",
    "hsn": "Contact for Details",
    "qty": "As per requirement",
    "rate": "Contact for Quotation",
    "image": "assets/machines/additional/ext-05-plate-exchanger.svg",
    "imageStatus": "Technical Blueprint Schematic (Specification on RFQ)",
    "alt": "Gasketed Plate and Frame Heat Exchanger schematic",
    "description": "High-efficiency corrugated stainless steel plate heat exchanger assembled between carbon steel frame plates with elastomeric gaskets for compact thermal exchange.",
    "applications": "Process heat recovery, cooling tower isolation loops, beverage pasteurization, chemical cooling.",
    "features": [
      "Chevron corrugated plates generating high turbulent flow",
      "Close approach temperatures down to 1°C",
      "Expandable thermal duty by adding or removing plates",
      "Gaskets in NBR, EPDM, and Viton suitable for various chemical media"
    ],
    "specs": [
      { "label": "Classification", "value": "Extended Catalogue (Technical Reference)" },
      { "label": "Plate Materials", "value": "SS304, SS316, Titanium, Hastelloy" },
      { "label": "Operating Pressure", "value": "Up to 16/25 Bar (g)" },
      { "label": "Commercial Status", "value": "Contact for Quotation & Sizing" }
    ],
    "related": ["po1_boiler", "sup5_exchanger", "sup1_cooling"]
  },

  "ext6_refrig_condenser": {
    "id": "ext6_refrig_condenser",
    "name": "AIR-COOLED FINNED-TUBE REFRIGERATION CONDENSER",
    "shortName": "Air-Cooled Refrigeration Condenser",
    "category": "thermal",
    "categoryLabel": "Thermal & Heat Transfer",
    "statusType": "extended",
    "badgeLabel": "EXTENDED CATALOGUE",
    "hsn": "Contact for Details",
    "qty": "As per requirement",
    "rate": "Contact for Quotation",
    "image": "assets/machines/additional/ext-06-refrig-condenser.svg",
    "imageStatus": "Technical Blueprint Schematic (Specification on RFQ)",
    "alt": "Air-Cooled Finned-Tube Refrigeration Condenser schematic",
    "description": "Industrial remote air-cooled condenser equipped with high-efficiency copper tubes, sine-wave aluminium fins, and axial condenser fan modules for water-free heat rejection.",
    "applications": "Industrial cold rooms, dry refrigeration plants, chemical chiller heat rejection without cooling towers.",
    "features": [
      "Staggered inner-grooved copper tube geometry",
      "Epoxy-coated or hydrophilic aluminium fins for corrosion protection",
      "Low-noise axial fans with individual motor overload protection",
      "Heavy-duty galvanized steel powder-coated casing"
    ],
    "specs": [
      { "label": "Classification", "value": "Extended Catalogue (Technical Reference)" },
      { "label": "Refrigerant Compatibility", "value": "R134a, R404A, R407C, R410A" },
      { "label": "Fan Control", "value": "Step control or EC fan speed modulation" },
      { "label": "Commercial Status", "value": "Contact for Quotation & Sizing" }
    ],
    "related": ["sup2_chiller", "sup1_cooling", "sup5_exchanger"]
  },

  "ext7_evaporator": {
    "id": "ext7_evaporator",
    "name": "INDUSTRIAL FALLING-FILM CHEMICAL EVAPORATOR",
    "shortName": "Falling-Film Chemical Evaporator",
    "category": "process",
    "categoryLabel": "Process Equipment",
    "statusType": "extended",
    "badgeLabel": "EXTENDED CATALOGUE",
    "hsn": "Contact for Details",
    "qty": "As per requirement",
    "rate": "Contact for Quotation",
    "image": "assets/machines/additional/ext-07-evaporator.svg",
    "imageStatus": "Technical Blueprint Schematic (Specification on RFQ)",
    "alt": "Industrial Falling-Film Chemical Evaporator schematic",
    "description": "Multi-effect falling-film evaporation plant designed for concentration of heat-sensitive chemical solutions, effluent water recovery, and zero liquid discharge (ZLD) plants.",
    "applications": "Chemical concentration, caustic recovery, effluent evaporation, pharmaceutical drying concentration.",
    "features": [
      "Short residence time preventing thermal product degradation",
      "High heat transfer coefficient under low temperature differentials",
      "Vapour recompression (MVR / TVR) options for steam economy",
      "Stainless steel SS316L / Titanium construction"
    ],
    "specs": [
      { "label": "Classification", "value": "Extended Catalogue (Technical Reference)" },
      { "label": "System Type", "value": "Single / Multiple Effect Falling Film or Forced Circulation" },
      { "label": "Steam Consumption", "value": "Optimized per kg of water evaporated via thermal recompression" },
      { "label": "Commercial Status", "value": "Contact for Quotation & Sizing" }
    ],
    "related": ["po1_boiler", "po2_insulation", "ext8_storage_tank"]
  },

  "ext8_storage_tank": {
    "id": "ext8_storage_tank",
    "name": "INDUSTRIAL STAINLESS STEEL CHEMICAL STORAGE TANK",
    "shortName": "Chemical Storage Tank Vessel",
    "category": "process",
    "categoryLabel": "Process Equipment",
    "statusType": "extended",
    "badgeLabel": "EXTENDED CATALOGUE",
    "hsn": "Contact for Details",
    "qty": "As per requirement",
    "rate": "Contact for Quotation",
    "image": "assets/machines/additional/ext-08-storage-tank.svg",
    "imageStatus": "Technical Blueprint Schematic (Specification on RFQ)",
    "alt": "Industrial Stainless Steel Chemical Storage Tank schematic",
    "description": "Vertical cylindrical atmospheric storage tank built with high-grade stainless steel plates, dished or conical heads, and full instrumentation nozzles.",
    "applications": "Chemical feedstock storage, emulsion holding, solvent tanks, treated water reservoir.",
    "features": [
      "Precision TIG welded stainless steel SS304/SS316L vessel",
      "Internal pickling and passivation treatment",
      "Standard nozzles for level transmitters, vent, drain, and overflow",
      "Top manway access with davit arm"
    ],
    "specs": [
      { "label": "Classification", "value": "Extended Catalogue (Technical Reference)" },
      { "label": "Capacity Range", "value": "1,000 Litres to 50,000 Litres" },
      { "label": "Design Code", "value": "API 650 / IS 803 / ASME standards" },
      { "label": "Commercial Status", "value": "Contact for Quotation & Sizing" }
    ],
    "related": ["po2_insulation", "ext9_mixing_tank", "ext1_vacuum_pump"]
  },

  "ext9_mixing_tank": {
    "id": "ext9_mixing_tank",
    "name": "JACKETED MIXING TANK WITH MOTORIZED AGITATOR",
    "shortName": "Jacketed Mixing Tank with Agitator",
    "category": "process",
    "categoryLabel": "Process Equipment",
    "statusType": "extended",
    "badgeLabel": "EXTENDED CATALOGUE",
    "hsn": "Contact for Details",
    "qty": "As per requirement",
    "rate": "Contact for Quotation",
    "image": "assets/machines/additional/ext-09-mixing-tank.svg",
    "imageStatus": "Technical Blueprint Schematic (Specification on RFQ)",
    "alt": "Jacketed Mixing Tank with Motorized Agitator schematic",
    "description": "Heavy-duty reaction and blending vessel featuring a steam/hot water dimple jacket, top-entry motorized gear drive, and high-shear or anchor agitator blades.",
    "applications": "Emulsion manufacturing, chemical blending, resin formulation, polymer batch processing.",
    "features": [
      "Top-mounted geared motor drive with variable frequency control",
      "Dimple or limpet coil jacket rated for thermal heating and cooling",
      "Double mechanical seal with water flushing pot",
      "Mirror-polished wetted surfaces for hygienic, residue-free draining"
    ],
    "specs": [
      { "label": "Classification", "value": "Extended Catalogue (Technical Reference)" },
      { "label": "Impeller Types", "value": "Anchor, Marine Propeller, Pitch Blade Turbine, Cowles Dissolver" },
      { "label": "Jacket Pressure", "value": "Rated up to 6 Bar steam pressure" },
      { "label": "Commercial Status", "value": "Contact for Quotation & Sizing" }
    ],
    "related": ["po1_boiler", "po2_insulation", "ext8_storage_tank"]
  },

  "ext10_air_receiver": {
    "id": "ext10_air_receiver",
    "name": "COMPRESSED AIR RECEIVER PRESSURE VESSEL",
    "shortName": "Air Receiver Pressure Vessel",
    "category": "air",
    "categoryLabel": "Air & Compressed-Air",
    "statusType": "extended",
    "badgeLabel": "EXTENDED CATALOGUE",
    "hsn": "Contact for Details",
    "qty": "As per requirement",
    "rate": "Contact for Quotation",
    "image": "assets/machines/additional/ext-10-air-receiver.svg",
    "imageStatus": "Technical Blueprint Schematic (Specification on RFQ)",
    "alt": "Compressed Air Receiver Pressure Vessel schematic",
    "description": "Vertical cylindrical compressed air receiver built according to ASME Section VIII Div 1, providing dampening of air pulsations, condensate precipitation, and pneumatic reserve storage.",
    "applications": "Rotary screw compressor buffers, plant instrument air storage, pneumatic peak-demand smoothing.",
    "features": [
      "ASME Section VIII Div 1 / IS 2825 manufacturing standard",
      "Complete with calibrated safety relief valve and pressure gauge",
      "Manual and automated timed timer condensate drain valve",
      "Internally coated with anti-corrosive epoxy primer"
    ],
    "specs": [
      { "label": "Classification", "value": "Extended Catalogue (Technical Reference)" },
      { "label": "Working Pressure", "value": "8.5 Bar, 10.5 Bar, 16 Bar options" },
      { "label": "Volume Range", "value": "500 Litres to 10,000 Litres" },
      { "label": "Commercial Status", "value": "Contact for Quotation & Sizing" }
    ],
    "related": ["sup4_compressor", "ext11_centrifugal_blower", "ext12_air_dryer"]
  },

  "ext11_centrifugal_blower": {
    "id": "ext11_centrifugal_blower",
    "name": "INDUSTRIAL HIGH-PRESSURE CENTRIFUGAL BLOWER",
    "shortName": "Industrial Centrifugal Blower",
    "category": "air",
    "categoryLabel": "Air & Compressed-Air",
    "statusType": "extended",
    "badgeLabel": "EXTENDED CATALOGUE",
    "hsn": "Contact for Details",
    "qty": "As per requirement",
    "rate": "Contact for Quotation",
    "image": "assets/machines/additional/ext-11-centrifugal-blower.svg",
    "imageStatus": "Technical Blueprint Schematic (Specification on RFQ)",
    "alt": "Industrial High-Pressure Centrifugal Blower schematic",
    "description": "Heavy industrial centrifugal blower designed for combustion air supply, boiler forced/induced draft (FD/ID fans), pneumatic conveying, and industrial fume extraction.",
    "applications": "Boiler combustion air supply, kiln exhaust draft, ventilation systems, pneumatic material handling.",
    "features": [
      "Dynamically balanced backward-curved or radial blade impeller",
      "Heavy-gauge welded steel scroll casing with drain plug",
      "Direct-driven or V-belt coupled IE3 induction electric motor",
      "Vibration isolators and flexible inlet/outlet expansion bellows"
    ],
    "specs": [
      { "label": "Classification", "value": "Extended Catalogue (Technical Reference)" },
      { "label": "Pressure Range", "value": "Up to 15,000 Pa (1500 mmWC)" },
      { "label": "Flow Capacity", "value": "500 m³/hr to 80,000 m³/hr" },
      { "label": "Commercial Status", "value": "Contact for Quotation & Sizing" }
    ],
    "related": ["po1_boiler", "sup4_compressor", "ext10_air_receiver"]
  },

  "ext12_air_dryer": {
    "id": "ext12_air_dryer",
    "name": "REFRIGERATED COMPRESSED AIR DRYER UNIT",
    "shortName": "Refrigerated Air Dryer Unit",
    "category": "air",
    "categoryLabel": "Air & Compressed-Air",
    "statusType": "extended",
    "badgeLabel": "EXTENDED CATALOGUE",
    "hsn": "Contact for Details",
    "qty": "As per requirement",
    "rate": "Contact for Quotation",
    "image": "assets/machines/additional/ext-12-air-dryer.svg",
    "imageStatus": "Technical Blueprint Schematic (Specification on RFQ)",
    "alt": "Refrigerated Compressed Air Dryer Unit schematic",
    "description": "Self-contained refrigerated air drying system removing water vapour from compressed air lines to provide ISO 8573-1 Class 4 dry instrument air.",
    "applications": "Instrument air purification, pneumatic tool protection, pharmaceutical packaging air lines.",
    "features": [
      "Aluminium plate heat exchanger module for minimal pressure drop",
      "Consistent +3°C pressure dew point output",
      "Automatic zero-air-loss electronic condensate drain",
      "Eco-friendly R134a/R410A refrigeration circuit"
    ],
    "specs": [
      { "label": "Classification", "value": "Extended Catalogue (Technical Reference)" },
      { "label": "Pressure Dew Point", "value": "+3°C PDP at rated ambient" },
      { "label": "Air Flow Capacity", "value": "20 CFM to 2,000 CFM" },
      { "label": "Commercial Status", "value": "Contact for Quotation & Sizing" }
    ],
    "related": ["sup4_compressor", "ext10_air_receiver", "ext15_cartridge_filter"]
  },

  "ext13_filtration_system": {
    "id": "ext13_filtration_system",
    "name": "MULTI-GRADE WATER FILTRATION SYSTEM (SAND & CARBON)",
    "shortName": "Multi-Grade Sand & Carbon Filter",
    "category": "water",
    "categoryLabel": "Water Treatment & Filtration",
    "statusType": "extended",
    "badgeLabel": "EXTENDED CATALOGUE",
    "hsn": "Contact for Details",
    "qty": "As per requirement",
    "rate": "Contact for Quotation",
    "image": "assets/machines/additional/ext-13-filtration-system.svg",
    "imageStatus": "Technical Blueprint Schematic (Specification on RFQ)",
    "alt": "Multi-Grade Water Filtration System schematic",
    "description": "Pressure sand and activated carbon filtration dual-column skid engineered to remove suspended solids, turbidity, free chlorine, and organic odour from raw industrial water.",
    "applications": "Pretreatment for reverse osmosis plants, cooling tower makeup filtration, boiler feedwater raw filtration.",
    "features": [
      "Graded silica pebbles, sand, and high-iodine activated carbon media",
      "Multi-port multiport or pneumatic butterfly valve manifold for backwash",
      "Epoxy-lined mild steel or FRP composite pressure vessels",
      "Differential pressure gauges monitoring bed fouling"
    ],
    "specs": [
      { "label": "Classification", "value": "Extended Catalogue (Technical Reference)" },
      { "label": "Operating Flow", "value": "1 m³/hr to 100 m³/hr" },
      { "label": "Operating Pressure", "value": "Up to 5.0 Bar (g)" },
      { "label": "Commercial Status", "value": "Contact for Quotation & Sizing" }
    ],
    "related": ["ext16_ro_system", "ext17_water_softener", "sup1_cooling"]
  },

  "ext14_bag_filter": {
    "id": "ext14_bag_filter",
    "name": "STAINLESS STEEL BAG FILTER HOUSING VESSEL",
    "shortName": "Bag Filter Housing Vessel",
    "category": "water",
    "categoryLabel": "Water Treatment & Filtration",
    "statusType": "extended",
    "badgeLabel": "EXTENDED CATALOGUE",
    "hsn": "Contact for Details",
    "qty": "As per requirement",
    "rate": "Contact for Quotation",
    "image": "assets/machines/additional/ext-14-bag-filter.svg",
    "imageStatus": "Technical Blueprint Schematic (Specification on RFQ)",
    "alt": "Stainless Steel Bag Filter Housing Vessel schematic",
    "description": "Side-entry, bottom-outlet stainless steel filter housing designed for standard #1 and #2 filter bags for high-volume coarse to fine particulate interception.",
    "applications": "Cooling water filtration, resin filtration, raw chemical screening, paint and emulsion clarifying.",
    "features": [
      "Heavy swing-bolt quick-release lid mechanism with eye nuts",
      "Internal perforated stainless steel support basket",
      "Zero liquid bypass positive O-ring sealing arrangement",
      "Electropolished SS316 construction"
    ],
    "specs": [
      { "label": "Classification", "value": "Extended Catalogue (Technical Reference)" },
      { "label": "Bag Size Compatibility", "value": "Standard Size #1 (7\"x17\") and Size #2 (7\"x32\")" },
      { "label": "Micron Rating", "value": "1 micron to 200 microns (based on selected bag media)" },
      { "label": "Commercial Status", "value": "Contact for Quotation & Sizing" }
    ],
    "related": ["ext13_filtration_system", "ext15_cartridge_filter", "sup3_pump"]
  },

  "ext15_cartridge_filter": {
    "id": "ext15_cartridge_filter",
    "name": "MULTI-ELEMENT MICRONIC CARTRIDGE FILTER HOUSING",
    "shortName": "Cartridge Filter Housing",
    "category": "water",
    "categoryLabel": "Water Treatment & Filtration",
    "statusType": "extended",
    "badgeLabel": "EXTENDED CATALOGUE",
    "hsn": "Contact for Details",
    "qty": "As per requirement",
    "rate": "Contact for Quotation",
    "image": "assets/machines/additional/ext-15-cartridge-filter.svg",
    "imageStatus": "Technical Blueprint Schematic (Specification on RFQ)",
    "alt": "Multi-Element Micronic Cartridge Filter Housing schematic",
    "description": "Multi-cartridge vertical pressure vessel holding DOE (Double Open End) or SOE (Code 7) pleated/spun polypropylene micronic cartridges for critical polishing.",
    "applications": "RO membrane guard filtration (5 micron), boiler polished feedwater, demineralized water polish.",
    "features": [
      "Accommodates 3, 5, 7, 12, or 24 cartridge elements (10\" to 40\" length)",
      "Top cover davit arm lift for ergonomic cartridge replacement",
      "Sanitary SS316L mirror polish with zero crevice construction",
      "Dual pressure tapings for differential pressure monitoring"
    ],
    "specs": [
      { "label": "Classification", "value": "Extended Catalogue (Technical Reference)" },
      { "label": "Cartridge Rating", "value": "0.2 micron to 10 micron retention" },
      { "label": "Vessel Pressure", "value": "Design pressure up to 10 Bar (g)" },
      { "label": "Commercial Status", "value": "Contact for Quotation & Sizing" }
    ],
    "related": ["ext14_bag_filter", "ext16_ro_system", "ext17_water_softener"]
  },

  "ext16_ro_system": {
    "id": "ext16_ro_system",
    "name": "INDUSTRIAL REVERSE OSMOSIS WATER TREATMENT SYSTEM",
    "shortName": "Industrial Reverse Osmosis Plant",
    "category": "water",
    "categoryLabel": "Water Treatment & Filtration",
    "statusType": "extended",
    "badgeLabel": "EXTENDED CATALOGUE",
    "hsn": "Contact for Details",
    "qty": "As per requirement",
    "rate": "Contact for Quotation",
    "image": "assets/machines/additional/ext-16-ro-system.svg",
    "imageStatus": "Technical Blueprint Schematic (Specification on RFQ)",
    "alt": "Industrial Reverse Osmosis Water Treatment System schematic",
    "description": "Complete skid-mounted industrial RO desalination system featuring spiral-wound composite polyamide membranes, high-pressure vertical multistage pump, and automated CIP flush.",
    "applications": "High-pressure boiler feedwater demineralization, cooling tower makeup, chemical process pure water.",
    "features": [
      "High-rejection 8\" spiral-wound polyamide reverse osmosis membranes",
      "Vertical multistage SS316 high-pressure pump with VFD drive",
      "Online conductivity meters, flow rotameters, and digital PLC panel",
      "Automated clean-in-place (CIP) and low-pressure auto-flush cycle"
    ],
    "specs": [
      { "label": "Classification", "value": "Extended Catalogue (Technical Reference)" },
      { "label": "Salt Rejection", "value": "99.0% to 99.5% nominal TDS removal" },
      { "label": "Permeate Capacity", "value": "500 LPH to 50,000 LPH" },
      { "label": "Commercial Status", "value": "Contact for Quotation & Sizing" }
    ],
    "related": ["po1_boiler", "ext13_filtration_system", "ext17_water_softener"]
  },

  "ext17_water_softener": {
    "id": "ext17_water_softener",
    "name": "AUTOMATED INDUSTRIAL WATER SOFTENER PLANT",
    "shortName": "Industrial Water Softener Plant",
    "category": "water",
    "categoryLabel": "Water Treatment & Filtration",
    "statusType": "extended",
    "badgeLabel": "EXTENDED CATALOGUE",
    "hsn": "Contact for Details",
    "qty": "As per requirement",
    "rate": "Contact for Quotation",
    "image": "assets/machines/additional/ext-17-water-softener.svg",
    "imageStatus": "Technical Blueprint Schematic (Specification on RFQ)",
    "alt": "Automated Industrial Water Softener Plant schematic",
    "description": "Ion-exchange water softening plant with high-capacity cation exchange resin, salt brine tank, and automated multiport regeneration valve to eliminate hardness ions.",
    "applications": "Boiler feedwater scale prevention, cooling tower water softening, laundry, process wash water.",
    "features": [
      "Premium strong-acid cation exchange resin in sodium form",
      "Automated volume or time-based multiport control valve",
      "Heavy HDPE salt saturator brine regeneration tank with safety grid",
      "Corrosion-free FRP composite pressure vessel"
    ],
    "specs": [
      { "label": "Classification", "value": "Extended Catalogue (Technical Reference)" },
      { "label": "Treated Hardness", "value": "< 5 ppm (as CaCO3)" },
      { "label": "Flow Rates", "value": "1,000 LPH to 60,000 LPH" },
      { "label": "Commercial Status", "value": "Contact for Quotation & Sizing" }
    ],
    "related": ["po1_boiler", "sup1_cooling", "ext16_ro_system"]
  },

  "ext18_diesel_generator": {
    "id": "ext18_diesel_generator",
    "name": "PRIME POWER INDUSTRIAL DIESEL GENERATOR (DG SET)",
    "shortName": "Industrial Diesel Generator (DG Set)",
    "category": "electrical",
    "categoryLabel": "Electrical Equipment",
    "statusType": "extended",
    "badgeLabel": "EXTENDED CATALOGUE",
    "hsn": "Contact for Details",
    "qty": "As per requirement",
    "rate": "Contact for Quotation",
    "image": "assets/machines/additional/ext-18-diesel-generator.svg",
    "imageStatus": "Technical Blueprint Schematic (Specification on RFQ)",
    "alt": "Prime Power Industrial Diesel Generator DG Set schematic",
    "description": "Acoustic-enclosed stationary industrial diesel generator set designed for emergency standby and continuous prime electrical power generation during grid outages.",
    "applications": "Uninterrupted plant utility power, emergency boiler safety drives, continuous chemical plant power.",
    "features": [
      "Turbocharged water-cooled heavy-duty diesel engine",
      "Brushless self-excited Class H insulation synchronous alternator",
      "Sound-attenuated CPCB-compliant acoustic enclosure (<75 dBA at 1m)",
      "Digital Auto Mains Failure (AMF) control and changeover panel"
    ],
    "specs": [
      { "label": "Classification", "value": "Extended Catalogue (Technical Reference)" },
      { "label": "Electrical Output", "value": "415V, 3-Phase, 50 Hz, 0.8 PF" },
      { "label": "Rating Range", "value": "62.5 kVA to 1,500 kVA" },
      { "label": "Commercial Status", "value": "Contact for Quotation & Sizing" }
    ],
    "related": ["po4_ltbreaker", "po5_htbreaker", "ext20_mcc_panel"]
  },

  "ext19_electric_motor": {
    "id": "ext19_electric_motor",
    "name": "HEAVY-DUTY IE3 PREMIUM EFFICIENCY ELECTRIC MOTOR",
    "shortName": "IE3 Premium Efficiency Electric Motor",
    "category": "electrical",
    "categoryLabel": "Electrical Equipment",
    "statusType": "extended",
    "badgeLabel": "EXTENDED CATALOGUE",
    "hsn": "Contact for Details",
    "qty": "As per requirement",
    "rate": "Contact for Quotation",
    "image": "assets/machines/additional/ext-19-electric-motor.svg",
    "imageStatus": "Technical Blueprint Schematic (Specification on RFQ)",
    "alt": "Heavy-Duty IE3 Premium Efficiency Electric Motor schematic",
    "description": "Totally Enclosed Fan Cooled (TEFC) cast-iron three-phase squirrel cage induction motor engineered to IEC 60034-30 IE3 efficiency standards for industrial machinery drives.",
    "applications": "Centrifugal pump drives, air compressor motors, agitator motors, centrifugal blowers.",
    "features": [
      "IE3 Premium Efficiency class reducing plant power consumption",
      "Rugged cast iron frame with optimized cooling ribs",
      "Class F insulation with Class B temperature rise rating",
      "IP55 weather and dust ingress protection standard"
    ],
    "specs": [
      { "label": "Classification", "value": "Extended Catalogue (Technical Reference)" },
      { "label": "Voltage & Frequency", "value": "415V ±10%, 50 Hz, 3-Phase" },
      { "label": "Power Range", "value": "0.75 kW to 315 kW (2-pole, 4-pole, 6-pole)" },
      { "label": "Commercial Status", "value": "Contact for Quotation & Sizing" }
    ],
    "related": ["po8_electrification", "sup3_pump", "ext20_mcc_panel"]
  },

  "ext20_mcc_panel": {
    "id": "ext20_mcc_panel",
    "name": "COMPARTMENTALIZED MOTOR CONTROL CENTRE (MCC) PANEL",
    "shortName": "Motor Control Centre (MCC) Panel",
    "category": "electrical",
    "categoryLabel": "Electrical Equipment",
    "statusType": "extended",
    "badgeLabel": "EXTENDED CATALOGUE",
    "hsn": "Contact for Details",
    "qty": "As per requirement",
    "rate": "Contact for Quotation",
    "image": "assets/machines/additional/ext-20-mcc-panel.svg",
    "imageStatus": "Technical Blueprint Schematic (Specification on RFQ)",
    "alt": "Compartmentalized Motor Control Centre MCC Panel schematic",
    "description": "Form 3b/4b fully compartmentalized motor control centre panel housing intelligent DOL, Star-Delta, Soft Starter, and VFD modules with busbar chamber.",
    "applications": "Centralized factory motor coordination, plant automation, utility drive management.",
    "features": [
      "Fully compartmentalized modular draw-out or fixed feeder design",
      "Electrolytic grade high-conductivity insulated copper busbars",
      "Integration of Variable Frequency Drives (VFD) and intelligent motor relays",
      "IP54 sheet steel enclosure with safety interlocks and padlocking"
    ],
    "specs": [
      { "label": "Classification", "value": "Extended Catalogue (Technical Reference)" },
      { "label": "Rated Insulation Voltage", "value": "1000V AC" },
      { "label": "Short Circuit Withstand", "value": "50 kA RMS for 1 second" },
      { "label": "Commercial Status", "value": "Contact for Quotation & Sizing" }
    ],
    "related": ["po7_network", "po8_electrification", "ext19_electric_motor", "po3_apfc1"]
  }
}

# Write JS file
js_content = "/**\n * M/s. PUKHRAJ HASTIMAL & CO. — Central Product Catalogue Database\n * Total Verified Products: 33 (8 Original PO + 5 Supplementary + 20 Extended)\n */\n\nconst products = " + json.dumps(products, indent=2) + ";\n\nif (typeof module !== 'undefined' && module.exports) {\n  module.exports = products;\n}\n"

with open('d:/Client Websites/assets/products-data.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f"Generated assets/products-data.js with {len(products)} products.")
