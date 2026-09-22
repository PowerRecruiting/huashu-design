# Frankfurt Airport Hotel HAT 3 — Projektexposé

10-seitiges A4-Exposé im Corporate Design der Growth Investment Group.
Stand: Entwurf V1, 22.09.2026. **Nicht zur Weitergabe an Anleger.**

## Dateien

| Datei | Zweck |
|---|---|
| `brand.css` | Marken-Tokens, gespiegelt aus dem GIG-Design-System. |
| `expose.css` | A4-Master: Seitenmöbel, Typografie, Komponenten. |
| `expose.src.html` | Arbeitsdatei. Hier wird inhaltlich geändert. |
| `expose.html` | Erzeugt von `build.py`; selbstenthalten, für den Export. |
| `fonts.py` | Lädt Jost und Lato nach `assets/fonts/`. |
| `build.py` | Bettet Schriften, Bilder und CSS ein. |
| `shoot.py` | Rendert jede Seite als PNG, meldet Satzspiegel-Überläufe. |

    python3 fonts.py                       # einmalig
    python3 build.py                       # nach jeder Änderung
    python3 shoot.py expose.html preview   # Sichtprüfung

## Quelle der Gestaltung

Farben, Schriften und Formmotive stammen aus dem GIG-Design-System
(Drive-Ordner `tokens/`, `guidelines/`, `assets/`), nicht aus einer
Bildschirmmessung der Website:

- Kern-Teal `#095666`, aus der Logodatei gemessen
- Jost als Display-Schrift, Lato für den Fließtext
- Teal-Banner mit 45°-Notch an der auslaufenden Kante
- Haarlinien-Klammer um Display-Titel
- Teal-Schleier über jeder vollflächigen Abbildung
- Navy und Blau des Assetprofile-Decks bleiben außen vor: laut System nie
  mit Teal im selben Layout

## Was der Adobe-Express-Import verträgt

Am Rückgabe-HzHTML geprüft:

| Konstrukt | Ergebnis |
|---|---|
| CSS `clip-path: polygon(...)` | wird zu `shape-type="path"` — Vektor, editierbar |
| `<div>`, `<table>`, Text | native Express-Objekte |
| `<img>` mit `data:`-URI | landet im Express-Blobstore |
| Inline `<svg>` | **wird verworfen** |
| `::before` / `::after` | **wird verworfen** |

Deshalb: Strich-Aufzählungen als echte `<span class="dash">`, Kapitalstruktur
als gestapelter Balken aus `<div>`, Pfeile als Textzeichen. Kein Inline-SVG
im Dokument.

Jost wird beim Import durch Futura PT Web ersetzt. Das ist unkritisch — das
Design-System nennt Futura selbst als Zielfamilie, Jost steht dort nur
stellvertretend.

## Inhaltliche Grundlage

Wo das Briefing und das Dokument „HAT3 Projektexposé – Nützliche Infos je
Kapitel" sich widersprechen, gilt der Abgleich. Offene Punkte sind im
Dokument sichtbar als `[…]` gesetzt (Klasse `.tbd`) und müssen vor
Drucklegung ersetzt oder gestrichen werden.
