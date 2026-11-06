# Reel 33 – „Seu laudo em inglês: fixo ou por página?“ (Fr 13.11.2026)

Thema nach marketing/ENTSCHEIDEN.md (Lauf 06.11., Zeile in marketing/lernen/social.md): **Laudo/Texto em inglês → português = preço por página; Documento padrão = preço fixo; Preisbeispiel Laudo = Texto especial inglês → português a partir de R$ 139 por página (Tabelle)** (korrigiert nach Abnahme 33-A).
Kaufnachweis (nur intern, nie öffentlich): pedidos 30 T. ohne Tests und ohne interne Adressen: EN→PT Carta clínica (2 S., als Text/Lauda berechnet) 1× bezahlt am 03.11.; analises 30 T. en/outro 11 Uploads (Texte ohne Dokumenttyp). Score **20** (K3 N1 E1 B2 L3), Kandidaten siehe lernen/social.md.
- **Abgrenzung:** kein CNH-Thema (R21/R30/R32), kein Certidão-de-nascimento-ES (R28), kein Diploma/Histórico ES (R29), keine Certidão FR (R31), keine „já apostilada“ (R23). Neu: **Preislogik Text vs. Documento padrão** – erstes Reel zu Laudos/Contratos (pc3).
- **Format (Pflicht-Wechsel):** **Kinetic-Type + Papier-Seiten**: Seiten fächern auf und bekommen Seitenzahlen (1–3, 1–4), Stempel „POR PÁGINA“, Anhänger „R$ ?“. Kein Split-Screen (R32), kein Dark-Objekt-Close-up mit Antwortkarten (R31), kein pc2-Rechnerausschnitt (R30/R31). Der Formatwechsel ist Regelpflicht, **nicht** die Test-Variable.
- Grund **Sálvia #97B9A8** (R32 Areia, R31 Dark, R30 Névoa). Paare: Dark auf Sálvia (Hook, Endcard, 5,7 : 1), Weiß auf Dark (Caption-Pillen, Mitmach-Chip, 12,1 : 1), Dark auf Areia (Marker, CTA-Chip, Belege, Stempel, 9,2 : 1), Dark auf Papier (Seiten, Etikett). Kein Weiß auf Sálvia/Areia.
- Musik `lib/music.py` **lofi 120 BPM** (Erklär-Tisch/Dokumente, Raster E2), Tonart D, seed 33 (R32 pop, R31 bossa, R30 funk), Master v2, −14 LUFS.
- **Eine Variable:** Mitmach-Antwort mit **Inhaltswörtern „FIXO ou PÁGINA“** statt „SIM ou NÃO“ (R30, R32) – Ein-Wort-Antwort auf eine Inhaltsfrage (v3 #7). Alles andere wie R32: Hook-Länge, Endcard-Kopf „Envie a foto: preço na hora.“, LinkedIn-Link in Zeile 1, Payoff 2,5 s, Chip ab 3 s.

## Quellen (nur was die Quelle trägt)
| Q | Quelle | Wortlaut / Inhalt | Geöffnet |
|---|---|---|---|
| Q1 | Supabase `precos` (ypdvpytpajgkzglbzxwg) `WHERE ativo AND NOT placeholder` | `en / to_pt / tecnica` **13900** (Laudo/Contrato = texto especial) · `en / to_pt / comum` 11900 (nur texto comum wie Cartas/E-Mails, nur YT/LinkedIn als Gegenbeispiel) · Documentos padrão EN→PT ab 12900 | SQL read-only 06.11.2026 |
| Q1b | Einstufung comum/técnica | Edge-Function `analisar` (Prompt v29+): técnico = „jurídico/judicial (contrato, sentença …), médico (laudo, exame, receita, prontuário, relatório médico) …“; Rechner `precoItem` `k = tec ? "tecnica" : "comum"`; Rechner-Info „laudos periciais … texto especial“ | Abnahme 33-A 06.11.2026; analises en/outro 60 T.: 9 von 11 técnico, bezahlter EN-Text ebenfalls técnico |
| Q2 | Rechner live /orcamento-app/?lang=pt, Box „Como o preço é calculado“ pc3 | „**Textos longos e várias páginas** (contratos, laudos…): preço por página.“ | curl 06.11.2026 (HTTP 200) |
| Q3 | ebd. pc1 | „**Documentos padrão** (certidões, diplomas, CNH…): preço fixo por documento.“ | curl 06.11.2026 |
| Q4 | ebd. fl1/fl2 (+ fl3/fl4 nur LinkedIn) | „Foto ou PDF, quantos precisar.“ · „Valor e data de entrega na hora.“ · „Pague por Pix“ · „PDF juramentado com assinatura digital.“ | curl 06.11.2026 |
| Q5 | ebd. Info-Text Via física | „… na dúvida, confirme antes com quem vai receber.“ | curl 06.11.2026 |
| Q6 | Supabase `pedidos`/`analises` (nur intern) | EN→PT Carta clínica 1× bezahlt (03.11.), en/outro 11 Uploads | SQL read-only 06.11.2026, Tests/interne Adressen ausgeschlossen |

Nicht verwendet: Lauda-Definition (Zeichenzahl, nicht öffentlich in der UI), Einstufung comum/técnica (im Bild nur „Texto especial · preço de tabela“), Rabatte, Fristen, Eil-Option, Papier-Versand, Verso/Apostila (R23/R30), Behördenlisten, Gesundheitsdaten, Kundenfälle, Zertifikats-Infrastruktur der Signatur, Sprachlisten.

## Zeitachse Hauptfassung (31,0 s, 120 BPM, Schlag 0,5 s)
Text x 90–900, y 300–1500. Caption-Pillen ab y 320, CTA-Chip y 552, Objekte y 780–1380, Beleg y 1384.

| Zeit | Bild | Text im Bild | Q | Ton |
|---|---|---|---|---|
| 0,0–3,0 | **Frame 0 fertig:** Laudo-Stapel (3 Seiten, Kreuz-Symbol, keine Daten) wippt, Anhänger „R$ ?“ pendelt. **2,5 Payoff:** Stempel „POR PÁGINA“ knallt auf den Stapel, Punch | Hook „Seu laudo / em inglês: / fixo ou / **por página?**“ (8 W.) · Chip „Comenta FIXO ou PÁGINA“ | Q2 | pop 0,03 · impact 2,5 |
| 3,0–6,5 | Seiten fächern auf, Seitenzahlen 1–3 (3,5) | „Laudo é texto: / **preço por página.**“ · Beleg „Textos longos: preço por página“ | Q2 | whoosh 3,0 · pop 3,5 |
| 6,5–10,0 | Certidão · Diploma · CNH (Requisiten ohne Schrift), je Haken 7,0, Punch | „Certidão, diploma, / CNH: **preço fixo.**“ · Beleg „Documento padrão: preço fixo“ | Q3 | whoosh 6,5 · impact 7,0 |
| 10,0–13,5 | Contrato, 4 Seiten, Zahlen 1–4 nacheinander (10,5/11,0/11,5/12,0), Punch 12,0 | „Contrato também: / **por página.**“ · Beleg „Contratos, laudos: por página“ | Q2 | whoosh 10,0 · pop 10,5 · pop 11,5 · impact 12,0 |
| 13,5–17,0 | 13,5 Laudo-Seite groß · 14,0 Preis-Etikett „inglês → português · R$ 139 · por página“ | „Laudo em inglês: / **a partir de R$ 139**“ · Beleg ab 14,5 „Texto especial · preço de tabela“ | Q1, Q1b | whoosh 13,5 · stamp 14,0 |
| 17,0–20,5 | Handy fotografiert eine Seite, Haken 18,5 (keine UI-Schrift) | „Foto ou PDF: / **preço na hora.**“ · Beleg „No site, antes de pagar“ | Q4 | whoosh 17,0 · click 18,5 |
| 20,5–24,0 | Gebäude (Órgão) + Laudo, „?“ → Haken 21,5, Punch 22,0 | „Pede juramentada? / **Confirme no órgão.**“ · Beleg „Na dúvida, confirme antes“ | Q5 (Handlungsempfehlung) | whoosh 20,5 · pop 21,5 · impact 22,0 |
| 24,0–30,7 | **Endcard** (Absender traduzme), Laudo klein | „Laudo em / inglês? / **Envie a foto:** / **preço na hora.**“ · Chip „link na bio“ · traduzme.com.br · (61) 99803-8363 | Q4 | hit + stamp 24,0 |
| 30,7–31,0 | harter Schnitt auf Frame 0 | Hook | Loop | – |

Szenenwechsel alle 3,5 s (0,29/s). Punches 2,5 · 7,0 · 12,0 · 22,0 (Abstand ≥ 4,5 s). CTA-Chip 3,0–24,0. Preis-/Kauf-Anteil 13,5–20,5 = 7 von 24 s = 29 % (≤ 30 %), Preis frühestens 13,5 s. Endcard 24,0–30,7 = 6,7 s, ohne Preis.
Preis-Szene gestaffelt (Caption 13,5 · Etikett 14,0 · Beleg 14,5), damit je 0,5 s ≤ 12 neue Wörter (C5). Dokument („Laudo“), Richtung („inglês → português“) und Preis stehen ab 14,0 s gleichzeitig im Bild.

## GMB-Fassung (27,5 s)
Ohne 17,0–20,5 (Foto ou PDF). Chip „Preço na hora no site“, Endcard-Chip „no site“, kein „link na bio“. Endcard 20,5–27,2, Loop 27,2, END 27,5. gmb/reel.html = reel.html mit `GMB=1` und Pfad `../fonts`.

## Kritiker-Runden Storyboard + Bild (getrennte Durchgänge, je ein Blickwinkel; kein Sub-Agent verfügbar)
| Runde | Fakten | Design | Hook/Tempo | Conversion/LinkedIn |
|---|---|---|---|---|
| 1 | **F1:** „Laudo médico“ im Hook gestrichen → „laudo“ (pc3 nennt „laudos“ allgemein; kein Gesundheitsbezug nötig). **F2:** Preis: „R$ 119 por página“ allein wäre für technische Laudos falsch (Tabelle técnica 139) und für rabattierte Endpreise keine Untergrenze → „a partir de R$ 119“ (niedrigster EN→PT-Listenwert, Regel preistabelle-live) + Beleg „Texto comum · preço de tabela“; técnico 139 nur in YT/LinkedIn ausgeschrieben. **F3:** „Pede juramentada?“ ohne Rechtsaussage, nur „Confirme no órgão“ (Q5-Wortlaut im Beleg). **F4:** „Lauda = Zeichenzahl“ steht nicht in der sichtbaren UI → nicht verwendet, öffentlich nur „por página“ wie pc3. | Sálvia-Grund; Hook Dark, Marker Areia. DOM-Messung V1: Marker-Spans x 88 (margin −8 bei left 96, auch Endcard) → Hook/Endcard left 104 → x ≥ 96. Stempel unten y 1253 > 1250 → y 1116 → max. 1239. Caption „Certidão, diploma, CNH:“ wäre x ≈ 990 → zweizeilig „Certidão, diploma, / CNH: preço fixo.“ | qa_frames V1: `empty` 10,0 (Contrato-Seiten Pop ab Skala 0,7) → Pop ab 0,9 (D2), ebenso Etikett und Seitenzahlen. `words` Loop-Naht 30,7 (13 W.: Hook 8 + Chip 4 + „R$ ?“) → ignoreText nur exakt „R$ ?“ (Frage-Requisite) mit Grund. `words`-Warnung 13,0–13,6 (Caption + Etikett + Beleg zugleich 13 W.) → gestaffelt 13,5/14,0/14,5. | Chip ab 3,0; GMB ohne „link na bio“; Preis nur mit Dokument + Richtung; Endcard ohne Preis. IG/TikTok: Antwort („por página“) und Preis tabu, Zeile 2 „Resposta no vídeo 👀“. LinkedIn B2B: escritórios (contratos), RH/mobilidade (laudos, relatórios), UTM in Zeile 1. |
| 2 | Alle Bildzeilen gegen Q1–Q5 gelesen: gedeckt. Kein „sempre/nunca“, kein Superlativ, keine Rechtsaussage, keine Kundendaten. Sperr-grep 0. | Kontaktbögen V2 angesehen; 13,5–14,0 Lücke im Held-Objekt → Laudo-Seite 1,5× bis das Etikett kommt. DOM-Maß aller Text-Elemente inkl. Requisiten (Seitenzahlen, „R$ ?“, Stempel, Etikett, „?“) 10 fps: 0 außerhalb x 90–900 / y 300–1500; Etikett x 209–871, y 778–1228 (≤ 1250). | Hook 8 W. (Seu·laudo·em·inglês·fixo·ou·por·página), Frame 0 fertig, Payoff 2,5 s, 1. Lernpunkt 3,0 s; Captions 3,42 s ≥ max(1,8; 0,4 × 4 W.); ≤ 4 W./Zeile; Szenen 3,5 s. | Weiterschick-Satz „Manda pra quem tem laudo ou contrato em inglês pra traduzir“ (IG/TikTok/YT). |
| 3 (getrennt, Schlussrunde) | Sperr-grep + Fakten erneut über reel.html, gmb/reel.html, audio.py und alle Texte. | Kontaktbögen der Endfassung (Haupt + GMB) alle angesehen. | Gate siehe reel33-texte.md. | **keine offenen Mängel** |

## Video-Runden (am gerenderten Video, nach Runde 2)
- V3 Hook/Tempo: qa_check YDIF 0–1 s 0,31 → 0,64 → **0,89** (Stapel wippt ±36 px / ±14°, untere Seiten gegenläufig, Anhänger pendelt ±24° und ±26 px; im Loop tb = 0 = Frame 0).
- V4 Design (Kontaktbögen 2,5–2,9 s): Stempel „POR PÁGINA“ wurde vom Anhänger „R$ ?“ überdeckt → Stempel 400 px breit, Mitte x 372, über dem Anhänger (z-Reihenfolge). DOM-Maß Stempel x 100–641, y 1001–1230.
- V5 Ton: Spitze Mix gegenüber Musik im selben 0,2-s-Fenster (Stems): impact 7,0 lag +11 dB über der Musik (leiser Takt im lofi) → Gains gesenkt (impact 2,5 .6 · 7,0 .2 · 12,0 .4; whoosh 3,0 .45 · 17,0/20,5 .6; pop 3,5/10,5 1,2). Danach alle SFX ≤ +3,8 dB (Haupt) / ≤ +3,7 dB (GMB). LRA 3,3 / 3,1.
- V6 Loop: letzter Frame = Frame 0 pixelgleich (beide Fassungen), SSIM 0,996 / 0,997.
- V7 Kontaktbögen der Endfassung: Haupt 0–31 s alle 16 Bögen, GMB 02/16/20/26 (0–17 s identisch mit Haupt bis auf Chip-Text). Keine offenen Mängel.

## Abnahme-Fix 06.11. (33-A, 33-1, 33-2, 33-3)

- **33-A (blockierend):** Runde-1-Entscheidung F2 war falsch: Laudo und Contrato laufen im Rechner als texto especial (lauda técnica, R$ 139), nicht als texto comum (R$ 119). Bild (beide HTML): „a partir de R$ 139“, Etikett „R$ 139“, Beleg „Texto especial · preço de tabela“; Texte in reel33-texte.md nachgezogen. Lehre: Preis-Einstufung vor dem Bau im analisar-Prompt und in precos prüfen.
- **33-2:** SFX stamp 24,0 → 1.0, impact 7,0 → .15, click 18,5 → 1.6 (mit 1.8 lag True Peak nach AAC bei genau −1,0 dBTP an der K.-o.-Grenze; 1.6 → −1,8 dBTP); nachgemessen (Spitze Mix vs. Musik, 0,2-s-Fenster): click +2,5 dB, stamp 24 +1,6 dB, impact 7 +2,6 dB, max. +3,7 dB (impact 12,0).
- **33-3:** Quellen-Tabelle Q1 → `tecnica` 13900 + Q1b Einstufung.
- **33-1:** Länge einheitlich: Datei 31,0 s, Loop-Punkt/Endcard-Ende 30,7 s (GMB Datei 27,5 s, Loop-Punkt 27,2 s).
