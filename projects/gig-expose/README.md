# Projektexposé — Growth Investment Group

A4-Exposé-Vorlage im Corporate Design der Growth Investment Group.
Struktur nach dem Vorbild eines 11-seitigen Immobilien-Projektexposés,
Gestaltung vollständig auf das GIG-CD umgestellt.

## Dateien

| Datei | Zweck |
|---|---|
| `brand.css` | Marken-Tokens (Farbe, Schrift, Raster). Einzige Wahrheitsquelle. |
| `expose.css` | A4-Master: Seitenmöbel, Typografie, Komponenten. |
| `expose.src.html` | Arbeitsdatei — hier werden Inhalte eingesetzt. |
| `expose.html` | Erzeugt von `build.py`; selbstenthalten, für Export/Import. |
| `fonts.py` | Lädt die Poppins-Schnitte einmalig nach `assets/fonts/`. |
| `build.py` | Bettet Schriften, Bilder und CSS ein → `expose.html`. |
| `shoot.py` | Rendert jede Seite als PNG und meldet Satzspiegel-Überläufe. |

## Ablauf

    python3 fonts.py     # einmalig
    python3 build.py     # nach jeder Änderung an .src.html / *.css
    python3 shoot.py expose.html preview

`expose.html` geht anschließend nach Adobe Express (Import) oder in den
PDF-Druck.

## Farbquelle

Die Werte in `brand.css` stammen aus den globalen Theme-Variablen von
growth-investment-group.de, nicht aus einer Bildschirmmessung:

- `theme_css_vars.css` → `--porto-primary-color: #0f5969`
- Elementor-Kit `post-1844.css` → `--e-global-color-primary/secondary/tertiary`

Nicht verwendet: `#1863DC` (Cookie-Banner-Plugin) und `#E04622`
(Porto-Theme-Demo) — beides sind keine Markenfarben.

Gold `#EEAB26` ist der deklarierte Sekundärton der Marke, in diesem Exposé
aber bewusst nicht eingesetzt.

## Platzhalter

Alles in `⟨spitzen Klammern⟩` ist zu ersetzen. `shoot.py` meldet, wenn Text
nach dem Einsetzen über den Satzspiegel hinausläuft.
