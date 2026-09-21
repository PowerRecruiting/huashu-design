#!/usr/bin/env python3
"""Laedt die Poppins-Schnitte (latin) einmalig nach assets/fonts/."""
import pathlib, re, subprocess, sys

UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120 Safari/537.36")
OUT = pathlib.Path(__file__).parent / "assets" / "fonts"; OUT.mkdir(parents=True, exist_ok=True)

css = subprocess.run(
    ["curl", "-sS", "--max-time", "60", "-A", UA,
     "https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap"],
    capture_output=True, text=True, check=True).stdout

# Nur den latin-Block je Schnitt - deckt Deutsch inkl. Umlaute, EUR und Anfuehrung ab.
blocks = re.findall(r"/\* latin \*/\s*@font-face \{(.*?)\}", css, re.S)
for b in blocks:
    w = re.search(r"font-weight:\s*(\d+)", b).group(1)
    url = re.search(r"url\((https://[^)]+\.woff2)\)", b).group(1)
    dst = OUT / f"poppins-{w}.woff2"
    subprocess.run(["curl", "-sS", "--max-time", "60", "-A", UA, url, "-o", str(dst)], check=True)
    print(f"{dst.name}  {dst.stat().st_size // 1024} KB")
if not blocks:
    sys.exit("Keine latin-Bloecke in der Google-Fonts-Antwort gefunden.")
