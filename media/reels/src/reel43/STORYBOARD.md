# Reel 43 – „CNH em árabe e inglês: conta como dois?“ (Do 26.11.2026)

> **Fix-Fassung nach Abnahme 18.11. (43-A blockierend):** Die Erstfassung („traduz tudo?“ → „Traduz tudo: árabe e inglês.“, „inclusive o que já está em inglês“) behauptete, die AR-Übersetzung übersetze die englischen Felder im AR-Festpreis mit – dafür gibt es keine Quelle (FAQ a1 = Treue, a7 = Upload-Umfang; Übersetzer sind je Sprache habilitiert, IN DREI 52/2022 Art. 12 § 2 / 16 § 1). Umgebaut auf Belegtes: Frage „conta como dois?“ → Antwort „Um documento só, não dois.“ (analisar v40 / FAQ a4 / pc1). **Keine Aussage darüber, welche Sprachteile übersetzt werden.** Abschnitte unten auf die Fix-Fassung aktualisiert; Erstfassung im Git-Verlauf (4e689b9).

**Thema (ENTSCHEIDEN 18.11., Score 16, Ben-Wunsch Arabisch):** CNH estrangeira árabe → português – Kauf-Zweifel vor dem Upload: Viele Führerscheine aus arabischsprachigen Ländern tragen Arabisch **und** Englisch. Zählt die zweisprachige Karte als ein oder als zwei Dokumente (zwei Sprachen = zweimal zahlen?) – und reicht das Englische auf der Karte vielleicht schon? Kaufnachweis (nur intern, nie öffentlich): analises 30 T. `ar/cnh` 2 Uploads am 03.11. (ägyptische Fahrerlaubnis, Name auf Arabisch und Englisch; eine davon unscharf); pedidos 30 T. status PAGO ohne AR-Bestellung (19.10.-Einträge = Testtag, nicht gezählt) → K = 2.
- **Abgrenzung:** R21 (CNH estrangeira allgemein: Detran-Liste, 180 dias, Portugal), R30 (CNH ES: Verso-Preisfrage), R32 (CNH argentina: PF × Detran, Gültigkeit), R42 (CNH ES: Foto als Vorlage), R26 (Atestado árabe), R34 (Certidão árabe: Preisfrage). Neu hier: **zweisprachige Karte – ein Dokument oder zwei**, „Inglês não dispensa“ (nur CNH auf Portugiesisch ist ausgenommen), ein Dokument = ein Preis. Kein Verso-Lernpunkt (Lehre 42-2), kein Foto-Lernpunkt (R42), keine Gültigkeit/180 dias (R21/R32), keine Permissão Internacional (Contran erlaubt Besuchern das Fahren mit PID → nicht pauschal sagen).
- **Antwort im Video:** UM – die Fahrerlaubnis ist ein Dokument Typ `cnh` mit Festpreis je Dokument (analisar v40; FAQ a4 „Documentos padrão, como certidões, diplomas, RG e CNH, têm preço fixo por documento“); das Englische ersetzt die Übersetzung in der Regel nicht (Detran-GO: „Tradução juramentada (exceto para CNH em idioma português)“). Nicht gesagt: welche Sprachteile übersetzt werden.
- **Hinweis 43-5 (nur intern):** analisar setzt idioma_origem = Hauptsprache. Ist eine zweisprachige Karte überwiegend englisch, erkennt analisar evtl. `en` statt `ar`; weicht das von der im Rechner gewählten Sprache ab, geht der Auftrag in Revision (`precisaRevisao`, idioma) statt „preço na hora“. Beim ägyptischen Beispiel (03.11.) korrekt `ar`. Im Bild/Text nichts dazu.

**Etikett Frame 0 (Standard seit R35, keine Variable):** „CNH estrangeira · árabe → português · R$ 299 na tabela“. Sagt nicht, ob die zweisprachige Karte als ein oder zwei Dokumente zählt → verrät UM/DOIS nicht. Hook-Frage = Kauf-Zweifel (Anzahl Dokumente), nicht die Preisfrage.
**Eine neue Variable (nicht im Bild; berührt Etikett, LinkedIn-Einstieg, Szenenlänge, Endcard, Hook-Typ, Erstkommentar und IG-Caption-Länge nicht):** **YT-Titel kurz mit Suchbegriff vorn** – „Tradução juramentada de CNH em árabe e inglês: conta como dois?“ (63 Zeichen, ohne Preis) statt Frage + Suchbegriff + „R$ … na tabela“ (81–96 Zeichen, R37–R42). Vorhersage + Messung: reel43-texte.md / lernlog.md.
**Standard (keine Variable):** Hook = Dokument-/Kauf-Zweifel-Frage, Endcard „CNH em árabe? Envie a foto: preço na hora.“, Szenen 3,5 s, Etikett in Frame 0, LinkedIn Frage + UTM in Zeile 1, Erstkommentar Frage + CTA + 3 Tags, IG-Caption Standard-Länge wie R40.
**Pflichtwechsel (keine Variable):** Format **„Cartão bilíngue na mesa“** (Dokument-Tisch) – Held-Objekt Schreibtisch-Brett 760 × 1080 mit zweisprachiger Karte (Zone Latein-Balken oben, Zone Schwung-Zeilen unten – abstrakte Formen, keine echten Schriftzeichen, keine Sprachliste), Übersetzungsblatt, Órgão-Gebäude, Siegel, Preisschild ohne Zahl, Kartennadel, PDF. Szenenwechsel = **Masken-Wisch mit harter Kante** über das Brett (0,14 s, Start 0,07 s vor der Caption, Lehre 38-4) statt Verschluss-Blinzeln (R42) / Match-Cut (R41). Grund **Pinho #376259** (R42 Dark, R41 Areia). Musik `music.py` **pop 120 BPM**, D, seed 43 (R42 funk, R41 lofi). Endcard-Bild passt zum Text (Lehre 42-1): gerade Karte, Foto-Ecken rasten ein, Haken – erst die Loop-Naht springt auf die Hook-Pose.

## Ablauf (Designzeit, 120 BPM, Schlag 0,5 s; Szenen 3,5 s)

| Zeit | Bild (Held-Objekt Brett) | Text im Bild | Beleg-Pille | Quelle |
|---|---|---|---|---|
| 0,0–3,0 | Brett-Oberkante 1176 (43-1), Karte schief (0,9), die zwei Zonen leuchten abwechselnd, „?“ pulsiert. **2,5 s Payoff:** Karte richtet sich gerade, EIN Foto-Ecken-Rahmen um die ganze Karte, Haken, Punch | Hook „CNH em árabe / e inglês: / conta como dois?“ (7 W.) · Mitmach-Chip „UM ou DOIS?“ · Etikett | – | Q1, Q5 |
| 3,0–6,5 | Brett steigt; Karte mittig; 3,5 Zone oben leuchtet, 4,0 Zone unten leuchtet (beide auf derselben Karte), 4,5 EIN Rahmen um die ganze Karte, Haken 5,5, Karte wippt 6,0 | „Um documento só, / não dois.“ | CNH: preço fixo por documento | Q2, Q5 |
| 6,5–10,0 | Karte gleitet zum Órgão-Gebäude; 7,0 Sperr-Zeichen; 7,5 Übersetzungsblatt heftet sich an (Punch); Haken 8,5; Gebäude wippt 9,0 | „Em geral, o inglês / não dispensa.“ | Exceção: CNH em português | Q4 |
| 10,0–13,5 | Blatt groß; Unterschrift 10,5–11,3; Siegel landet 11,5; Haken 12,5; Gebäude (Junta) klein unten, Puls 13,0 | „Tradutor juramentado / de árabe.“ | Registrado na Junta Comercial | Q3, Q4 |
| 13,5–17,0 | Karte + Blatt rücken zusammen; 14,0 Klammer; 14,5 Ring bündelt beides (Punch); Haken 15,5; Ring-Puls 16,0 | „Leve ao Detran: / CNH + tradução.“ | Exemplo: lista do Detran-GO | Q4b |
| 17,0–20,5 | Karte klein; Fläche (generisch, keine echte Karte); 17,5 Nadel fällt; 18,0 Gebäude; Haken 19,0; Nadel wippt 19,5; Gebäude-Puls 20,0 | „Confirme no Detran / do seu estado.“ | A lista muda por estado | Q6 |
| 20,5–24,0 | Karte klein links, Preisschild ohne Zahl rechts (21,0), Punch 21,5, Haken 22,5, Schwung 23,0 | „CNH em árabe: / R$ 299 na tabela.“ | Para português · tabela | Q1, Q2 |
| 24,0–27,5 | PDF; Unterschrift 24,5–25,5; Siegel landet auf dem Blatt 25,5; Haken 26,5; Siegel-Puls 27,0 | „Chega em PDF com / assinatura digital.“ | Valor e data na hora | Q7 |
| 27,5–34,2 | Endcard (harter Schnitt), Brett in Hook-Position (Oberkante 1176, Karte 70 px höher, 43-1): Karte gerade, 28,0 Foto-Ecken rasten ein, 28,5 Haken, Haken-Puls 29,5 | „CNH em / árabe? / Envie a foto: / preço na hora.“ · link na bio · traduzme.com.br · (61) 99803-8363 | – | Q7 |
| 34,2–34,5 | Loop: Frame 0 | – | – | – |

GMB (≤ 30 s): ohne 17,0–20,5 („Confirme no Detran“), harter Schnitt, Chip „Preço na hora no site“, Endcard-Chip „no site“, Endcard 24,0–29,0 = 5,0 s → 29,3 s Datei (Loop-Punkt 29,0 s; Muster R39–R42). Der Hinweis „confirme no Detran“ steht in GMB nicht im Bild (GMB hat keinen Text) – Szene 6,5 trägt „Em geral“.
Kauf-/Preis-Szenen vor der Endcard: 20,5–27,5 = 7,0 s von 27,5 s = 25 % (≤ 30 %), frühestens 20,5 s. (Erstentwurf „Árabe e inglês: um preço só.“ + Preisschild 13,5 hätte 38 % ergeben → umgebaut auf „um documento só.“ ohne Preis.)
Captions je 3,42 s ≥ max(1,8; 0,4 × Wörter); ≤ 4 Wörter je Zeile („Tradutor juramentado“ 2, „Em geral, o inglês“ 4).
SFX 27 auf 34,5 s = 0,78/s (≤ 0,8).

## Quellen (Whitelist oder selbst geöffnet 18.11.2026)

| Nr. | Aussage | Quelle | Wie geprüft |
|---|---|---|---|
| Q1 | CNH estrangeira árabe → português R$ 299 (Etikett, Preis-Szene, Texte) | Supabase `precos` (ypdvpytpajgkzglbzxwg) `WHERE ativo AND NOT placeholder`: `ar / to_pt / cnh` **29900**, extra_pag null (updated 19.10.); ebenso rg/passaporte/certidões AR→PT 29900 → niedrigster AR→PT-Dokumentpreis, aber nur „R$ 299 na tabela“ mit Dokument, kein Ab-Preis | SELECT 18.11.2026 (read-only) |
| Q2 | Einstufung: Fahrerlaubnis = Typ `cnh`, ein Dokument (Vorder-/Rückseite = Peça); idioma_origem = „idioma principal do texto“; Festpreis (pix-cob: Festpreis bis 4 Seiten je Datei, Lehre R41 – eine CNH hat 1–2) | Edge-Function `analisar` v40: „cnh: carteira de motorista (CNH …), driver's license, licencia de conducir; 1 página com frente e verso“; „idioma_origem: Código ISO 639-1 do idioma principal do texto“; analises 03.11. ägyptische CNH → `ar`/`cnh` | get_edge_function + SELECT 18.11.2026 |
| Q3 | „Registrado na Junta Comercial“ · Tradutor juramentado | Rechner FAQ a1 (Whitelist): „… o chamado tradutor juramentado: um profissional aprovado em concurso público e registrado na Junta Comercial.“ (Erstfassung nutzte a1/a7 auch für „traduz tudo“ – gestrichen, 43-A) | curl /orcamento-app/?lang=pt 18.11.2026 (HTTP 200) |
| Q4 | „Em geral, o inglês não dispensa.“ · „Exceção: CNH em português“ · Übersetzung durch tradutor juramentado | Detran-GO „Informações sobre CNH“ (goias.gov.br/detran/informacoes-sobre-cnh/), Registro estrangeiro: „Tradução juramentada“ „(exceto para CNH em idioma português)“; „A tradução deverá ser feita por tradutor oficial juramentado“. Präzedenz Detran-PR/SC (R21/R30 Q5): Übersetzung durch Tradutor Juramentado der Junta | WebFetch 18.11.2026 (selbst geöffnet; curl aus der Sandbox 403); Detran-PR heute nicht erreichbar → nur „Em geral“ + Beispiel GO in den Texten |
| Q4b | „Leve ao Detran: CNH + tradução.“ · „Exemplo: lista do Detran-GO“ (Bild 13,5 s; YT Pkt. 3, LinkedIn Pkt. 4 „entre outros documentos“) | Detran-GO, gleiche Seite: „Documentação necessária (originais e cópias) para Registro de Habilitação Estrangeira“ mit „Habilitação do país de origem dentro do prazo de validade legal“ und „Tradução juramentada (exceto para CNH em idioma português)“ (neben RNE, CPF, Passaporte, Comprovante …); nur als Beispiel, Folgeszene „Confirme no Detran do seu estado“ | WebFetch 18.11.2026 (Fix-Lauf, selbst geöffnet) |
| Q5 | „Um documento só, não dois.“ · „CNH: preço fixo por documento“ (Bild 2,5/3,0 s) · „a CNH é um documento padrão, com preço fixo por documento“ (YT/LinkedIn) | analisar v40 (Q2): Fahrerlaubnis = ein Dokument Typ `cnh`, Sprache = Hauptsprache; Rechner FAQ a4 (Whitelist): „Documentos padrão, como certidões, diplomas, RG e CNH, têm preço fixo por documento“; pc1 „… CNH…: preço fixo por documento.“ | get_edge_function + curl 18.11.2026 |
| Q6 | „Confirme no Detran do seu estado.“ · „A lista muda por estado“ | Detran-GO (Q4) verlangt u. a. RNE, CPF, Passaporte, Comprovante GO; Detran-PR/SC-Listen weichen ab (R30 Q5, R32 Q3/Q4, unabhängig abgenommen) → Liste je Bundesstaat verschieden; Aufforderung, keine Behauptung über einzelne Staaten | WebFetch 18.11.2026 + Whitelist-Präzedenz |
| Q7 | „Chega em PDF com assinatura digital“ · „Valor e data na hora“ · Endcard „Envie a foto: preço na hora“ | Rechner fl4_d „PDF juramentado com assinatura digital …“ (nur „assinatura digital“, ohne Zertifikats-Infrastruktur), fl2_d „Valor e data de entrega na hora.“, fl1_d „Foto ou PDF, quantos precisar.“ (Whitelist) | curl 18.11.2026 |
| – | Requisiten (Brett, zweisprachige Karte mit Balken/Schwung-Zeilen, Übersetzungsblatt, Gebäude, Siegel, Unterschrift, Klammer, Preisschild ohne Zahl, Fläche, Nadel, PDF, Foto-Ecken) | eigene SVG ohne Schrift, ohne Daten, ohne echte arabische/lateinische Buchstaben, kein Land, kein Kundenfall | – |

Bewusst **nicht** verwendet: welche Sprachteile einer zweisprachigen Karte übersetzt werden (unbelegt, 43-A), Permissão Internacional (Detran-GO: kein Reconhecimento; für Besucher erlaubt Contran das Fahren mit PID – Widerspruchsgefahr), 180 dias, Gültigkeit, Prüfungen/Exames, Abkommen einzelner Länder, Länder- oder Sprachlisten, welche Sprache man im Rechner wählt (Rechner-Verhalten bei Sprachabweichung nur im Code, nicht öffentlich), Lieferfristen, Urgência/Via física (AR-Regel 12), Kundendaten.

## Kritiker-Runden Storyboard (getrennte Durchgänge des Bauers mit festem Blickwinkel)

**Runde 1**
- Fakten: (F1) Erstentwurf Hook „CNH em árabe e inglês: precisa traduzir?“ verworfen – das Pflicht-Etikett mit Übersetzungspreis hätte die Antwort SIM nahegelegt → Umfangsfrage „traduz tudo?“ (Etikett sagt nichts über den englischen Teil). (F2) Szene „Só a permissão internacional? Não.“ gestrichen: Detran-GO verweigert nur den Reconhecimento/Registro; Besucher dürfen nach Contran mit PID fahren → pauschale Aussage wäre falsch. (F3) Szene „Escolha árabe → português“ gestrichen: nur durch internen Code belegt. (F4) „Em geral, o inglês não dispensa“ statt absolut; Beleg nur „Exceção: CNH em português“ (wörtlich Detran-GO). (F5) Preis 29900 Festpreis, eine Karte = ein Dokument → „um preço só“ widerspricht keinem Preis (Lehre R39); 4-Seiten-Grenze (Lehre R41) bei CNH nicht erreicht.
- Design: (D1) Pinho-Grund: Hook/Endcard Weiß auf Pinho, Marker Areia/Dark, Caption-Pillen Areia/Dark mit Sálvia-Marker/Dark, CTA-Chip Sálvia/Dark, Mitmach-Chip und Belege Papier/Dark; kein Weiß auf Sálvia/Areia. (D2) Brett 760 px = 70 % Breite; Requisiten per clipPath im Brett. (D3) „Arabische“ Zone nur als Schwung-Linien mit Punkten – keine echte Schrift (Regel: keine Sprachlisten/Schrift in Grafiken).
- Hook/Tempo: (H1) Payoff 2,5 s (Blatt + Pfeile aus beiden Zonen + Haken), Antwort-Text 3,0 s. (H2) je Szene ≥ 3 Mikro-Ereignisse im 0,5-s-Raster. (H3) Hook, Chip, Etikett voll bis 2,97 s, harter Schnitt (Lehre 39-2).
- Conversion: (C1) Endcard Standard, Bild passt zum Text (Lehre 42-1). (C2) IG/TikTok verraten TUDO nicht (kein „tudo“, kein „fiel“, kein „um documento só“, kein „inglês não dispensa“). (C3) Variable nur im YT-Titel.

**Runde 2**
- Fakten: „Tradutor juramentado de árabe“ – Rechner bietet Árabe (FAQ a9 Live-Fassung), Übersetzung durch juramentado (a1). OK. „A lista muda por estado“ durch GO vs. PR/SC belegt. OK.
- Design: Szene 2 (6,5) Blatt lag hinter der Karte → Karte nach links, Blatt rechts daneben. Szene 1 Inhalte zu tief → Karte links oben, Blatt rechts. Preis-Szene ohne Karte (Bug `n<=5`) → Karte sichtbar. OK.
- Hook/Tempo: Frame 0 Wörter 6 + 5 + 7 = 18 → qa-Ausnahme maxNewWords 22 wie R35–R42 (Loop-Naht). OK.
- Conversion: GMB ohne „link na bio“. LinkedIn: RH/Mobilidade/Imigração mit Mitarbeitenden aus arabischsprachigen Ländern; Frage + UTM Zeile 1. OK.

**Runde 3 (getrennt):** Preis-Anteil 38 % > 30 % (Design-Regel v3 Nr. 6) durch „um preço só“ + Preisschild 13,5 → Szene auf „um documento só.“ mit Ring statt Preisschild umgebaut (25 %). Danach keine offenen Mängel.

## Bau-Fixes (nach Snapshots, qa_frames und Kontaktbögen)
- Kontaktbogen 1. Lauf: Wisch 0,20 s zeigte an jedem Szenenwechsel 1–2 Bilder eine volle Sálvia-Fläche → 0,14 s (volle Deckung ≈ 1 Frame).
- PDF-Siegel lag neben dem Blatt (wirkte wie Zahnrad) → auf die Blattecke.
- Szene 17,0–20,5: 19,0–20,4 fast still → Gebäude-Puls 20,0.
- Szene 13,5: Übersetzungsblatt-Deckkraft hing vom vorherigen Frame ab (parallel gerenderte Seiten) → in der Szene explizit gesetzt.
- qa_frames Haupt / `cut=gmb` / gmb/reel.html: 0 Befunde.

## Fix-Runde nach Abnahme 18.11.
- 43-A: Hook/Mitmach/Payoff/Szene 3,0/Szene 13,5 neu (siehe Ablauf); Pfeile von den Sprach-Zonen zum Blatt entfernt (hätten „beide Sprachen werden übersetzt“ gezeigt); Zonen-Leuchten in Szene 13,5 entfernt.
- 43-1: Brett in Hook/Endcard Oberkante 1236 → 1176; Hook-Karte 0,9 und −50 px; Endcard-Karte −70 px statt +30 px → Karte im 3:4-Ausschnitt ganz (Hook-Unterkante ≤ 1655, Endcard-Rahmen ≤ 1642). Hook-Markerzeile „conta como dois?“ 90 px (endet x 884, vor der rechten UI-Zone).
- 43-3: siehe Ton.
- 43-5: siehe Hinweis oben.

## Ton
`music.py` pop 120 BPM, D, seed 43, Master v2 (Ceiling −2,0 dBTP Haupt / −3,0 GMB), 15-ms-Einblendung, Fade 0,15 s; GMB aus derselben Spur mit SKIP 17,0–20,5 und eigener Gain-Tabelle `GJ_GMB`.
SFX im 0,5-s-Raster (Pop 0,03 = Frame 1), keine gleichen SFX < 1 s, keine Glocken. Gains per Stem-Messung iterativ eingestellt (44,1 kHz, Fenster 400 ms RMS / 0,2 s Spitze, Mix − Musik). Fix 43-3: Whooshes 6,5/13,5/20,5 (GMB auch 24,0) d = 0,25 s statt 0,4 s (Spitze vor dem Schlagzeug-Schlag) und lauter, Clicks leicht lauter. Haupt RMS max **+3,97 dB** (Whoosh 24,0), Spitze max **+3,67 dB**, Whoosh-/Click-Spitzen +2,0…+3,7 dB. GMB RMS max **+3,95 dB**, Spitze max **+3,93 dB**, Whoosh-/Click-Spitzen +1,8…+3,7 dB. Kein SFX > +4 dB. Clicks RMS weiter +0,2 dB (sehr kurz). Hörbarkeit **nicht mit dem Ohr geprüft**.
audio.py findet die Lib ohne Env-Variable (R43LIB → ../../lib → `git show a9df053:media/reels/lib/…` in ein Temp-Verzeichnis), sonst klare Abbruchmeldung (Lehre 38-7). Ohne Env geprüft.
