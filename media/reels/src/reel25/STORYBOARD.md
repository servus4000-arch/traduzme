# Reel 25 – „O que é isso?“ (Sonder-Reel Dinamarquês, Serienstart)

Auftrag Ben (30.10.): virales, teilbares Dänisch-Reel zum Mitmachen, als Serie ausbaubar. Dänisch steht **nicht** im Rechner → kein „Preço na hora“, keine Rechner-Ausschnitte; CTA = Anfrage per WhatsApp (61) 99803-8363.
- Idee A + B: Mitmach-Quiz mit dänischem Wort (rødgrød med fløde, A/B/C) → echter Anlass: dänische Heiratsurkunde (vielsesattest) → Tradução juramentada → Traslado → Apostila → Foto per WhatsApp.
- Bildsprache **Kinetic-Quiz + Dokument-Objekte** (R24 Figur-Story, R23 Dokument-Tisch). Grund **Névoa #BDCBCB** mit Dark-Text (R24 Pinho, R23 Sálvia). Captions Dark-Pille/Weiß, Marker Areia, CTA-Chip Pinho/Weiß.
- Musik `lib/music.py` **bossa 120 BPM**, Master v2 (R24 pop). Schlag 0,5 s.
- Neue Variable (genau eine): **Hook-Typ „Kurioses Fremdwort-Quiz“** (Wort statt Dokument-/Lebensereignis-Frage). Kein Serien-Badge (wäre zweite Variable), kein Teilen-Bild (E2) → Teilen-Satz „Manda pra quem mora na Dinamarca“ nur in den Texten.

## Quellen (Q)
| Q | Aussage im Bild | Quelle | Geprüft |
|---|---|---|---|
| Q1 | rødgrød med fløde = Sobremesa: frutas vermelhas e creme | lex.dk (Den Store Danske) „rødgrød“: „klassisk dansk sommerdessert, hvortil der serveres kold fløde eller mælk“; Beeren (jordbær, hindbær, ribs, kirsebær …) | WebFetch 30.10. |
| Q2 | Vielsesattest = certidão de casamento | kk.dk (Københavns Kommune, „Vielsesattest“), borger.dk (Vielsesattest, viet i folkekirken) | WebFetch 30.10. |
| Q3 | Versão internacional sem português (Ex.: Copenhague) | kk.dk: „på dansk eller i en international version (på dansk, engelsk, spansk, fransk og tysk)“ | WebFetch 30.10.; nur Kopenhagen belegt → Beleg „Ex.: Copenhague (kk.dk)“ |
| Q4 | Pra valer no Brasil: vai em português | Código Civil art. 224 (Whitelist 10-gegenkritik §0) | Whitelist; planalto aus Sandbox gesperrt |
| Q5 | Casou na Dinamarca? Traslado no cartório | Res. CNJ 155/2012 art. 2º/13 (Whitelist R16): Traslado der im Ausland geschlossenen Ehe von Brasilianer:in, certidão legalizada/apostilada + tradução por tradutor público juramentado (oder Konsulatsurkunde) → „Em geral“ | Whitelist R16 |
| Q6 | Apostila: feita na Dinamarca | HCCH Statustabelle (cid=41): Dänemark Vertragsstaat, in Kraft 29.12.2006; Brasilien in Kraft 14.08.2016. um.dk: Udenrigsministeriet (Legaliseringskontoret) stellt Apostille aus → „Em geral · confirme no cartório“ | WebFetch 30.10. |
| Q7 | Dinamarquês? A gente traduz. / Orçamento no WhatsApp | Ben 30.10.: Dänisch im Angebot, Anfrage per WhatsApp (nicht im Rechner); keine Frist-/Preis-/Formzusage | Auftrag |

## Zeitachse (Designzeit, Hauptfassung 34,0 s)
| Zeit | Bild | Text | Q | SFX |
|---|---|---|---|---|
| 0–3 | Karte „rødgrød / med fløde“ (wippt), Antwort-Pillen A certidão / B sobremesa / C bom-dia (0,25/0,5/0,75 s) | Hook „O que é **isso?**“, Chip „Comenta: A, B ou C“; 2,5 s B Areia + Haken + Punch | Q1 | impact 2,5 |
| 3–6 | Schale Beeren + Creme | „Sobremesa: frutas / vermelhas e creme.“ · Beleg „Den Store Danske (lex.dk)“ | Q1 | whoosh 3,0 · pop 3,5 |
| 6–9 | Urkunde „VIELSESATTEST“ + „?“-Plakette | „E numa certidão / dinamarquesa?“ | Q2 | whoosh 6,0 · pop 6,5 |
| 9–12 | Ringe landen auf der Urkunde (Punch 9,5) | „É a certidão / de casamento.“ · „kk.dk · borger.dk“ | Q2 | stamp 9,5 |
| 12–15 | Etikett X „PORTUGUÊS“ | „Versão internacional? / Sem português.“ · „Ex.: Copenhague (kk.dk)“ | Q3 | stamp 12,5 |
| 15–18 | Urkunde + „TRADUÇÃO JURAMENTADA“ (Punch 15,5) | „Pra valer no Brasil: / vai em português.“ · „Regra geral: Código Civil, art. 224“ | Q4 | whoosh 15,0 · impact 15,5 |
| 18–21 | Pasta „TRASLADO“, zwei Blätter fliegen ein, Haken 20,0 | „Casou na Dinamarca? / Traslado no cartório.“ · „Em geral · Res. CNJ 155/2012“ | Q5 | whoosh 18,0 · pop 18,5 · pop 20,0 |
| 21–24 | Urkunde + „APOSTILLE“ (Punch 21,5) | „Apostila: feita / na Dinamarca.“ · „Em geral · confirme no cartório“ | Q6 | stamp 21,5 |
| 24–27 | Handy (eigene Grafik), Mini-Urkunde fliegt ins Handy, Tipp 25,0, Haken 25,5 (Punch) | „Do dinamarquês? / Manda a foto.“ | Q7 | whoosh 24,45 · click 25,0 · impact 25,5 |
| 27–33,7 | Endcard: Karte + Urkunde klein unten | „Dinamarquês? / **A gente traduz.**“, Chip „Orçamento no WhatsApp“, WhatsApp „(61) 99803-8363“, „traduzme.com.br“ | Q7 | hit + stamp 27,0 |
| 33,7–34 | Loop = Frame 0 | | | |

CTA-Chip (Pinho, WhatsApp-SVG + „(61) 99803-8363“) 3,0–27,0 s. Zoom-Punches 2,5/9,5/15,5/21,5/25,5. Ducking −4 dB 6–9/12–15/18–21/24–27.

## GMB-Fassung (28,0 s)
`SKIP=[[12,3],[24,3]]`: ohne Design 12–15 (Versão internacional) und 24–27 (Handy). Endcard ab Echtzeit 21,0 s, Loop ab 27,7 s. Kein „link na bio“ (gibt es in keiner Fassung). Audio schneidet dieselben Fenster (audio.py `SKIP`).

## Bewusst nicht verwendet
Preise, Fristen, Lieferform (Papier/Eil), Sprachlisten im Bild, Aussprache-Mythen zu rødgrød (nicht belegt), Personattest (→ Serienfolge), Konsulat-Details, Namen von Personen.

## Kritiker-Protokoll (Selbst-Durchgänge, kein Sub-Agent verfügbar)
| Runde | Fakten | Design | Hook/Viralität | Conversion |
|---|---|---|---|---|
| S1 | „sem português“ nur für kk.dk belegt → Beleg „Ex.: Copenhague“; Traslado/Apostila mit „Em geral“ | – | Hook ≤ 6 Wörter ✓, Ein-Buchstaben-Antwort ✓ | Chip ohne Nummer → Nummer in den Chip |
| V1 | – | c1/c3/c8 zu breit; QB/TRAD/APO zu nah am Rand | Payoff 2,5 s dezent → Punch + Haken | – |
| V2 | – | Handy-Szene leer → Urkunde rechts; X-Icon statt Durchstreichen (qa `cut`); Pillen gestaffelt (qa `words`) | YDIF 0,55 → Wippen/Push → 0,86 | – |
| V3 | – | GMB-Schnitt falsch (Bild 21–24 statt 24–27) → `[[12,3],[24,3]]` | – | – |
| V4 | keine offenen Mängel | keine offenen Mängel | keine offenen Mängel | keine offenen Mängel |
