# Ordliste til Ordbua

542 ordpar. I 246 av dem er bokmålsordet feil på nynorsk. I 51 av dem kan bokmålsformen også skrives på nynorsk (f.eks. tenke/tenkje, skole/skule), og da godtas begge. 245 ord skrives helt likt på bokmål og nynorsk (f.eks. bil, sove, glad, ofte, båt, finne). Spillet lar omtrent hvert tredje ord i en runde være et slikt ord. Lista brukes begge veier: fra bokmål til nynorsk og fra nynorsk til bokmål. Filene inneholder de samme dataene:
`ordliste.xlsx` (Excel-ark for å redigere ordene), `ordliste.csv` (for andre regneark) og `ordliste.json` (for spillet).

## Redigere ordene i Excel
1. Åpne `ordliste.xlsx` og endre, legg til eller slett rader i arket «Ordliste». Arket «Slik bruker du arket» forklarer kolonnene og har et eksempel.
2. Kjør `python3 ordliste/fra_excel.py` for å skrive arket tilbake til `ordliste.json` og `ordliste.csv`. Skriptet stopper uten å skrive noe hvis en rad mangler ord, har ukjent ordklasse eller noe annet enn ja/nei, eller står to ganger.
3. Bygg spillet på nytt med `python3 spill/bygg.py` (se `spill/README.md`).

`python3 ordliste/lag_excel.py` lager Excel-arket på nytt fra `ordliste.json`, for eksempel etter at lista er endret på annen måte. Det overskriver `ordliste.xlsx`.

## Kolonner
- **bokmal**: ordet spilleren ser.
- **nynorsk**: hovedsvaret.
- **godkjente_alternativer**: andre riktige nynorske svar. Det er parallellformer og a-infinitiv fra Nynorskordboka (f.eks. «vera»), og nynorske oversettelser med samme betydning fra dinordbok.no selv om de ikke står i Nynorskordboka (f.eks. «muleg», «glømme», «truleg»). Skilt med `;` i CSV.
- **bokmal_alternativer**: andre riktige bokmålssvar når spilleren får nynorskordet (retningen nynorsk til bokmål). Det er andre skrivemåter i samme artikkel i Bokmålsordboka (f.eks. «golv», «sjøl», «trett») og bokmålsoversettelser med samme betydning fra dinordbok.no (f.eks. «kun», «trygghet», «trolig»). Skilt med `;` i CSV.
- **ordklasse**
- **nynorskordboka**: lenke til artikkelen (første runde) eller oppslaget (andre runde) i Nynorskordboka som bekrefter svaret.
- **bokmalsform_godtas**: «ja» hvis bokmålsordet selv også er riktig nynorsk med samme betydning. Da står det også blant de godkjente svarene.
- **nynorskform_lov_pa_bokmal**: «ja» hvis hovedsvaret på nynorsk også er en tillatt skrivemåte på bokmål med samme betydning etter Bokmålsordboka (f.eks. heim, mjølk, golv, sjuk). Gjelder også ordene som skrives likt.
- **merknad**: feller, f.eks. at bokmålsformen finnes i Nynorskordboka som et annet ord.
- **ulikt_ord**: «ja» hvis bokmålsordet ikke kan oversettes direkte: nynorsk bruker et annet ord eller en annen ending, og bokmålsordet står ikke i Nynorskordboka (f.eks. benytte → nytte, kjærlighet → kjærleik). Disse ordene er en egen kategori, «Ulike ord», i spillet. Kolonnen heter «Annet ord på nynorsk» i Excel-arket.

## Hva som godtas
Et svar er riktig hvis det er en riktig nynorskform med samme betydning, enten den står i Nynorskordboka eller i dinordbok.no. Det gjelder også når nynorskformen er lik bokmålsordet (f.eks. «tenke», «komme», «spise»). Hvis bokmålsformen finnes på nynorsk bare med en annen betydning (f.eks. «lav» = plante, «høy» = tørket gras), godtas den ikke.

## Hva som godtas fra nynorsk til bokmål
Bokmålsordet, alle `bokmal_alternativer`, og nynorskordet selv når `nynorskform_lov_pa_bokmal` er «ja» (f.eks. «heim»). «kvar» står to ganger (hvor og hver), og da godtas begge.

## Slik ble ordene sjekket
- Hvert bokmålsord finnes i Bokmålsordboka, og hvert nynorskord i Nynorskordboka (ordbokene.no) med riktig betydning.
- Hvert par er sjekket mot dinordbok.no (norsk–nynorsk), og nynorske oversettelser derfra med samme betydning er lagt til som godkjente svar.
- 51 ord der bokmålsformen også er riktig nynorsk etter Nynorskordboka (f.eks. nå, skole, tenke, komme, måke, søndag) eller dinordbok.no (f.eks. spise, hjerte, drøm, grønn) har «ja» i kolonnen bokmalsform_godtas.
- Tre ord er tatt ut fordi de kan bety to ting: regne, male og dem.
- Ordlista bruker ingen ê (læreren ønsket det 20.10.2026): hovedsvarene er «ver», «viskeler» og «torever», som alle er godkjente skrivemåter i Nynorskordboka, og «vêre» er tatt ut som alternativ til «vere».
- Andre kontroll (17.10.2026): alle 219 ord med «nei» ble sjekket på nytt av to uavhengige kontrollører mot Nynorskordboka og dinordbok.no. Ingen av bokmålsformene er riktig nynorsk med samme betydning, så «nei» står. Tre manglende former ble lagt til: «éin» (en), «førstning» (begynnelse) og «tykke», «tykkja», «tykka» (synes).
- 45 nye ord som skrives likt (merknad «Skrives likt på bokmål og nynorsk.») er kontrollert i både Bokmålsordboka og Nynorskordboka, der den like formen er første eller eneste skrivemåte. Verbene har a-infinitiv som godkjent alternativ (f.eks. sova).
- Tredje kontroll (18.10.2026): alle 270 nynorske hovedsvar som skiller seg fra bokmålsordet ble slått opp i Bokmålsordboka av to uavhengige kontrollører (de var enige om alle). 62 av dem er også tillatt på bokmål med samme betydning. «høgd» (høyde) er bare tillatt på bokmål i betydningen bakke/høydedrag og har derfor «nei».
- Fjerde runde (18.10.2026): 200 nye ord som skrives likt er lagt til, slik at like ord får en større plass i spillet. Hvert ord er slått opp i Nynorskordboka (ord.uib.no eller ordbokene.no), og bare ord der den like formen er første oppslagsform med samme ordklasse og betydning, er tatt med. Ni kandidater ble avvist fordi nynorsk har en annen første form: bo (bu), tro (tru), gammel (gammal), sitte (sitje), tykk (tjukk), kjøkken (kjøken), ringe (ringje), glass (glas) og male (måle betyr å male med maling). Andre skrivemåter fra samme artikkel er godkjente alternativer (f.eks. lys/ljos, jul/jol, vi/me, billig/billeg), og verbene har a-infinitiv (f.eks. kasta).
- Femte runde (19.10.2026), for retningen nynorsk til bokmål: alle 270 ord der nynorsk og bokmål er ulike ble slått opp i Bokmålsordboka (andre skrivemåter) og i dinordbok.no fra nynorsk til bokmål (oversettelser). Hvert nytt svar ble kontrollert av en andre kontrollør, og alle 83 som sto igjen av en tredje. 82 svar i 74 ord er med, og 34 av dem er nye i forhold til hva spillet godtok fra før (f.eks. «hvorledes», «kun», «fornøgd», «juge», «speller», «trygghet», «fortsatt», «trett»). «spelle» ble tatt ut fordi det i Bokmålsordboka betyr å glitre, ikke å spille. Løsere synonymer som «starte» (byrje) og «lukke» (stengje) ble avvist. «søke», «forglemme» og «trolig» er med fordi to av tre kontrollører godtok dem, og fordi de speiler nynorskformene som allerede godtas andre veien («søkje», «forgløyme» og «truleg»).
- Lærerens korrektur (20.10.2026), gjort i Excel-arket: «ver», «viskeler» og «torever» uten ê, og «løysning» er tatt ut som godkjent svar for løsning.
- Ulike ord (21.10.2026): 41 ord har «ja» i `ulikt_ord`. 14 av dem fantes fra før (hvordan, kjærlighet, begynnelse, frihet, sannhet, overraskelse, hendelse, opplevelse, forståelse, hensyn, ensomhet, fremdeles, savne, oversette), og 27 er nye (f.eks. benytte → nytte, ansette → tilsetje, begrense → avgrense, belønne → løne, tålmodighet → tolmod, avgjørelse → avgjerd, tillatelse → løyve, forbrytelse → brotsverk, bevissthet → medvit, hensynsløs → omsynslaus, bekvem → makeleg). Reglene: bokmålsordet står ikke i Nynorskordboka (sjekket i ord.uib.no), nynorskordet står der med samme betydning og er oversettelsen i dinordbok.no, og det finnes ingen direkte nynorskform av bokmålsordet. Derfor er ord som bare bytter -het med -heit tatt ut (dumhet/dumheit, svakhet/svakheit, hemmelighet/hemmelegheit, enighet/einigheit, myndighet/myndigheit, takknemlighet/takknemlegheit), og det samme gjelder einig, ueinig, bekymra, betydeleg, utmerkt, begeistra, oppmerksam, misfornøgd, takknemleg, behageleg, framragande, framskritt, bevisstlaus, besværleg og bedrøva. Mange typiske an-/be-ord er nå riktig nynorsk etter Nynorskordboka og er heller ikke med: anbefale, bekymre, behandle, bevise, bekrefte, beskytte, betydning, unnskylde, forskjell, hensikt, erfaring, behøve, angripe, bevege, forsvinne, beholde (behalde) og forbedre (forbetre). Ord der svaret er flere ord (gjenkjenne → kjenne att, bekjempe → kjempe mot, beseire → vinne over) er ikke med. I retningen nynorsk til bokmål er «nynorskordet er lov på bokmål» sjekket i Bokmålsordboka for alle 27 nye ord (13 er lov, f.eks. nytte, avgrense, roe, løyve, vilkår, utdanning).
