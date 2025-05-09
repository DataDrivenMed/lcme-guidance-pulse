# src/tag_updates.py
import glob, json, re, itertools, pathlib, datetime as dt
from dateutil import parser as dparser

# 1. gather every row from every JSON file in /data
updates = list(itertools.chain.from_iterable(
    json.load(open(p)) for p in glob.glob("data/*.json")
))

# 2. regex to capture LCME Standard numbers 1.1 – 12.9
std_regex = re.compile(r"\b([1-9]\.\d)\b")

def clean_date(raw):
    """Return YYYY-MM-DD string or original if parse fails."""
    try:
        return dparser.parse(raw).date().isoformat()
    except Exception:
        return raw

# 3. enrich each record
for u in updates:
    u["date"] = clean_date(u.get("date", str(dt.date.today())))
    search_text = u.get("title","") + " " + u.get("link","").split("/")[-1]
    found = std_regex.findall(search_text)
    u["standard"] = ", ".join(sorted(set(found))) if found else "—"

# 4. deduplicate by (title, link)
seen = set()
unique = []
for u in updates:
    key = (u["title"], u["link"])
    if key not in seen:
        unique.append(u)
        seen.add(key)

# 5. save
out = pathlib.Path("data/updates_tagged.json")
out.write_text(json.dumps(unique, indent=2))
print("Tagged", len(unique), "unique items")
