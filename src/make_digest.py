import json, datetime as dt, pathlib
today = dt.date.today().isoformat()
rows = json.load(open("data/updates_tagged.json"))
rows = sorted(rows, key=lambda r: r["date"], reverse=True)[:50]  # recent 50
lines = [f"# LCME Guidance Pulse – {today}", "",
         "| Date | Standard | Title |",
         "|------|----------|-------|"]
for r in rows:
    title_md = f"[{r['title']}]({r['link']})"
    lines.append(f"| {r['date']} | {r['standard']} | {title_md} |")
out = pathlib.Path(f"digests/pulse_{today}.md")
out.write_text("\n".join(lines))
print("Wrote", out)
