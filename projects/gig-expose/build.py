#!/usr/bin/env python3
"""
Baut aus expose.src.html eine selbstenthaltene expose.html.

Warum: Der Adobe-Express-Import und der PDF-Export brauchen eine Datei ohne
externe Abhaengigkeiten. Schriften und Bilder werden deshalb als data:-URI
eingebettet, die beiden Stylesheets inline gesetzt.

    python3 build.py            # baut expose.html
    python3 fonts.py            # laedt die Poppins-Schnitte einmalig herunter
"""
import base64
import pathlib
import re

HERE = pathlib.Path(__file__).parent
FONT_DIR = HERE / "assets" / "fonts"

# Poppins-Schnitte, die das Layout tatsaechlich benutzt.
WEIGHTS = [300, 400, 500, 600]


def b64(path: pathlib.Path) -> str:
    return base64.b64encode(path.read_bytes()).decode()


def font_face_block() -> str:
    faces = []
    for w in WEIGHTS:
        f = FONT_DIR / f"poppins-{w}.woff2"
        if not f.exists():
            raise SystemExit(f"Fehlt: {f} — bitte zuerst 'python3 fonts.py' ausfuehren.")
        faces.append(
            "@font-face{font-family:'Poppins';font-style:normal;font-weight:%d;"
            "font-display:block;src:url(data:font/woff2;base64,%s) format('woff2')}"
            % (w, b64(f))
        )
    return "\n".join(faces)


def main() -> None:
    html = (HERE / "expose.src.html").read_text()

    # Externe Stylesheet-Verweise raus, Schrift und CSS inline rein.
    html = re.sub(r'\s*<link rel="(?:stylesheet|preconnect)"[^>]*>', "", html)
    inline = "\n".join([
        font_face_block(),
        (HERE / "brand.css").read_text(),
        (HERE / "expose.css").read_text(),
    ])
    html = html.replace("</head>", f"<style>\n{inline}\n</style>\n</head>")

    # Bilder als data:-URI. Externe Pfade blieben beim Import sonst leer.
    for src in sorted(set(re.findall(r'src="(assets/[^"]+)"', html))):
        p = HERE / src
        if not p.exists():
            raise SystemExit(f"Fehlt: {p}")
        mime = "image/png" if p.suffix == ".png" else "image/jpeg"
        html = html.replace(f'src="{src}"', f'src="data:{mime};base64,{b64(p)}"')

    out = HERE / "expose.html"
    out.write_text(html)
    print(f"{out.name}: {out.stat().st_size / 1024:.0f} KB, selbstenthalten")


if __name__ == "__main__":
    main()
