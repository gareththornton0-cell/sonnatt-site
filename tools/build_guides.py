#!/usr/bin/env python3
"""Builds sonnattai.com/guides/ (index + one page per article in articles.py).

Run from the repo root: python3 tools/build_guides.py
(tools/build_pages.py also calls this at the end, so one command rebuilds everything.)
Reuses the shared menu, footer, analytics and enquiry form from build_pages.py.
"""
import datetime, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_pages import GA, FOOTER, SITE, BOOKING, PAGE_BY_SLUG, e, nav
from articles import ARTICLES


def head(title, desc, url, ld, og_type="website", extra=""):
    return f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
{GA}
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1">
<meta name="theme-color" content="#05090F">
<meta name="sonnatt-booking" content="{e(BOOKING)}">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="en-GB" href="{url}">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="Sonnatt.ai">
<meta property="og:locale" content="en_GB">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Sonnatt.ai: website, chatbot and marketing for Leeds and Bradford businesses">
{extra}<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@600;700;800&family=Inter:wght@400;500;600;700&display=swap">
<link rel="stylesheet" href="/assets/site.css">
<script type="application/ld+json">
{ld}
</script>
</head>
<body>
"""


def enquire(interest, heading, text, related_html=""):
    # Same form as the service pages; assets/site.js saves it to website_leads.
    return f"""  <section class="cta-band" id="enquire"><div class="wrap">
    <h2>{e(heading)}</h2>
    <p>{e(text)}</p>
    <form class="enquire" id="lf" data-interest="{e(interest)}" novalidate>
      <div class="f"><label for="l-name">Your name</label><input id="l-name" name="name" autocomplete="name" required></div>
      <div class="f"><label for="l-biz">Business name</label><input id="l-biz" name="business" autocomplete="organization" required></div>
      <div class="f"><label for="l-email">Email</label><input id="l-email" name="email" type="email" autocomplete="email" required></div>
      <div class="f"><label for="l-phone">Phone (optional)</label><input id="l-phone" name="phone" type="tel" autocomplete="tel"></div>
      <div class="f wide"><label for="l-msg">What's slowing your business down online right now?</label><textarea id="l-msg" name="message" rows="3"></textarea></div>
      <input type="text" name="bot-field" tabindex="-1" autocomplete="off" aria-hidden="true" class="hp">
      <div class="wide foot"><button class="btn" type="submit">Book my walkthrough</button><span id="lnote" role="status" aria-live="polite"></span></div>
    </form>
    <p class="small">Or email <a href="mailto:info@sonnattai.com">info@sonnattai.com</a>. We only use your details to reply. <a href="/privacy">Privacy policy</a></p>
    {related_html}
  </div></section>"""


def dump(graph):
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, indent=1, ensure_ascii=False).replace("</", "<\\/")


def article_ld(a, url):
    org = {"@id": f"{SITE}/#organization"}
    return dump([
        {"@type": "Article", "@id": url + "#article", "headline": a["h1"], "description": a["desc"], "url": url,
         "mainEntityOfPage": url, "inLanguage": "en-GB", "datePublished": a["published"], "dateModified": a["updated"],
         "author": org, "publisher": org, "image": f"{SITE}/og-image.png", "abstract": a["summary"],
         "isPartOf": {"@id": f"{SITE}/guides/#webpage"}},
        {"@type": "BreadcrumbList", "@id": url + "#breadcrumb", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
            {"@type": "ListItem", "position": 2, "name": "Guides", "item": f"{SITE}/guides/"},
            {"@type": "ListItem", "position": 3, "name": a["h1"], "item": url}]},
        {"@type": "FAQPage", "@id": url + "#faq", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": ans}} for q, ans in a["faq"]]},
    ])


def nice_date(d):
    return datetime.date.fromisoformat(d).strftime("%-d %B %Y")


def build_article(a):
    url = f"{SITE}/guides/{a['slug']}/"
    faq = "\n".join(f'<details class="faq-i"><summary>{e(q)}</summary><p>{e(ans)}</p></details>' for q, ans in a["faq"])
    links = "".join(f'<li><a href="/{s}/">{e(PAGE_BY_SLUG[s]["crumb"])} →</a></li>' for s in a["related"])
    links += "".join(f'<li><a href="/guides/{o["slug"]}/">{e(o["h1"])} →</a></li>' for o in [x for x in ARTICLES if x is not a][:3])
    extra = f'<meta property="article:published_time" content="{a["published"]}">\n<meta property="article:modified_time" content="{a["updated"]}">\n'
    return head(a["title"], a["desc"], url, article_ld(a, url), "article", extra) + f"""{nav('/guides/')}
<main id="main">
  <article>
  <div class="page-hero">
    <div class="wrap narrow">
      <nav class="crumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/guides/">Guides</a></li><li aria-current="page">{e(a['h1'])}</li></ol></nav>
      <div class="eyebrow" style="margin-top:28px">Guide · {e(a['read'])}</div>
      <h1 class="article-h1">{e(a['h1'])}</h1>
      <p class="byline">By the Sonnatt.ai team, Leeds · Updated <time datetime="{a['updated']}">{nice_date(a['updated'])}</time></p>
      <div class="summary"><b>The short answer</b><p>{e(a['summary'])}</p></div>
    </div>
  </div>
  <section class="block"><div class="wrap narrow prose article-body">
{a['body']}
  </div></section>
  <section class="block" id="faq"><div class="wrap narrow">
    <h2>Frequently asked questions</h2>
    <div class="faq">
{faq}
    </div>
  </div></section>
  </article>
{enquire("Guide: " + a["h1"], "Want this handled for you?", "Sonnatt.ai builds and runs websites, chatbots and marketing for Leeds and Bradford businesses. The 15-minute walkthrough is free and there's no obligation.", f'<ul class="related" aria-label="Related pages">{links}</ul>')}
</main>
{FOOTER}
</body>
</html>
"""


def build_index():
    url = f"{SITE}/guides/"
    title = "Guides for Small Business Websites & Marketing | Sonnatt.ai"
    desc = "Plain-English guides for Leeds and Bradford small businesses on websites, chatbots, Google Business Profile and getting found online."
    ld = dump([
        {"@type": "CollectionPage", "@id": url + "#webpage", "url": url, "name": title, "description": desc, "inLanguage": "en-GB",
         "isPartOf": {"@id": f"{SITE}/#website"}, "publisher": {"@id": f"{SITE}/#organization"},
         "mainEntity": {"@type": "ItemList", "itemListElement": [
             {"@type": "ListItem", "position": i + 1, "url": f"{SITE}/guides/{a['slug']}/", "name": a["h1"]} for i, a in enumerate(ARTICLES)]}},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
            {"@type": "ListItem", "position": 2, "name": "Guides", "item": url}]},
    ])
    cards = "".join(f'<a class="card guide-card" href="/guides/{a["slug"]}/"><span class="eyebrow">{e(a["read"])}</span><h2>{e(a["h1"])}</h2><p>{e(a["desc"])}</p><span class="quiet">Read the guide →</span></a>' for a in ARTICLES)
    return head(title, desc, url, ld) + f"""{nav('/guides/')}
<main id="main">
  <div class="page-hero">
    <div class="wrap">
      <nav class="crumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li aria-current="page">Guides</li></ol></nav>
      <div class="eyebrow" style="margin-top:28px">Guides</div>
      <h1>Plain-English guides for small businesses</h1>
      <p class="lede">Straight answers on websites, chatbots and getting found on Google, written for small businesses in Leeds, Bradford and across Yorkshire.</p>
    </div>
  </div>
  <section class="block"><div class="wrap"><div class="cards guides">{cards}</div></div></section>
{enquire("Guides", "Rather have it done for you?", "One dedicated account manager builds and runs your website, chatbot and marketing. £995 setup, £995 a month, cancel with 30 days' notice.")}
</main>
{FOOTER}
</body>
</html>
"""


def main():
    for a in ARTICLES:
        os.makedirs(os.path.join("guides", a["slug"]), exist_ok=True)
        with open(os.path.join("guides", a["slug"], "index.html"), "w") as f:
            f.write(build_article(a))
        print("built guides/" + a["slug"])
    with open(os.path.join("guides", "index.html"), "w") as f:
        f.write(build_index())
    print("built guides/")


if __name__ == "__main__":
    main()
