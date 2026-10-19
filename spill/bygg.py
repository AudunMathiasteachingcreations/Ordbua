"""Bygger ordbua.html (spillet Ordbua) fra mal.html og ordlista.

Bruk:  python3 bygg.py [--artefakt] [utfil] [spill-url]
Standard utfil er ordbua.html ved siden av dette skriptet, og standard spill-url er adressen på GitHub Pages.
Uten --artefakt blir fila en fullstendig nettside som virker alene, i Teams og på GitHub Pages.
Med --artefakt blir den et sideutdrag for Artifact-verktøyet til Claude, som legger til resten selv.
Ordlista leses fra ../ordliste/ordliste.json, så en oppdatert liste kommer med neste gang skriptet kjøres.
"""
import json
import sys
from pathlib import Path

HER = Path(__file__).resolve().parent
ORDLISTE = HER.parent / "ordliste" / "ordliste.json"
SPILL_URL = "https://audunmathiasteachingcreations.github.io/Ordbua/"
FELT = ["bokmal", "nynorsk", "godkjente_alternativer", "bokmal_alternativer", "ordklasse", "nynorskordboka", "bokmalsform_godtas", "nynorskform_lov_pa_bokmal"]
LISTEFELT = {"godkjente_alternativer", "bokmal_alternativer"}
# head og body er valgfrie i HTML, så nettleseren legger tittel og stil i head og resten i body
TOPP = """<!doctype html>
<html lang="nn">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
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
assert "/*ORDLISTE*/" in mal and "/*SPILL_URL*/" in mal
side = mal.replace("/*ORDLISTE*/", data_json).replace("/*SPILL_URL*/", url.replace('"', ""))
if not artefakt:
    side = TOPP + side.replace('<meta name="claude:viewport-fit-sides" content="cover">\n', "")
ut.write_text(side, encoding="utf-8")
print(f"Skrev {ut} med {len(data)} ord ({'sideutdrag for Claude' if artefakt else 'fullstendig nettside'})")
