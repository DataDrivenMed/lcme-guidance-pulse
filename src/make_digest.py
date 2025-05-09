import json, datetime as dt, pathlib

today = dt.date.today().isoformat()
# NEW LINE ▼
pathlib.Path("digests").mkdir(exist_ok=True)   # ensures folder exists

rows = json.load(open("data/updates_tagged.json"))
...
out = pathlib.Path(f"digests/pulse_{today}.md")
out.write_text("\n".join(lines))
print("Wrote", out)

