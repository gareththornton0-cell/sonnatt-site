"""Guides (articles) for sonnattai.com/guides/. Built by tools/build_pages.py.

Each article: slug, title (<title>), desc (meta description), h1, summary (the
short answer shown first, which AI assistants tend to quote), body (HTML),
faq [(q, a)], published / updated dates, related service pages.
Keep claims to things that are generally true or stated elsewhere on the site.
"""

ARTICLES = [
  {
    "slug": "small-business-website-cost-leeds",
    "title": "How Much Does a Small Business Website Cost in Leeds? | Sonnatt.ai",
    "desc": "What a small business website really costs: the one-off build, the monthly running costs people forget, the three ways to get one, and what to ask first.",
    "h1": "How much does a small business website cost in Leeds?",
    "summary": "A small business website has two costs: the one-off build and the ongoing cost of keeping it running, which covers hosting, security updates, changes and the marketing that brings people to it. Most surprises come from the second part. Ask any web designer what is included each month, who owns the domain, and what changes cost before you agree to anything.",
    "published": "2026-10-11",
    "updated": "2026-10-11",
    "read": "6 min read",
    "related": ["website-design-leeds", "pricing"],
    "body": """
<h2>The two parts of the cost</h2>
<p>Almost every quote you get will split into the same two parts, even if it is not written that way:</p>
<ul>
<li><b>The build</b>: planning the pages, writing or organising the words, design, building the site and putting it live.</li>
<li><b>Keeping it running</b>: the domain name, hosting, security and software updates, backups, small changes, and anything that brings visitors to the site, such as your Google Business Profile, social media or adverts.</li>
</ul>
<p>A low build price with nothing included afterwards often ends up costing more over a couple of years than a higher price that covers the running costs.</p>

<h2>What you are actually paying for</h2>
<ul>
<li><b>Domain name</b>: your web address, such as yourbusiness.co.uk. Usually a small yearly fee. Make sure it is registered in your name or your company's name.</li>
<li><b>Hosting</b>: the server your site lives on. Cheap hosting is fine for a small site, as long as someone keeps it secure and backed up.</li>
<li><b>Design and build</b>: the biggest one-off cost. A site built around your services and customers takes longer than a template with your logo dropped in, and it usually works harder for you.</li>
<li><b>Words and photos</b>: often forgotten. If you have to write every page yourself, factor in your own time.</li>
<li><b>Updates and changes</b>: new prices, new services, a new photo. Find out whether these are included or charged per change.</li>
<li><b>Getting found</b>: a website on its own rarely brings in work. Your Google Business Profile, reviews, social posts and follow-ups do a lot of the heavy lifting.</li>
</ul>

<h2>Three common ways to get a website</h2>
<h3>1. Build it yourself</h3>
<p>Website builders charge a monthly subscription and you do the work. It is the cheapest option in money, but the most expensive in time, and the site is only as good as the hours you put in. It suits people who enjoy it and have the time.</p>
<h3>2. A freelancer or agency builds it</h3>
<p>You pay a one-off fee for the build, then either look after it yourself or pay extra for hosting, maintenance and changes. Good if you want a professional site and are happy to manage the rest.</p>
<h3>3. A managed service builds and runs it</h3>
<p>You pay a setup fee and a monthly fee, and one team builds the site, hosts it, keeps it up to date and does the marketing. It costs more each month, but there is nothing for you to manage, and the site keeps improving rather than slowly going out of date.</p>

<h2>The hidden cost: a website that doesn't bring in work</h2>
<p>The most expensive website is one that looks fine but never produces an enquiry. Common reasons are slow pages, a layout that is hard to use on a phone, no clear way to get in touch, out-of-date information, and nobody visiting because the business is hard to find on Google. Whatever route you choose, make sure someone is responsible for fixing those things.</p>

<h2>Questions to ask before you pay anyone</h2>
<ol>
<li>What exactly is included in the one-off price, and what is included each month?</li>
<li>Who owns the domain name and the website?</li>
<li>Who hosts it, and who keeps it secure and backed up?</li>
<li>How much do changes cost, and how quickly are they done?</li>
<li>Will it work well on a phone, and will it be built so Google can understand it?</li>
<li>How long is the contract, and what is the notice period?</li>
<li>How will I know whether it is bringing in enquiries?</li>
</ol>

<h2>What Sonnatt.ai charges</h2>
<p>We use the managed route. It costs <b>£995 one-off</b> to build it: a discovery session, your website and a chatbot built and live, connected to the tools you already use, and training for your team. Then it's <b>£995 a month</b> to run it: hosting, marketing and social media management, a monthly review call and priority support. There's no long contract; you can cancel with 30 days' notice. Businesses with several sites or branches can use our Scale plan, from £3,000 a month.</p>
<p>See our <a href="/website-design-leeds/">website design service</a> or the full <a href="/pricing/">pricing page</a>.</p>
""",
    "faq": [
      ("What is the difference between the build cost and the running cost of a website?", "The build cost is the one-off price for designing and putting the site live. The running cost is what it takes to keep it working and useful afterwards: the domain name, hosting, security updates, backups, changes, and the marketing that brings visitors to it."),
      ("Should I own my domain name?", "Yes. Make sure the domain is registered in your name or your company's name, so you keep your web address whoever builds or hosts the site."),
      ("Is a cheap website a false economy?", "It can be. A low build price with nothing included afterwards can cost more over time once hosting, updates and changes are added, and a site that brings in no enquiries costs you work as well as money."),
      ("How much does Sonnatt.ai charge for a website?", "£995 one-off to build your website and chatbot, then £995 a month to run it, including hosting, marketing and social media management, a monthly review call and priority support. You can cancel with 30 days' notice."),
    ],
  },
  {
    "slug": "does-my-business-need-a-website-chatbot",
    "title": "Does My Small Business Need a Website Chatbot? | Sonnatt.ai",
    "desc": "When a website chatbot is worth it for a small business, when it isn't, and what a good one does: answer common questions, capture enquiries, hand over to you.",
    "h1": "Does my small business need a website chatbot?",
    "summary": "A website chatbot is worth having if people regularly ask you the same questions, contact you outside working hours, or leave your site without getting in touch. A good one answers common questions, collects the visitor's details when they are ready, and passes the enquiry straight to you. It is not worth it if you get very few website visitors; fix that first.",
    "published": "2026-10-11",
    "updated": "2026-10-11",
    "read": "5 min read",
    "related": ["website-chatbot", "custom-apps-automation"],
    "body": """
<h2>What a website chatbot actually does</h2>
<p>A chatbot is the small chat window in the corner of a website. For a small business, a good one does three jobs:</p>
<ul>
<li><b>Answers common questions</b> such as prices, opening hours, areas covered and how to book.</li>
<li><b>Captures enquiries</b> by collecting the visitor's name, contact details and what they need, at any time of day.</li>
<li><b>Hands over to a person</b> by sending the enquiry straight to your inbox, calendar or CRM so you can follow up.</li>
</ul>

<h2>Signs a chatbot would help your business</h2>
<ul>
<li>You or your staff answer the same few questions by phone or email every day.</li>
<li>People visit your website in the evening or at weekends, when nobody can answer the phone.</li>
<li>Visitors look at your site but rarely fill in the contact form.</li>
<li>Your reception desk or inbox is busy with simple enquiries that could be handled online.</li>
<li>You take bookings or appointments and want people to be able to start that process straight away.</li>
</ul>

<h2>When a chatbot isn't the priority</h2>
<p>If very few people visit your website, a chatbot will have little to do. Getting found comes first: a clear website that works on a phone, an up-to-date Google Business Profile and a steady flow of reviews. A chatbot also won't fix a site that is confusing or out of date, so make sure the basics are right.</p>

<h2>What a good chatbot looks like</h2>
<ol>
<li><b>It is honest about what it is.</b> Visitors should know they are talking to an automated assistant, and how to reach a real person.</li>
<li><b>It sounds like your business.</b> Clear, friendly wording that matches how you talk to customers.</li>
<li><b>It gives correct answers.</b> It should only answer from information you have approved, such as your real prices and services.</li>
<li><b>It gets the enquiry to you fast.</b> Details should land somewhere you will see them straight away.</li>
<li><b>It respects privacy.</b> It should explain what happens to the details people give, in line with your privacy policy.</li>
</ol>

<h2>How to tell if it's working</h2>
<p>Track how many enquiries come through the chatbot each month, which questions people ask most, and how many of those enquiries become customers. The most-asked questions are also a useful guide to what should be clearer on your website.</p>

<h2>How Sonnatt.ai does it</h2>
<p>Every website we build includes a chatbot. It answers your most-asked questions, captures enquiries day and night and sends new leads straight to your inbox, and it can be connected to the calendar, booking tool or CRM you already use. It is built and put live as part of the £995 setup. You can try the one on <a href="/">our homepage</a>, or read more about our <a href="/website-chatbot/">website chatbots</a>.</p>
""",
    "faq": [
      ("What does a website chatbot do for a small business?", "It answers common questions, captures enquiries at any time of day by collecting the visitor's details, and passes them straight to you so you can follow up."),
      ("Is a chatbot worth it for a small business?", "It is worth it if you get regular website visitors who ask the same questions, contact you out of hours, or leave without getting in touch. If your site gets very few visitors, focus on getting found first."),
      ("Should a chatbot say it is automated?", "Yes. Visitors should know they are talking to an automated assistant and how to reach a real person."),
      ("Can a chatbot take bookings?", "It can be connected to the calendar or booking tool you already use, so customers can start a booking without waiting for a reply."),
    ],
  },
  {
    "slug": "google-business-profile-guide",
    "title": "How to Set Up and Optimise Your Google Business Profile | Sonnatt.ai",
    "desc": "A step-by-step guide to setting up, verifying and improving your Google Business Profile so local customers find you on Google Search and Maps.",
    "h1": "How to set up and optimise your Google Business Profile",
    "summary": "Your Google Business Profile is the box that appears on Google Search and Maps when people look for your business or for what you do nearby. To set it up, sign in at business.google.com, add your business name exactly as customers know it, choose the right category, add your location or service area and contact details, and verify it. Then keep it complete and active: accurate hours, services, photos, a booking link, regular posts, and genuine reviews that you reply to.",
    "published": "2026-10-11",
    "updated": "2026-10-11",
    "read": "7 min read",
    "related": ["social-media-marketing-leeds", "website-design-leeds"],
    "body": """
<h2>Why your Google Business Profile matters</h2>
<p>When someone searches for a business like yours, or for something like "accountant near me", Google often shows a map with a few local businesses before the normal search results. Those listings come from Google Business Profiles. A complete, active profile with good reviews gives you a much better chance of being one of them.</p>

<h2>Step 1: Create the profile</h2>
<ol>
<li>Go to <a href="https://business.google.com" target="_blank" rel="noopener">business.google.com</a> and sign in with the Google account you want to manage the business from. Use a business email address rather than a personal one if you can.</li>
<li>Enter your <b>business name exactly as customers see it</b> on your signs, website and invoices. Don't add extra keywords or locations to the name; Google's guidelines don't allow it and it can get a profile suspended.</li>
<li>Choose your <b>primary category</b>: the one that best describes your main business, for example "Accountant" or "Website designer". You can add a few secondary categories later.</li>
</ol>

<h2>Step 2: Location or service area</h2>
<p>If customers visit you, add your address. If you go to your customers, or work from home and don't want your address shown, set up a <b>service-area business</b> and list the towns or areas you cover instead.</p>

<h2>Step 3: Contact details and website</h2>
<p>Add your phone number and website. Use exactly the same business name, address and phone number everywhere online (your website, social media and directories). Consistent details help Google trust that the information is correct.</p>

<h2>Step 4: Verify your business</h2>
<p>Google needs to confirm the business is real before your profile shows publicly and before you can manage it fully. Google chooses the verification method, and it is often a short video showing your business, signage, tools or premises. Follow the instructions on screen, and don't edit key details such as your name or address while verification is in progress.</p>

<h2>Step 5: Complete every section</h2>
<ul>
<li><b>Business description</b>: up to 750 characters about what you do, who for and where. Write it for customers; don't include links or price promotions.</li>
<li><b>Opening hours</b>, including holiday hours when they change.</li>
<li><b>Services</b>: list each service, with a short description.</li>
<li><b>Photos</b>: your logo, a cover photo, your team, your work and your premises. Real photos are better than stock images.</li>
<li><b>Booking or appointment link</b>, if customers can book online.</li>
</ul>

<h2>Step 6: Keep it active</h2>
<ul>
<li><b>Post updates</b> regularly: news, offers, recent work or a short video.</li>
<li><b>Ask every happy customer for a review</b>, using the review link in your profile. Never pay or reward people for reviews, and don't offer anything to change a bad one; Google removes incentivised reviews and can restrict your profile.</li>
<li><b>Reply to every review</b>, good and bad, politely and promptly.</li>
<li><b>Check your details</b> every few months, and update them whenever your hours, phone number or services change.</li>
</ul>

<h2>Common mistakes to avoid</h2>
<ul>
<li>Stuffing keywords or town names into the business name.</li>
<li>Using different phone numbers or addresses on different websites.</li>
<li>Setting up the profile and never touching it again.</li>
<li>Ignoring reviews, especially negative ones.</li>
<li>Creating more than one profile for the same business.</li>
</ul>

<h2>Want it done for you?</h2>
<p>Keeping your Google Business Profile active and up to date, asking for reviews after each job and posting regular updates are all part of the Sonnatt.ai monthly plan. See our <a href="/social-media-marketing-leeds/">marketing and social media service</a>.</p>
""",
    "faq": [
      ("Is a Google Business Profile free?", "Yes. Creating and managing a Google Business Profile is free."),
      ("How do I verify my Google Business Profile?", "Google chooses the verification method for each business, and it is often a short video showing the business, its signage, tools or premises. Follow the on-screen instructions and avoid changing key details while verification is in progress."),
      ("Can I hide my home address on Google Business Profile?", "Yes. If you serve customers at their location or work from home, set up a service-area business and list the areas you cover instead of showing your address."),
      ("How long can a Google Business Profile description be?", "Up to 750 characters. Describe what you do, who for and where, without links or price promotions."),
      ("Can I offer customers a discount for a Google review?", "No. Google does not allow incentivised reviews, including payments, discounts or free services in exchange for a review, and can remove them and restrict the profile. You can ask customers for genuine reviews without offering anything."),
    ],
  },
]
