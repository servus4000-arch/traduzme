# Reel 21 – „Sua carteira de motorista é de fora?“ (Prio 1 aus Zahlen: CNH estrangeira no Detran, Mi 04.11.2026)

Format **Figur-Story + UI-Close-up** (Figur Sofía mit ihrer Karte, die sich dreht: Licencia → Tradução → CNH; danach echte Rechner-Screenshots) · Grundton **Areia #EEDECE** · Musik music.py **lofi** 120 BPM (Schlag = 0,5 s), Master v2 · 36,0 s (GMB-Fassung 28,5 s).
Abgrenzung: R16 Chat (Sálvia, bossa), R17 Dokument-Split (Pinho, funk), R19 POV/Dokument-Tisch (Névoa, pop). R18/R20 parallel, nicht angefasst.
Neue Variable dieses Reels (Messung): **ein Objekt, das sich dreht** (Karte als roter Faden) + ES-Fall.

## Quellen (selbst geöffnet 28.10.2026, nur was die Quelle trägt)
- **Q1 Res. CONTRAN nº 933/2022** (28.03.2022, in Kraft 01.04.2022; ersetzt Res. 360/2010 und 671/2017; PDF bei Detran-GO): Art. 2: estrangeiro habilitado pode dirigir amparado por convenções/acordos e reciprocidade „no prazo máximo de 180 dias“, respeitada a validade; § 4: após 180 dias de estada regular, para continuar dirigindo, exames para obter a CNH.
- **Q2 Detran-GO „Informações sobre CNH“** (goias.gov.br/detran/informacoes-sobre-cnh): Registro de habilitação estrangeira: „Tradução juramentada“ (exceto CNH em português), „A tradução deverá ser feita por tradutor oficial juramentado“; Habilitação do país de origem dentro da validade; RNE, CPF, comprovante de residência; exames.
- **Q3 Detran-PR Serviço „Solicitar registro de carteira de motorista estrangeiro“**: carteira original e na validade; RNE/RNM; comprovante de endereço; tradução juramentada (tradutor da Junta Comercial); „documentos de Portugal não precisam de tradução“.
- **Q4 Detran-SC Portaria 1108/2025** art. 8º: documento de identificação, CPF, comprovante de residência, habilitação estrangeira original e válida, V „tradução … realizada por tradutor público juramentado“; § 1º habilitação emitida em língua portuguesa: „não será necessária a tradução juramentada“.
- **Q5 Rechner live** (traduzme.com.br/orcamento-app, Screenshot per Playwright 28.10., pix-config gemockt, weil Supabase aus der Sandbox gesperrt ist; Schritt 1 zeigt keine Preise): Datei-Zeile, „Espanhol → Português“, „Calcular preço“; pc1 „Documentos padrão (certidões, diplomas, CNH…): preço fixo por documento.“; pc2 „Verso e Apostila (foto ou página) contam como parte do documento“; Flow fl2 „Valor e data de entrega na hora“, fl3 „Pague por Pix · Confirmação automática“, fl4 „PDF juramentado com assinatura digital“ / „Receba por e-mail“; „sem cadastro“; UI-String „Calculando…“.
- **Nicht** behauptet (keine Quelle trägt es): Mercosul ohne Übersetzung (Detran-GO befreit Mercosul nur vom Pass, nicht von der Übersetzung), Fristen/Kosten beim Detran, PID-Details. Deshalb „em geral“ + „confira no Detran do seu estado“.

## Ablauf (Endfassung nach Design-Regeln v3, 36,0 s)
| Zeit | Bild | Text im Bild (y 300–1500, x 90–900) | Quelle | Ton (Schlag) |
|---|---|---|---|---|
| 0,0–2,4 | **Frame 0 fertig:** Areia, Figur Sofía hält Karte „LICENCIA DE CONDUCCIÓN“ (Vektor, keine Daten), Wortmarke traduzme; Bewegung ab Frame 1 | „Sua carteira / de motorista / **é de fora?**“ (7 W.) | – | Groove ab 0 |
| 2,4–5,0 | Karte dreht sich (2,5–2,9) → „TRADUÇÃO JURAMENTADA“ mit Siegel | „Pro Detran, em geral: / **juramentada.**“ (V7: 2 Zeilen, Raster B3) · ab 3,0 Chip „Preço na hora · link na bio“ | Q2–Q4 | whoosh 2,5 · pop 3,0 |
| 5,0–7,5 | Karte raus, Kalender zählt 0 → 180, rastet ein (Punch) | „Mais de **180 dias** / no Brasil?“ (4,95–7,35) | Q1 Art. 2 | whoosh 5,0 · riser 5,8 · stamp 7,0 |
| 7,5–10,0 | Karte zurück (Licencia), dreht sich zur „CNH brasileira“ | „Pra seguir dirigindo: / **CNH brasileira.**“ | Q1 § 4 | pop 7,5 · whoosh 8,0 |
| 10,0–14,5 | 4 Zeilen-Karten: Carteira original e válida · Documento de identidade e CPF · Comprovante de residência · **Tradução juramentada** (Punch) | „No Detran, **em geral:**“ | Q2–Q4 | whoosh 10,0 · pop 10,5/11,0/11,5 · stamp 12,0 |
| 14,5–17,5 | „CARTA DE CONDUÇÃO“ (PT) + Haken | „Em português? / **Sem tradução.**“ (V7: 2 Zeilen, Raster B3) | Q3, Q4 § 1, Q2 | whoosh 14,5 · pop 15,0 |
| 17,5–20,0 | Detran-Gebäude + Pin | „Confira no Detran / **do seu estado.**“ | Vorsicht-Regel | whoosh 17,5 · pop 18,0 |
| 20,0–22,5 | **Echter Rechner-Screenshot**: licencia.jpg + Espanhol → Português, Fokus Datei (20,5) → Idiomas (21,5) | „Foto da carteira, / **frente e verso.**“ | Q5 pc2 | whoosh 20,0 · click 20,5/21,5 |
| 22,5–25,0 | **Echter Screenshot** „Como o preço é calculado“, Marker „CNH…“ + „preço fixo por documento.“ | „Documento padrão: / **preço fixo.**“ | Q5 pc1 | whoosh 22,5 · pop 23,0/23,5 |
| 25,0–28,5 | Tipp „Calcular preço“ (25,5), Button zeigt „Calculando…“ (25,6–26,5, harter Schnitt, UI-Grün nur im Button), dann Ergebnis im Site-Stil „Seu orçamento · Total · Entrega até · Continuar“ mit **unscharfen Balken** (keine Zahl) | „Preço e data / **na hora.**“ (26,45–28,25) | Q5 (UI-Strings live geprüft) | whoosh 25,0 · click 25,5 · Break 25,5–26,0 · hit 26,0 · pop 26,5 |
| 28,5–31,0 | Mitmach (Inhaltsfrage, kein Köder) | „Sua carteira é / de **qual país?**“ · „Comenta só o país:“ · Colômbia · EUA · Espanha | – | whoosh 28,5 · pop 29,0/29,5/30,0 |
| 31,0–36,0 | Endcard (Figur + Licencia wie im Hook, tiefer): „Preço **na hora** / no site.“ · „link na bio“ · traduzme.com.br · WhatsApp (61) 99803-8363, ruhig 4,5 s; 35,5–35,8 zurück in die Hook-Pose, 35,8–36,0 = Frame 0 | – | Ben-Regel | hit 31,0 · pop 31,5 |

Rechner-/Kauf-Anteil vor der Endcard: 20,0–28,5 = 8,5 s von 31,0 s = 27 % (v3 Nr. 6: ≤ 30 %, ab 6 s). Szenen 2,4–4,5 s, Mikro-Impuls je 0,5–1 s.
GMB-Fassung (28,5 s): ohne 5,0–10,0 (180 dias/CNH) und ohne Mitmach; Chip „Preço na hora no site“, Endcard ohne „link na bio“, Loop wie Haupt.
Bauzeit-Hinweis: reel.html rechnet intern mit der Bau-Zeitachse (39,5 s) und mappt per `SKIP` (Liste −1,0 s ab 14,5; Pix/PDF-Kacheln 29,5–32,0 entfernt, Inhalt steht in der Caption).

## Kritiker-Runden Storyboard (getrennte Prüfgänge, je eigener Fokus)
| Runde | Kritiker | Mängel | Fix |
|---|---|---|---|
| 1 | Fakten | (a) Brief nennt „Mercosul braucht ggf. keine Übersetzung“ – keine der geöffneten Quellen trägt das (GO befreit Mercosul nur vom Pass). (b) „Turista dirige 180 dias com a carteira“ wäre unvollständig (Vienna-Länder: PID, Acordo/Reciprocidade). (c) „O Detran pede tradução“ absolut – PT-Karten befreit. (d) Res. 360/2010 ist widerrufen. | (a) gestrichen, nur Q4 § 1 „em língua portuguesa“. (b) nur die Pflicht nach 180 Tagen (Q1 § 4) als Frage „No Brasil há mais de 180 dias?“. (c) „em geral“ + eigener Block PT + „confira no Detran do seu estado“. (d) Quelle Res. 933/2022. |
| 1 | Design | Captions zentriert bei x 540 laufen über x 900 (Fehler R17/R19); Chip „Preço na hora · link na bio“ 46 px evtl. > 810 breit; Weiß auf Areia; Karten-Titel bei Verkleinerung < 44 px; Screenshot-Text zu klein. | Captions linksbündig ab x 90, Breite automatisch gegen 810 geprüft; Chip dunkel (Dark/Weiß), Breite gemessen; Text auf Areia nur Dark, Marker Sálvia; Karte nie unter Skala 1 mit Titel; Panels 810 breit (UI-Text ≈ 40–48 px, Kernaussage trägt die Caption). |
| 1 | Hook/Tempo | „Sua CNH é estrangeira?“ – CNH ist streng die brasileira, wirkt widersprüchlich; Payoff erst bei 3,5 s geplant; Detran-Liste mit 15 W. in einem Block. | Hook „Sua carteira de motorista é de fora?“ (7 W.); Payoff ab 2,4 s; Liste Zeile für Zeile (1 s Abstand), Caption 4 W. |
| 1 | Conversion | Rechner kommt erst bei 26 s; kein Beleg, dass CNH im Rechner geht. | Chip ab 3,0 s; echter Screenshot pc1 „CNH… preço fixo“ mit Marker; ES→PT im echten Formular. |
| 2 | alle 4 getrennt | Fakten: „Documento de identidade e CPF“ – PR nennt für Ausländer RNE/RNM, kein CPF → durch „em geral“ gedeckt (GO, SC nennen CPF), ok. Design: Mitmach-Pillen zu dritt in einer Reihe > 810 → zwei Reihen. Tempo: Regras-Block 7 W. / 2,5 s = 0,36 s/W. knapp → Caption steht schon ab 18,6 bis 21,0 (2,4 s), Lesbarkeit im Video prüfen. Conversion: GMB ohne „link na bio“ → eigener Chip/Endcard. | eingebaut |
| 3 | getrennte Schlussrunde | **keine offenen Mängel** im Plan; Rest wird am Video geprüft (10-fps-Frames, Außenkanten-Messung). | – |

## Bau-Runden (Video, vor Encode)
| Runde | Prüfer | Befund | Fix |
|---|---|---|---|
| V1 | eigenes Frame-Mess-Skript (10 fps, Außenkanten) | Captions beim Ausblenden kurz über y 300 (translateY); Zeilen-Karten/Kacheln/Pillen per Overshoot bis x 916–958; Karte/Kalender/PT-Karte fuhren mit Text über y 1500 rein/raus; „assinatura digital, por e-mail“ bis x 905; Hook × Wortmarke bei 2,3 s | Ausblenden ohne Versatz; Karten 770 breit, Ursprung Mitte; Auf-/Abtritte als Skalieren am Platz; Kachel-Text „PDF assinado / por e-mail“; Hook ohne Versatz |
| V2 | qa_frames.js (a9df053) Haupt + GMB | empty ×5 (Pille mit erstem Wort), double „Calculando…“ × Panel A, empty Match-Cut-Fläche | Zeilen erscheinen ganz (gestaffelt 0,14 s); Panel A weg, bevor „Calculando…“ kommt; Fläche als Objekt (`data-qa-allow="empty"` mit Grund) |
| V3 | Kontaktbogen (19 Frames) | Detran-Gebäude doppelt versetzt (unsichtbar), Pin auf dem Chip | Gebäude-Position korrigiert, Pin rechts neben dem Dach |
| V4 | Tempo (Standzeit ≥ max(1,8 s; 0,4 s/W.)) | cap2 7 W. in 2,25 s, cap6 7 W. in 2,25 s, cap9 1,75 s | cap2 neu 6 W. 2,4 s; cap6 „Confira no Detran do seu estado.“ 5 W.; cap9 1,8 s; Tipp/Match-Cut auf Schlag 26,5 |
| V5 | Design-Regeln v3 (Koordinator 28.10.) | Rechner-Anteil 32 % (> 30 %), Detran-Liste 5,5 s (> 5 s), riser 1,35 s (> 1,2) | Pix/PDF-Kacheln raus (Caption), Liste 4,5 s, riser 1,2 s → 36,0 s |
| V6 | qa_check/qa_video (1. Encode) | BLOCK „fast leeres Bild“ 25,8–26,6 (grüne Vollfläche) = auch Raster B7 (Button-Grün als Fläche); Stillstand 17 %; Hook-Bewegung 0,5 | Vollfläche ersetzt durch Button-Zustand + Ergebnis-Karte (D5: Bild = „Preço e data na hora“), „Sem cadastro“ nur noch in der Caption; Mikro-Bewegung auf Karten/Zeilen/Gebäude; Karte wackelt im Hook stärker |

## V8 – nach unabhängiger Abnahme 28.10. (13-abnahme, Abschnitt „Abnahme Reel 21“)
| # | Befund | Fix |
|---|---|---|
| 21-1 | Kontaktzeile nur 4,17 s voll sichtbar | Endcard +1,0 s (Haupt 37,0 s, GMB 29,5 s), Einblendung 0,15 s ab 60 %, harter Schnitt zurück auf den Hook → voll sichtbar 5,5 s |
| 21-2 | CTA-Chip wirkt im Mitmach-Block wie 4. Antwort | Chip endet mit dem Schnitt auf den Mitmach-Block (28,5 s) |
| 21-3 | Hook-Bewegung YDIF 0,71 | Karte pendelt ±4,5° + Zoom 1,00→1,05→1,00 in 0–2,4 s → YDIF 1,06 |
| 21-4 | Überblendung Panel A→B, Panel B schiebt aus der Safe Zone | harte Schnitte 22,5 / 25,0 s, Panel B nur leichter Scale-in |
| 21-5 | UI-Schrift Panel B 30–32 px | neuer Live-Ausschnitt (cap4.js, Viewport 320 px): nur „Documentos padrão (certidões, diplomas, CNH…): preço fixo por documento“, 13 px × 810/260 = 40,5 px, Marker neu |
| 21-6 | „Sem tradução.“ ohne „em geral“ | „Em português? / Em geral, sem tradução.“ (Zeile 2 mit 60 px, sonst > x 900); IG-Absatz 2 „Em geral, sim“ |
| 21-7 | 28,4–28,7 fast leer | Ergebnis-Karte bis zum Schnitt, Mitmach-Zeilen ganz ab dem Schnitt |
| 21-8 | letzte Zeile beantwortet den Hook nicht | Endcard-Headline „Juramentada, preço na hora.“ |
| 21-9 | Figur/Karte bis y ≈ 1790 | Endcard ohne Karte, Figur 0,58 und winkend, sichtbar bis y ≈ 1495; Karte kommt erst zur Loop-Rückkehr zurück |
| 21-10 | Pegelsprung +6 dB an der Loop-Naht | Fade 0,15 s statt 0,4 s, Hook 0–2,3 s −2,5 dB, GMB-Ende +2 dB → Sprung 0,1 dB (Haupt), 1,6 dB (GMB) |
| V8-Prüfrunde | Figur lief schon bei 30,9 s während der Mitmach-Frage ins Bild | Einlauf auf 31,0–31,5 s gelegt |
