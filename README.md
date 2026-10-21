# Ordbua

Et ordspill på tid for bokmål og nynorsk. Spilleren velger retning, får et ord og skal skrive det på den andre målformen:

- **Bokmål → nynorsk**: man får et ord på bokmål og skriver det på nynorsk. All tekst i spillet står på nynorsk.
- **Nynorsk → bokmål**: man får et ord på nynorsk og skriver det på bokmål. All tekst i spillet står på bokmål.

Spilleren kan øve på alle ordene, eller bare på verb, substantiv eller adjektiv. En runde varer i 2 minutter, og hvert ord har 10 sekunder. Raske riktige svar gir mest poeng. Etter runden kan spilleren se alle svarene med fasit og lenke til ordboka, filtrere på riktige og feil, og dele poengsummen.

## Spille
Spillet ligger på **https://audunmathiasteachingcreations.github.io/Ordbua/** og åpnes i alle nettlesere, uten konto.

Spillet kan også installeres som app fra den samme lenken, med eget ikon og spill uten nett:
- **iPhone og iPad**: åpne lenken i Safari, trykk på Del-knappen (eventuelt under •••) og velg «Legg til på Hjem-skjerm».
- **Android**: trykk på «Installer appen» på startskjermen i spillet, eller velg ⋮ › «Installer og opprett snarvei» › «Installer» i Chrome.
- **PC og Chromebook**: trykk på «Installer appen» på startskjermen i spillet, eller på installeringsikonet til høyre i adressefeltet i Chrome eller Edge.

Man kan også laste ned `spill/ordbua.html` og åpne den direkte i en nettleser. Fila er selvstendig og trenger ikke server. Uten internett brukes standardskrifter i stedet for spillets egne.

## Innhold
- `spill/`: malen (`mal.html`), byggeskriptet (`bygg.py`) og den ferdige siden (`ordbua.html`). Se `spill/README.md` for regler og innstillinger.
- `index.html`: forsiden på GitHub Pages, som sender videre til `spill/ordbua.html`. `.nojekyll` gjør at GitHub Pages viser filene slik de er.
- `manifest.webmanifest`, `sw.js` og `ikon/`: det som gjør spillet til en app som kan installeres og spilles uten nett. Se «Som app» i `spill/README.md`.
- `ordliste/`: 515 ordpar bokmål–nynorsk i JSON og CSV, med godkjente svar begge veier, kontrollert mot Nynorskordboka, Bokmålsordboka og dinordbok.no. Se `ordliste/README.md`.

## Bygge på nytt etter endringer
Kjør fra denne mappa:

    python3 spill/bygg.py

Skriptet legger `ordliste/ordliste.json` inn i `spill/mal.html` og skriver den ferdige siden `spill/ordbua.html`, med adressen på GitHub Pages i Del-knappene. Når endringen er lastet opp til `main`, oppdaterer GitHub Pages spillet av seg selv etter et par minutter.
