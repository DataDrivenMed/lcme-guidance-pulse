import glob, json, re, pathlib, datetime as dt

std_regex = re.compile(r"\b([1-9]\.\d)\b")  # matches 1.1 – 12.5
updates = []
for f in glob.glob("data/*.json"):
    updates += json.load(open(f))

for u in updates:
    found = std_regex.findall(u["title"])
    u["standard"] = ", ".join(sorted(set(found))) if found else "—"

out = pathlib.Path("data/updates_tagged.json")
out.write_text(json.dumps(updates, indent=2))
print("Tagged", len(updates), "items")
