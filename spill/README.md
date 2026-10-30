# Ordbua

Ordspill på tid: man får et ord og skriver det på den andre målformen. Spillet het «Nynorsk-spillet» til 19.10.2026.

Spillet ligger publisert to steder:
- **GitHub Pages**: https://audunmathiasteachingcreations.github.io/Ordbua/ (fra 20.10.2026). Åpnes uten konto, og det er denne lenken Del-knappene i spillet deler. Herfra kan spillet også installeres som app (se «Som app» under). Kildekoden ligger i repoet https://github.com/AudunMathiasteachingcreations/Ordbua.
- **Claude-artefakt**: https://claude.ai/artifact/7iYUX62HsutPgYpndtfYmf. Privat til eieren deler den.

## Filer
- `mal.html`: selve spillet (HTML, CSS og JavaScript) uten ordliste. Poengtabell, tider, navn og lenke står i `KONFIG` øverst i skriptet, og all tekst står i `TEKST` like under. Malen har egen grunnstil (`[hidden]` og `body`-marg), så den ikke er avhengig av Claude-visningen.
- `bygg.py`: legger ordlista fra `../ordliste/ordliste.json` inn i malen og skriver `ordbua.html`. Lenken i Del-knappene er GitHub Pages-adressen hvis ikke en annen gis. I den fullstendige nettsiden legger skriptet også til fanikon, appfarge og appnavn, og slår på app-delen (`app` i `KONFIG`).
- `laerar-mal.html`: lærersiden (lagt inn 25.10.2026), uten ordliste. Se «Lærerversjon uten Feide» under.
- `laerar.html`: lærersiden ferdig bygget av `bygg.py`. Legges i repoet ved siden av spillet.
- `ordbua.html`: ferdig bygget, fullstendig nettside med `<!doctype html>`, tegnsett og viewport. Det er denne som ligger på GitHub Pages og som kan sendes til elever som fil. Fram til 20.10.2026 manglet fila dette, så den virket bare inne i Claude.

## Når ordlista endres
Ordene redigeres enklest i `../ordliste/ordliste.xlsx`; kjør da først `python3 ordliste/fra_excel.py` (se `../ordliste/README.md`). Kjør så fra mappa som har både `spill/` og `ordliste/`:

    python3 spill/bygg.py
    python3 spill/bygg.py --artefakt <midlertidig fil>
    python3 spill/bygg.py --laerar --artefakt <midlertidig fil>
Den første lager `spill/ordbua.html` og `spill/laerar.html`. Last den opp til `main` i repoet, så oppdaterer GitHub Pages seg selv. Den andre lager et sideutdrag uten `<!doctype>` for Artifact-verktøyet, som publiseres på nytt til artefaktlenken over.

## To retninger
- På startskjermen velger man **Bokmål → nynorsk** (standard) eller **Nynorsk → bokmål**. Valget huskes i nettleseren.
- All tekst i spillet står på målformen man øver på: nynorsk når man oversetter til nynorsk, bokmål når man oversetter til bokmål. Tekstene står i `TEKST.nn` og `TEKST.bm` i `mal.html`. Nynorsken er lest av to uavhengige kontrollører og bokmålen av én (19.10.2026).
- Etter runden kan man spille igjen eller gå tilbake til start for å bytte retning.
- På startskjermen velger man også hvilke ord man vil øve på (lagt inn 21.10.2026): **Alle ord**, eller bare **Verb**, **Substantiv** eller **Adjektiv**. Runden, eksemplene og antallet ord i faktaboksen følger valget, og valget huskes i nettleseren. Hver ordklasse har sin egen rekord i hver retning (`ordbua.rekord.<retning>.<ordklasse>`), mens «Alle ord» beholder de gamle rekordene. Resultatsiden og delingsteksten nevner ordklassen. Hvilke ordklasser man kan velge står i `ordklasseValg` i `KONFIG`; en ordklasse uten ord i ordlista blir ikke vist.
- Ved siden av ordklassene er det et femte valg, **Ulike ord** (lagt inn 21.10.2026): ordene som ikke kan oversettes direkte, fordi nynorsk bruker et annet ord eller en annen ending (f.eks. benytte → nytte, kjærlighet → kjærleik). Det er ordene med «ja» i `ulikt_ord` i ordlista (41 ord, se `../ordliste/README.md`). I `ordklasseValg` heter valget `"ulike"`, og navnet og forklaringen (vises når man holder musa over knappen) står i `TEKST.nn.namn`, `TEKST.bm.namn` og `ulikeForklaring`. Det har egen rekord som de andre valgene (`ordbua.rekord.<retning>.ulike`).
- Startskjermen har en Del-knapp (lagt inn 20.10.2026) som deler lenken til spillet med en kort tekst på målformen som er valgt. På mobil åpnes delingsmenyen, på PC kopieres teksten. Resultatsiden har sin egen Del-knapp som deler poengsummen.
- Nederst i spillet står en opphavsrettsmerknad med lenke til vilkårene i `LICENSE` (lagt inn 30.10.2026). Teksten står i `opphav` og `vilkaar` i `TEKST.nn` og `TEKST.bm`. Lærersiden har sin egen merknad nederst i `laerar-mal.html`.
- Hver retning har sin egen rekord og sine egne rangtitler (Nynorsklegende/Bokmålslegende, Ivar Aasen-nivå/Knud Knudsen-nivå osv.).

## Som app
Fra 21.10.2026 kan spillet installeres som app fra GitHub Pages, med eget ikon, uten nettleserlinjer og med spill uten nett. Det bruker den samme adressen og trenger ikke noe eget domene.
- Appfilene ligger i repoets rot, én mappe over `spill/`: `manifest.webmanifest` (navn, ikon, farger og hvilken side appen åpner), `sw.js` (lagrer spillet for bruk uten nett) og `ikon/` (PNG-ikonene og SVG-kildene deres).
- Spillet legger til manifestet og app-ikonet og starter `sw.js` bare når det er åpnet fra en nettadresse, ikke er bygget inn i en annen side (iframe) og `app` i `KONFIG` er sann, altså på GitHub Pages. Som nedlastet fil, i Claude-artefakten og innebygd i for eksempel Google Sites er app-delen av.
- `sw.js` henter spillet fra nettet først, så endringer når elevene neste gang de åpner det. Er nettet borte, treigere enn 3 sekunder eller svarer med en feil, brukes den lagrede kopien. Skriftene fra Google Fonts lagres også, så spillet ser likt ut uten nett.
- Endre `VERSJON` øverst i `sw.js` når ikonene eller fillista der endres, så appen lagrer dem på nytt. Nye utgaver av spillet trenger ikke det.
- Alle GitHub Pages-sidene på kontoen deler ett lager i nettleseren. `sw.js` sletter derfor bare lagre som begynner med `ordbua-`, og en annen app på kontoen bør på samme måte bruke sitt eget prefiks.
- På startskjermen kommer knappen **Installer appen** ved siden av Del-knappen når nettleseren kan installere spillet (Chrome og Edge på PC, Chromebook og Android). På iPhone og iPad viser knappen en kort forklaring i stedet. Knappen vises ikke når spillet allerede kjører som app.

Slik installerer man:
- **iPhone og iPad**: åpne lenken i Safari, trykk på Del-knappen (eventuelt under •••) og velg «Legg til på Hjem-skjerm».
- **Android**: trykk på «Installer appen» på startskjermen i spillet, eller velg ⋮ › «Installer og opprett snarvei» › «Installer» i Chrome (eldre Chrome-versjoner kaller det «Installer app» eller «Legg til på startskjermen»).
- **PC og Chromebook**: trykk på «Installer appen» på startskjermen i spillet, eller på installeringsikonet til høyre i adressefeltet i Chrome eller Edge.
- **Mac med Safari**: Arkiv-menyen › «Legg til i Dock».

Appen må åpnes med nett én gang før den virker uten nett.

## Lærerversjon uten Feide (fra 25.10.2026)

Første del av lærerversjonen, bygget så langt det går uten Feide, server og avtaler. Planen for hele lærerversjonen står i `../kommersialisering/02-feide-teknisk-plan.md`.

**Adresse:** https://audunmathiasteachingcreations.github.io/Ordbua/laerer/ (sender videre til `spill/laerar.html`). Siden er åpen for alle, men hver lærer ser bare det som er lagret i sin egen nettleser.

**Slik virker det**
1. Læreren åpner `laerar.html`, lager en klasse (bare et navn, f.eks. 8A) og en oppgave: tittel, retning, ordutvalg (alle ord, en ordklasse, ulike ord eller ord læreren krysser av selv) og eventuelt frist.
2. Lærersiden lager en lenke til spillet som slutter på `#oppgave=...`. Læreren deler den i Teams, Classroom e.l.
3. Eleven åpner lenka. Spillet viser oppgaven øverst, låser retning og ordutvalg og spiller vanlige runder (samme regler og poeng). Hver oppgave har sin egen rekord (`ordbua.rekord.oppgave.<id>`). «Spel utan oppgåva» tar eleven til det vanlige spillet.
4. Etter runden skriver eleven navnet sitt og trykker «Lag innleveringskode». Koden (rundt 300 tegn) kopieres, og eleven limer den inn der læreren vil, f.eks. som innlevering i Teams.
5. Læreren limer inn kodene på lærersiden (mange på en gang, også med annen tekst rundt). Siden viser elevene med beste runde, alle rundene, og «ord klassen strever med». Runder og ordstatistikk kan lastes ned som CSV for Excel.

«Prøv selv» på lærersiden legger `&prov` til lenka, og da viser spillet en lenke tilbake til `laerar.html`. Bekreftelser bruker en boks på siden, fordi `confirm()` og `prompt()` ikke virker i Teams-faner og i Claude. En testutgave med begge sidene ligger som Claude-artefakt: https://claude.ai/artifact/PqrusCzqhMG9As8gBzeHAQ (der virker ikke nedlasting av CSV og sikkerhetskopi).

**Egne ord fra læreren** (fra 26.10.2026): under «Velg ord selv» kan læreren også skrive eller lime inn egne ord og bøyningsformer, ett per linje: `bokmål ; nynorsk ; andre riktige svar ; merknad` (eller kolonner fra Excel). Andre riktige svar gjelder språket eleven skriver på, og merknaden (f.eks. «verb, preteritum») vises for eleven der ordklassen ellers står. Ordene står i lenka (`e` i oppgaven), så de virker uten server. I innleveringskoden heter de `~0`, `~1` osv. Lærersiden lenker hvert nynorskord til Nynorskordboka, så læreren kan sjekke det.

**Hvor dataene er**
- Oppgaven står i selve lenka. Delen etter `#` sendes ikke til GitHub, så ingen server ser den.
- Klasser, oppgaver og innleveringer lagres bare i nettleseren til læreren (`localStorage`, nøkkel `ordbua.laerer.v1`). Siden har knapper for sikkerhetskopi (JSON), henting fra sikkerhetskopi (slås sammen med det som finnes) og sletting. Etter 1. august minner siden om å slette innleveringer fra forrige skoleår.
- Koden har navnet eleven skriver, tidspunkt, retning, ordutvalg, poeng og for hvert ord: hvilket ord, rett/feil og sekunder igjen. Det eleven skrev (fritekst) er ikke med, som i planen.
- Eleven husker navnet sitt i egen nettleser (`ordbua.namn`).

**Kodeformat:** `ORDBUA.<versjon>.<data>.<sjekksum>`. Data er JSON i base64url, komprimert med `deflate-raw` (versjon 2) eller ukomprimert (versjon 1) i nettlesere uten `CompressionStream`. Sjekksummen (FNV-1a) fanger opp koder som er klippet av. Lærersiden regner poengene ut fra svarene på nytt og merker runden «sjekk» hvis de ikke stemmer. Det hindrer ikke en elev som vil jukse og kan programmere; først serverversjonen gjør det. Poengtabellen i `laerar-mal.html` (`KONFIG`) må derfor være lik den i `mal.html`.

**Ord i lenker og koder** pekes til med bokmålsordet (alle 542 er unike nå), eller `bokmål|nynorsk` hvis samme bokmålsord kommer flere ganger. Fjernes et ord fra ordlista, hopper spillet over det i oppgaver med egne ord, og lærersiden viser det som «ikke i ordlista lenger».

**Plugger for Feide** (merket `PLUGG FOR FEIDE` i koden):
- `Lagring` i `laerar-mal.html`: bytt `last()`/`lagre()` med kall mot API-et. Klasser skal da komme fra Feides Groups API i stedet for å lages for hånd.
- `Innlogging` i `laerar-mal.html` og knappen «Logg inn med Feide» øverst, som blir lenke til `/auth/feide/login`.
- `Levering.lever()` i `mal.html`: send runden til serveren (`/api/runder`) i stedet for å lage kode. `rundeData()` har allerede feltene fra tabellene `runde` og `svar` i planen.

**Før den legges ut:** last opp `laerar.html` sammen med ny `ordbua.html`. Lenkene peker til spill-adressen i `bygg.py` (GitHub Pages-roten). Sjekk at en oppgavelenke åpner spillet med oppgaven, altså at roten viser spillet og at `#oppgave=...` blir med.

**Neste steg uten Feide:** QR-kode til tavla, flere oppgaver per lenke (ukeplan), og oversikt over en elev på tvers av oppgaver.

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
