import requests, bs4, json, datetime as dt, pathlib
DATA = pathlib.Path("data"); DATA.mkdir(exist_ok=True)
today = dt.date.today()
url = "https://www.aamc.org/professional-development/leadership-development/faculty-accreditation"
soup = bs4.BeautifulSoup(requests.get(url, timeout=30).text, "html.parser")
rows = []
for li in soup.select("li a"):
    title = li.text.strip()
    link  = "https://www.aamc.org" + li["href"] if li["href"].startswith("/") else li["href"]
    rows.append({"date": str(today), "title": title, "link": link})
(path := DATA / f"aamc_{today}.json").write_text(json.dumps(rows, indent=2))
print("Saved", path)
