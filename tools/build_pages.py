#!/usr/bin/env python3
"""Builds the Sonnatt.ai inner pages (services, area and pricing pages).

Run from the repo root:  python3 tools/build_pages.py
Each page is written to <slug>/index.html. Content uses only facts the
homepage already states, so the site never contradicts itself. Edit the
PAGES list below and re-run to change wording; the tools/ folder is not
published.
"""
import html, json, os

SITE = "https://sonnattai.com"
UPDATED = "2026-10-10"
BOOKING = ""  # Google Calendar appointment-schedule link; keep in step with index.html

NAV = [("/website-design-leeds/", "Websites"), ("/website-chatbot/", "Chatbots"),
       ("/social-media-marketing-leeds/", "Marketing"), ("/custom-apps-automation/", "Apps & automation"),
       ("/pricing/", "Pricing"), ("/#faq", "FAQ"), ("/#contact", "Contact")]

PRICING_FACTS = [("Setup", "£995 one-off"), ("Ongoing", "£995 a month"), ("Contract", "cancel with 30 days' notice")]

STEPS = [("We learn your business", "A short discovery session: your services, your customers, what your site needs to do, and the systems you already use."),
         ("We build your presence", "A real person builds your website, chatbot, any custom apps and your marketing, using AI to work quickly, then checks it all with you."),
         ("We run it with you", "We host it, keep it running and handle your marketing every month, with a review call to plan what's next.")]

PAGES = [
  {
    "slug": "website-design-leeds",
    "title": "Website Design in Leeds | Built, Hosted & Run for You | Sonnatt.ai",
    "desc": "Website design for Leeds businesses, built by a real person around your services, then hosted and kept up to date. £995 setup, £995 a month all-in.",
    "crumb": "Website design in Leeds",
    "service": "Website design and hosting",
    "eyebrow": "Website design · Leeds",
    "h1": "Website design in Leeds, built and run for you",
    "lede": "A real person on our team designs and builds your website around your actual services, not a template with your logo on it. Then we host it, keep it running and make changes whenever you need them.",
    "sections": [
      ("What you get", "cards", [
        ("Designed around your business", "Built for your services and your customers, so it explains what you do and makes it easy to get in touch."),
        ("Hosting and updates included", "Hosting and running costs are in the monthly plan. We monitor the site, fix issues and keep everything up to date."),
        ("Built to be found", "We build your site so search engines understand it, and keep your Google Business Profile active so you show up locally."),
        ("A chatbot on every site", "It answers your most-asked questions and captures enquiries day and night. New leads go straight to your inbox."),
        ("Connected to your tools", "Linked to the calendar, booking tool or CRM you already use, so information is entered once."),
        ("Changes handled for you", "Direct access to the team, not a ticket queue, plus a monthly review call."),
      ]),
      ("Already have a website?", "prose", [
        "No problem. We can rebuild it properly or improve what you've got. Either way, we'll look at your current site on the walkthrough call and tell you honestly what we'd change.",
        "Most small-business websites look fine but don't bring in work: they're slow, hard to read on a phone, never updated, and give people no easy way to ask a question. We fix that, then keep it that way every month.",
      ]),
      ("How it works", "steps", STEPS),
      ("What it costs", "prose", [
        "<b>£995 one-off setup</b>: a discovery and strategy session, your website and chatbot built and live, connected to the tools you already use, and a training session for your team.",
        "<b>£995 a month</b>: hosting and running costs, marketing and social media management, a monthly review call and priority support. There's no long contract; you can cancel with 30 days' notice.",
        'See the full breakdown on our <a href="/pricing/">pricing page</a>.',
      ]),
    ],
    "faq": [
      ("How much does a website cost with Sonnatt.ai?", "The website is part of the £995 one-off setup, together with your chatbot, connection to your existing tools and team training. After that it's £995 a month, which covers hosting, marketing and social media management, a monthly review call and priority support."),
      ("Is hosting included?", "Yes. Hosting and running costs are included in the monthly plan. We monitor your site, fix issues and keep everything up to date, so there's nothing extra for you to manage."),
      ("Can you improve my existing website instead of starting again?", "Yes. We can rebuild it properly or improve what you've got. We'll look at your current site on the free walkthrough call and tell you honestly what we'd change."),
      ("How long does it take to build a website?", "It depends on what you need and how much content you already have. We'll give you a clear timeline on the discovery call, before you commit to anything."),
      ("Do you only work with businesses in Leeds?", "We're based in Leeds, West Yorkshire, and work with businesses in Leeds, Bradford and across Yorkshire. If you're further away, get in touch anyway; most of the work can be done remotely."),
    ],
    "related": ["website-chatbot", "social-media-marketing-leeds", "web-design-bradford", "pricing"],
  },
  {
    "slug": "web-design-bradford",
    "title": "Website Design & Marketing in Bradford | Sonnatt.ai",
    "desc": "Website design, chatbots and marketing for Bradford businesses from a Leeds-based team. One dedicated account manager. £995 setup, £995 a month.",
    "crumb": "Bradford",
    "service": "Website design, chatbots and marketing in Bradford",
    "area": "Bradford",
    "eyebrow": "Bradford · West Yorkshire",
    "h1": "Website design and marketing for Bradford businesses",
    "lede": "Sonnatt.ai is based in Leeds, just down the road, and works with businesses across Bradford. One dedicated account manager builds and runs your website, chatbot and marketing, so you're not juggling six freelancers who don't talk to each other.",
    "sections": [
      ("Everything your business needs online", "cards", [
        ("Website build and hosting", "Built by a real person for your real business, then hosted and kept up to date."),
        ("Chatbot and systems", "A chatbot for your site, connected to the calendar, booking tool or CRM you already use."),
        ("Marketing and social growth", "Content, follow-ups, review requests and your Google profile, run for you every month."),
        ("Custom apps and automation", "Simple apps and dashboards built around how you work, and the admin between systems handled."),
      ]),
      ("Who we work with in Bradford", "prose", [
        "We build for real, local businesses that need a proper online presence and a bit of help running it:",
        "<ul><li><b>Letting and property management</b>: a website and chatbot that handle guest queries and viewing bookings.</li><li><b>Accountants and advisers</b>: a professional site and chatbot for client questions, backed by marketing.</li><li><b>Clinics and practices</b>: appointment enquiries and patient questions handled online, off your reception desk.</li><li><b>Salons, gyms and venues</b>: a booking-ready website and chatbot, plus the social content that keeps you full.</li><li><b>Trades and contractors</b>: a site that wins the job before the phone rings, with the admin handled behind it.</li></ul>",
      ]),
      ("How it works", "steps", STEPS),
      ("Same simple pricing", "prose", [
        "Bradford businesses pay the same as everyone else: <b>£995 one-off</b> to build it and <b>£995 a month</b> to run it, with no long contract (cancel with 30 days' notice). Businesses with several sites or branches can use our Scale plan, from £3,000 a month. <a href=\"/pricing/\">Full pricing</a>.",
      ]),
    ],
    "faq": [
      ("Do you work with businesses in Bradford?", "Yes. We're based in Leeds, West Yorkshire, and work with businesses in Bradford, Leeds and across Yorkshire."),
      ("Is the price different for Bradford?", "No. It's £995 one-off for setup and £995 a month to run it, wherever you are in Yorkshire."),
      ("Do we need to meet in person?", "Most of the work can be done remotely: the free walkthrough, the discovery session and the monthly review calls all work over a video call. If you'd prefer to meet, mention it when you get in touch."),
      ("What happens on the free walkthrough?", "It takes 15 minutes. We'll show you what your new site and chatbot could look like, using your own business, before you commit to anything. There's no obligation."),
    ],
    "related": ["website-design-leeds", "website-chatbot", "social-media-marketing-leeds", "pricing"],
  },
  {
    "slug": "website-chatbot",
    "title": "Website Chatbot for Small Businesses | Leeds & Bradford | Sonnatt.ai",
    "desc": "A website chatbot that answers your most-asked questions, captures enquiries day and night and connects to your calendar or CRM. Included in the £995 setup.",
    "crumb": "Website chatbots",
    "service": "Website chatbot and systems",
    "eyebrow": "Chatbots & systems",
    "h1": "A website chatbot that answers questions and captures enquiries",
    "lede": "We add a chatbot to your website that answers your most-asked questions and captures enquiries day and night. New leads go straight to your inbox, so you stop losing customers who visit after hours.",
    "sections": [
      ("What your chatbot does", "cards", [
        ("Answers common questions", "Prices, opening hours, what you offer, how to book: the questions your team answers every day."),
        ("Captures enquiries 24/7", "When someone is ready, it collects their name, contact details and what they need, and sends it straight to you."),
        ("Connects to your tools", "Linked to the calendar, booking tool or CRM you already use, so enquiries and bookings land in the right place."),
        ("Written in your voice", "We set it up around your business and check the wording with you before it goes live."),
      ]),
      ("See one working", "prose", [
        'The assistant on <a href="/">our homepage</a> is built the same way. Ask it about pricing or how we work, or ask it to book a call, and you\'ll see exactly what your customers would get.',
        "Once your website and systems are running well, we can also add a personal AI agent trained on your business to handle bookings and repeat questions. That's the next step, not the starting point.",
      ]),
      ("How it works", "steps", STEPS),
    ],
    "faq": [
      ("What can a website chatbot do for a small business?", "It answers your most-asked questions, captures enquiries day and night and sends new leads straight to your inbox. It can also be connected to the calendar, booking tool or CRM you already use."),
      ("Is the chatbot included in the price?", "Yes. Your website and chatbot are both built and put live as part of the £995 one-off setup, and running costs are covered by the £995 monthly plan."),
      ("Where do enquiries from the chatbot go?", "Straight to your inbox, and into your live client dashboard so you can see every lead in one place."),
      ("Can the chatbot take bookings?", "It can be connected to the calendar or booking tool you already use, so customers can get booked in without waiting for a reply."),
      ("Do you build AI agents?", "Yes, as a later step. Once your website and systems are running well, we can add a personal AI agent trained on your business to handle bookings and repeat questions."),
    ],
    "related": ["website-design-leeds", "custom-apps-automation", "social-media-marketing-leeds", "pricing"],
  },
  {
    "slug": "social-media-marketing-leeds",
    "title": "Social Media & Marketing Management in Leeds | Sonnatt.ai",
    "desc": "Social posts, Google Business Profile, follow-ups and review requests, run for Leeds and Bradford businesses every month. Part of the £995 monthly plan.",
    "crumb": "Marketing and social media",
    "service": "Marketing and social media management",
    "eyebrow": "Marketing & social growth · Leeds",
    "h1": "Marketing and social media, run for you every month",
    "lede": "Marketing and social growth are part of the monthly plan. We keep you visible on social media and Google, follow up every enquiry and ask happy customers for reviews, all written in your voice and checked with you first.",
    "sections": [
      ("What's included", "cards", [
        ("Regular social posts", "Content planned and posted for you, so your pages stay active without you finding the time."),
        ("Google Business Profile", "Kept active and up to date, so you show up when people nearby search for what you do."),
        ("Automatic follow-ups", "Every enquiry and quote followed up, so leads don't go cold while you're busy working."),
        ("Review requests", "Sent after each job, to build the reviews that help new customers choose you."),
        ("Plain-English reporting", "A live dashboard showing leads, customers, revenue and the marketing we're running for you."),
        ("Local search", "We build your site so search engines understand it and run content that helps you show up locally."),
      ]),
      ("Why one team works better", "prose", [
        "Most small businesses end up with a web designer, a social media freelancer and someone who \"does Google\", none of whom talk to each other. With Sonnatt.ai, one dedicated account manager runs your website, chatbot and marketing together, so every post, follow-up and page points customers the same way.",
      ]),
      ("How it works", "steps", STEPS),
    ],
    "faq": [
      ("What marketing is included in the monthly plan?", "Regular social posts, your Google Business Profile, automatic follow-ups on enquiries and quotes, review requests after each job, and plain-English reporting."),
      ("Do I get to approve posts before they go out?", "Yes. Every message is written in your voice and checked with you first."),
      ("Do you manage Google Business Profiles?", "Yes. We keep your Google Business Profile active and up to date as part of the monthly plan, which helps you show up in local searches and on Google Maps."),
      ("How do I see whether the marketing is working?", "Every client gets a live dashboard showing leads, customers, revenue and the marketing and automated tasks we're running for you, reported in plain English."),
      ("Is marketing an extra cost?", "No. Marketing and social media management are included in the £995 monthly plan, along with hosting, a monthly review call and priority support."),
    ],
    "related": ["website-design-leeds", "website-chatbot", "web-design-bradford", "pricing"],
  },
  {
    "slug": "custom-apps-automation",
    "title": "Custom Apps, Dashboards & Workflow Automation | Leeds | Sonnatt.ai",
    "desc": "Simple apps, client portals and dashboards built around how you work, plus automation that ends double data entry. For Leeds and Bradford businesses.",
    "crumb": "Apps and automation",
    "service": "Custom apps and workflow automation",
    "eyebrow": "Custom apps & automation",
    "h1": "Custom apps and automation built around how you work",
    "lede": "When off-the-shelf software doesn't fit how you work, we build a simple app or dashboard around your actual process, and automate the admin between your systems so information is entered once and updated everywhere.",
    "sections": [
      ("What we build", "cards", [
        ("Client portals", "A simple place for your customers to see what they need, without emailing you for it."),
        ("Booking dashboards", "See and manage bookings in one view, connected to the tools you already use."),
        ("Internal trackers", "Replace the spreadsheet everyone's afraid to touch with a purpose-made tool."),
        ("Workflow automation", "The admin between systems, handled: information entered once and updated everywhere."),
      ]),
      ("Hosted and maintained", "prose", [
        "We host every app we build and keep it maintained, so there's nothing for you to look after. Every client also gets a live dashboard showing leads, customers, revenue and the automated tasks we're running for them.",
        "Apps and automation sit alongside your website, chatbot and marketing, all run by the same dedicated account manager.",
      ]),
      ("How it works", "steps", STEPS),
    ],
    "faq": [
      ("What kind of apps do you build?", "Simple, purpose-made apps and dashboards such as client portals, booking dashboards and internal trackers, built around how you actually work."),
      ("What is workflow automation?", "It's handling the admin between your systems automatically, so information is entered once and updated everywhere instead of being copied by hand."),
      ("Who hosts and maintains the app?", "We do. We host it and keep it maintained as part of your plan."),
      ("How much do custom apps cost?", "For a single-site business, apps are part of the standard £995 setup and £995 a month plan; we confirm exactly what's included on the discovery call. Businesses with several sites or many system integrations use our Scale plan, from £3,000 a month, scoped after discovery."),
    ],
    "related": ["website-chatbot", "website-design-leeds", "social-media-marketing-leeds", "pricing"],
  },
  {
    "slug": "pricing",
    "title": "Pricing: £995 Setup, £995 a Month, Everything Included | Sonnatt.ai",
    "desc": "Simple pricing for your website, chatbot and marketing: £995 one-off setup, then £995 a month with no long contract. Scale plan from £3,000 a month.",
    "crumb": "Pricing",
    "service": None,
    "eyebrow": "Pricing",
    "h1": "Simple for most. Scoped for bigger operations.",
    "lede": "One price covers your website, chatbot, hosting, marketing and support, run by one dedicated account manager. No long contract: cancel any time with 30 days' notice.",
    "sections": [
      ("Plans", "plans", [
        ("Setup", "£995", "One-off, paid once", ["Discovery and strategy session", "Your website and chatbot, built and live", "Connected to your existing systems", "Team training session"], False),
        ("Ongoing", "£995<small>/month</small>", "Cancel any time · single-site businesses", ["Hosting and running costs", "Marketing and social media management", "Monthly review call", "Priority support"], True),
        ("Sonnatt Scale", "£3,000<small>+/month</small>", "Custom setup, scoped after discovery", ["Multiple sites and locations", "Multiple system integrations", "Named account manager", "Same-day priority support", "Quarterly strategy reviews"], False),
      ]),
      ("What £995 a month replaces", "prose", [
        "Instead of paying a web designer, a hosting company, a social media freelancer and someone to set up your systems separately, one team builds and runs the whole thing. You get one point of contact, one monthly bill, and a live dashboard showing what your investment is doing.",
        "The 15-minute walkthrough is free and there's no obligation. We'll show you what your new site and chatbot could look like, using your own business, before you commit to anything.",
      ]),
    ],
    "faq": [
      ("How much does Sonnatt.ai cost?", "£995 one-off to build it, then £995 a month to run it. The monthly plan covers hosting and running costs, marketing and social media management, a monthly review call and priority support."),
      ("Is there a contract?", "There's no long contract. You can cancel any time with 30 days' notice."),
      ("What's included in the £995 setup?", "A discovery and strategy session, your website and chatbot built and live, connection to the tools you already use, and a training session for your team."),
      ("What is the Scale plan?", "For businesses with several sites, branches or systems. It starts from £3,000 a month and includes a named account manager, same-day priority support and quarterly strategy reviews. The setup is quoted after a discovery call."),
      ("Is the first call free?", "Yes. The 15-minute walkthrough is free and there's no obligation."),
    ],
    "related": ["website-design-leeds", "website-chatbot", "social-media-marketing-leeds", "custom-apps-automation"],
  },
]

GA = """<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-V5KS40EXWS"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  // Analytics stays off until the visitor accepts the cookie banner (UK PECR / GDPR).
  var ckChoice = null;
  try { ckChoice = localStorage.getItem('sonnatt_cookie_consent'); } catch (e) {}
  gtag('consent', 'default', {
    analytics_storage: ckChoice === 'granted' ? 'granted' : 'denied',
    ad_storage: 'denied', ad_user_data: 'denied', ad_personalization: 'denied'
  });
  gtag('js', new Date());

  gtag('config', 'G-V5KS40EXWS');
</script>"""

# Industry, Google Business Profile and case-study pages.
PAGES += [{'slug': 'websites-for-accountants-leeds',
  'title': 'Websites for Accountants in Leeds | Sonnatt.ai',
  'desc': 'Professional websites, client chatbots and marketing for accountants and advisers in Leeds and Bradford. £995 setup, £995 a month, '
          'everything included.',
  'crumb': 'Websites for accountants',
  'eyebrow': 'Accountants & advisers · Leeds',
  'h1': 'Websites for accountants and advisers in Leeds',
  'lede': 'Prospective clients compare three or four practices before they call. We build a professional site that explains your services and fees '
          'clearly, add a chatbot that answers the routine questions, and run the marketing that keeps new enquiries coming in.',
  'service': 'Websites and marketing for accountants and advisers',
  'sections': [('Sound familiar?',
                'cards',
                [('The same questions all year',
                  '"Do you do self-assessment?", "What do you charge for a limited company?", "Can you take over from my old accountant?"'),
                 ('Busy season swallows everything', 'January and the year-end months leave no time to reply to new enquiries quickly.'),
                 ('A site that undersells the practice',
                  "Generic stock photos and a list of services don't explain why someone should choose you.")]),
               ('What we build and run for you',
                'prose',
                ['<ul><li>A clear, professional website with service pages for each type of client</li><li>A chatbot that answers common questions '
                 'and books discovery calls</li><li>Online enquiry forms connected to your practice management or CRM</li><li>Regular posts and '
                 'reminders around tax deadlines</li><li>Review requests to build your Google rating</li></ul>']),
               ('How it works', 'steps', STEPS),
               ('What it costs',
                'prose',
                ['<b>£995 one-off setup</b>: a discovery session, your website and chatbot built and live, connected to the tools you already use, '
                 'and training for your team.',
                 '<b>£995 a month</b>: hosting, marketing and social media management, a monthly review call and priority support. Cancel any time '
                 "with 30 days' notice.",
                 'See the full breakdown on our <a href="/pricing/">pricing page</a>.'])],
  'faq': [('Can the chatbot give tax advice?',
           "No, and it shouldn't. It answers questions about your services, fees and process, and hands anything specific to a person on your team."),
          ('Will it work with our practice software?',
           "Usually, yes. We connect to common calendars, booking tools and CRMs. We'll check yours in the discovery session."),
          ('Can you post around tax deadlines?',
           'Yes. We plan content around self-assessment, VAT and year-end dates so your practice stays visible when people are looking.'),
          ('Do you handle client data securely?',
           "Enquiry details are stored securely and only used to reply to enquiries. We'll go through how your data is handled before we start.")],
  'related': ['website-design-leeds', 'website-chatbot', 'websites-for-clinics-leeds', 'websites-for-salons-gyms-leeds']},
 {'slug': 'websites-for-clinics-leeds',
  'title': 'Websites for Clinics & Practices in Leeds | Sonnatt.ai',
  'desc': 'Websites and booking chatbots for clinics, therapists and practices in Leeds and Bradford. Take enquiries off the reception desk. £995 '
          'setup, £995 a month.',
  'crumb': 'Websites for clinics',
  'eyebrow': 'Clinics & practices · Leeds',
  'h1': 'Websites for clinics and practices in Leeds',
  'lede': 'Your reception team spends hours on the phone answering the same questions about prices, availability and parking. We build a website and '
          'chatbot that handle those questions and appointment requests online, so the desk can look after the people in front of them.',
  'service': 'Websites and booking chatbots for clinics',
  'sections': [('Sound familiar?',
                'cards',
                [('Phones ringing during appointments',
                  'Missed calls are missed bookings, especially for smaller practices without a full-time receptionist.'),
                 ('Patients want to book at night', "Many people look for a physio, dentist or therapist in the evening, when you're closed."),
                 ("Treatment pages that don't convert", 'People want to know what a treatment involves and what it costs before they commit.')]),
               ('What we build and run for you',
                'prose',
                ['<ul><li>A calm, trustworthy website with clear treatment and price pages</li><li>A chatbot that answers common questions and takes '
                 'appointment requests</li><li>Your online booking system connected and easy to find</li><li>Automatic review requests after '
                 'appointments</li><li>Monthly social content and Google profile updates</li></ul>']),
               ('How it works', 'steps', STEPS),
               ('What it costs',
                'prose',
                ['<b>£995 one-off setup</b>: a discovery session, your website and chatbot built and live, connected to the tools you already use, '
                 'and training for your team.',
                 '<b>£995 a month</b>: hosting, marketing and social media management, a monthly review call and priority support. Cancel any time '
                 "with 30 days' notice.",
                 'See the full breakdown on our <a href="/pricing/">pricing page</a>.'])],
  'faq': [('Does the chatbot give medical advice?',
           'No. It answers practical questions about your services, prices and opening times, and passes anything clinical to your team.'),
          ('Can it connect to our booking system?',
           'In most cases, yes. We connect to common clinic booking tools and calendars, and check yours during discovery.'),
          ('Is it suitable for private practices?',
           'Yes. Physios, dental practices, therapists, aesthetics clinics and other private practices are a good fit.'),
          ('How do you handle patient information?',
           "The website only collects what's needed to reply to an enquiry. We'll agree how enquiries are handled and stored before launch.")],
  'related': ['website-design-leeds', 'website-chatbot', 'websites-for-accountants-leeds', 'websites-for-salons-gyms-leeds']},
 {'slug': 'websites-for-salons-gyms-leeds',
  'title': 'Websites for Salons, Gyms & Venues in Leeds | Sonnatt.ai',
  'desc': 'Booking-ready websites, chatbots and social media for salons, gyms and venues in Leeds and Bradford. £995 setup, £995 a month, everything '
          'included.',
  'crumb': 'Websites for salons and gyms',
  'eyebrow': 'Salons, gyms & venues · Leeds',
  'h1': 'Websites and social media for salons, gyms and venues in Leeds',
  'lede': 'Your customers find you on Instagram and Google, then want to book in two taps. We build a booking-ready website and chatbot, and run the '
          'social content that keeps your diary full.',
  'service': 'Websites and social media for salons, gyms and venues',
  'sections': [('Sound familiar?',
                'cards',
                [('DMs at midnight', '"Have you got anything Saturday?" arrives while you\'re asleep and the customer books elsewhere by morning.'),
                 ('Quiet weekdays', "The weekend is full but Tuesday afternoons need filling, and there's no time to plan promotions."),
                 ('Posting is a chore', "You know you should post more, but you're busy with clients all day.")]),
               ('What we build and run for you',
                'prose',
                ['<ul><li>A booking-ready website that looks great on a phone</li><li>A chatbot that answers prices and availability and links to '
                 'your booking tool</li><li>Social media content planned and posted every month</li><li>Offers and reminders to fill quiet '
                 'slots</li><li>Review requests after visits to grow your Google rating</li></ul>']),
               ('How it works', 'steps', STEPS),
               ('What it costs',
                'prose',
                ['<b>£995 one-off setup</b>: a discovery session, your website and chatbot built and live, connected to the tools you already use, '
                 'and training for your team.',
                 '<b>£995 a month</b>: hosting, marketing and social media management, a monthly review call and priority support. Cancel any time '
                 "with 30 days' notice.",
                 'See the full breakdown on our <a href="/pricing/">pricing page</a>.'])],
  'faq': [('Can you work with my booking app?',
           'Yes. We link your website and chatbot to the booking tool you already use, such as Fresha, Treatwell, Mindbody or similar.'),
          ('Do you make the social posts?', 'Yes. We plan, create and post content every month, and you can approve it before it goes out.'),
          ('Can you promote offers for quiet days?', "Yes. We'll set up promotions and reminders aimed at the times you most need to fill."),
          ('What if I already have a website?', "If it works well we'll improve it. If it's slowing bookings down we'll rebuild it.")],
  'related': ['website-design-leeds', 'website-chatbot', 'websites-for-accountants-leeds', 'websites-for-clinics-leeds']},
 {'slug': 'websites-for-trades-leeds',
  'title': 'Websites for Trades & Contractors in Leeds | Sonnatt.ai',
  'desc': 'Websites for builders, plumbers, electricians and contractors in Leeds and Bradford, with missed-call follow-up and admin handled. £995 '
          'setup, £995 a month.',
  'crumb': 'Websites for trades',
  'eyebrow': 'Trades & contractors · Leeds',
  'h1': 'Websites for trades and contractors in Leeds',
  'lede': 'When someone needs a builder, plumber or electrician they search, look at two or three sites and ring the one that looks most reliable. '
          'We build a site that wins that job before the phone rings, then handle the follow-ups and admin behind it.',
  'service': 'Websites for trades and contractors',
  'sections': [('Sound familiar?',
                'cards',
                [('Missing calls on the job', "You can't answer with your hands full, and a missed call is usually a missed job."),
                 ('Evenings spent on admin', 'Quotes, follow-ups, chasing reviews and replying to messages after a full day on site.'),
                 ('No photos of your best work online', "You do great work but the website doesn't show it.")]),
               ('What we build and run for you',
                'prose',
                ['<ul><li>A website that shows your work, areas covered and accreditations</li><li>Automatic text-back when you miss a call, so the '
                 'customer hears from you</li><li>A chatbot that collects job details and photos before you call back</li><li>Review requests after '
                 'every finished job</li><li>Your Google profile and social pages kept active with your projects</li></ul>']),
               ('How it works', 'steps', STEPS),
               ('What it costs',
                'prose',
                ['<b>£995 one-off setup</b>: a discovery session, your website and chatbot built and live, connected to the tools you already use, '
                 'and training for your team.',
                 '<b>£995 a month</b>: hosting, marketing and social media management, a monthly review call and priority support. Cancel any time '
                 "with 30 days' notice.",
                 'See the full breakdown on our <a href="/pricing/">pricing page</a>.'])],
  'faq': [('What areas do you cover?', 'Trades across Leeds, Bradford and West Yorkshire. Your website will list the towns and areas you work in.'),
          ("I'm a sole trader, is this for me?",
           "If your website isn't bringing in work and you'd rather not deal with it, yes. The monthly plan includes everything, so there are no "
           'surprise bills.'),
          ('Can you show my accreditations?', 'Yes. Gas Safe, NICEIC, TrustMark and other memberships can be shown clearly on the site.'),
          ('Do I need to take photos?', "Send us photos from your phone as you finish jobs and we'll turn them into project posts.")],
  'related': ['website-design-leeds', 'website-chatbot', 'websites-for-accountants-leeds', 'websites-for-clinics-leeds']},
 {'slug': 'websites-for-letting-agents-leeds',
  'title': 'Websites for Letting Agents & Property Managers in Leeds | Sonnatt.ai',
  'desc': 'Websites and chatbots for letting agents, property managers and short-let hosts in Leeds and Bradford. Handle viewing requests and guest '
          'queries online.',
  'crumb': 'Websites for letting agents',
  'eyebrow': 'Letting & property · Leeds',
  'h1': 'Websites for letting agents and property managers in Leeds',
  'lede': 'Tenants, landlords and guests all expect quick answers. We build a website and chatbot that handle viewing requests, guest questions and '
          'landlord enquiries, connected to the systems you already use.',
  'service': 'Websites and chatbots for letting agents and property managers',
  'sections': [('Sound familiar?',
                'cards',
                [('The same questions on repeat', '"Is it still available?", "Are pets allowed?", "What\'s the check-in time?"'),
                 ('Viewings booked by phone tag', 'Arranging viewings takes several calls and messages for every applicant.'),
                 ('Landlords judge you online', 'Landlords choosing an agent compare websites, reviews and how professional you look.')]),
               ('What we build and run for you',
                'prose',
                ['<ul><li>A professional website for tenants, landlords and guests</li><li>A chatbot that answers property questions and books '
                 'viewings</li><li>Connections to your calendar, CRM or property software</li><li>A landlord enquiry page and follow-up '
                 'process</li><li>Social media and Google profile updates every month</li></ul>']),
               ('How it works', 'steps', STEPS),
               ('What it costs',
                'prose',
                ['<b>£995 one-off setup</b>: a discovery session, your website and chatbot built and live, connected to the tools you already use, '
                 'and training for your team.',
                 '<b>£995 a month</b>: hosting, marketing and social media management, a monthly review call and priority support. Cancel any time '
                 "with 30 days' notice.",
                 'See the full breakdown on our <a href="/pricing/">pricing page</a>.'])],
  'faq': [('Does it work for short lets and serviced accommodation?',
           'Yes. The chatbot can answer guest questions about check-in, parking and amenities, day or night.'),
          ('Can it book viewings?', 'Yes. It can collect applicant details and offer viewing slots from your calendar.'),
          ('Will it connect to our property software?', "We connect to many common tools and calendars. We'll check yours during discovery."),
          ('Can you help us win more landlords?', 'Yes. We build landlord-focused pages and marketing to bring in new instructions.')],
  'related': ['website-design-leeds', 'website-chatbot', 'websites-for-accountants-leeds', 'websites-for-clinics-leeds']},
 {'slug': 'google-business-profile-management',
  'title': 'Google Business Profile Management in Leeds | Sonnatt.ai',
  'desc': 'We set up, optimise and run your Google Business Profile: categories, services, photos, weekly posts and review requests. For Leeds and '
          'Bradford businesses.',
  'crumb': 'Google Business Profile management',
  'eyebrow': 'Service · Google Business Profile',
  'h1': 'Google Business Profile management for Leeds businesses',
  'lede': 'For a local business, your Google profile is often seen before your website. We set it up properly, keep it active every week and help '
          'you collect the reviews that decide who shows up first on Google Maps.',
  'service': 'Google Business Profile management',
  'sections': [('Sound familiar?',
                'cards',
                [('A profile you set up once and forgot',
                  "Out-of-date hours, a handful of old photos and no posts tell Google and customers that nobody's minding it."),
                 ('Not showing up on the map', 'Competitors with more reviews and a busier profile appear above you for searches in your own area.'),
                 ('Reviews that never get asked for', 'Happy customers would leave a review, but nobody sends them the link at the right moment.')]),
               ('What we build and run for you',
                'prose',
                ['<ul><li>Profile set up or cleaned up: categories, services, service areas, hours and description</li><li>Your name, address and '
                 'phone number made consistent across Google, your website and the main UK directories</li><li>Regular posts with offers, updates '
                 'and photos of your work</li><li>Automatic review requests after jobs or appointments, with replies to every review</li><li>A '
                 'monthly report on calls, direction requests and website clicks from your profile</li></ul>']),
               ('How it works', 'steps', STEPS),
               ('What it costs',
                'prose',
                ['<b>£995 one-off setup</b>: a discovery session, your website and chatbot built and live, connected to the tools you already use, '
                 'and training for your team.',
                 '<b>£995 a month</b>: hosting, marketing and social media management, a monthly review call and priority support. Cancel any time '
                 "with 30 days' notice.",
                 'See the full breakdown on our <a href="/pricing/">pricing page</a>.'])],
  'faq': [('Can you guarantee the top spot on Google Maps?',
           'No one honestly can. Distance from the searcher matters a lot. What we can do is make your profile complete, active and well-reviewed, '
           'which are the parts you control.'),
          ('Do I need a shop or office?',
           'No. Businesses that travel to customers can set up as a service-area business, with the address hidden from the public.'),
          ('Is this included in the monthly plan?', 'Yes. Google Business Profile management is part of the £995 monthly plan.'),
          ('Will you reply to reviews for me?', 'Yes, in your tone, and we flag any negative review to you before replying.')],
  'related': ['website-design-leeds', 'social-media-marketing-leeds', 'website-chatbot']},
 {'slug': 'work-help-u-property',
  'title': 'Help U Property Website | Our Work | Sonnatt.ai',
  'desc': 'How Sonnatt.ai built the website for Help U Property, a Leeds property maintenance company selling to letting agents and landlords on '
          'subscription.',
  'crumb': 'Case study: Help U Property',
  'eyebrow': 'Our work · Property maintenance · Leeds',
  'h1': 'A subscription website for Help U Property',
  'lede': 'Help U Property keeps rented homes across Leeds safe and compliant. We built them a website that explains their subscription service to '
          'agents and owners, keeps the emergency line one tap away and turns visits into demo bookings.',
  'service': None,
  'kind': 'work',
  'og': '/media/work-helpuproperty-desktop.jpg',
  'sections': [('',
                'raw',
                '\n'
                '<section class="block"><div class="wrap"><div class="shots">\n'
                '<figure class="shot"><img src="/media/work-helpuproperty-desktop.jpg" width="1200" height="633" alt="The Help U Property homepage '
                'on a laptop, showing the headline, emergency phone line and a preview of the Dispatch job dashboard" '
                'loading="lazy"><figcaption>Desktop homepage</figcaption></figure>\n'
                '<figure class="shot"><img src="/media/work-helpuproperty-mobile.jpg" width="390" height="760" alt="The Help U Property homepage on '
                'a phone, with the emergency number pinned to the top" loading="lazy"><figcaption>On a phone</figcaption></figure>\n'
                '</div></div></section>\n'
                '<section class="block"><div class="wrap"><dl class="cs-facts">\n'
                '<div><dt>Client</dt><dd>Help U Property, Leeds</dd></div>\n'
                '<div><dt>Sector</dt><dd>Property maintenance for letting agents and landlords</dd></div>\n'
                '<div><dt>What we built</dt><dd>Website, chatbot, client portal entry, pricing and demo booking</dd></div>\n'
                '<div><dt>Live site</dt><dd><a href="https://www.helpuproperty.co.uk" rel="noopener" '
                'target="_blank">helpuproperty.co.uk</a></dd></div>\n'
                '</dl></div></section>\n'
                '<section class="block"><div class="wrap"><h2>The brief</h2><div class="prose">\n'
                '<p>Help U Property is a Leeds property maintenance company that works for '
                'letting agents, landlords and homeowners: emergency repairs, plumbing, electrical, joinery, refurbishments and compliance checks. '
                'They were moving to a subscription model built around Dispatch, their platform for tracking jobs, compliance and invoices.</p>\n'
                '<p>They needed a website that explains a subscription service to two very '
                'different audiences, agencies managing whole portfolios and owners with one home, and that turns visits into demo bookings, trial '
                'sign-ups and emergency calls.</p>\n'
                '</div></div></section>\n'
                '<section class="block"><div class="wrap"><h2>What we built</h2><div class="cards">\n'
                '<div class="card"><h3>Two audiences, one site</h3><p>Separate paths for estate agents and property owners from the first screen, '
                'each explaining what they get in their own terms.</p></div>\n'
                '<div class="card"><h3>Emergency line always visible</h3><p>The 24/7 number sits at the top of every page and as a floating button '
                'on phones, so a tenant with a leak can call in one tap.</p></div>\n'
                '<div class="card"><h3>The platform, explained</h3><p>A section showing what Dispatch does, with job tracking, compliance reminders '
                'and invoicing, and a four-step "how it works" from reported issue to invoice.</p></div>\n'
                '<div class="card"><h3>Clear subscription pricing</h3><p>Three plans with monthly and annual billing, a free trial and a "talk to '
                'us" route for larger agencies.</p></div>\n'
                '<div class="card"><h3>Chat assistant</h3><p>An on-site assistant that answers common questions and points visitors to the right '
                'next step.</p></div>\n'
                '<div class="card"><h3>Built to be found</h3><p>Service sections for every trade, an FAQ, Leeds areas covered and a prompt for '
                'customers to leave a Google review.</p></div>\n'
                '</div></div></section>\n'
                '<section class="block"><div class="wrap"><h2>What happens next</h2><div class="prose">\n'
                '<p>Help U Property joined our monthly plan in October 2026, which covers hosting, '
                "updates, social media and marketing. We'll add results here once there are a few months of real numbers to share.</p>\n"
                '</div></div></section>\n')],
  'faq': [],
  'related': ['website-design-leeds', 'websites-for-letting-agents-leeds', 'website-chatbot']}]

def e(s):
    return html.escape(s, quote=True)

def strip(s):
    import re
    return re.sub(r"<[^>]+>", "", s)

PAGE_BY_SLUG = {p["slug"]: p for p in PAGES}

def nav(current):
    def link(href, label, cls=""):
        cur = ' aria-current="page"' if href == current else ""
        return f'<a href="{href}"{cur}{cls}>{label}</a>'
    links = "".join(link(h, l) for h, l in NAV)
    return f"""<a class="skip" href="#main">Skip to content</a>
<header class="nav">
  <div class="wrap">
    <a class="brand" href="/"><img src="/img/logo-64.png" width="30" height="30" alt="" decoding="async"><span>Sonnatt<span class="ai">.ai</span></span></a>
    <nav class="links" aria-label="Main">{links}</nav>
    <div class="nav-right">
      <a class="btn btn-sm" href="#enquire" data-book>Book a call</a>
      <button class="nav-toggle" id="navToggle" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="mnav"><span></span><span></span><span></span></button>
    </div>
  </div>
  <nav class="mnav" id="mnav" aria-label="Menu">
    <a href="/">Home</a>{links}
    <a class="btn" href="#enquire" data-book>Book a free call</a>
  </nav>
</header>"""

FOOTER = """<footer>
  <div class="wrap">
    <div class="cols">
      <div><h2>Sonnatt.ai</h2><ul><li>Websites, chatbots and marketing, built and run for you</li><li>Leeds, West Yorkshire</li><li><a href="mailto:info@sonnattai.com">info@sonnattai.com</a></li><li><a href="https://www.facebook.com/1380063305186616" rel="me noopener" target="_blank">Facebook</a> · <a href="https://www.instagram.com/sonnatt.ai/" rel="me noopener" target="_blank">Instagram</a></li></ul></div>
      <div><h2>Services</h2><ul><li><a href="/website-design-leeds/">Website design in Leeds</a></li><li><a href="/website-chatbot/">Website chatbots</a></li><li><a href="/social-media-marketing-leeds/">Marketing and social media</a></li><li><a href="/custom-apps-automation/">Custom apps and automation</a></li><li><a href="/google-business-profile-management/">Google Business Profile</a></li></ul></div>
      <div><h2>Industries</h2><ul><li><a href="/websites-for-accountants-leeds/">Accountants</a></li><li><a href="/websites-for-clinics-leeds/">Clinics</a></li><li><a href="/websites-for-salons-gyms-leeds/">Salons and gyms</a></li><li><a href="/websites-for-trades-leeds/">Trades</a></li><li><a href="/websites-for-letting-agents-leeds/">Letting agents</a></li></ul></div>
      <div><h2>More</h2><ul><li><a href="/pricing/">Pricing</a></li><li><a href="/web-design-bradford/">Bradford</a></li><li><a href="/work-help-u-property/">Our work</a></li><li><a href="/#faq">FAQ</a></li><li><a href="/#contact">Contact</a></li></ul></div>
    </div>
    <div class="base"><span>© Sonnatt.ai · <a href="/privacy">Privacy policy</a> · <a href="#" data-cookie-settings>Cookie settings</a></span><span>Smarter Business. Real Results.</span></div>
  </div>
</footer>
<div id="ckBanner" role="dialog" aria-label="Cookie choices" hidden>
  <p>We use Google Analytics cookies to see how people use this site and improve it. They only switch on if you accept. <a href="/privacy">Privacy policy</a></p>
  <div class="ck-row"><button type="button" class="ck-yes" id="ckYes">Accept</button><button type="button" id="ckNo">Decline</button></div>
</div>
<script src="/assets/site.js" defer></script>"""

def section_html(title, kind, body):
    if kind == "raw":
        return body
    out = [f'<section class="block"><div class="wrap">', f"<h2>{e(title)}</h2>"]
    if kind == "cards":
        out.append('<div class="cards">' + "".join(f'<div class="card"><h3>{e(t)}</h3><p>{e(d)}</p></div>' for t, d in body) + "</div>")
    elif kind == "steps":
        out.append('<ol class="steps">' + "".join(f"<li><b>{e(t)}</b>{e(d)}</li>" for t, d in body) + "</ol>")
    elif kind == "prose":
        out.append('<div class="prose">' + "".join(p if p.startswith("<ul") else f"<p>{p}</p>" for p in body) + "</div>")
    elif kind == "plans":
        cards = []
        for name, price, note, items, lit in body:
            cards.append(f'<div class="card{" lit" if lit else ""}"><h3>{e(name)}</h3><div class="price blue-text">{price}</div><p>{e(note)}</p><ul>' + "".join(f"<li>{e(i)}</li>" for i in items) + "</ul></div>")
        out.append('<div class="cards">' + "".join(cards) + "</div>")
    out.append("</div></section>")
    return "\n".join(out)

def jsonld(p):
    url = f"{SITE}/{p['slug']}/"
    org = {"@id": f"{SITE}/#organization"}
    graph = [
        {"@type": "WebPage", "@id": url + "#webpage", "url": url, "name": strip(p["title"]), "description": p["desc"],
         "inLanguage": "en-GB", "isPartOf": {"@id": f"{SITE}/#website"}, "about": org,
         "breadcrumb": {"@id": url + "#breadcrumb"}, "dateModified": UPDATED,
         "primaryImageOfPage": {"@type": "ImageObject", "url": SITE + p.get("og", "/og-image.png")}},
        {"@type": "BreadcrumbList", "@id": url + "#breadcrumb", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
            {"@type": "ListItem", "position": 2, "name": p["crumb"], "item": url}]},
    ]
    if p["faq"]:
        graph.append({"@type": "FAQPage", "@id": url + "#faq", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p["faq"]]})
    if p.get("kind") == "work":
        graph.append({"@type": "CreativeWork", "@id": url + "#work", "name": strip(p["h1"]), "url": url, "creator": org,
                      "image": SITE + p["og"], "about": {"@type": "Organization", "name": "Help U Property", "url": "https://www.helpuproperty.co.uk"}})
    elif p.get("service"):
        area = [{"@type": "City", "name": p["area"]}] if p.get("area") else [{"@type": "City", "name": "Leeds"}, {"@type": "City", "name": "Bradford"}, {"@type": "AdministrativeArea", "name": "West Yorkshire"}]
        graph.append({"@type": "Service", "@id": url + "#service", "name": p["service"], "serviceType": p["service"],
                      "description": strip(p["lede"]), "url": url, "provider": org, "areaServed": area,
                      "offers": [{"@type": "Offer", "name": "Setup", "price": "995", "priceCurrency": "GBP"},
                                 {"@type": "Offer", "name": "Ongoing monthly plan", "priceCurrency": "GBP",
                                  "priceSpecification": {"@type": "UnitPriceSpecification", "price": "995", "priceCurrency": "GBP", "unitText": "MONTH"}}]})
    else:
        graph.append({"@type": "OfferCatalog", "@id": url + "#plans", "name": "Sonnatt.ai plans", "itemListElement": [
            {"@type": "Offer", "name": "Setup", "price": "995", "priceCurrency": "GBP", "seller": org},
            {"@type": "Offer", "name": "Ongoing monthly plan", "seller": org, "priceSpecification": {"@type": "UnitPriceSpecification", "price": "995", "priceCurrency": "GBP", "unitText": "MONTH"}},
            {"@type": "Offer", "name": "Sonnatt Scale", "seller": org, "priceSpecification": {"@type": "UnitPriceSpecification", "minPrice": "3000", "priceCurrency": "GBP", "unitText": "MONTH"}}]})
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, indent=1, ensure_ascii=False).replace("</", "<\\/")

def build(p):
    url = f"{SITE}/{p['slug']}/"
    facts = "".join(f"<li>{e(k)}: <b>{e(v)}</b></li>" for k, v in PRICING_FACTS)
    sections = "\n".join(section_html(*s) for s in p["sections"])
    faq = "\n".join(f'<details class="faq-i"><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q, a in p["faq"])
    faq_block = f'''  <section class="block" id="faq"><div class="wrap">
    <h2>Frequently asked questions</h2>
    <div class="faq">
{faq}
    </div>
  </div></section>''' if p["faq"] else ""
    facts_html = f'<ul class="facts">{facts}</ul>' if p.get("kind") != "work" else ""
    related = "".join(f'<li><a href="/{s}/">{e(PAGE_BY_SLUG[s]["crumb"])} →</a></li>' for s in p["related"])
    return f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
{GA}
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(p['title'])}</title>
<meta name="description" content="{e(p['desc'])}">
<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1">
<meta name="theme-color" content="#05090F">
<meta name="sonnatt-booking" content="{e(BOOKING)}">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="en-GB" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Sonnatt.ai">
<meta property="og:locale" content="en_GB">
<meta property="og:title" content="{e(p['title'])}">
<meta property="og:description" content="{e(p['desc'])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}{p.get('og', '/og-image.png')}">
<meta property="og:image:alt" content="Sonnatt.ai: website, chatbot and marketing for Leeds and Bradford businesses">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@600;700;800&family=Inter:wght@400;500;600;700&display=swap">
<link rel="stylesheet" href="/assets/site.css">
<script type="application/ld+json">
{jsonld(p)}
</script>
</head>
<body>
{nav('/' + p['slug'] + '/')}
<main id="main">
  <div class="page-hero">
    <div class="wrap">
      <nav class="crumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li aria-current="page">{e(p['crumb'])}</li></ol></nav>
      <div class="eyebrow" style="margin-top:28px">{e(p['eyebrow'])}</div>
      <h1>{e(p['h1'])}</h1>
      <p class="lede">{e(p['lede'])}</p>
      {facts_html}
      <div class="cta"><a class="btn" href="#enquire" data-book>Book a free 15-minute call</a><a class="quiet" href="mailto:info@sonnattai.com">Email info@sonnattai.com →</a></div>
    </div>
  </div>
{sections}
{faq_block}
  <section class="cta-band" id="enquire"><div class="wrap">
    <h2>See what your business could look like online</h2>
    <p>15 minutes, free, no obligation. Tell us a little about your business and we'll show you what your new site and chatbot could look like before you commit to anything.</p>
    <form class="enquire" id="lf" data-interest="{e(p['eyebrow'])}" novalidate>
      <div class="f"><label for="l-name">Your name</label><input id="l-name" name="name" autocomplete="name" required></div>
      <div class="f"><label for="l-biz">Business name</label><input id="l-biz" name="business" autocomplete="organization" required></div>
      <div class="f"><label for="l-email">Email</label><input id="l-email" name="email" type="email" autocomplete="email" required></div>
      <div class="f"><label for="l-phone">Phone (optional)</label><input id="l-phone" name="phone" type="tel" autocomplete="tel"></div>
      <div class="f wide"><label for="l-msg">What's slowing your business down online right now?</label><textarea id="l-msg" name="message" rows="3"></textarea></div>
      <input type="text" name="bot-field" tabindex="-1" autocomplete="off" aria-hidden="true" class="hp">
      <div class="wide foot"><button class="btn" type="submit">Book my walkthrough</button><span id="lnote" role="status" aria-live="polite"></span></div>
    </form>
    <p class="small">We reply within one working day. Or email <a href="mailto:info@sonnattai.com">info@sonnattai.com</a>. We only use your details to reply. <a href="/privacy">Privacy policy</a></p>
    <ul class="related" aria-label="Related pages">{related}</ul>
  </div></section>
</main>
{FOOTER}
</body>
</html>
"""

if __name__ == "__main__":
    for p in PAGES:
        os.makedirs(p["slug"], exist_ok=True)
        with open(os.path.join(p["slug"], "index.html"), "w") as f:
            f.write(build(p))
        print("built", p["slug"])
