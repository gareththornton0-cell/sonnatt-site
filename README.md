# Sonnatt.ai website

Published free with GitHub Pages at https://sonnattai.com.

- `index.html` is the homepage, `privacy.html` the privacy policy, `dashboard/` the team dashboard.
- Contact-form and chatbot enquiries are saved to the `website_leads` table in the Sonnatt Supabase project.
- Every push to `main` publishes the site (see `.github/workflows/pages.yml`).

## Self-serve products (added October 2026)

- **Plans:** Chatbot £99 setup + £49/month, Starter (website + chatbot) £299 setup + £149/month, alongside Core (£995 + £995/month) and Scale. Shown on the homepage, `pricing/` and `website-chatbot/`.
- **Online signup:** the form on `pricing/#start` (handled in `assets/site.js`) saves a `plan-signup` lead. To take payment straight away, paste a Stripe Payment Link into the `sonnatt-pay-chat`, `sonnatt-pay-starter` or `sonnatt-pay-core` meta tag on `pricing/index.html` (and `sonnatt-pay-chat` on `website-chatbot/index.html`). Until then the team emails a payment link.
- **Chatbot widget:** `widget.js`. A client adds `<script src="https://sonnattai.com/widget.js" data-sonnatt-widget="CLIENT-ID" async></script>` to their site. Each client is a row in the `chat_widgets` table (business, greeting, accent colour, booking link, `faqs` as `[{"q":..., "keys":[...], "a":...}]`, `alert_email`). Their leads are saved as `widget-lead` and emailed to `alert_email` by the `lead-alert` function. The `demo` row powers the demo on `website-chatbot/`.
- **Free website checker:** `check/` calls the `site-check` Supabase function (source in `supabase/functions/site-check/`), and saves a `site-check` lead when someone asks for the report.
- The database change is recorded in `supabase/migrations/`. The `supabase/` folder is not published with the site.
