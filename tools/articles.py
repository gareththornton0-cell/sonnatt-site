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
<li><b>Ask every happy customer for a review</b>, using the review link in your profile. Never pay or reward people for reviews, and don't offer anything to change a bad one; Google removes incentivised reviews and can restrict your profile. See <a href="/guides/how-to-get-more-google-reviews/">how to get more Google reviews</a>.</li>
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
<p>Keeping your Google Business Profile active and up to date, asking for reviews after each job and posting regular updates are all part of the Sonnatt.ai monthly plan. See our <a href="/google-business-profile-management/">Google Business Profile management</a> and <a href="/social-media-marketing-leeds/">marketing and social media</a> services.</p>
""",
    "faq": [
      ("Is a Google Business Profile free?", "Yes. Creating and managing a Google Business Profile is free."),
      ("How do I verify my Google Business Profile?", "Google chooses the verification method for each business, and it is often a short video showing the business, its signage, tools or premises. Follow the on-screen instructions and avoid changing key details while verification is in progress."),
      ("Can I hide my home address on Google Business Profile?", "Yes. If you serve customers at their location or work from home, set up a service-area business and list the areas you cover instead of showing your address."),
      ("How long can a Google Business Profile description be?", "Up to 750 characters. Describe what you do, who for and where, without links or price promotions."),
      ("Can I offer customers a discount for a Google review?", "No. Google does not allow incentivised reviews, including payments, discounts or free services in exchange for a review, and can remove them and restrict the profile. You can ask customers for genuine reviews without offering anything."),
    ],
  },
  {
    "slug": "website-vs-social-media-small-business",
    "title": "Website or Social Media: Which Does Your Business Need? | Sonnatt.ai",
    "desc": "Do you need a website if you're on Facebook and Instagram? What each one does well, where each falls short, and how they work best together.",
    "h1": "Website vs social media: which does a small business need?",
    "summary": "Most small businesses need both, because they do different jobs. Social media helps people discover you and stay in touch. Your website is the place you own, where people check you're legitimate, see your prices and services, find you on Google and get in touch. Social media brings people in; a good website turns them into enquiries.",
    "published": "2026-10-11",
    "updated": "2026-10-11",
    "read": "5 min read",
    "related": ["website-design-leeds", "social-media-marketing-leeds"],
    "body": """
<h2>What social media does well</h2>
<ul>
<li><b>Getting discovered</b>: people come across your posts, shares and videos without searching for you.</li>
<li><b>Showing personality</b>: behind-the-scenes photos, recent work and short videos build trust.</li>
<li><b>Staying in touch</b>: followers see your news, offers and updates over time.</li>
<li><b>Quick conversations</b>: comments and messages make it easy for people to ask a question.</li>
</ul>

<h2>Where social media falls short on its own</h2>
<ul>
<li><b>You don't own it.</b> The platform decides who sees your posts, can change its rules at any time, and can restrict or close accounts.</li>
<li><b>It's hard to find information.</b> Prices, services, opening hours and areas covered get lost in a feed of posts.</li>
<li><b>It doesn't show up well when people search on Google</b> for a service in their area.</li>
<li><b>Not everyone uses it.</b> Some customers don't use a particular platform at all, and many people expect a business to have a proper website before they get in touch.</li>
</ul>

<h2>What a website does well</h2>
<ul>
<li><b>You own it</b>, and you decide what it says and how it looks.</li>
<li><b>It answers the questions people have before they contact you</b>: what you do, where, how much, and how to book.</li>
<li><b>It can be found on Google</b>, alongside your Google Business Profile, when people search for what you do nearby.</li>
<li><b>It turns visitors into enquiries</b> with a contact form, a booking link or a chatbot that works day and night.</li>
<li><b>It makes you look established</b>: people often check a website before trusting a business they found on social media.</li>
</ul>

<h2>How they work best together</h2>
<p>Think of social media as the shop window and your website as the shop. Your posts get attention; your website is where people go to find out more and get in touch. In practice:</p>
<ol>
<li>Put your website link in every social profile bio.</li>
<li>Point posts at a specific page, such as a service, your prices or a booking page, rather than just the homepage.</li>
<li>Show your social feeds or recent work on your website so it never looks out of date.</li>
<li>Keep your business name, contact details and opening hours the same everywhere.</li>
<li>Follow up every enquiry, whichever route it came from.</li>
</ol>

<h2>If you can only do one right now</h2>
<p>If people mostly find you by searching on Google, or need details such as prices, services and booking before they decide, start with a good website and your Google Business Profile. If your customers mainly discover businesses like yours by scrolling and you already have a steady stream of messages, social media might come first, but you'll still want a simple website so people can check you out and get in touch.</p>

<h2>How Sonnatt.ai handles both</h2>
<p>We build and run your <a href="/website-design-leeds/">website</a> and your <a href="/social-media-marketing-leeds/">social media and marketing</a> together, run by one dedicated account manager, so every post points people the same way. It's £995 to set up and £995 a month, with no long contract.</p>
""",
    "faq": [
      ("Do I need a website if I have a Facebook page?", "Usually, yes. A Facebook page helps people discover you, but you don't own it, information is hard to find, and it doesn't appear well in Google searches. A website gives people a place to check your services, prices and contact details and to get in touch."),
      ("Is social media enough for a small business?", "For some businesses it's a good start, but most benefit from having both. Social media brings people in; a website and Google Business Profile help them find you through search and turn their interest into an enquiry."),
      ("Should my social posts link to my website?", "Yes. Put your website in every profile bio and link posts to a relevant page, such as a service, your prices or a booking page, so interested people can take the next step."),
    ],
  },
  {
    "slug": "how-to-get-more-google-reviews",
    "title": "How to Get More Google Reviews (Within Google's Rules) | Sonnatt.ai",
    "desc": "Practical ways for a small business to get more genuine Google reviews: when to ask, how to make it easy, how to reply, and what Google doesn't allow.",
    "h1": "How to get more Google reviews (without breaking Google's rules)",
    "summary": "The way to get more Google reviews is to ask every happy customer, at the right moment, with a direct link that makes it take seconds. Send the link from your Google Business Profile straight after a job goes well, keep the request short and personal, and reply to every review you get. Never pay or reward people for reviews, or offer anything to change a bad one; Google removes those reviews and can restrict your profile.",
    "published": "2026-10-11",
    "updated": "2026-10-11",
    "read": "6 min read",
    "related": ["google-business-profile-management", "social-media-marketing-leeds"],
    "body": """
<h2>Why reviews matter</h2>
<p>Reviews are often the first thing people look at when they find a local business on Google Search or Maps. A steady flow of recent, genuine reviews helps people choose you over the business next door, and an active, well-reviewed profile helps you show up in local results.</p>

<h2>1. Get your review link</h2>
<p>In your Google Business Profile, find the option to ask for reviews and copy the link. It takes customers straight to the review box, so they don't have to search for you. Keep it somewhere handy: your phone, your email signature, your invoice template.</p>

<h2>2. Ask at the right moment</h2>
<p>The best time to ask is straight after something has gone well: the job is finished, the customer has said thank you, or they've just collected their order. Memories fade quickly, so a request the same day works far better than one a month later.</p>

<h2>3. Make it personal and short</h2>
<p>A short, friendly message works better than a long one. For example:</p>
<p><i>"Thanks again for choosing us, Sarah. If you've got a minute, a quick Google review would really help a small local business like ours: [link]. Thank you!"</i></p>
<p>Send it however your customer prefers to hear from you: text, email or WhatsApp.</p>

<h2>4. Make asking a habit, not a campaign</h2>
<ul>
<li>Ask every customer, not just the ones you think will be most positive.</li>
<li>Add the review link to invoices, receipts and follow-up emails.</li>
<li>Put a QR code linking to your review page on your counter, van or business cards.</li>
<li>Set up an automatic review request after each job, so it happens even on busy days.</li>
</ul>

<h2>5. Reply to every review</h2>
<p>Thank people for positive reviews, ideally mentioning what they liked. For negative reviews, reply calmly and politely, apologise where it's fair, and offer to sort it out offline. Future customers read your replies as much as the reviews themselves.</p>

<h2>What Google doesn't allow</h2>
<ul>
<li><b>No incentives.</b> Don't offer payments, discounts, free products or services, or prize-draw entries in exchange for a review.</li>
<li><b>No paying to change bad reviews.</b> Don't offer anything to have a negative review removed or changed.</li>
<li><b>No fake reviews.</b> Don't write reviews yourself, or ask staff, friends or family to review the business.</li>
<li><b>No review gating.</b> Don't only send your review link to customers you expect to be happy after filtering out the rest.</li>
</ul>
<p>Google can remove reviews that break these rules and restrict your profile, for example by stopping new reviews for a period. Asking customers for genuine, honest reviews without offering anything in return is fine.</p>

<h2>Want it done for you?</h2>
<p>Automatic review requests after each job and replies to reviews are part of our <a href="/google-business-profile-management/">Google Business Profile management</a> and the Sonnatt.ai monthly plan. For setting up the profile itself, see our guide on <a href="/guides/google-business-profile-guide/">setting up and optimising your Google Business Profile</a>.</p>
""",
    "faq": [
      ("How do I ask customers for a Google review?", "Copy the review link from your Google Business Profile and send it in a short, personal message straight after a job goes well, by text, email or WhatsApp, whichever your customer prefers."),
      ("Can I give customers a discount for leaving a review?", "No. Google does not allow incentives such as payments, discounts or free products or services in exchange for reviews, and can remove those reviews and restrict your profile."),
      ("Should I reply to negative reviews?", "Yes. Reply calmly and politely, apologise where it's fair, and offer to resolve the issue offline. Future customers read your replies as well as the reviews."),
      ("Can I only ask happy customers for reviews?", "You should ask every customer. Filtering customers so that only the ones you expect to be happy get your review link, known as review gating, goes against Google's rules."),
    ],
  },
  {
    "slug": "what-to-put-on-a-small-business-website",
    "title": "What to Put on Your Website So Customers Get in Touch | Sonnatt.ai",
    "desc": "A checklist of what a small business website needs so visitors trust you and get in touch: clear services, prices, proof, contact options and the legal basics.",
    "h1": "What to put on your website so customers get in touch",
    "summary": "A small business website should answer the questions customers have before they contact you, and make contacting you easy. That means a clear headline saying what you do and where, your services, an idea of price, proof such as reviews and examples of your work, and an obvious way to get in touch on every page. It must also work well on a phone, load quickly, and include the legal basics such as a privacy policy.",
    "published": "2026-10-11",
    "updated": "2026-10-11",
    "read": "6 min read",
    "related": ["website-design-leeds", "website-chatbot"],
    "body": """
<h2>1. Say what you do, for whom and where, straight away</h2>
<p>Within a few seconds of landing on your homepage, a visitor should know what you do, who it's for and where you work. "Emergency plumber in Leeds" beats "Welcome to our website". Put this in your main headline, not buried further down.</p>

<h2>2. A clear list of services</h2>
<p>List each service in plain words. If you offer several, give each its own section or page with what it includes, who it suits and roughly how long it takes. Separate pages also help you show up when people search for that specific service.</p>

<h2>3. An idea of price</h2>
<p>People want to know if they can afford you before they get in touch. If you can't give exact prices, give a starting price, a typical range or explain what affects the cost. Even a rough guide filters out poor-fit enquiries and builds trust.</p>

<h2>4. Proof that you're good at it</h2>
<ul>
<li><b>Reviews</b>, ideally linked to your Google reviews so people can see they're real.</li>
<li><b>Examples of your work</b>: photos, before-and-afters or short case studies.</li>
<li><b>Qualifications, memberships and insurance</b> relevant to your trade or profession.</li>
<li><b>Real photos of you and your team</b>, rather than stock images.</li>
</ul>

<h2>5. An easy way to get in touch, on every page</h2>
<ul>
<li>Your phone number, tappable on mobile.</li>
<li>A short contact form: name, email or phone, and what they need. Don't ask for more than you need.</li>
<li>A booking link, if customers can book online.</li>
<li>A chatbot that answers common questions and captures enquiries outside working hours.</li>
<li>A clear button such as "Get a quote" or "Book a call" near the top of each page.</li>
</ul>

<h2>6. Answers to common questions</h2>
<p>An FAQ section answering the questions you hear every week (areas covered, payment, timescales, guarantees) saves you time and reassures customers. It also helps search engines and AI assistants understand your business.</p>

<h2>7. Works on a phone and loads quickly</h2>
<p>Many visitors will be on a phone. Check that text is readable without zooming, buttons are easy to tap, and pages load quickly. A slow, fiddly site loses people before they've read anything.</p>

<h2>8. The legal and trust basics</h2>
<ul>
<li><b>A privacy policy</b> explaining what you do with the details people give you, and a cookie notice if you use analytics or advertising cookies.</li>
<li><b>If you're a limited company</b>, your website must show your registered company name, company number, the part of the UK where it's registered and your registered office address.</li>
<li><b>Your professional body's requirements</b>, if you're in a regulated profession.</li>
<li><b>Your business address or the areas you cover</b>, matching your Google Business Profile.</li>
</ul>

<h2>9. Keep it up to date</h2>
<p>Out-of-date prices, old opening hours or a "latest news" post from three years ago make people wonder if you're still trading. Review your site every few months, or have someone do it for you.</p>

<h2>How Sonnatt.ai builds it</h2>
<p>Every website we build covers all of the above, includes a chatbot, and is hosted and kept up to date for you. See our <a href="/website-design-leeds/">website design service</a> or <a href="/pricing/">pricing</a>.</p>
""",
    "faq": [
      ("What should be on a small business homepage?", "A clear headline saying what you do and where, your main services, proof such as reviews and examples of your work, and an obvious way to get in touch, such as a phone number, contact form or booking button."),
      ("Should I put prices on my website?", "If you can. Exact prices, a starting price or a typical range help people decide whether to contact you and build trust. If prices vary, explain what affects the cost."),
      ("What legal information does a limited company website need?", "A UK limited company's website must show its registered company name, company number, the part of the UK where it's registered and its registered office address. Most websites also need a privacy policy, and a cookie notice if they use analytics or advertising cookies."),
      ("Does my website need to work on mobile?", "Yes. Many visitors will be on a phone, so text should be readable without zooming, buttons easy to tap and pages quick to load."),
    ],
  },
  {
    "slug": "what-should-an-accountants-website-include",
    "title": "What Should an Accountant's Website Include? | Sonnatt.ai",
    "desc": "A practical checklist for accountancy and advisory firm websites: services, fees, specialisms, trust signals, client portals, enquiries and the legal basics.",
    "h1": "What should an accountant's website include?",
    "summary": "An accountant's website should make it obvious which clients you work with and what you do for them, give an idea of fees, and show why people can trust you: qualifications, professional body membership, real reviews and the people behind the firm. It should make enquiries easy, handle common questions, and include the legal basics, plus anything your professional body requires.",
    "published": "2026-10-11",
    "updated": "2026-10-11",
    "read": "6 min read",
    "related": ["websites-for-accountants-leeds", "website-chatbot"],
    "body": """
<h2>1. Who you help</h2>
<p>"Accountants in Leeds" describes hundreds of firms. Say who you're best for: sole traders, limited companies, landlords, contractors, start-ups, a particular industry, or personal tax clients. Visitors who see themselves in your description are far more likely to get in touch.</p>

<h2>2. Services, explained in plain English</h2>
<p>List each service (bookkeeping, year-end accounts, self-assessment, VAT returns, payroll, management accounts, tax planning and so on) with a sentence on what it includes and who it's for. Give your most important services their own pages so people searching for them can find you.</p>

<h2>3. Fees, or how fees work</h2>
<p>Many people delay contacting an accountant because they're worried about cost. Fixed monthly packages, starting prices or a clear explanation of how you quote all help. If you offer a free initial call, say so prominently.</p>

<h2>4. Trust signals</h2>
<ul>
<li><b>Qualifications and professional body membership</b>, shown clearly.</li>
<li><b>Real reviews</b>, ideally from your Google Business Profile.</li>
<li><b>The people</b>: photos and short bios of the partners and team, so clients know who they'll be dealing with.</li>
<li><b>Software you work with</b>, such as the accounting packages your clients already use.</li>
</ul>

<h2>5. Easy ways to get in touch</h2>
<ul>
<li>A short enquiry form asking what kind of client they are and what they need.</li>
<li>A booking link for an initial call.</li>
<li>A chatbot that answers questions about your services, fees and process, and passes anything specific to a person. It should never give tax advice.</li>
</ul>

<h2>6. Helpful, timely content</h2>
<p>Deadline reminders, plain-English explainers and answers to the questions clients ask every year show expertise and help you appear in searches. Keep anything time-sensitive, such as rates and thresholds, up to date or clearly dated.</p>

<h2>7. A route for existing clients</h2>
<p>A clear link for existing clients, whether that's a client portal, a secure way to send documents or simply the right contact details, saves your team time and looks professional.</p>

<h2>8. The legal and regulatory basics</h2>
<ul>
<li><b>A privacy policy</b> covering how you handle enquiry and client data, and a cookie notice if you use analytics.</li>
<li><b>If the firm is a limited company</b>, its registered name, company number, place of registration and registered office address.</li>
<li><b>Anything your professional body requires</b> on your website or letterhead. Check your body's current guidance.</li>
</ul>

<h2>How Sonnatt.ai helps accountants</h2>
<p>We build and run websites, chatbots and marketing for accountants and advisers, including the plain-English service pages, enquiry handling and deadline-season content described above. See <a href="/websites-for-accountants-leeds/">websites for accountants in Leeds</a>.</p>
""",
    "faq": [
      ("What should an accountant's website include?", "Who you help, your services explained in plain English, an idea of fees, trust signals such as qualifications, professional body membership, reviews and team photos, easy ways to get in touch, and the legal basics including a privacy policy."),
      ("Should accountants show fees on their website?", "It helps. Fixed packages, starting prices or a clear explanation of how you quote reduce the worry about cost that stops many people getting in touch."),
      ("Can a chatbot on an accountant's website give tax advice?", "It shouldn't. A chatbot should answer questions about your services, fees and process, and pass anything specific to a qualified person on your team."),
    ],
  },
]
