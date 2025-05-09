import glob, markdown, pathlib, datetime as dt
latest = sorted(glob.glob("digests/pulse_*.md"))[-1]
html_body = markdown.markdown(open(latest).read(), extensions=["tables"])
html = f"""<!doctype html>
<html><head><meta charset="utf-8">
<link rel="stylesheet" href="https://cdn.simplecss.org/simple.min.css">
<title>LCME Guidance Pulse</title></head><body>
<h1>LCME Guidance Pulse</h1>
<p><em>Last updated {dt.datetime.utcnow():%Y-%m-%d %H:%M UTC}</em></p>
{html_body}
</body></html>"""
out = pathlib.Path("docs/index.html"); out.parent.mkdir(exist_ok=True)
out.write_text(html); print("Wrote", out)
