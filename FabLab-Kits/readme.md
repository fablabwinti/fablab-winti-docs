# Etiketten für FabLab-Kits

Die Etiketten (PDFs in out/) sind passend für A4-Etikettenbogen mit 12 Stück 97 mm × 42.33 mm (Herma 5056, Avery 6123 o.ä.).

## PDFs neu generieren

1. Font [Lato](https://fonts.google.com/?query=lato) installieren.
2. `make`. Das Makefile ist gemacht für Unix-ähnliche Plattformen, vielleicht funktioniert es in Git Bash auf Windows, vielleicht nicht.
Wenn dein Inkscape nicht am selben Ort wie meines installiert ist, per Variable `INKSCAPE` angeben – z.B. `make INKSCAPE=inkscape`, falls `inkscape` im $PATH ist.

## Texte ändern

1. Entsprechendes .patch-File in Texteditor öffnen und anpassen.

## QR-Codes ändern

1. Neues Inkscape-Dokument
2. Erweiterungen ▸ Rendern ▸ Strichcode ▸ QR Code
3. Grösse 25x25, Quadratgrösse 2.3 (falls das nicht reicht: 29x29, 2.0; dann muss aber die Translation der umliegenden Gruppe angepasst werden)
4. QR-Code einmal gruppieren (für die richtige Texteinrückung)
5. SVG sichern und in Texteditor öffnen
6. `<g inkscape:label="QR Code: …` finden
7. `transform`-Attribut löschen
8. Gesamtes `<g>…</g>` mit Inhalt an der entsprechenden Stelle ins .patch-File einfügen
9. Vor jeder Zeile `+` einfügen (z.B. mit rechteckiger Auswahl, falls vom Editor unterstützt)
10. Zeilenanzahl im Hunk-Header (`@@ -304 +304,2342 @@`) anpassen

## Neue Etiketten hinzufügen

1. Ein bestehendes .patch-File kopieren und anpassen.
2. In Makefile unter `all:` das entsprechende PDF aufführen.

## Master-Layout ändern

1. In labels.svg die obere linke Etikette in der Ebene «Master» bearbeiten. Die restlichen (in der Ebene «Clones») folgen automatisch.
2. Eventuell passen dann die Patches nicht mehr und es müssen Zeilennummern oder alte Zeilen angepasst werden.
