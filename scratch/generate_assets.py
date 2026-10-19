import os

items = [
    ('ext-01-vacuum-pump.svg', 'INDUSTRIAL VACUUM PUMP', 'Liquid-Ring Vacuum System', 'Pumps & Fluid Handling'),
    ('ext-02-gear-pump.svg', 'POSITIVE DISPLACEMENT GEAR PUMP', 'External Rotary Gear Pump', 'Pumps & Fluid Handling'),
    ('ext-03-dosing-pump.svg', 'CHEMICAL DOSING PUMP', 'Precision Diaphragm Metering Pump', 'Pumps & Fluid Handling'),
    ('ext-04-circulation-pump.svg', 'VERTICAL INLINE CIRCULATION PUMP', 'Water Circulation & Pressure Booster', 'Pumps & Fluid Handling'),
    ('ext-05-plate-exchanger.svg', 'PLATE HEAT EXCHANGER', 'Gasketed Plate & Frame Exchanger', 'Thermal & Heat Transfer'),
    ('ext-06-refrig-condenser.svg', 'AIR-COOLED REFRIGERATION CONDENSER', 'Finned-Tube Industrial Condenser', 'Thermal & Heat Transfer'),
    ('ext-07-evaporator.svg', 'INDUSTRIAL CHEMICAL EVAPORATOR', 'Falling-Film Evaporation Plant', 'Process Equipment'),
    ('ext-08-storage-tank.svg', 'INDUSTRIAL STORAGE TANK', 'Stainless Steel Chemical Vessel', 'Process Equipment'),
    ('ext-09-mixing-tank.svg', 'INDUSTRIAL MIXING TANK WITH AGITATOR', 'Jacketed Blending Reactor Vessel', 'Process Equipment'),
    ('ext-10-air-receiver.svg', 'COMPRESSED AIR RECEIVER TANK', 'ASME Section VIII Pressure Vessel', 'Air & Compressed-Air'),
    ('ext-11-centrifugal-blower.svg', 'INDUSTRIAL CENTRIFUGAL BLOWER', 'High-Pressure Heavy-Duty Air Blower', 'Air & Compressed-Air'),
    ('ext-12-air-dryer.svg', 'REFRIGERATED AIR DRYER UNIT', 'Compressed Air Moisture Separator', 'Air & Compressed-Air'),
    ('ext-13-filtration-system.svg', 'MULTI-GRADE WATER FILTRATION SYSTEM', 'Pressure Sand & Carbon Filtration Skid', 'Water Treatment & Filtration'),
    ('ext-14-bag-filter.svg', 'BAG FILTER HOUSING VESSEL', 'Stainless Steel Particulate Trap', 'Water Treatment & Filtration'),
    ('ext-15-cartridge-filter.svg', 'CARTRIDGE FILTER HOUSING', 'Multi-Element Micronic Filtration Housing', 'Water Treatment & Filtration'),
    ('ext-16-ro-system.svg', 'REVERSE OSMOSIS WATER TREATMENT', 'Industrial RO Desalination Skid', 'Water Treatment & Filtration'),
    ('ext-17-water-softener.svg', 'INDUSTRIAL WATER SOFTENER PLANT', 'Automated Ion-Exchange Softening Unit', 'Water Treatment & Filtration'),
    ('ext-18-diesel-generator.svg', 'INDUSTRIAL DIESEL GENERATOR (DG SET)', 'Prime & Standby Power Diesel GenSet', 'Electrical Equipment'),
    ('ext-19-electric-motor.svg', 'INDUSTRIAL ELECTRIC MOTOR (IE3)', 'Three-Phase Premium Efficiency Induction Motor', 'Electrical Equipment'),
    ('ext-20-mcc-panel.svg', 'MOTOR CONTROL CENTRE (MCC) PANEL', 'Compartmentalized Motor Feeder Switchboard', 'Electrical Equipment')
]

folder = 'd:/Client Websites/assets/machines/additional'
os.makedirs(folder, exist_ok=True)

for fname, title, sub, cat in items:
    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 520" width="100%" height="100%">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0a1714" />
      <stop offset="60%" stop-color="#122822" />
      <stop offset="100%" stop-color="#081210" />
    </linearGradient>
    <pattern id="cadGrid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="rgba(200, 231, 122, 0.06)" stroke-width="1" />
    </pattern>
  </defs>
  <rect width="800" height="520" fill="url(#bg)" />
  <rect width="800" height="520" fill="url(#cadGrid)" />
  
  <!-- Outer Technical Blueprint Border -->
  <rect x="24" y="24" width="752" height="472" fill="none" stroke="rgba(200, 231, 122, 0.22)" stroke-width="1.5" rx="10" />
  <circle cx="38" cy="38" r="3.5" fill="#c8e77a" opacity="0.7" />
  <circle cx="762" cy="38" r="3.5" fill="#c8e77a" opacity="0.7" />
  <circle cx="38" cy="482" r="3.5" fill="#c8e77a" opacity="0.7" />
  <circle cx="762" cy="482" r="3.5" fill="#c8e77a" opacity="0.7" />

  <!-- Technical Category Banner -->
  <text x="50" y="65" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="700" font-size="11" fill="#c8e77a" letter-spacing="2">{cat.upper()} · CATALOGUE REFERENCE</text>

  <!-- Center Machinery Schematic Representation -->
  <g transform="translate(400, 235)" stroke="rgba(200, 231, 122, 0.6)" stroke-width="2" fill="rgba(20, 48, 38, 0.45)">
    <!-- Main Equipment Geometry -->
    <rect x="-140" y="-75" width="280" height="150" rx="12" stroke="rgba(200, 231, 122, 0.45)" />
    <circle cx="0" cy="0" r="85" />
    <circle cx="0" cy="0" r="65" stroke-dasharray="6 4" />
    <circle cx="0" cy="0" r="30" fill="rgba(200, 231, 122, 0.2)" />
    <!-- Flanges and Piping Ports -->
    <rect x="-160" y="-30" width="20" height="60" rx="3" stroke="#c8e77a" />
    <rect x="140" y="-30" width="20" height="60" rx="3" stroke="#c8e77a" />
    <line x1="-160" y1="0" x2="160" y2="0" stroke="#c8e77a" stroke-width="1.5" stroke-dasharray="4 2" />
    <line x1="0" y1="-95" x2="0" y2="95" stroke="#c8e77a" stroke-width="1.5" stroke-dasharray="4 2" />
  </g>

  <!-- Equipment Title & Subtitle -->
  <text x="400" y="375" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="800" font-size="22" fill="#ffffff" letter-spacing="-0.5" text-anchor="middle">{title}</text>
  <text x="400" y="405" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14.5" fill="#bad3c5" text-anchor="middle">{sub}</text>

  <!-- Verified Status Pill -->
  <g transform="translate(400, 448)">
    <rect x="-185" y="-15" width="370" height="30" rx="15" fill="rgba(10, 24, 20, 0.9)" stroke="rgba(200, 231, 122, 0.45)" stroke-width="1" />
    <circle cx="-162" cy="0" r="4.5" fill="#c8e77a" />
    <text x="-148" y="4" font-family="monospace" font-size="10" fill="#c8e77a" letter-spacing="1">TECHNICAL REFERENCE · SPECIFICATIONS ON RFQ</text>
  </g>
</svg>'''
    filepath = os.path.join(folder, fname)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(svg_content)

print(f"Generated {len(items)} SVG assets in {folder}")
