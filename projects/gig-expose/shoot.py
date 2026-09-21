"""Rendert jede .slide als PNG - fuer die visuelle Kontrolle vor dem Export."""
import sys, pathlib
from playwright.sync_api import sync_playwright

src = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "expose.src.html").resolve()
out = pathlib.Path(sys.argv[2] if len(sys.argv) > 2 else "preview"); out.mkdir(exist_ok=True)

with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/opt/pw-browsers/chromium-1194/chrome-linux/chrome", args=["--no-sandbox"])
    pg = b.new_page(viewport={"width": 900, "height": 1200}, device_scale_factor=2)
    pg.goto(src.as_uri())
    pg.wait_for_timeout(3500)
    for i, s in enumerate(pg.query_selector_all(".slide"), 1):
        s.screenshot(path=str(out / f"s{i:02d}.png"))
    print("rendered", len(pg.query_selector_all(".slide")), "slides ->", out)
    # Ueberlauf-Kontrolle: ragt Inhalt ueber den Satzspiegel hinaus?
    print(pg.evaluate("""() => document.querySelectorAll('.slide').length ?
      [...document.querySelectorAll('.pg-body')].map((e,i) => {
        const over = e.scrollHeight - e.clientHeight;
        return over > 1 ? `Seite ${i+2}: ${over}px Ueberlauf` : null;
      }).filter(Boolean) : []"""))
    b.close()
