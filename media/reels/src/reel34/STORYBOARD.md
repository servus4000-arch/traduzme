# Reel 34 – „Sua certidão em árabe: quanto custa?“ (Sa 14.11.2026)

Thema nach ENTSCHEIDEN (Lauf 07.11., marketing/lernen/social.md): Preisbeispiel **Certidão em árabe → português, R$ 299 na tabela**, Árabe-Fall (jedes 3. Reel AR/DE/ES).
Format (Pflicht-Wechsel): **Dokument-Tisch** in Draufsicht mit Kamera-Fahrt über den Tisch (Pan je Szene) · Grund **Pinho #376259** mit dunkler Tischplatte (Dark #1F3B35) · Musik `music.py` **funk 120 BPM** (Raster E2: Preis/Rechner → funk).
R33 = Kinetic-Type + Papier-Seiten / Sálvia / lofi · R32 = Split-Screen / Areia / pop · R31 = Dark / bossa / Objekt-Close-up → alles anders.
**Eine Variable:** Mitmach als **freie Zahl** („Comenta seu chute em R$“ = Ein-Wort-Antwort Zahl) statt Auswahl aus zwei Wörtern (R28–R32 SIM/NÃO, R33 FIXO/PÁGINA).

## Preis-Einstufung (Lehre 33-5, vor dem Bau geprüft 07.11.2026)
| Prüfung | Befund |
|---|---|
| precos (SELECT `ativo and not placeholder`, ar/to_pt) | certidao de nascimento / casamento / obito / divorcio / negativa je **29900**, inteiro teor 34900; lauda comum 22900, técnica 23900 |
| analisar-Prompt (Edge-Function, nucleo.ts) | „certidao de nascimento“ umfasst ausländische Geburtsregister und „certidões antigas manuscritas“; **„Certidões, actas e certificates ESTRANGEIROS nunca são inteiro teor: ficam no tipo da certidão“** → nie 34900; Certidões = tecnico=false; Apostila/legalização consular/verso/Folgeseite ohne eigenen Kopf = **peça** (kein Aufpreis) |
| Ist-Daten analises | AR-Upload 21.10.: arabische Geburtsurkunde → typ „certidao de nascimento“ (nicht outro/lauda) |
| Ist-Preise precos_ia | Einzeldokument AR → PT 26.10. und 03.11.: tabela 29900 = final 29900 (keine Ermäßigung bei 1 Dokument). Mehrere Dokumente können günstiger werden → im Bild „na tabela“, nie „a partir de“ (niedrigster Dokumentpreis AR→PT ist ebenfalls 299) |
| Ergebnis | Eine Certidão em árabe (Geburt, Ehe, Tod, Scheidung) kommt im Rechner als Documento padrão mit **R$ 299 (Tabelle)** heraus. Gezeigt wird nur dieser Wert, mit Dokument + Richtung. |

## Ablauf (120 BPM, Schlag 0,5 s; Szenenwechsel alle 3,5 s)
| Zeit | Bild | Text (Bild) | Quelle |
|---|---|---|---|
| 0,0–3,0 | Tisch von oben: arabische Certidão (Schriftlinien angedeutet, Siegel, ohne Daten), Preis-Anhänger „R$ ?“ pendelt ab Frame 1 | Hook „Sua certidão / em árabe: / quanto / custa?“ (6 W., Frame 0 fertig) + Mitmach „Comenta seu chute em R$“ | – |
| 2,5 | Payoff: Anhänger klappt zum Etikett „árabe → português · R$ 299“ (Punch + impact) | Etikett (Richtung + Preis) | Q1 |
| 3,0–6,5 | Etikett bleibt auf der Certidão | „Árabe → português: / R$ 299 na tabela.“ · Beleg „Certidões · preço de tabela“ · CTA-Chip ab 3,0 | Q1, Q2 |
| 6,5–10,0 | Schloss springt aufs Etikett (7,0 Punch) | „Preço fixo / por documento.“ · Beleg „Documento padrão: preço fixo“ | Q3 |
| 10,0–13,5 | Fahrt: Frente, Verso, Apostila fächern auf, Klammer + Haken (12,0 Punch) | „Verso e apostila: / sem custo extra.“ · Beleg „Parte do documento“ | Q4 |
| 13,5–17,0 | Fahrt: Certidão bekommt zwei Siegel, Globus | „Antes: apostila / ou legalização.“ · Beleg „Em geral, no país de origem“ | Q5 |
| 17,0–20,5 | Fahrt: Übersetzungsblatt, Stift unterschreibt, Siegel (19,0 Punch) | „A juramentada: / feita no Brasil.“ · Beleg „Em geral · Polícia Federal“ | Q5 |
| 20,5–24,0 | Fahrt: Handy fotografiert die Certidão, Haken (22,0) | „Foto ou PDF: / preço na hora.“ · Beleg „No site, antes de pagar“ | Q6 |
| 24,0–27,5 | Fahrt: PDF-Blatt, Haken-Siegel (25,0 Punch) | „Chega em PDF com / assinatura digital.“ · Beleg „Na dúvida, confirme no órgão“ (PDF-Blatt fährt ohne Kopfschrift ein, „PDF“ ab 24,5) | Q7, Q8 |
| 27,5–34,2 | Endcard auf Pinho/Tisch, kleine Certidão unten rechts | „Certidão em / árabe? / Envie a foto: / preço na hora.“ · „link na bio“ · traduzme.com.br · WhatsApp (61) 99803-8363 · **kein Preis** | – |
| 34,2–34,5 | harter Schnitt auf Frame 0 (Loop) | Hook | – |

GMB (27,5 s): ohne 17,0–24,0 (Brasil + Foto/PDF), Chip „Preço na hora no site“, Endcard-Chip „no site“, Endcard 20,5–27,2, eigener Loop.

## Quellen
- **Q1** Supabase `precos` ar/to_pt certidões 29900 (SELECT 07.11.2026) + analisar-Prompt (ausländische Certidão = Typ Certidão, nie inteiro teor) + precos_ia Einzeldokument AR→PT final 29900.
- **Q2** „na tabela“ / „preço de tabela“: Memory preistabelle-live (Endpreis kann unter Liste liegen).
- **Q3** Rechner pc1 „Documentos padrão (certidões, diplomas, CNH…): preço fixo por documento.“ (curl /orcamento-app/?lang=pt 07.11., HTTP 200)
- **Q4** Rechner pc2 „Verso e Apostila (foto ou página) contam como parte do documento: sem custo extra.“ (curl 07.11.)
- **Q5** PF-FAQ (Whitelist 10-gegenkritik Abschnitt 0/3): „de maneira geral … legalizados e traduzidos“, Übersetzung durch tradutor juramentado im Brasil, auch mit Apostila; Ausnahmen → „Em geral“. gov.br aus dieser Sandbox gesperrt (Proxy 403), daher nur Whitelist-Stand.
- **Q6** Rechner „Foto ou PDF, quantos precisar.“ / „Valor e data de entrega na hora.“ (curl 07.11.)
- **Q7** Rechner „PDF juramentado com assinatura digital.“ (curl 07.11.)
- **Q8** Rechner-Info „… na dúvida, confirme antes com quem vai receber.“ (curl 07.11.)
- AR-Regeln (v2 #12): keine Via física, keine Urgência im Bild; Ziel Brasil → keine „PDF no exterior“-Zeile nötig.

## Kritiker-Runden Storyboard (getrennte Durchgänge, kein Sub-Agent)
**Runde 1**
- Fakten: (a) „R$ 299“ ohne Richtung im Payoff → Etikett trägt „árabe → português“. (b) Hook „Sua certidão“ deckt Geburt/Ehe/Tod/Scheidung (alle 29900) ✓; inteiro teor ausgeschlossen (Prompt) ✓. (c) „Apostila ou legalização: no país de origem“ absolut → Beleg „Em geral · Polícia Federal“. (d) Kein Land nennen (zweisprachige Urkunden könnten als Französisch erkannt werden → anderer Preis).
- Design: (a) „quanto custa?“ in einer Zeile ≈ x 930 → Hook auf 4 Zeilen. (b) Etikett muss als Kerninfo x 90–900, y ≤ 1250 bleiben, auch beim Punch (Lehre 32-B). (c) Text-Objekte nie während einer Fahrt sichtbar (safe/cut) → Etikett/PDF erst nach der Fahrt.
- Hook/Tempo: Payoff 2,5 s ✓; Caption-Zeilen ≤ 4 Wörter; Standzeit 3,42 s ≥ 2,8 s ✓.
- Conversion: IG/TikTok ohne Preis und ohne Antwort; Teilen-Satz Caption; LinkedIn B2B Zeile 1 mit UTM.
**Runde 2**
- Fakten: „sem custo extra“ nur pc2-wörtlich (Apostila des Originals), nicht die Option Apostilamento (Lehre 30-9) → Beleg „Parte do documento“; LinkedIn präzisiert „página da apostila do original“.
- Design: Beleg-Pillen ≤ 830 px Breite; Endcard-Zeilen über der Tischplatte (Weiß/Dark ✓).
- Conversion: Mitmach Zahl ist echte Inhaltsfrage (Raster v3 #7), kein Köder ✓.
**Runde 3 (getrennt):** keine offenen Mängel in allen vier Blickwinkeln.

## Kritiker-Runden Video (nach dem Bau)
- V1 Design/Safe Zone: qa_frames blockte 3 Captions (x 909–914: „Apostila ou legalização:“, „Tradução juramentada:“, „com assinatura digital.“) → umformuliert (s. Tabelle). Anhänger „R$ ?“ ragte per DOM-Maß bis x 914 (per ignoreText vom Gate ausgenommen) → x 772 → 744, jetzt ≤ 886. Schloss verdeckte „português“ → unter den Preis (x ≤ 860). Haken/Siegel überdeckten Beleg-Pillen → versetzt. Etikett-Kopf beim Pop 41 px → Pop ab Skala .92.
- V2 Tempo/Bild: 24,3–24,4 leerer Tisch (PDF erst ab 24,5) → PDF-Blatt fährt mit, nur der Kopf „PDF“ erscheint nach der Fahrt.
- V3 Ton: Payoff-impact 2,5 s +6,5 dB (400-ms-Fenster) → Gain .7 → .45; Pops/Klick ≈ 0 dB → angehoben; danach alle 18 SFX ≤ +4,0 dB (Kurzzeit) bzw. ≤ +3,4 dB (Spitze/Spitze).
- V4 Kontaktbögen: alle 18 Haupt-Bögen (0–34,5 s) und GMB 16/26 (Schnitt 17,0, Endcard, Loop) angesehen; GMB 0–16 s bildgleich mit Haupt bis auf den Chip-Text. Keine offenen Mängel.
