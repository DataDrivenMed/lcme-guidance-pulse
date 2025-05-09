import feedparser, json, datetime as dt, pathlib
DATA = pathlib.Path("data"); DATA.mkdir(exist_ok=True)
today = dt.date.today()
feed = feedparser.parse("https://lcme.org/feed/")
rows = [{"date": entry.published, "title": entry.title, "link": entry.link}
        for entry in feed.entries]
(path := DATA / f"lcme_{today}.json").write_text(json.dumps(rows, indent=2))
print("Saved", path)
