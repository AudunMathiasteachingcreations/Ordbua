"""Bygger ordbua.html (spillet Ordbua) fra mal.html og ordlista.

Bruk:  python3 bygg.py [--artefakt] [utfil] [spill-url]
Standard utfil er ordbua.html ved siden av dette skriptet, og standard spill-url er adressen på GitHub Pages.
Uten --artefakt blir fila en fullstendig nettside som virker alene, i Teams og på GitHub Pages,
og som kan installeres som app når den ligger på GitHub Pages sammen med manifest.webmanifest, sw.js og ikon/ i repoets rot.
Med --artefakt blir den et sideutdrag for Artifact-verktøyet til Claude, som legger til resten selv.
Ordlista leses fra ../ordliste/ordliste.json, så en oppdatert liste kommer med neste gang skriptet kjøres.
"""
import json
import sys
from pathlib import Path
from urllib.parse import quote

HER = Path(__file__).resolve().parent
ORDLISTE = HER.parent / "ordliste" / "ordliste.json"
SPILL_URL = "https://audunmathiasteachingcreations.github.io/Ordbua/"
FELT = ["bokmal", "nynorsk", "godkjente_alternativer", "bokmal_alternativer", "ordklasse", "nynorskordboka", "bokmalsform_godtas", "nynorskform_lov_pa_bokmal", "ulikt_ord"]
LISTEFELT = {"godkjente_alternativer", "bokmal_alternativer"}
# Fanen i nettleseren får appikonet. Det ligger inne i fila, så det virker også når fila er lastet ned.
IKON = ("<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><rect width='32' height='32' rx='7' fill='#2a72b8'/>"
        "<path d='M0 24.8H32V25A7 7 0 0 1 25 32H7A7 7 0 0 1 0 25Z' fill='#3f739d'/>"
        "<g transform='translate(16 16) scale(.8) translate(-16 -16)'><circle cx='22' cy='10' r='5' fill='#f4b53f'/>"
        "<path d='M1 27L10 12L15 19L20 13L31 27Z' fill='#f7fafd'/></g></svg>")
# head og body er valgfrie i HTML, så nettleseren legger tittel og stil i head og resten i body.
# Fargen og navnet brukes når spillet er installert som app; manifest og app-ikon legger spillet selv til på GitHub Pages.
TOPP = f"""<!doctype html>
<html lang="nn">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#2a72b8">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Ordbua">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<link rel="icon" href="data:image/svg+xml,{quote(IKON, safe=" '=/:.,-()")}">
"""

argv = sys.argv[1:]
artefakt = "--artefakt" in argv
argv = [a for a in argv if a != "--artefakt"]
ut = Path(argv[0]) if len(argv) > 0 else HER / "ordbua.html"
url = argv[1] if len(argv) > 1 else SPILL_URL

ord_ = json.loads(ORDLISTE.read_text(encoding="utf-8"))
for o in ord_:
    mangler = [f for f in ("bokmal", "nynorsk") if not str(o.get(f, "")).strip()]
    if mangler:
        sys.exit(f"Ordet {o} mangler {mangler}")
data = [{f: o.get(f, [] if f in LISTEFELT else "") for f in FELT} for o in ord_]
data_json = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")

mal = (HER / "mal.html").read_text(encoding="utf-8")
assert "/*ORDLISTE*/" in mal and "/*SPILL_URL*/" in mal and "/*APP*/false" in mal
side = mal.replace("/*ORDLISTE*/", data_json).replace("/*SPILL_URL*/", url.replace('"', ""))
if not artefakt:
    side = TOPP + side.replace('<meta name="claude:viewport-fit-sides" content="cover">\n', "").replace("/*APP*/false", "true")
ut.write_text(side, encoding="utf-8")
print(f"Skrev {ut} med {len(data)} ord ({'sideutdrag for Claude' if artefakt else 'fullstendig nettside'})")
