#!/usr/bin/env python3
"""Buduje grywalna strone index.html ze zrodla src/spektrum.html.

src/spektrum.html to tresc strony bez <!doctype>, <head> i <body> — w takiej
postaci trafia na claude.ai, ktore samo dokleja wlasny szkielet i reset CSS.
Ten skrypt dokleja rownowazny szkielet, zeby ta sama gra dzialala takze
z dysku i z GitHub Pages.

Uzycie: python3 build.py
"""
import pathlib

ROOT = pathlib.Path(__file__).parent
SRC = ROOT / "src" / "spektrum.html"
OUT = ROOT / "index.html"

SKELETON = """<!doctype html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<!-- Plik generowany przez build.py — nie edytuj recznie. Zrodlo: src/spektrum.html -->
<style>
:root{color-scheme:light; padding-top:env(safe-area-inset-top,0px); padding-bottom:env(safe-area-inset-bottom,0px)}
body{margin:0; font:14px system-ui,-apple-system,sans-serif}
img{max-width:100%}
[hidden]{display:none!important}
</style>
"""

OUT.write_text(SKELETON + SRC.read_text(encoding="utf-8") + "\n</html>\n", encoding="utf-8")
print(f"zbudowano {OUT} ({OUT.stat().st_size} bajtow) ze zrodla {SRC.name}")
