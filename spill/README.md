# Ordbua

Ordspill på tid: man får et ord og skriver det på den andre målformen. Spillet het «Nynorsk-spillet» til 19.10.2026.

Spillet ligger publisert to steder:
- **GitHub Pages**: https://audunmathiasteachingcreations.github.io/Ordbua/ (fra 20.10.2026). Åpnes uten konto, og det er denne lenken Del-knappene i spillet deler. Kildekoden ligger i repoet https://github.com/AudunMathiasteachingcreations/Ordbua.
- **Claude-artefakt**: https://claude.ai/artifact/7iYUX62HsutPgYpndtfYmf. Privat til eieren deler den.

## Filer
- `mal.html`: selve spillet (HTML, CSS og JavaScript) uten ordliste. Poengtabell, tider, navn og lenke står i `KONFIG` øverst i skriptet, og all tekst står i `TEKST` like under. Malen har egen grunnstil (`[hidden]` og `body`-marg), så den ikke er avhengig av Claude-visningen.
- `bygg.py`: legger ordlista fra `../ordliste/ordliste.json` inn i malen og skriver `ordbua.html`. Lenken i Del-knappene er GitHub Pages-adressen hvis ikke en annen gis.
- `ordbua.html`: ferdig bygget, fullstendig nettside med `<!doctype html>`, tegnsett og viewport. Det er denne som ligger på GitHub Pages og som kan sendes til elever som fil. Fram til 20.10.2026 manglet fila dette, så den virket bare inne i Claude.

## Når ordlista endres
Ordene redigeres enklest i `../ordliste/ordliste.xlsx`; kjør da først `python3 ordliste/fra_excel.py` (se `../ordliste/README.md`). Kjør så fra mappa som har både `spill/` og `ordliste/`:

    python3 spill/bygg.py
    python3 spill/bygg.py --artefakt <midlertidig fil>
Den første lager `spill/ordbua.html`. Last den opp til `main` i repoet, så oppdaterer GitHub Pages seg selv. Den andre lager et sideutdrag uten `<!doctype>` for Artifact-verktøyet, som publiseres på nytt til artefaktlenken over.

## To retninger
- På startskjermen velger man **Bokmål → nynorsk** (standard) eller **Nynorsk → bokmål**. Valget huskes i nettleseren.
- All tekst i spillet står på målformen man øver på: nynorsk når man oversetter til nynorsk, bokmål når man oversetter til bokmål. Tekstene står i `TEKST.nn` og `TEKST.bm` i `mal.html`. Nynorsken er lest av to uavhengige kontrollører og bokmålen av én (19.10.2026).
- Etter runden kan man spille igjen eller gå tilbake til start for å bytte retning.
- På startskjermen velger man også hvilke ord man vil øve på (lagt inn 21.10.2026): **Alle ord**, eller bare **Verb**, **Substantiv** eller **Adjektiv**. Runden, eksemplene og antallet ord i faktaboksen følger valget, og valget huskes i nettleseren. Hver ordklasse har sin egen rekord i hver retning (`ordbua.rekord.<retning>.<ordklasse>`), mens «Alle ord» beholder de gamle rekordene. Resultatsiden og delingsteksten nevner ordklassen. Hvilke ordklasser man kan velge står i `ordklasseValg` i `KONFIG`; en ordklasse uten ord i ordlista blir ikke vist.
- Startskjermen har en Del-knapp (lagt inn 20.10.2026) som deler lenken til spillet med en kort tekst på målformen som er valgt. På mobil åpnes delingsmenyen, på PC kopieres teksten. Resultatsiden har sin egen Del-knapp som deler poengsummen.
- Hver retning har sin egen rekord og sine egne rangtitler (Nynorsklegende/Bokmålslegende, Ivar Aasen-nivå/Knud Knudsen-nivå osv.).

## Ytelse
- Bakgrunnshimmelen tegnes høyst 30 ganger i sekundet og med høyst 1,5 punkt per CSS-piksel (høyst 2 millioner punkter). Før 21.10.2026 ble den tegnet i full oppløsning 60 ganger i sekundet hele tiden, også på startsiden, og det er den sannsynlige grunnen til at spillet lukket seg etter en stund på nettbrett og mobil. En test med åtte runder etter hverandre viste ingen minnelekkasje.

## Regler slik de er bygget inn
- 2 minutter per runde, 10 sekunder per ord. Ordene kommer i tilfeldig rekkefølge uten gjentak, men omtrent hvert tredje ord er et ord som skrives likt på bokmål og nynorsk (`andelLike` i `KONFIG`, nå 0,35; `null` gir helt tilfeldig trekning).
- Riktig svar: poeng etter hele sekunder igjen (10: 6 000, 9: 5 000, 8: 4 200, 7: 3 500, 6: 2 900, 5: 2 400, 4: 2 000, 3: 1 600, 2: 1 300, 1: 1 000). Tabellen ble senket 18.10.2026 for at høye summer skal bli vanskeligere; før var den 8 000 til 2 000, med spillregeldokumentets 6 000, 3 700 og 2 000 ved 8, 5 og 1 sekund igjen. Svar etter rundt 2 sekunder gir nå omtrent 230 000 poeng i en runde (før omtrent 310 000).
- Feil svar eller tiden ute: 300 poeng, men det står ikke noe sted i spillet (fjernet fra startsiden og som «+300» etter feil svar 21.10.2026). Under svarfeltet vises bare fasiten i rødt (med et kryss) i 0,8 sekunder (runde-klokka går), Enter hopper videre.
- Poeng for ordet vises først etter at man har svart (som «+4 200» som flyter opp). Oversikten etter runden viser ikke poeng per ord, og kan filtreres på alle, riktige og feil.
- Merker i oversikten: ord som skrives likt får «Likt på bokmål og nynorsk». Når nynorskformen også er lov på bokmål, navngir merket ordet, for eksempel «oppleving» kan òg skrivast på bokmål. I retningen nynorsk → bokmål får ord der bokmålsordet også er riktig nynorsk merket «tenke» kan også skrives på nynorsk. Andre godkjente svar står under «Også rett» / «Også riktig».
- Godkjent fra bokmål til nynorsk: `nynorsk`, alle `godkjente_alternativer`, og bokmålsordet når `bokmalsform_godtas` er «ja».
- Godkjent fra nynorsk til bokmål: `bokmal`, alle `bokmal_alternativer`, og nynorskordet når `nynorskform_lov_pa_bokmal` er «ja». Ord med samme nynorskform deler svarene, så «kvar» godtar både «hvor» og «hver». Fasiten lenker til Bokmålsordboka.
- Store/små bokstaver og ekstra mellomrom spiller ingen rolle; aksenter må være med der de står i lista. Spillet har knapper for æ, ø og å, men ikke ê (fjernet 20.10.2026), og ordlista har ingen ord med ê.
- Et ord som er i gang når de 2 minuttene går ut, telles ikke.
- Scoren holdes mellom 0 og 500 000 (`maksScore` i `KONFIG`; `null` gir ingen tak). Taket var 200 000 til 18.10.2026. Taket vises ikke i spillet: startskjermen viser antall ord i ordlista i stedet, og resultatsiden har ingen måler.
- Personlig rekord lagres bare i nettleseren til den som spiller, én per retning. Nøklene beholdt navnet fra før navnebyttet (`nynorskspillet.rekord.v2` for nynorsk, `nynorskspillet.rekord.bokmal.v1` for bokmål), så gamle rekorder står.
