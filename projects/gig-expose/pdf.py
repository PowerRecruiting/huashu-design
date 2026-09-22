#!/usr/bin/env python3
"""Erzeugt aus expose.html ein druckfertiges A4-PDF (randlos, 10 Seiten)."""
import pathlib, sys
from playwright.sync_api import sync_playwright

CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
src = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "expose.html").resolve()
out = pathlib.Path(sys.argv[2] if len(sys.argv) > 2 else "HAT3-Projektexpose-Entwurf-V1.pdf")

with sync_playwright() as p:
    b = p.chromium.launch(executable_path=CHROME, args=["--no-sandbox"])
    pg = b.new_page()
    pg.goto(src.as_uri())
    pg.wait_for_timeout(2500)
    pg.emulate_media(media="print")
    pg.pdf(path=str(out), prefer_css_page_size=True, print_background=True,
           margin={"top": "0", "right": "0", "bottom": "0", "left": "0"})
    b.close()
print(f"{out}  {out.stat().st_size // 1024} KB")
