/**
 * M/s. Pukhraj Hastimal & Co. — Industrial Machinery Website
 * Core Logic: 240-Frame Scroll Assembly Animation & Verified Product Catalogue
 * 
 * FACTUAL ACCURACY NOTICE:
 * - Items 1 through 8 are derived directly from Purchase Order Ref: PH/001/26-27.
 * - Items 9 through 13 are supplementary plant equipment matching the client's uploaded photos.
 */

// ============================================================================
// 1. VERIFIED PRODUCT CATALOGUE DATABASE
// ============================================================================
const products = {
  // --- 8 VERIFIED ORIGINAL PURCHASE ORDER MACHINES ---
  po1_boiler: {
    id: "po1_boiler",
    poItemNo: 1,
    name: "BOILER 850 KG/HR CAPACITY WITH OIL & GAS BURNER DUAL",
    shortName: "Steam Boiler 850 KG/HR (Dual Burner)",
    category: "po",
    categoryLabel: "Purchase Order Item 01",
    hsn: "84029090",
    qty: "1 NOS",
    rate: "₹16,50,000.00",
    image: "assets/machines/po-01-boiler.png",
    alt: "Boiler 850 kg/hr capacity with oil & gas burner dual",
    isPoItem: true,
    poDescription: "BOILER 850 KG/HR CAPACITY WITH OIL & GAS BURNER DUAL.",
    verifiedDetails: "Industrial high-pressure steam boiler with a rated capacity of 850 kg/hr, equipped with an automated dual-fuel burner firing light oil and natural gas.",
    specs: [
      { label: "Document Reference", value: "Purchase Order Ref: PH/001/26-27 · Line Item 01" },
      { label: "HSN / SAC Code", value: "84029090" },
      { label: "Document Quantity", value: "1 NOS" },
      { label: "Stated Basic Rate", value: "₹16,50,000.00" },
      { label: "Steam Capacity", value: "850 kg/hr" },
      { label: "Burner Assembly", value: "Dual Fuel (Oil & Natural Gas compatible)" },
      { label: "Application", value: "Process steam generation for plant heating, reboilers, and distillation jackets" },
      { label: "Delivery Consignee", value: "Indian Emulsifiers Limited, MIDC Tal–Khed, Ratnagiri" }
    ]
  },

  po2_insulation: {
    id: "po2_insulation",
    poItemNo: 2,
    name: "HOT & COLD INSULATION LRB MATTRESS WITH ALUMINIUM CLADDING",
    shortName: "Thermal Insulation & Aluminium Cladding",
    category: "po",
    categoryLabel: "Purchase Order Item 02",
    hsn: "87089900",
    qty: "1 NOS (Full Scope)",
    rate: "₹45,38,500.00",
    image: "assets/machines/po-02-insulation.png",
    alt: "Hot and cold insulation LRB mattress with aluminium cladding",
    isPoItem: true,
    poDescription: "INSULATION HOT INSULATION LRB MATRESS AS PER REQUIRED SIZE WITH ALUMINIUM CLADDING FOR REACTOR REBOILER COLUMN VESSEL STEAN LINE HOT LINES, COLD LINES INSULATION ON CHILLED WATER LINES.",
    verifiedDetails: "Complete thermal insulation execution using Light Resin Bonded (LRB) rockwool mattresses clad with protective aluminium sheets across process reactors, reboiler columns, vessels, steam hot lines, and chilled water cold lines.",
    specs: [
      { label: "Document Reference", value: "Purchase Order Ref: PH/001/26-27 · Line Item 02" },
      { label: "HSN / SAC Code", value: "87089900" },
      { label: "Document Quantity", value: "1 NOS (Complete Plant Scope)" },
      { label: "Stated Basic Rate", value: "₹45,38,500.00" },
      { label: "Insulation Material", value: "Light Resin Bonded (LRB) Mattress as per required thickness & size" },
      { label: "Protective Cladding", value: "Aluminium sheet cladding with secure jointing" },
      { label: "Scope Coverage", value: "Reactor, reboiler column, vessel, steam lines, hot process lines & chilled water lines" },
      { label: "Delivery Consignee", value: "Indian Emulsifiers Limited, MIDC Tal–Khed, Ratnagiri" }
    ]
  },

  po3_apfc1: {
    id: "po3_apfc1",
    poItemNo: 3,
    name: "APFC PANELS WITH HARMONIC FILTERS",
    shortName: "APFC Panel with Harmonic Filters (Item 03)",
    category: "po",
    categoryLabel: "Purchase Order Item 03",
    hsn: "85321000",
    qty: "1 NOS",
    rate: "₹17,15,000.00",
    image: "assets/machines/po-03-apfc-panel.png",
    alt: "APFC panel with harmonic filters",
    isPoItem: true,
    poDescription: "APFC PANELS WITH HARMONIC FILTERS",
    verifiedDetails: "Automatic Power Factor Correction (APFC) panel enclosure equipped with capacitor banks and detuned copper-wound harmonic suppression filter inductors.",
    specs: [
      { label: "Document Reference", value: "Purchase Order Ref: PH/001/26-27 · Line Item 03" },
      { label: "HSN / SAC Code", value: "85321000" },
      { label: "Document Quantity", value: "1 NOS" },
      { label: "Stated Basic Rate", value: "₹17,15,000.00" },
      { label: "System Function", value: "Automatic power factor compensation with harmonic mitigation" },
      { label: "Components Visible", value: "Heavy-duty capacitor units, detuned harmonic filter inductors, busbar arrangement" },
      { label: "Voltage Rating", value: "415V, 3-Phase, 50 Hz" },
      { label: "Delivery Consignee", value: "Indian Emulsifiers Limited, MIDC Tal–Khed, Ratnagiri" }
    ]
  },

  po4_ltbreaker: {
    id: "po4_ltbreaker",
    poItemNo: 4,
    name: "TRANSFORMER & LT ORRECTION BREAKER",
    shortName: "Transformer & LT Breaker Panel",
    category: "po",
    categoryLabel: "Purchase Order Item 04",
    hsn: "995461",
    qty: "1 NOS",
    rate: "₹38,36,250.00",
    image: "assets/machines/po-04-transformer-lt.png",
    alt: "Transformer & LT correction breaker substation installation",
    isPoItem: true,
    poDescription: "TRANSFORMER & LT ORRECTION BREAKER",
    verifiedDetails: "Substation step-down distribution transformer coupled with low-tension (LT) main circuit breaker and power distribution cubicle.",
    specs: [
      { label: "Document Reference", value: "Purchase Order Ref: PH/001/26-27 · Line Item 04" },
      { label: "HSN / SAC Code", value: "995461" },
      { label: "Document Quantity", value: "1 NOS" },
      { label: "Stated Basic Rate", value: "₹38,36,250.00" },
      { label: "Equipment Role", value: "Power transformation & primary low-tension isolation / protection" },
      { label: "Substation Structure", value: "Outdoor/indoor transformer with cable terminations to LT main board" },
      { label: "Delivery Consignee", value: "Indian Emulsifiers Limited, MIDC Tal–Khed, Ratnagiri" }
    ]
  },

  po5_htbreaker: {
    id: "po5_htbreaker",
    poItemNo: 5,
    name: "TRANSFORMER & HT CONNECTION BREAKER",
    shortName: "Transformer & HT Connection Breaker (VCB)",
    category: "po",
    categoryLabel: "Purchase Order Item 05",
    hsn: "85042100",
    qty: "1 NOS",
    rate: "₹37,48,000.00",
    image: "assets/machines/po-05-transformer-ht.png",
    alt: "Transformer & HT Connection Vacuum Circuit Breaker (VCB)",
    isPoItem: true,
    poDescription: "TRANSFORMER & HT CONNECTION BREAKER",
    verifiedDetails: "High-tension 11kV connection switchgear featuring Vacuum Circuit Breakers (VCB), Current Transformers (CTs), Potential Transformers (PT), digital protection relay, busbars, and metering section.",
    specs: [
      { label: "Document Reference", value: "Purchase Order Ref: PH/001/26-27 · Line Item 05" },
      { label: "HSN / SAC Code", value: "85042100" },
      { label: "Document Quantity", value: "1 NOS" },
      { label: "Stated Basic Rate", value: "₹37,48,000.00" },
      { label: "Breaker Type", value: "VCB (Vacuum Circuit Breaker) with spring charge motor & trip/close coils" },
      { label: "Instrumentation", value: "Current Transformers (CTs), Potential Transformers (PT), Protection Relay & Metering" },
      { label: "Protection Scope", value: "Incoming HT connection, busbars, and transformer high-voltage switching" },
      { label: "Delivery Consignee", value: "Indian Emulsifiers Limited, MIDC Tal–Khed, Ratnagiri" }
    ]
  },

  po6_apfc2: {
    id: "po6_apfc2",
    poItemNo: 6,
    name: "APFC PANNELS WITH HARMONIC FILTERS",
    shortName: "APFC Panel with Harmonic Filters (Item 06)",
    category: "po",
    categoryLabel: "Purchase Order Item 06",
    hsn: "85321000",
    qty: "1 NOS",
    rate: "₹17,35,000.00",
    image: "assets/machines/po-06-apfc-panel-2.png",
    alt: "Secondary APFC panel with harmonic filters",
    isPoItem: true,
    poDescription: "APFC PANNELS WITH HARMONIC FILTERS",
    verifiedDetails: "Second distinct APFC harmonic filter panel line item in the purchase order, designated for secondary plant bus power factor correction.",
    specs: [
      { label: "Document Reference", value: "Purchase Order Ref: PH/001/26-27 · Line Item 06" },
      { label: "HSN / SAC Code", value: "85321000" },
      { label: "Document Quantity", value: "1 NOS" },
      { label: "Stated Basic Rate", value: "₹17,35,000.00" },
      { label: "System Function", value: "Secondary power factor correction and harmonic distortion suppression" },
      { label: "Designation", value: "Line Item 06 in formal PO (distinct rate from Item 03)" },
      { label: "Delivery Consignee", value: "Indian Emulsifiers Limited, MIDC Tal–Khed, Ratnagiri" }
    ]
  },

  po7_network: {
    id: "po7_network",
    poItemNo: 7,
    name: "LT NETWORKING IN PLANT SUPPLYING OF METERING KIOSK SQICTHER GEARM BREAKERS, CABLING, PANELING, TERMINATION JOINTS COPPER STRIPS EARTHING LIGHT & FIXTURES",
    shortName: "LT Plant Networking & Main Switchgear",
    category: "po",
    categoryLabel: "Purchase Order Item 07",
    hsn: "84734090",
    qty: "1 NOS (Complete Plant Scope)",
    rate: "₹47,00,000.00",
    image: "assets/machines/po-07-lt-networking.png",
    alt: "LT Networking in plant supplying metering kiosks and switchgear",
    isPoItem: true,
    poDescription: "LT NETWORKING IN PLANT SUPPLYING OF METERING KIOSK SQICTHER GEARM BREAKERS, CABLING, PANELING, TERMINATION JOINTS COPPER STRIPS EARTHING LIGHT & FIXTURES.",
    verifiedDetails: "Full plant low-tension electrical distribution infrastructure including metering kiosks, multi-tier switchgear cubicles, coloured busbar runs (R-Y-B-N), circuit breakers, cable termination joints, copper earthing strips, and plant lighting fixtures.",
    specs: [
      { label: "Document Reference", value: "Purchase Order Ref: PH/001/26-27 · Line Item 07" },
      { label: "HSN / SAC Code", value: "84734090" },
      { label: "Document Quantity", value: "1 NOS (Turnkey Plant Scope)" },
      { label: "Stated Basic Rate", value: "₹47,00,000.00" },
      { label: "Distribution Scope", value: "Metering kiosk, main switchgear breakers, cabling, paneling" },
      { label: "Earthing & Lighting", value: "Copper earthing strips, termination joints, lighting & fixtures" },
      { label: "Delivery Consignee", value: "Indian Emulsifiers Limited, MIDC Tal–Khed, Ratnagiri" }
    ]
  },

  po8_electrification: {
    id: "po8_electrification",
    poItemNo: 8,
    name: "CHARGES FOR ELECTRIFICATION, LIASO PERMISSION GRAWINGS APPROVALS, ELECTRICAL — ELECTRIFICATION FOR EQUIPMENT CABLE TRAY STARTERS PUSH BUTTON ETC",
    shortName: "Plant Electrification, Trays & Starters",
    category: "po",
    categoryLabel: "Purchase Order Item 08",
    hsn: "995461",
    qty: "1 NOS (Complete Scope)",
    rate: "₹64,50,000.00",
    image: "assets/machines/po-08-electrification.png",
    alt: "Plant Electrification cable tray starters and push buttons",
    isPoItem: true,
    poDescription: "CHARGES FOR ELECTRIFICATION, LIASO PERMISSION GRAWINGS APPROVALS, ELECTRICAL — ELECTRIFICATION FOR EQUIPMENT CABLE TRAY STARTERS PUSH BUTTON ETC.",
    verifiedDetails: "Execution of turnkey plant equipment electrification, perforated steel cable trays, heavy motor drive connections, local push-button emergency stations (LPBS), engineering drawings, and statutory permissions.",
    specs: [
      { label: "Document Reference", value: "Purchase Order Ref: PH/001/26-27 · Line Item 08" },
      { label: "HSN / SAC Code", value: "995461" },
      { label: "Document Quantity", value: "1 NOS (Complete Execution)" },
      { label: "Stated Basic Rate", value: "₹64,50,000.00" },
      { label: "Equipment Hardware", value: "Galvanized cable trays, motor starters, local control push-button stations" },
      { label: "Engineering Scope", value: "Equipment electrification, liaison permission, CAD drawings, statutory approvals" },
      { label: "Delivery Consignee", value: "Indian Emulsifiers Limited, MIDC Tal–Khed, Ratnagiri" }
    ]
  },

  // --- 5 SUPPLEMENTARY PLANT EQUIPMENT (FROM CLIENT PHOTOGRAPHS) ---
  sup1_cooling: {
    id: "sup1_cooling",
    name: "INDUSTRIAL COOLING TOWER (INDUCED DRAFT)",
    shortName: "Industrial Induced-Draft Cooling Tower",
    category: "supplementary",
    categoryLabel: "Supplementary Plant Equipment",
    hsn: "Contact for Details",
    qty: "Contact for Details",
    rate: "Contact for Details",
    image: "assets/machines/sup-01-cooling-tower.png",
    alt: "Industrial FRP cooling tower with circulation piping",
    isPoItem: false,
    poDescription: "Supplementary industrial machine verified from client uploaded photograph (Screenshot 2026-10-19 110351.png). Not listed as a line item in PO Ref: PH/001/26-27.",
    verifiedDetails: "Multi-cell induced-draft industrial cooling tower structure complete with galvanized steel maintenance staircase, overhead walkway, upper fan stacks, and process water piping headers.",
    specs: [
      { label: "Inventory Classification", value: "Supplementary Plant Utility (From Uploaded Photos)" },
      { label: "Purchase Order Status", value: "Not in PO Ref: PH/001/26-27 (Offered as Associated Plant Utility)" },
      { label: "Verified Photograph", value: "Screenshot 2026-10-19 110351.png" },
      { label: "Structure", value: "Multi-cell industrial tower with upper fan shrouds & galvanized staircase" },
      { label: "Cooling Application", value: "Heat rejection from recirculating condenser water and plant cooling circuits" },
      { label: "Specifications & Pricing", value: "Contact for Details" }
    ]
  },

  sup2_chiller: {
    id: "sup2_chiller",
    name: "WATER-COOLED SCREW CHILLER (ZENVENT ENGINEERING)",
    shortName: "Water-Cooled Screw Chiller",
    category: "supplementary",
    categoryLabel: "Supplementary Plant Equipment",
    hsn: "Contact for Details",
    qty: "Contact for Details",
    rate: "Contact for Details",
    image: "assets/machines/sup-02-screw-chiller.png",
    alt: "Water-Cooled Screw Chiller (Zenvent Engineering)",
    isPoItem: false,
    poDescription: "Supplementary industrial refrigeration unit verified from client uploaded photograph (Screenshot 2026-10-19 110405.png / 110421.png). Labeled 'WATER-COOLED SCREW CHILLER' and 'Zenvent Engineering'. Not listed in PO Ref: PH/001/26-27.",
    verifiedDetails: "Heavy-duty industrial water-cooled screw chiller featuring horizontal shell-and-tube heat exchange vessel, twin screw compressor assembly, and dedicated PLC electrical control cabinet labeled 'Zenvent Engineering'.",
    specs: [
      { label: "Inventory Classification", value: "Supplementary Plant Utility (From Uploaded Photos)" },
      { label: "Purchase Order Status", value: "Not in PO Ref: PH/001/26-27 (Offered as Associated Plant Utility)" },
      { label: "Verified Photographs", value: "Screenshot 2026-10-19 110405.png & 110421.png" },
      { label: "Visible Branding", value: "Zenvent Engineering (on electrical control panel)" },
      { label: "Visible Machine Name", value: "WATER-COOLED SCREW CHILLER (printed on blue unit plaque)" },
      { label: "Specifications & Pricing", value: "Contact for Details" }
    ]
  },

  sup3_pump: {
    id: "sup3_pump",
    name: "CENTRIFUGAL PROCESS & CHEMICAL SLURRY PUMP",
    shortName: "Centrifugal Chemical Process Pump",
    category: "supplementary",
    categoryLabel: "Supplementary Plant Equipment",
    hsn: "Contact for Details",
    qty: "Contact for Details",
    rate: "Contact for Details",
    image: "assets/machines/sup-03-centrifugal-pump.png",
    alt: "Industrial blue centrifugal slurry and chemical process pump",
    isPoItem: false,
    poDescription: "Supplementary industrial pump verified from client uploaded photograph (Screenshot 2026-10-19 110434.png). Not listed in PO Ref: PH/001/26-27.",
    verifiedDetails: "Base-mounted industrial centrifugal process pump with flanged radial discharge, high-torque TEFC induction motor, and rigid steel skid.",
    specs: [
      { label: "Inventory Classification", value: "Supplementary Plant Utility (From Uploaded Photos)" },
      { label: "Purchase Order Status", value: "Not in PO Ref: PH/001/26-27 (Offered as Associated Plant Utility)" },
      { label: "Verified Photograph", value: "Screenshot 2026-10-19 110434.png" },
      { label: "Design", value: "Single-stage horizontal centrifugal pump mounted on common steel channel baseplate" },
      { label: "Application", value: "Fluid circulation across heat exchangers, reactor jackets, and cooling towers" },
      { label: "Specifications & Pricing", value: "Contact for Details" }
    ]
  },

  sup4_compressor: {
    id: "sup4_compressor",
    name: "ROTARY SCREW AIR COMPRESSOR BK90-8GH",
    shortName: "Rotary Screw Air Compressor BK90-8GH",
    category: "supplementary",
    categoryLabel: "Supplementary Plant Equipment",
    hsn: "Contact for Details",
    qty: "Contact for Details",
    rate: "Contact for Details",
    image: "assets/machines/sup-04-screw-compressor.png",
    alt: "Rotary Screw Air Compressor Model BK90-8GH",
    isPoItem: false,
    poDescription: "Supplementary industrial compressor verified from client uploaded photograph (Screenshot 2026-10-19 110443.png). Machine model visibly printed as 'BK90-8GH'. Not listed in PO Ref: PH/001/26-27.",
    verifiedDetails: "Cabinet-enclosed industrial rotary screw air compressor marked with model designation 'BK90-8GH', featuring integrated microcomputer digital control panel, ventilation louvers, and emergency trip button.",
    specs: [
      { label: "Inventory Classification", value: "Supplementary Plant Utility (From Uploaded Photos)" },
      { label: "Purchase Order Status", value: "Not in PO Ref: PH/001/26-27 (Offered as Associated Plant Utility)" },
      { label: "Verified Photograph", value: "Screenshot 2026-10-19 110443.png" },
      { label: "Visible Model Number", value: "BK90-8GH (printed on blue front access door)" },
      { label: "Enclosure Type", value: "Sound-attenuated heavy-gauge industrial canopy with fork-lift base slots" },
      { label: "Specifications & Pricing", value: "Contact for Details" }
    ]
  },

  sup5_exchanger: {
    id: "sup5_exchanger",
    name: "SHELL & TUBE HEAT EXCHANGER / INDUSTRIAL CONDENSER",
    shortName: "Shell & Tube Industrial Heat Exchanger",
    category: "supplementary",
    categoryLabel: "Supplementary Plant Equipment",
    hsn: "Contact for Details",
    qty: "Contact for Details",
    rate: "Contact for Details",
    image: "assets/machines/sup-05-heat-exchanger.png",
    alt: "Industrial Shell and Tube Heat Exchanger fabrication",
    isPoItem: false,
    poDescription: "Supplementary process equipment verified from client uploaded photograph (Screenshot 2026-10-19 110452.png). Not listed in PO Ref: PH/001/26-27.",
    verifiedDetails: "Twin stacked industrial shell-and-tube heat exchangers with bolted flanged tube sheets and multi-pass shell connections, shown during assembly in an engineering workshop bay.",
    specs: [
      { label: "Inventory Classification", value: "Supplementary Plant Utility (From Uploaded Photos)" },
      { label: "Purchase Order Status", value: "Not in PO Ref: PH/001/26-27 (Offered as Associated Plant Utility)" },
      { label: "Verified Photograph", value: "Screenshot 2026-10-19 110452.png" },
      { label: "Configuration", value: "Twin horizontal shell-and-tube units with bolted circular end-covers and baffles" },
      { label: "Application", value: "Thermal transfer between process fluid circuits, vapor condensation & heat recovery" },
      { label: "Specifications & Pricing", value: "Contact for Details" }
    ]
  }
};

// ============================================================================
// 2. HERO ANIMATION ENGINE: 240-FRAME SCROLL-DRIVEN PIPELINE
// ============================================================================
const TOTAL_FRAMES = 240;
const frameImages = new Array(TOTAL_FRAMES);
const loadedFrames = new Set();

const canvas = document.getElementById("heroCanvas");
const ctx = canvas ? canvas.getContext("2d", { alpha: false }) : null;
const heroFallback = document.getElementById("heroFallback");
const scrollPrompt = document.getElementById("scrollPrompt");

// Telemetry Elements
const telemetryFill = document.getElementById("telemetryFill");
const telemetryPercent = document.getElementById("telemetryPercent");
const telemetryFrame = document.getElementById("telemetryFrame");

let currentRenderedFrame = -1;
let isFirstFrameReady = false;
let isReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

function getFrameUrl(frameNum) {
  const padded = String(frameNum).padStart(3, "0");
  return `assets/hero-frames/ezgif-frame-${padded}.jpg`;
}

function resizeCanvas() {
  if (!canvas || !ctx) return;
  const dpr = Math.min(window.devicePixelRatio || 1, 2);
  const rect = canvas.getBoundingClientRect();
  const width = Math.round(rect.width * dpr);
  const height = Math.round(rect.height * dpr);

  if (canvas.width !== width || canvas.height !== height) {
    canvas.width = width;
    canvas.height = height;
    ctx.imageSmoothingEnabled = true;
    ctx.imageSmoothingQuality = "high";
    
    if (currentRenderedFrame >= 0) {
      drawFrame(currentRenderedFrame);
    }
  }
}

function drawFrame(frameIndex) {
  if (!ctx || !canvas) return;

  // Double buffering: find nearest available loaded frame if target is pending
  let imgToDraw = frameImages[frameIndex];
  if (!imgToDraw || !imgToDraw.complete || imgToDraw.naturalWidth === 0) {
    for (let i = frameIndex - 1; i >= 0; i--) {
      if (frameImages[i] && frameImages[i].complete && frameImages[i].naturalWidth > 0) {
        imgToDraw = frameImages[i];
        break;
      }
    }
    if (!imgToDraw) {
      for (let i = frameIndex + 1; i < TOTAL_FRAMES; i++) {
        if (frameImages[i] && frameImages[i].complete && frameImages[i].naturalWidth > 0) {
          imgToDraw = frameImages[i];
          break;
        }
      }
    }
  }

  if (!imgToDraw || !imgToDraw.complete || imgToDraw.naturalWidth === 0) return;

  const canvasWidth = canvas.width;
  const canvasHeight = canvas.height;
  const imgWidth = imgToDraw.naturalWidth;
  const imgHeight = imgToDraw.naturalHeight;

  const imgRatio = imgWidth / imgHeight;
  const canvasRatio = canvasWidth / canvasHeight;

  let renderWidth, renderHeight, offsetX, offsetY;

  if (canvasRatio > imgRatio) {
    renderWidth = canvasWidth;
    renderHeight = canvasWidth / imgRatio;
    offsetX = 0;
    offsetY = (canvasHeight - renderHeight) / 2;
  } else {
    renderHeight = canvasHeight;
    renderWidth = canvasHeight * imgRatio;
    const excessWidth = renderWidth - canvasWidth;
    offsetX = -excessWidth * 0.68; // Bias rightwards to center the boiler assembly
    offsetY = 0;
  }

  ctx.drawImage(imgToDraw, offsetX, offsetY, renderWidth, renderHeight);
  currentRenderedFrame = frameIndex;

  if (!isFirstFrameReady) {
    isFirstFrameReady = true;
    if (heroFallback) heroFallback.classList.add("hidden");
  }
}

function updateTelemetry(progress, frameIndex) {
  const percent = Math.min(100, Math.max(0, Math.round(progress * 100)));
  const frameDisplay = String(frameIndex + 1).padStart(3, "0");

  if (telemetryFill) telemetryFill.style.width = `${percent}%`;
  if (telemetryPercent) telemetryPercent.textContent = `${percent}% ASSEMBLED`;
  if (telemetryFrame) telemetryFrame.textContent = `FRAME ${frameDisplay} / 240`;

  if (scrollPrompt) {
    if (progress > 0.03) {
      scrollPrompt.classList.add("faded");
    } else {
      scrollPrompt.classList.remove("faded");
    }
  }
}

function preloadFrames() {
  const isMobile = window.innerWidth <= 768;

  // On mobile touchscreens: Load completed frame immediately, saving cellular bandwidth and memory
  if (isMobile) {
    loadSingleFrame(TOTAL_FRAMES - 1, () => {
      resizeCanvas();
      drawFrame(TOTAL_FRAMES - 1);
      updateTelemetry(1, TOTAL_FRAMES - 1);
    });
    return;
  }

  // Desktop & High-Speed Viewports: Load Frame 1 immediately, then preload sequence in chunks
  loadSingleFrame(0, () => {
    resizeCanvas();
    drawFrame(0);
    updateTelemetry(0, 0);

    if (isReducedMotion) {
      loadSingleFrame(TOTAL_FRAMES - 1, () => {
        drawFrame(TOTAL_FRAMES - 1);
        updateTelemetry(1, TOTAL_FRAMES - 1);
      });
      return;
    }

    // Load next burst (frames 1-25)
    preloadBatch(1, 25, () => {
      loadRemainingChunks(26);
    });
  });
}

function loadSingleFrame(index, callback) {
  if (frameImages[index] && frameImages[index].complete) {
    if (callback) callback();
    return;
  }

  const img = new Image();
  img.src = getFrameUrl(index + 1);
  img.onload = () => {
    loadedFrames.add(index);
    if ("decode" in img) {
      img.decode().catch(() => {}).finally(() => {
        if (callback) callback();
      });
    } else {
      if (callback) callback();
    }
  };
  img.onerror = () => {
    if (callback) callback();
  };
  frameImages[index] = img;
}

function preloadBatch(startIndex, endIndex, callback) {
  let pending = endIndex - startIndex + 1;
  if (pending <= 0) {
    if (callback) callback();
    return;
  }

  for (let i = startIndex; i <= endIndex; i++) {
    loadSingleFrame(i, () => {
      pending--;
      if (pending === 0 && callback) callback();
    });
  }
}

function loadRemainingChunks(nextIndex) {
  if (nextIndex >= TOTAL_FRAMES) return;
  const chunkSize = 15;
  const endIndex = Math.min(TOTAL_FRAMES - 1, nextIndex + chunkSize - 1);

  preloadBatch(nextIndex, endIndex, () => {
    if ("requestIdleCallback" in window) {
      window.requestIdleCallback(() => loadRemainingChunks(endIndex + 1), { timeout: 100 });
    } else {
      setTimeout(() => loadRemainingChunks(endIndex + 1), 30);
    }
  });
}

function initScrollAnimation() {
  if (isReducedMotion) return;

  const heroContainer = document.getElementById("home");
  const heroViewport = document.getElementById("heroPinViewport");

  if (!heroContainer || !heroViewport) return;

  if (typeof gsap !== "undefined" && typeof ScrollTrigger !== "undefined") {
    gsap.registerPlugin(ScrollTrigger);

    ScrollTrigger.matchMedia({
      // Desktop & Large Viewports (> 768px): Full 240-frame interactive scroll assembly
      "(min-width: 769px)": function() {
        return ScrollTrigger.create({
          trigger: heroContainer,
          start: "top top",
          end: "bottom bottom",
          pin: heroViewport,
          scrub: 0.5,
          anticipatePin: 1,
          onUpdate: (self) => {
            const progress = self.progress;
            const targetFrame = Math.min(TOTAL_FRAMES - 1, Math.max(0, Math.floor(progress * (TOTAL_FRAMES - 1))));
            requestAnimationFrame(() => {
              drawFrame(targetFrame);
              updateTelemetry(progress, targetFrame);
            });
          }
        });
      },

      // Mobile Touch Viewports (<= 768px): No scroll hijacking, show completed assembly over factory backdrop
      "(max-width: 768px)": function() {
        loadSingleFrame(TOTAL_FRAMES - 1, () => {
          drawFrame(TOTAL_FRAMES - 1);
          updateTelemetry(1, TOTAL_FRAMES - 1);
        });
      }
    });
  } else {
    // Native Fallback
    if (window.innerWidth > 768) {
      let ticking = false;
      window.addEventListener("scroll", () => {
        if (!ticking) {
          window.requestAnimationFrame(() => {
            const rect = heroContainer.getBoundingClientRect();
            const scrollDistance = rect.height - window.innerHeight;
            let progress = 0;

            if (rect.top <= 0 && scrollDistance > 0) {
              progress = Math.min(1, Math.max(0, -rect.top / scrollDistance));
            } else if (rect.top > 0) {
              progress = 0;
            } else {
              progress = 1;
            }

            const targetFrame = Math.min(TOTAL_FRAMES - 1, Math.max(0, Math.floor(progress * (TOTAL_FRAMES - 1))));
            drawFrame(targetFrame);
            updateTelemetry(progress, targetFrame);
            ticking = false;
          });
          ticking = true;
        }
      }, { passive: true });
    } else {
      loadSingleFrame(TOTAL_FRAMES - 1, () => {
        drawFrame(TOTAL_FRAMES - 1);
      });
    }
  }
}

window.addEventListener("resize", () => {
  resizeCanvas();
  if (typeof ScrollTrigger !== "undefined") {
    ScrollTrigger.refresh();
  }
});

// ============================================================================
// 3. CATALOGUE FILTERING & SEARCH
// ============================================================================
const cards = [...document.querySelectorAll(".equipment-card")];
const searchInput = document.getElementById("searchInput");
const filterButtons = [...document.querySelectorAll(".filter-btn")];
const resultsCount = document.getElementById("resultsCount");
const emptyState = document.getElementById("emptyState");
let activeFilter = "all";

function updateCatalogue() {
  const query = searchInput ? searchInput.value.trim().toLowerCase() : "";
  let visible = 0;

  cards.forEach(card => {
    const cardCategory = card.dataset.categoryType; // "po" or "supplementary"
    const matchesFilter = activeFilter === "all" || cardCategory === activeFilter;
    const haystack = `${card.dataset.name} ${card.dataset.categoryLabel} ${card.innerText}`.toLowerCase();
    const matchesQuery = !query || haystack.includes(query);
    const show = matchesFilter && matchesQuery;

    card.hidden = !show;
    if (show) visible++;
  });

  if (resultsCount) {
    if (activeFilter === "po") {
      resultsCount.textContent = `Showing ${visible} of 8 Original Purchase Order Machines`;
    } else if (activeFilter === "supplementary") {
      resultsCount.textContent = `Showing ${visible} of 5 Supplementary Plant Utilities (Not in PO)`;
    } else {
      resultsCount.textContent = `Showing ${visible} of 13 Verified Industrial Machines (8 PO + 5 Supplementary)`;
    }
  }

  if (emptyState) {
    emptyState.hidden = visible !== 0;
  }
}

if (searchInput) {
  searchInput.addEventListener("input", updateCatalogue);
}

filterButtons.forEach(button => {
  button.addEventListener("click", () => {
    activeFilter = button.dataset.filter;
    filterButtons.forEach(btn => {
      const selected = btn === button;
      btn.classList.toggle("active", selected);
      btn.setAttribute("aria-pressed", String(selected));
    });
    updateCatalogue();
  });
});

// ============================================================================
// 4. PRODUCT DETAIL MODAL DIALOG
// ============================================================================
const dialog = document.getElementById("equipmentDialog");
const dialogImage = document.getElementById("dialogImage");
const dialogMeta = document.getElementById("dialogMeta");
const dialogTitle = document.getElementById("dialogTitle");
const dialogPoTag = document.getElementById("dialogPoTag");
const dialogDescription = document.getElementById("dialogDescription");
const dialogSpecsTable = document.getElementById("dialogSpecsTable");
const dialogEnquire = document.getElementById("dialogEnquire");
const equipmentSelect = document.getElementById("equipment");
const quantityInput = document.getElementById("quantity");

function openProductModal(id) {
  const item = (window.PRODUCTS_DATA && window.PRODUCTS_DATA[id]) || products[id];
  if (!item || !dialog) return;

  dialogImage.src = item.image;
  dialogImage.alt = item.alt;
  dialogMeta.textContent = item.categoryLabel;
  dialogTitle.textContent = item.name;

  if (dialogPoTag) {
    if (item.isPoItem) {
      dialogPoTag.textContent = `VERIFIED PO LINE ITEM · PO REF: PH/001/26-27 (ITEM ${String(item.poItemNo).padStart(2, '0')})`;
      dialogPoTag.className = "dialog-po-tag po-verified";
    } else if (item.statusType === "extended") {
      dialogPoTag.textContent = `AUTHENTIC INDUSTRIAL EQUIPMENT · ${item.rateDisplay || ('MARKET REF: ' + item.rate)}`;
      dialogPoTag.className = "dialog-po-tag po-extended";
    } else {
      dialogPoTag.textContent = "SUPPLEMENTARY PLANT UTILITY · FROM CLIENT MACHINERY PHOTOS (NOT IN PO)";
      dialogPoTag.className = "dialog-po-tag po-supplementary";
    }
  }

  dialogDescription.textContent = item.verifiedDetails;

  // Build specifications table
  if (dialogSpecsTable) {
    dialogSpecsTable.innerHTML = "";
    item.specs.forEach(spec => {
      const tr = document.createElement("tr");
      const tdLabel = document.createElement("td");
      tdLabel.className = "spec-label";
      tdLabel.textContent = spec.label;
      const tdValue = document.createElement("td");
      tdValue.className = "spec-value";
      tdValue.textContent = spec.value;
      tr.appendChild(tdLabel);
      tr.appendChild(tdValue);
      dialogSpecsTable.appendChild(tr);
    });
  }

  // Hook Request a Quote CTA to preselect machine in form
  if (dialogEnquire) {
    dialogEnquire.onclick = () => {
      dialog.close();
      if (equipmentSelect) {
        for (let opt of equipmentSelect.options) {
          if (opt.value === item.id || opt.text.toLowerCase().includes(item.shortName.toLowerCase())) {
            equipmentSelect.value = opt.value;
            break;
          }
        }
      }
      if (quantityInput && item.qty) {
        quantityInput.value = item.qty.includes("1") ? "1" : "1";
      }
    };
  }

  dialog.showModal();
}

document.querySelectorAll("[data-open]").forEach(btn => {
  btn.addEventListener("click", () => openProductModal(btn.dataset.open));
});

const dialogCloseBtn = document.getElementById("dialogClose");
if (dialogCloseBtn) {
  dialogCloseBtn.addEventListener("click", () => dialog.close());
}

if (dialog) {
  dialog.addEventListener("click", (e) => {
    if (e.target === dialog) dialog.close();
  });
}

// ============================================================================
// 5. MOBILE NAVIGATION TOGGLE
// ============================================================================
const menuToggle = document.getElementById("menuToggle");
const primaryNav = document.getElementById("primaryNav");

if (menuToggle && primaryNav) {
  menuToggle.addEventListener("click", () => {
    const isOpen = primaryNav.classList.toggle("open");
    menuToggle.setAttribute("aria-expanded", String(isOpen));
    menuToggle.setAttribute("aria-label", isOpen ? "Close navigation menu" : "Open navigation menu");
  });

  primaryNav.querySelectorAll("a").forEach(link => {
    link.addEventListener("click", () => {
      primaryNav.classList.remove("open");
      menuToggle.setAttribute("aria-expanded", "false");
      menuToggle.setAttribute("aria-label", "Open navigation menu");
    });
  });
}

// ============================================================================
// 6. QUOTATION / CONTACT FORM WITH COMPREHENSIVE FIELDS
// ============================================================================
const contactForm = document.getElementById("contactForm");
const formFeedback = document.getElementById("formFeedback");

if (contactForm) {
  contactForm.addEventListener("submit", (e) => {
    e.preventDefault();
    if (!contactForm.reportValidity()) return;

    const formData = new FormData(contactForm);
    const customerName = formData.get("name") || "";
    const companyName = formData.get("company") || "Not provided";
    const email = formData.get("email") || "";
    const phone = formData.get("phone") || "Not provided";
    const selectedMachineId = formData.get("equipment") || "";
    const quantity = formData.get("quantity") || "1";
    const message = formData.get("message") || "";

    const productObj = (window.PRODUCTS_DATA && window.PRODUCTS_DATA[selectedMachineId]) || products[selectedMachineId];
    const machineTitle = productObj ? (productObj.shortName || productObj.name) : selectedMachineId;
    const poStatus = productObj && productObj.isPoItem 
      ? `PO Line Item #${productObj.poItemNo} (HSN: ${productObj.hsn})` 
      : (productObj && productObj.statusType === "extended" ? "Extended Technical Model" : "Supplementary Plant Utility");

    const subject = `Official RFQ: ${machineTitle} — [${companyName}]`;
    const body = [
      `FORMAL MACHINERY PROCUREMENT ENQUIRY`,
      `============================================================`,
      `Customer / Representative: ${customerName}`,
      `Company Name:              ${companyName}`,
      `Official Email:            ${email}`,
      `Contact Phone:             ${phone}`,
      `Date:                      ${new Date().toLocaleDateString("en-IN")}`,
      `------------------------------------------------------------`,
      `Machine of Interest:       ${machineTitle}`,
      `Catalogue Classification:  ${poStatus}`,
      `Quantity Required:         ${quantity}`,
      `------------------------------------------------------------`,
      `Technical Specifications & Delivery Scope:`,
      message,
      `============================================================`,
      `Addressed to: M/s. PUKHRAJ HASTIMAL & CO.`,
      `Registered Office: Office No 03, 2nd Floor, 7 Kika Bhai Mansion, Gulalwadi, Mumbai - 400004`,
      `GST NO: 27AFMPJ3478A1ZG | Email: pukhrajhastimal@gmail.com`
    ].join("\n");

    if (formFeedback) {
      formFeedback.textContent = "Launching your email client with your formal RFQ quotation draft...";
      formFeedback.className = "form-feedback feedback-active";
    }

    setTimeout(() => {
      window.location.href = `mailto:pukhrajhastimal@gmail.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
      if (formFeedback) {
        formFeedback.textContent = "Your email application has been launched with the complete quotation enquiry draft.";
      }
    }, 350);
  });
}

// Copyright Year
const yearEl = document.getElementById("year");
if (yearEl) {
  yearEl.textContent = new Date().getFullYear();
}

// ============================================================================
// 7. INITIALIZATION LIFECYCLE
// ============================================================================
document.addEventListener("DOMContentLoaded", () => {
  resizeCanvas();
  preloadFrames();
  initScrollAnimation();
  updateCatalogue();
});
