# Reel 30 – „CNH em espanhol: o verso paga à parte?“ (Di 10.11.2026)

Thema nach marketing/ENTSCHEIDEN.md (Lauf 03.11., Zeile in marketing/lernen/social.md): **CNH em espanhol → português, Preisbeispiel R$ 129 + „frente e verso = um documento“**. Kaufnachweis: pedidos 30 T. ohne Tests: CNH ES→PT 2× bezahlt (26.10. und 01.11., je 2 Seiten = Frente + Verso, je R$ 129), CNH EN→PT 1× (25.10.). Score 18 (K3 N2 E1 B0 L3).
- **Abgrenzung R21** (CNH estrangeira no Detran, 04.11.): R21 erklärt den Detran-Ablauf (180 dias, Liste, Carteira em português) **ohne Preis**. R30 = Preisfrage des Käufers (Verso, Tabelle ES→PT) + zwei neue Lernpunkte (Junta Comercial, Carteira na validade). Kein 180-dias-, kein Portugal-Block.
- Format **Objekt-Close-up** (Held-Objekt Licencia-Karte, die sich dreht) + ein echter Rechner-Ausschnitt (pc2). R29 Dokument-Tisch, R28 Etikett-Close-up.
- Grund **Névoa #BDCBCB** (R28 Pinho, R29 Pinho). Text Dark auf Névoa, Captions Weiß auf Dark-Pille mit Areia-Marker (Dark-Text), Chip und Belege Areia/Dark. Erlaubte Paare: Dark/Névoa, Weiß/Dark, Dark/Areia.
- Musik `lib/music.py` **funk 120 BPM** (R28 pop, R29 lofi), Master v2, −14 LUFS.
- **Eine Variable (Lernlog 03.11.):** LinkedIn-Text mit Preisfall + UTM-Link **in Zeile 1** (R28/R29: Zeile 3 bzw. 2). Grund: KW44 41 Social-Sitzungen < Soll KW45 50 → Conversion-Variable statt Design (REELS-REGELN-v2 „Soll Social-Sitzungen“). Alles andere bleibt wie R28/R29 (Quiz SIM/NÃO, Payoff 2,5 s, Chip ab 3 s, Endcard 6,6 s).

## Quellen (nur was die Quelle trägt)
| Q | Quelle | Wortlaut / Inhalt | Geöffnet |
|---|---|---|---|
| Q1 | Supabase `precos` (ypdvpytpajgkzglbzxwg) `WHERE ativo AND NOT placeholder` | `es / to_pt / cnh` valor_cents **12900** (updated 15.10.2026); `en / to_pt / cnh` 12900; `es / to_pt / passaporte` 12900, `rg` 12900 (nur LinkedIn) | SQL read-only 03.11.2026 = Memory preistabelle-live („Passaporte, RG, CNH: ES 129, EN 129/139“) |
| Q2 | Rechner live /orcamento-app/?lang=pt, „Como o preço é calculado“ pc2 | „Verso e Apostila (foto ou página) contam como parte do documento: sem custo extra.“ · pc1 „Documentos padrão (certidões, diplomas, CNH…): preço fixo por documento.“ | Playwright **ohne Mock** 03.11.2026 (capture_ui.js → shots/pc2_live.png, ungeschnitten) |
| Q3 | Rechner live „Como funciona“ | fl1 „Foto ou PDF, quantos precisar.“ · fl2 „Valor e data de entrega na hora.“ · fl4 „PDF juramentado com assinatura digital.“ | curl 03.11.2026 |
| Q4 | Detran-GO „Informações sobre CNH“ (goias.gov.br/detran/informacoes-sobre-cnh/) | Reconhecimento de habilitação estrangeira: „Habilitação do país de origem dentro do prazo de validade legal“ · „Tradução juramentada (exceto para CNH em idioma português)“ · „A tradução deverá ser feita por tradutor oficial juramentado“ (Verweis auf Lista de tradutores públicos der JUCEG) · „A Habilitação Estrangeira fora do prazo de validade não será reconhecida pelo Brasil“ | WebFetch 03.11.2026 (selbst geöffnet) |
| Q5 | Detran-PR „Solicitar registro de carteira de motorista estrangeiro“ und Detran-SC Portaria 1108/2025 art. 8º | PR: carteira original e na validade, tradução juramentada (tradutor da Junta Comercial). SC: habilitação estrangeira original e válida; tradução por tradutor público juramentado; § 1º língua portuguesa ohne Übersetzung | Whitelist-Präzedenz: R21 STORYBOARD Q3/Q4, unabhängig abgenommen (2e835fd/5f77fa1) |
| Q6 | Supabase `pedidos` (nur intern, nicht öffentlich) | CNH ES→PT bezahlt 26.10. + 01.11. (je 2 Seiten, R$ 129), CNH EN→PT 25.10. | SQL read-only 03.11.2026, Tests ausgeschlossen |

Nicht verwendet: „a partir de“, Endpreis-/Rabatt-Versprechen, Eil-Option, Papier-Versand, Fristen, 180 dias (R21), Mercosul, Ländernamen, Sprachlisten, Kundenfälle, Zertifikats-Infrastruktur der Signatur.

## Zeitachse Hauptfassung (31,0 s, 120 BPM, Schlag 0,5 s)
Text x 90–900, y 300–1500. Caption-Pillen ab y 320, CTA-Chip y 552, Objektzone y 700–1360, Beleg y 1384.

| Zeit | Held-Objekt + Handlung | Text im Bild | Q | Ton |
|---|---|---|---|---|
| 0,0–3,0 | **Frame 0 fertig:** Licencia-Karte „LICENCIA DE CONDUCIR“ (Requisite ohne Daten) pendelt ab Frame 1 + Karten SIM / NÃO. **2,5 Payoff:** NÃO Areia mit Haken, SIM blass, Karte dreht auf die Rückseite (Punch) | Hook „CNH em / espanhol: / o verso paga / **à parte?**“ (7 W.) · Chip „Comenta SIM ou NÃO“ | Q2 | pop 0,03 · impact 2,5 |
| 3,0–6,0 | Vorder- und Rückseite (Mini-Karten) schieben zusammen; darunter **echter Rechner-Ausschnitt pc2** | „Frente e verso: / **um documento só.**“ · Beleg „No site: preço por documento“ | Q2 | pop 3,0 · stamp 4,5 |
| 6,0–9,0 | Preis-Etikett „CNH · espanhol → português · R$ 129“ (Pfeil = SVG), Punch 7,0 | „CNH em espanhol / **R$ 129**“ · Beleg „Para português · preço de tabela“ | Q1 | whoosh 6,0 · impact 7,0 |
| 9,0–12,0 | Detran-Gebäude + Blatt „TRADUÇÃO JURAMENTADA“, Siegel 10,5 | „Pro Detran, em geral: / **juramentada.**“ · Beleg „Ex.: Detran-GO, PR e SC“ | Q4, Q5 | whoosh 9,0 · stamp 10,5 |
| 12,0–15,0 | Register-Buch mit Liste, Haken 12,5 (Punch) | „Tradutor registrado / **na Junta Comercial.**“ · Beleg „Ex.: Detran-GO e PR“ | Q4, Q5 | whoosh 12,0 · impact 12,5 |
| 15,0–18,0 | Licencia + Kalender, Kreuz 16,0 | „Carteira vencida? / **Em geral, não vale.**“ · Beleg „Detran-GO: dentro da validade“ | Q4, Q5 | whoosh 15,0 · stamp 16,0 · (Punch 17,0) impact |
| 18,0–21,0 | Handy mit zwei Bildern (Frente / Verso), Haken 19,5 | „Envie os dois lados: / **foto ou PDF.**“ · Beleg „No site: foto ou PDF“ | Q3 fl1 | whoosh 18,0 · pop 19,5 |
| 21,0–24,0 | Pin + Gebäude + Lupe, Punch 22,0 | „Confira no Detran / **do seu estado.**“ · Beleg „As regras variam por estado“ | Q4/Q5 (Vorsicht) | whoosh 21,0 · impact 22,0 · click 23,0 |
| 24,0–30,7 | **Endcard** (Absender traduzme), Licencia klein | „CNH em / espanhol? / **Verso incluído.**“ · Chip · traduzme.com.br · (61) 99803-8363 | Q2 / CTA | hit + stamp 24,0 |
| 30,7–31,0 | harter Schnitt auf Frame 0 | Hook | Loop | – |

Szenenwechsel alle 3,0 s (0,33/s). Punches 2,5 · 7,0 · 12,5 · 17,0 · 22,0 (Abstand ≥ 4 s). CTA-Chip 3,0–24,0. Rechner-/Preis-Anteil 3–9 s = 6 von 24 s = 25 % (≤ 30 %); Preis-Szene startet 6,0 s. Endcard voll 24,12–30,7 = 6,6 s.
Payoff 2,5 s zeigt nur die Antwort NÃO (Verso ohne Aufpreis), keinen Preis.

## GMB-Fassung (28,0 s)
Ohne 18,0–21,0 (Foto ou PDF). Chip/Endcard „Preço na hora no site“, kein „link na bio“. Endcard 21,0–27,7, Loop 27,7, END 28,0. gmb/reel.html = reel.html mit `GMB=1` und Pfaden `../`.

## Kritiker-Runden Storyboard (getrennte Durchgänge, je ein Blickwinkel)
| Runde | Fakten | Design | Hook/Tempo | Conversion/LinkedIn |
|---|---|---|---|---|
| 1 | (a) „Verso não paga à parte“ nur für Documento padrão belegt (pc2 + pc1 nennt CNH) → im Bild Beleg „No site: preço por documento“, Caption sagt nichts über andere Dokumente. (b) „Carteira vencida não vale“ ist eine Detran-Regel (GO wörtlich), nicht bundesweit geprüft → „Em geral“ + Beleg „Detran-GO“. (c) „Tradutor da Junta“: GO sagt „tradutor oficial juramentado“ + JUCEG-Liste, PR „tradutor da Junta Comercial“ → Beleg „Ex.:“. (d) Preis nur mit Dokument + Richtung („CNH em espanhol“ + „Para português · preço de tabela“), Endcard ohne Preis (Lehre 28-A). | Névoa-Grund: Weiß auf Névoa verboten → Captions als Dark-Pille mit Weiß; Hook Dark auf Névoa; Chip/Beleg Areia/Dark (nur 3 Flächenfarben + Papier). Hook-Zeile „CNH em espanhol:“ wäre bei 104 px > 900 → 4 Zeilen. | Hook 7 W. ≤ 8; Payoff 2,5; Wortzahl Frame 0: Hook 7 + Chip 4 + SIM/NÃO 2 = 13 > 12 → Karten-Titel „LICENCIA DE CONDUCIR“ per ignoreText begründen, Chip auf „Comenta SIM ou NÃO“ (4). | Chip „Preço na hora · link na bio“ ab 3,0; LinkedIn B2B mit Link in Zeile 1 (Variable); YT-Titel mit Dokument + Richtung + Preis; IG/TikTok ohne Antwort und ohne Preis. |
| 2 | Alle Bildaussagen gegen Q1–Q5 gelesen: gedeckt. Kein „sempre/nunca“, kein „a partir de“. | „Envie frente e verso,“ bei 66 px ≈ 830 + 90 > 900 → „Envie os dois lados:“. Pillen-Breiten werden am Video gemessen (qa_frames safe). | Standzeit je Caption 2,92 s ≥ max(1,8; 0,4 × 7 W.) ✓; ≤ 4 W./Zeile ✓ | GMB 28,0 s ohne „link na bio“ ✓; UTM reel30 je Kanal. |
| 3 | keine offenen Mängel | keine offenen Mängel | keine offenen Mängel | keine offenen Mängel |
Video-Runden: /mnt/project-files/social/reels/reel30-texte.md, „Prüfprotokoll“.
