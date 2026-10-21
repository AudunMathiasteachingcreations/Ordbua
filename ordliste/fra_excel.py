"""Leser ordliste.xlsx (arket «Ordliste») tilbake til ordliste.json og ordliste.csv.

Bruk: python3 fra_excel.py [ordliste.xlsx]
Bygg deretter spillet på nytt med spill/bygg.py. Skriptet stopper uten å skrive noe hvis arket har feil.
"""
import csv
import json
import sys
from pathlib import Path
from urllib.parse import quote

from openpyxl import load_workbook

from lag_excel import KOLONNER, ORDKLASSER

HER = Path(__file__).resolve().parent
FELT = ["bokmal", "nynorsk", "godkjente_alternativer", "bokmal_alternativer", "ordklasse", "nynorskordboka", "bokmalsform_godtas", "nynorskform_lov_pa_bokmal", "merknad", "ulikt_ord"]
LISTEFELT = {"godkjente_alternativer", "bokmal_alternativer"}


def tekst(v):
    return " ".join(str(v).split()) if v is not None else ""


def les(fil):
    ws = load_workbook(fil, data_only=True)["Ordliste"]
    overskrifter = [tekst(c.value) for c in ws[1]]
    kol = {}
    for navn, felt, _, _ in KOLONNER:
        if navn not in overskrifter:
            sys.exit(f"Fant ikke kolonnen «{navn}» i arket Ordliste. Ikke gi nytt navn til overskriftene.")
        kol[felt] = overskrifter.index(navn)

    ord_, feil, sett = [], [], {}
    for r, rad in enumerate(ws.iter_rows(min_row=2, values_only=True), 2):
        v = {felt: tekst(rad[i]) if i < len(rad) else "" for felt, i in kol.items()}
        if not any(v.values()):
            continue
        o = {}
        for felt in FELT:
            if felt in LISTEFELT:
                o[felt] = [x.strip().lower() for x in v[felt].split(";") if x.strip()]
            else:
                o[felt] = v[felt]
        o["bokmal"], o["nynorsk"], o["ordklasse"] = o["bokmal"].lower(), o["nynorsk"].lower(), o["ordklasse"].lower()
        for f in ("bokmalsform_godtas", "nynorskform_lov_pa_bokmal", "ulikt_ord"):
            o[f] = o[f].lower() or ("ja" if o["bokmal"] == o["nynorsk"] and f != "ulikt_ord" else "nei")  # tomt: ja for like ord, ellers nei
            if o[f] not in ("ja", "nei"):
                feil.append(f"Rad {r}: «{v[f]}» skal være ja eller nei.")
        if not o["bokmal"] or not o["nynorsk"]:
            feil.append(f"Rad {r}: både Bokmål og Nynorsk må fylles ut.")
        if o["ordklasse"] not in ORDKLASSER:
            feil.append(f"Rad {r}: ukjent ordklasse «{v['ordklasse']}».")
        if not o["nynorskordboka"] and o["nynorsk"]:
            o["nynorskordboka"] = "https://ordbokene.no/nno/nn/" + quote(o["nynorsk"])
        nokkel = (o["bokmal"], o["ordklasse"])
        if nokkel in sett:
            feil.append(f"Rad {r}: «{o['bokmal']}» ({o['ordklasse']}) står også i rad {sett[nokkel]}.")
        sett[nokkel] = r
        ord_.append(o)
    return ord_, feil


def skriv(ord_):
    (HER / "ordliste.json").write_text(json.dumps(ord_, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    with open(HER / "ordliste.csv", "w", encoding="utf-8", newline="") as f:
        wr = csv.writer(f)
        wr.writerow(FELT)
        for o in ord_:
            wr.writerow([";".join(o[k]) if k in LISTEFELT else o[k] for k in FELT])


if __name__ == "__main__":
    fil = Path(sys.argv[1]) if len(sys.argv) > 1 else HER / "ordliste.xlsx"
    ord_, feil = les(fil)
    if feil:
        print("Arket har feil, så ingenting ble skrevet:")
        print("\n".join(feil))
        sys.exit(1)
    skriv(ord_)
    like = sum(1 for o in ord_ if o["bokmal"] == o["nynorsk"])
    print(f"Skrev ordliste.json og ordliste.csv med {len(ord_)} ord ({like} like). Bygg spillet på nytt med spill/bygg.py.")
