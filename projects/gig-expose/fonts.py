#!/usr/bin/env python3
"""Laedt Jost und Lato (latin, statisch) nach assets/fonts/."""
import hashlib, pathlib, re, subprocess, sys

# Bewusst eine aeltere Browserkennung: Google Fonts liefert modernen Browsern
# eine Variable Font aus. Chromium bettet die beim PDF-Druck als Type3 ein -
# nicht durchsuchbar und schlecht im Druck. Mit dieser Kennung kommen je
# Schnitt getrennte statische Dateien.
UA = ("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36")
OUT = pathlib.Path(__file__).parent / "assets" / "fonts"; OUT.mkdir(parents=True, exist_ok=True)

SPEC = {"Jost": "300;400;500;600", "Lato": "300;400;700"}

seen = {}
for fam, weights in SPEC.items():
    url = f"https://fonts.googleapis.com/css2?family={fam}:wght@{weights}&display=swap"
    css = subprocess.run(["curl", "-sS", "--max-time", "60", "-A", UA, url],
                         capture_output=True, text=True, check=True).stdout
    # Nur der latin-Block je Schnitt - deckt Deutsch, EUR, Anfuehrung und Pfeile ab.
    blocks = re.findall(r"/\* latin \*/\s*@font-face \{(.*?)\}", css, re.S)
    if not blocks:
        sys.exit(f"Keine latin-Bloecke fuer {fam} gefunden.")
    for b in blocks:
        w = re.search(r"font-weight:\s*(\d+)", b).group(1)
        src = re.search(r"url\((https://[^)]+\.woff2)\)", b).group(1)
        dst = OUT / f"{fam.lower()}-{w}.woff2"
        subprocess.run(["curl", "-sS", "--max-time", "60", "-A", UA, src, "-o", str(dst)], check=True)
        digest = hashlib.md5(dst.read_bytes()).hexdigest()
        seen.setdefault(fam, set()).add(digest)
        print(f"{dst.name}  {dst.stat().st_size // 1024} KB")

# Gleiche Pruefsumme ueber alle Schnitte = wieder eine Variable Font.
for fam, digests in seen.items():
    if len(digests) == 1 and len(SPEC[fam].split(";")) > 1:
        sys.exit(f"{fam}: alle Schnitte identisch - es kam eine Variable Font zurueck.")
