#!/usr/bin/env python3
"""Generates static pages /apps/<slug>/ and /about/ for felix-helleckes.github.io.

Run from the repo root: python3 scripts/gen-app-pages.py
Pages are plain HTML in public/, so Google can read them without JavaScript.
"""
import html
import json
import os

BASE = "https://felix-helleckes.github.io"
PERSON_ID = BASE + "/#person"

APPS = [
    {
        "slug": "clickwheel", "name": "Clickwheel", "icon": "/projects/clickwheel.png",
        "tagline": "Offline music player with a real click wheel",
        "category": "MultimediaApplication", "os": "iOS, Android",
        "web": "https://clickwheel-app.pages.dev/",
        "stores": [("App Store", "https://apps.apple.com/app/id6809613029"),
                   ("Google Play", "https://play.google.com/store/apps/details?id=com.helleckes.clickwheel")],
        "intro": "Clickwheel turns your phone into a dedicated music player that you operate with a click wheel, the way MP3 players worked in the 2000s. It plays the files that are on your device: no account, no streaming, no ads.",
        "story": "I built Clickwheel because I missed listening to my own music without notifications, autoplay and a monthly bill. The wheel rotates by angle and clicks audibly, and you can try it right in the browser on the website before installing anything.",
        "features": ["Plays MP3, M4A/AAC, FLAC, WAV, AIFF, OGG and Opus from your device",
                     "Real click wheel: rotate to scroll, press the center to select",
                     "Works completely offline, the Android version has no internet permission",
                     "Folder view, playlists, tag manager and seven case colours",
                     "Free player, one-time purchase for the extras, no subscription"],
        "shots": ["https://clickwheel-app.pages.dev/shot-menu-en.png", "https://clickwheel-app.pages.dev/shot-musik-en.png",
                  "https://clickwheel-app.pages.dev/shot-einstellungen-en.png", "https://clickwheel-app.pages.dev/shot-farben-en.png"],
        "portrait": True,
    },
    {
        "slug": "project-pet", "name": "Project P.E.T.", "icon": "/projects/megaman-pet.png",
        "tagline": "Walking RPG with real-time grid battles",
        "category": "GameApplication", "os": "iOS, Android, Windows, macOS",
        "web": "https://mega-man-advanced-pet.vercel.app/",
        "stores": [("App Store", "https://apps.apple.com/app/id6787106134"),
                   ("Google Play", "https://play.google.com/store/apps/details?id=com.megaman.advancedpet")],
        "intro": "Project P.E.T. is a fan-made walking RPG: your real-life steps charge the Cyber-Meter, and you spend it on real-time battles on a 3×6 grid. Free on phone and desktop.",
        "story": "It started as a personal tribute to the handheld games I grew up with and turned into my most played app, with thousands of downloads, a Discord community and online duels, co-op boss raids and tournaments.",
        "features": ["Real-time grid battles against viruses, bosses and other players",
                     "Your real steps charge the energy you need to battle",
                     "Hundreds of battle chips to collect and combine",
                     "Co-op boss raids, tournaments, missions and a live online hub",
                     "Cosmetic purchases only, no pay-to-win"],
        "shots": ["https://mega-man-advanced-pet.vercel.app/assets/web/screenshots/netbattle.jpg",
                  "https://mega-man-advanced-pet.vercel.app/assets/web/screenshots/the-square.jpg",
                  "https://mega-man-advanced-pet.vercel.app/assets/web/screenshots/coop-raid.jpg"],
        "portrait": True,
    },
    {
        "slug": "dash-and-slash", "name": "Dash & Slash", "icon": "/projects/dash-and-slash.png",
        "tagline": "One-thumb neon action roguelite",
        "category": "GameApplication", "os": "iOS, Android",
        "web": "https://dash-and-slash.pages.dev/",
        "stores": [("App Store", "https://apps.apple.com/app/id6822111804"),
                   ("Google Play", "https://play.google.com/store/apps/details?id=com.helleckes.dashandslash")],
        "intro": "Pull back, aim in slow motion, release and slash through everything. Dash & Slash is a free one-thumb roguelite for Android and iPhone.",
        "story": "I wanted a real action game that works with one thumb on the train. Every sprite and every sound in Dash & Slash is generated in code, there are no bought assets.",
        "features": ["Drag and release to dash through enemies, tap to parry",
                     "Procedurally generated rooms across three zones",
                     "Three bosses with three phases each",
                     "28 relics and 8 synergies to build your run",
                     "Free with optional rewarded ads and a VIP pass"],
        "shots": ["https://dash-and-slash.pages.dev/assets/shots/en_01_dash_zielen.jpg",
                  "https://dash-and-slash.pages.dev/assets/shots/en_02_synergien.jpg",
                  "https://dash-and-slash.pages.dev/assets/shots/en_03_boss.jpg",
                  "https://dash-and-slash.pages.dev/assets/shots/en_04_parade.jpg"],
        "portrait": True,
    },
    {
        "slug": "moto-log", "name": "Moto-Log", "icon": "/projects/motolog.png",
        "tagline": "Offline service logbook for motorcycles",
        "category": "UtilitiesApplication", "os": "iOS, Android",
        "web": "https://motologbuch.netlify.app/",
        "stores": [("App Store", "https://apps.apple.com/app/id6786716897"),
                   ("Google Play", "https://play.google.com/store/apps/details?id=com.motorrad.logbuch")],
        "intro": "Moto-Log keeps track of maintenance, service intervals and running costs for your motorcycles, completely offline.",
        "story": "Moto-Log is one place for oil changes, tyres and receipts that needs no account and never sends your data anywhere. It was the first app I released in both the App Store and Google Play.",
        "features": ["Maintenance entries with date, mileage and cost",
                     "Service intervals with reminders",
                     "Running costs per bike at a glance",
                     "No account, no trackers, data stays on your phone",
                     "Available in five languages"],
        "shots": ["https://motologbuch.netlify.app/og-image.png"],
        "portrait": False,
    },
    {
        "slug": "world-clock-live", "name": "World Clock Live", "icon": "/projects/worldclocklive.png",
        "tagline": "LED world clock and live wallpaper for Windows and Mac",
        "category": "UtilitiesApplication", "os": "Windows, macOS",
        "web": "https://worldclocklive.pages.dev/",
        "stores": [("Mac App Store", "https://apps.apple.com/app/id6811101383")],
        "intro": "World Clock Live is a free desktop world clock and live LED wallpaper for Windows and Mac, built for teams that work across time zones.",
        "story": "World Clock Live puts the cities you work with directly on your desktop in 7-segment LED digits, so you can see every time zone at a glance without opening an app.",
        "features": ["LED world clock as a live desktop wallpaper",
                     "Up to 24 cities with automatic daylight-saving time",
                     "Near-zero CPU usage",
                     "Windows setup, portable app, Microsoft Store and Mac App Store"],
        "shots": ["https://worldclocklive.pages.dev/img/youtube-worldclock-thumbnail.png"],
        "portrait": False,
    },
    {
        "slug": "retrogram", "name": "Retrogram", "icon": "/projects/retrogram.png",
        "tagline": "WhatsApp and Telegram in a retro desktop messenger",
        "category": "CommunicationApplication", "os": "Windows, macOS, Linux",
        "web": "https://icq-retrogram.pages.dev/",
        "stores": [("Mac App Store", "https://apps.apple.com/app/id6824973968"),
                   ("GitHub", "https://github.com/Felix-Helleckes/ICQ")],
        "intro": "Retrogram brings WhatsApp and Telegram into a desktop messenger in the style of the early 2000s, with a separate chat window per contact and switchable skins. Free and open source.",
        "story": "Retrogram is a nostalgia project: the look and feel of a 2000s desktop messenger for the chats people use today.",
        "features": ["WhatsApp and Telegram in one app",
                     "A separate window for every conversation",
                     "Classic notification sound and three skins",
                     "Windows, macOS and Linux, open source on GitHub"],
        "shots": ["https://icq-retrogram.pages.dev/og.png"],
        "portrait": False,
    },
    {
        "slug": "eu-compliance-suite", "name": "EU Compliance Suite", "icon": "/projects/eu-compliance-suite.png",
        "tagline": "Shopify app for the 2026 EU consumer-law duties",
        "category": "BusinessApplication", "os": "Web",
        "web": "https://eu-compliance-suite.fly.dev/",
        "stores": [("Shopify App Store", "https://apps.shopify.com/eu-compliance-suite")],
        "intro": "The EU Compliance Suite covers three 2026 EU duties for Shopify stores in one app: the withdrawal button, the harmonised legal-guarantee notice and the durability label, in 24 languages.",
        "story": "The app is built so that a store owner can switch on the new EU requirements without touching theme code.",
        "features": ["Withdrawal button according to Art. 11a CRD",
                     "Harmonised legal-guarantee notice",
                     "Durability label blocks, free forever",
                     "24 EU languages, no theme code needed"],
        "shots": ["https://eu-compliance-suite.fly.dev/img/en/screenshot-cover.png",
                  "https://eu-compliance-suite.fly.dev/img/en/screenshot-form.png"],
        "portrait": False,
    },
]

CSS = """
:root{--bg:#f6f7f9;--card:#fff;--text:#16181d;--muted:#5b6270;--line:#e2e5ea;--accent:#0a66c2}
@media (prefers-color-scheme:dark){:root{--bg:#101216;--card:#181b21;--text:#eceef2;--muted:#a2a9b6;--line:#2a2f38;--accent:#5aa9ff}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--text);font:16px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif}
a{color:var(--accent)}.wrap{max-width:860px;margin:0 auto;padding:32px 16px 64px}
.crumbs{font-size:.9rem;color:var(--muted)}header.app{display:flex;gap:18px;align-items:center;margin:16px 0 8px}
header.app img{width:84px;height:84px;border-radius:20px}h1{font-size:2rem;line-height:1.2;margin:0}.sub{color:var(--muted);margin:.25rem 0 0}
.btns{display:flex;flex-wrap:wrap;gap:10px;margin:20px 0}.btn{display:inline-block;padding:10px 16px;border-radius:10px;border:1px solid var(--line);background:var(--card);text-decoration:none;font-weight:600}
.btn.primary{background:var(--accent);color:#fff;border-color:var(--accent)}
h2{font-size:1.3rem;margin:2rem 0 .5rem}ul{padding-left:1.2rem}li{margin:.3rem 0}
.shots{display:flex;gap:12px;overflow-x:auto;padding:8px 0}.shots img{height:360px;border-radius:14px;border:1px solid var(--line)}
.shots.wide img{height:auto;width:100%;max-width:820px}
.more{display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:10px}.more a{display:flex;gap:10px;align-items:center;padding:10px;border:1px solid var(--line);border-radius:12px;background:var(--card);text-decoration:none;color:var(--text)}
.more img{width:40px;height:40px;border-radius:10px}footer{margin-top:2.5rem;color:var(--muted);font-size:.9rem}
@media (max-width:520px){.shots img{height:260px}h1{font-size:1.6rem}}
"""

FOOT = """<footer><p>Made by <a href="/" rel="author">Felix Helleckes</a>, indie app developer from Cologne ·
<a href="/apps/">All apps</a> · <a href="/about/">About</a> · <a href="https://github.com/Felix-Helleckes" rel="me">GitHub</a> ·
<a href="https://www.linkedin.com/in/felix-helleckes/" rel="me">LinkedIn</a></p></footer>"""


def e(s):
    return html.escape(s, quote=True)


def head(title, desc, url, img, ld):
    return f"""<!doctype html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title><meta name="description" content="{e(desc)}"><link rel="canonical" href="{url}">
<meta name="author" content="Felix Helleckes"><link rel="icon" href="/favicon.ico">
<meta property="og:type" content="website"><meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}"><meta property="og:image" content="{img}"><meta name="twitter:card" content="summary_large_image">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
<style>{CSS}</style></head><body><div class="wrap">"""


def app_page(a):
    url = f"{BASE}/apps/{a['slug']}/"
    title = f"{a['name']} by Felix Helleckes – {a['tagline']}"
    desc = f"{a['intro']} An app by indie developer Felix Helleckes from Cologne."
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "SoftwareApplication", "name": a["name"], "url": a["web"], "applicationCategory": a["category"],
         "operatingSystem": a["os"], "description": a["intro"], "image": a["shots"][0],
         "author": {"@id": PERSON_ID}, "sameAs": [s[1] for s in a["stores"]]},
        {"@type": "Person", "@id": PERSON_ID, "name": "Felix Helleckes", "url": BASE + "/"},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Felix Helleckes", "item": BASE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Apps", "item": BASE + "/apps/"},
            {"@type": "ListItem", "position": 3, "name": a["name"], "item": url}]}]}
    out = [head(title, desc, url, a["shots"][0], ld)]
    out.append(f'<p class="crumbs"><a href="/">Felix Helleckes</a> › <a href="/apps/">Apps</a> › {e(a["name"])}</p>')
    out.append(f'<header class="app"><img src="{a["icon"]}" alt="{e(a["name"])} icon" width="84" height="84"><div>'
               f'<h1>{e(a["name"])}</h1><p class="sub">{e(a["tagline"])} · by Felix Helleckes</p></div></header>')
    out.append(f'<p>{e(a["intro"])}</p>')
    btns = [f'<a class="btn primary" href="{a["web"]}">Website</a>'] + [f'<a class="btn" href="{u}">{e(n)}</a>' for n, u in a["stores"]]
    out.append('<div class="btns">' + "".join(btns) + "</div>")
    out.append(f'<div class="shots{"" if a["portrait"] else " wide"}">' + "".join(
        f'<img src="{s}" alt="{e(a["name"])} screenshot {i+1}" loading="lazy">' for i, s in enumerate(a["shots"])) + "</div>")
    out.append("<h2>Why I built it</h2><p>" + e(a["story"]) + "</p>")
    out.append("<h2>Features</h2><ul>" + "".join(f"<li>{e(f)}</li>" for f in a["features"]) + "</ul>")
    out.append("<h2>More apps by Felix Helleckes</h2><div class=\"more\">" + "".join(
        f'<a href="/apps/{o["slug"]}/"><img src="{o["icon"]}" alt="" width="40" height="40"><span>{e(o["name"])}</span></a>'
        for o in APPS if o is not a) + "</div>")
    out.append(FOOT + "</div></body></html>")
    return "\n".join(out)


def about_page():
    url = BASE + "/about/"
    title = "About Felix Helleckes – Indie App Developer & Senior QA Engineer from Cologne"
    desc = ("Felix Helleckes is an indie app developer and senior QA automation engineer from Cologne, Germany. "
            "He builds Clickwheel, Project P.E.T., Dash & Slash, Moto-Log, World Clock Live, Retrogram and the EU Compliance Suite.")
    ld = {"@context": "https://schema.org", "@type": "ProfilePage", "url": url, "mainEntity": {
        "@type": "Person", "@id": PERSON_ID, "name": "Felix Helleckes", "url": BASE + "/",
        "image": "https://github.com/Felix-Helleckes.png", "jobTitle": ["Indie App Developer", "Senior QA Engineer"],
        "homeLocation": {"@type": "Place", "name": "Cologne, Germany"},
        "knowsAbout": ["Flutter", "Mobile apps", "Test automation", "Playwright", "Quality assurance", "Electron"],
        "sameAs": ["https://github.com/Felix-Helleckes", "https://www.linkedin.com/in/felix-helleckes/",
                   "https://apps.apple.com/de/developer/felix-helleckes/id6786716900",
                   "https://play.google.com/store/apps/developer?id=Felix+Helleckes",
                   "https://dev.to/felix-helleckes", "https://www.producthunt.com/@felix_helleckes",
                   "https://felix-helleckes.itch.io", "https://alternativeto.net/user/felix-helleckes/",
                   "https://www.youtube.com/@TheEfficientDev", "https://www.crunchbase.com/person/felix-helleckes"]}}
    out = [head(title, desc, url, "https://github.com/Felix-Helleckes.png", ld)]
    out.append('<p class="crumbs"><a href="/">Felix Helleckes</a> › About</p>')
    out.append('<header class="app"><img src="https://github.com/Felix-Helleckes.png" alt="Felix Helleckes" width="84" height="84" style="border-radius:50%">'
               '<div><h1>Felix Helleckes</h1><p class="sub">Indie app developer &amp; senior QA engineer · Cologne, Germany</p></div></header>')
    out.append("<p>I'm Felix Helleckes, a senior QA automation engineer with more than eight years of experience in web, mobile and IoT testing. "
               "In my spare time I build small, focused apps and ship them myself, from the first line of code to the store listing.</p>")
    out.append("<p>Most of my apps bring back a piece of 2000s technology in a modern form: a click-wheel music player, a walking RPG with grid battles, "
               "a retro desktop messenger and an LED world clock. I build mobile apps with Flutter and desktop apps with Electron.</p>")
    out.append("<h2>My apps</h2><div class=\"more\">" + "".join(
        f'<a href="/apps/{o["slug"]}/"><img src="{o["icon"]}" alt="" width="40" height="40"><span>{e(o["name"])}</span></a>' for o in APPS) + "</div>")
    out.append("<h2>Find me</h2><ul>"
               '<li><a href="https://github.com/Felix-Helleckes" rel="me">GitHub</a></li>'
               '<li><a href="https://www.linkedin.com/in/felix-helleckes/" rel="me">LinkedIn</a></li>'
               '<li><a href="https://apps.apple.com/de/developer/felix-helleckes/id6786716900" rel="me">App Store developer page</a></li>'
               '<li><a href="https://play.google.com/store/apps/developer?id=Felix+Helleckes" rel="me">Google Play developer page</a></li>'
               '<li><a href="https://www.youtube.com/@TheEfficientDev" rel="me">YouTube: Felix Helleckes · The Efficient Dev</a></li>'
               '<li><a href="https://dev.to/felix-helleckes" rel="me">dev.to</a> · <a href="https://www.producthunt.com/@felix_helleckes" rel="me">Product Hunt</a> · '
               '<a href="https://felix-helleckes.itch.io" rel="me">itch.io</a> · <a href="https://www.crunchbase.com/person/felix-helleckes" rel="me">Crunchbase</a></li></ul>')
    out.append(FOOT + "</div></body></html>")
    return "\n".join(out)


def main():
    root = os.path.join(os.path.dirname(__file__), "..", "public")
    for a in APPS:
        d = os.path.join(root, "apps", a["slug"])
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
            f.write(app_page(a))
    os.makedirs(os.path.join(root, "about"), exist_ok=True)
    with open(os.path.join(root, "about", "index.html"), "w", encoding="utf-8") as f:
        f.write(about_page())
    print("ok", len(APPS) + 1)


if __name__ == "__main__":
    main()
