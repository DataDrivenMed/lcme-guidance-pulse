import json, datetime as dt, pathlib

# 1.  Prepare paths & create folder
today = dt.date.today().isoformat()
pathlib.Path("digests").mkdir(exist_ok=True)          # makes /digests if absent
out_path = pathlib.Path(f"digests/pulse_{today}.md")  # file we’ll write

# 2.  Load the tagged updates
rows = json.load(open("data/updates_tagged.json"))

# 3.  Build the Markdown lines
rows = sorted(rows, key=lambda r: r["date"], reverse=True)[:50]
lines = [f"# LCME Guidance Pulse – {today}", "",
         "| Date | Standard | Title |",
         "|------|----------|-------|"]
for r in rows:
    title_md = f"[{r['title']}]({r['link']})"
    lines.append(f"| {r['date']} | {r['standard']} | {title_md} |")

# 4.  Write the file
out_path.write_text("\n".join(lines))
print("Wrote", out_path)

