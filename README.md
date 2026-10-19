# Industrial Equipment Catalogue

A responsive static website based on the industrial equipment purchase-order details provided in the conversation.

## Files
- `index.html` — page content and catalogue cards
- `styles.css` — responsive styling and accessibility preferences
- `script.js` — search, category filters, equipment detail dialogs, mobile navigation and email-draft form

## Run locally
1. Download and extract the ZIP.
2. Open `index.html` in a modern browser. For a local server, run `python -m http.server 8000` from this folder and visit `http://localhost:8000`.

## Publish
Upload the folder to any static hosting service (for example GitHub Pages, Netlify, or Cloudflare Pages). No build step is required.

## Important setup / limitations
- Product imagery is illustrative and loads from Unsplash over the internet. Replace with verified manufacturer photos and confirm usage rights before production.
- Google Fonts are loaded from Google Fonts; system fallbacks are provided.
- The enquiry form validates in the browser and opens a pre-filled `mailto:` draft to `pukhrajhastimal@gmail.com`. It does not send/store submissions on a server. For a production form, connect a trusted form backend/service and add spam protection.
- No phone or WhatsApp number was provided, so none is invented.
- Product specifications are intentionally described as typical roles and confirmation notes; exact makes, models, ratings and certifications were not provided.
- The supplied PO's tax arithmetic and some item descriptions/HSN classifications need verification before use.
- Before production, test all image URLs and replace generic illustrative imagery with approved manufacturer images.
