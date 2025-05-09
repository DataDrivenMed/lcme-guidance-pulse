import requests, bs4, pathlib, json, datetime as dt

DATA = pathlib.Path("data"); DATA.mkdir(exist_ok=True)
today = dt.date.today()

url  = "https://lcme.org/publications/"
html = requests.get(url, timeout=30).text
soup = bs4.BeautifulSoup(html, "html.parser")

items = []
for a in soup.select('a[href$=".pdf"]'):
    link  = a["href"]
    title = a.text.strip() or link.split("/")[-1]
    items.append({
        "date": str(today),
        "source": "LCME",
        "type": "Guideline PDF",
        "title": title,
        "link": link,
        "filetype": "pdf"
    })

out = DATA / f"lcme_pdf_{today}.json"
out.write_text(json.dumps(items, indent=2))
print("Saved", out, len(items), "PDF links")
