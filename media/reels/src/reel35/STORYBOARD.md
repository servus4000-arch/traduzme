# Reel 35 – „Seu histórico pro exterior: precisa do original?“ (Mo 16.11.2026)

Thema nach ENTSCHEIDEN (Lauf 09.11., marketing/lernen/social.md): **Histórico escolar português → inglês**, Preisbeispiel **R$ 149 + R$ 49 por página extra (tabela)**. Score 21 (K2 N2 E1 B3 L3).
Format (Pflicht-Wechsel): **Handy-Close-up** – Held-Objekt Handy (760 px = 70 % Breite), Bildschirm-Inhalt wechselt je Szene per Whip auf dem Schlag, keine Kamera-Fahrt über einen Tisch · Grund **Névoa #BDCBCB** · Musik `music.py` **pop 120 BPM** (Raster E2: Rechner/Preis → funk oder pop).
R34 = Dokument-Tisch Draufsicht + Kamera-Fahrt / Pinho / funk · R33 = Kinetic-Type / Sálvia / lofi → alles anders.
**Eine Variable (Wochenfazit KW45, fest vorgegeben):** Dokument + Richtung + Preis schon in **Frame 0** als Etikett im Hook-Bild („Histórico escolar · português → inglês · R$ 149 + R$ 49 por página extra“). Hook-Frage ist **nicht** die Preisfrage, sondern ein Kauf-Zweifel („precisa do original?“). Cover 1,0 s zeigt das Etikett.
Vorhersage: TikTok Ø Sehdauer +20 % gegenüber Median R28–R34 (72 h). Messung Do 19.11.2026.

## Preis-Einstufung (Lehre 33-5, vor dem Bau geprüft 09.11.2026)
| Prüfung | Befund |
|---|---|
| precos (SELECT `ativo and not placeholder`, en/from_pt) | `historico escolar` valor_cents **14900**, extra_pag_cents **4900** (categoria documento); diploma superior 13900; lauda comum 11900 / tecnica 13900 |
| analisar-Prompt (nucleo.ts, SABER_TIPOS) | „historico escolar: histórico escolar, transcript of records …; 1-10 páginas, **cobrado POR PÁGINA (cada página conta)**“; históricos = tecnico=false; Folgeseiten = `historico escolar#cont` (Preis je weitere Seite, nie gratis); „diploma + histórico de 7 páginas = 2 documentos“ |
| pix-cob v51 `precoItem` | Dokument mit extra_pag: `valor_cents + extra_pag_cents × (paginas − 1)` → 1 Seite 149, 4 Seiten 296, 6 Seiten 394 |
| Ist-Preise precos_ia (en/from_pt) | 05.11. Histórico 4 S. tabela 29600 · 09.11. Histórico 6 S. tabela 39400 · 08.11. Diploma + Histórico 5 S. tabela 48400 (= 139 + 149 + 4×49) → Formel bestätigt. Endpreis kann unter der Tabelle liegen (05.11. final 27900) → im Bild „tabela“, nie „a partir de“ |
| Randfall | Mehrere Dokumente in **einer** Datei → Lauda (outro). Im Video nicht thematisiert, keine falsche Aussage (Bild zeigt nur den Histórico) |
| Ergebnis | Ein Histórico escolar português → inglês kommt im Rechner als Dokument mit **R$ 149 (1ª página) + R$ 49 por página extra (tabela)** heraus. Gezeigt wird nur das, immer mit Dokument + Richtung. |

## Ablauf (120 BPM, Schlag 0,5 s; Szenen je 3,5 s)
| Zeit | Bild | Text (Bild) | Quelle |
|---|---|---|---|
| 0,0–2,95 | Handy unten (Sucher auf Histórico, Ecken pulsieren ab Frame 1), Etikett darüber | Hook „Seu histórico / pro exterior: / precisa do / original?“ (6 W.) + Mitmach „Comenta SIM ou NÃO“ + **Etikett** „Histórico escolar · português → inglês · R$ 149 + R$ 49 por página extra“ | Q1 |
| 2,5 | Auslöser-Blitz + Haken, Punch | – | – |
| 3,0–6,5 | Whip: Foto-Karte + PDF-Karte, Haken 3,5 / 4,5; Etikett bleibt | „Pra traduzir: / foto ou PDF.“ · Beleg „No site: foto ou PDF“ · CTA-Chip ab 3,0 | Q3 |
| 6,5–10,0 | Handy steigt (Etikett aus), 4 Seiten 7,0 / 8,0 | „Envie o histórico / completo.“ · Beleg „Todas as páginas“ | Q4, Q2 |
| 10,0–13,5 | Seite 1 mit Ring (11,0), Seiten 2–4 mit Plus (12,0) | „Histórico: R$ 149 / + R$ 49/pág. extra“ · Beleg „Português → inglês · tabela“ (gleichzeitig) | Q1, Q2 |
| 13,5–17,0 | Original + Übersetzung, je ein Siegel (14,0 / 15,0) | „Apostila: em geral, / original e tradução.“ · Beleg „Original em papel: no cartório“ | Q5 |
| 17,0–20,5 | PDF wird unterschrieben, Haken-Siegel 19,0 | „Chega em PDF com / assinatura digital.“ · Beleg „PDF juramentado“ | Q6 |
| 20,5–24,0 | Globus – Universität, Lupe prüft (22,0) | „A universidade aceita / PDF assinado?“ · Beleg „Confirme antes com o destino“ | Q7 |
| 24,0–27,5 | Beleg (Balken unscharf, keine Zahl) + Kalender | „Preço e data / na hora.“ · Beleg „No site, antes de pagar“ | Q8 |
| 27,5–34,2 | Endcard Névoa, Handy unten im Sucher (Bild-Reim auf den Hook) | „Histórico pro / exterior? / Envie a foto: / preço na hora.“ · „link na bio“ · traduzme.com.br · WhatsApp (61) 99803-8363 · **kein Preis** | – |
| 34,2–34,5 | harter Schnitt auf Frame 0 (Loop) | Hook + Etikett | – |

GMB (27,5 s): ohne 10,0–17,0 (Preis je Seite + Apostila; der Preis steht im Etikett 0–6,5 s), Chip „Preço na hora no site“, Endcard-Chip „no site“, Endcard 20,5–27,2, eigener Loop.

## Quellen
- **Q1** Supabase `precos` en/from_pt `historico escolar` 14900 + extra_pag 4900 (SELECT 09.11.2026) + pix-cob `precoItem` + precos_ia 05./08./09.11.
- **Q2** analisar-Prompt (Edge-Function, nucleo.ts): Histórico „cobrado POR PÁGINA (cada página conta)“.
- **Q3** Rechner fl1 „Foto ou PDF, quantos precisar.“ (curl /orcamento-app/?lang=pt 09.11., HTTP 200)
- **Q4** Rechner-Info „Diploma“: „… tradução juramentada do diploma e do histórico escolar completo …“ (curl 09.11.); absolut formuliert → im Video nur „Envie o histórico completo“ (Handlungsempfehlung), in Texten „em geral“.
- **Q5** Rechner-Info Apostila: „Apostilar o original ou a tradução? Em geral, os dois …“ + „Documento brasileiro para usar no exterior: … apostilar o original, fazer a tradução juramentada e, por fim, apostilar também a tradução.“ + Optionen im Orçamento „Apostila no documento original (digital)“ / „Apostila na tradução (digital)“ (curl 09.11.). `apo_hint_o`: „Só para documento brasileiro emitido em formato digital, com assinatura digital (ex.: certidão digital). Documento em papel deve ser apostilado em cartório antes do pedido.“
- **Q6** Rechner fl4 „PDF juramentado com assinatura digital.“ (curl 09.11.)
- **Q7** REELS-REGELN-v2 #12 (Ziel im Ausland: „confirme se aceitam PDF assinado“) + Rechner-Info „a aceitação da apostila digital varia conforme o país e o órgão de destino“ (curl 09.11.). Handlungsempfehlung, keine Tatsachenbehauptung.
- **Q8** Rechner fl2 „Valor e data de entrega na hora.“ (curl 09.11.)

## Kritiker-Runden Storyboard (getrennte Durchgänge, je ein fester Blickwinkel)
**Runde 1**
- Fakten: (a) Erstidee Hook „Histórico de 5 páginas: paga por página?“ = Preisfrage → verboten (Variable) → Kauf-Zweifel „precisa do original?“. (b) Erstidee PT→ES (Spanien/Argentinien): Annahme der brasilianischen Übersetzung im Zielland nicht belegt (Lehre 04.11.) → EN, und Pflicht-Zeile „confirme se aceitam PDF assinado“. (c) „histórico escolar completo“ steht im Rechner absolut („é obrigatória“) → Bild nur als Empfehlung „Envie o histórico completo“. (d) Apostila absolut → „em geral“ + Beleg „Opção no orçamento“ (kein Preis der Option).
- Design: (a) Hook-Text auf Névoa nur Dark (Weiß auf Névoa verboten, C2). (b) Etikett als Kerninfo in x 90–900 / y ≤ 1250 auch mit Punch/Push (Breite 744, x 128–872). (c) Handy darf im Hook nur unter dem Etikett liegen (Oberkante 1290) und steigt erst, wenn das Etikett weg ist (6,5).
- Hook/Tempo: Hook 6 W.; Antwort 3,0 s; Captions ≤ 4 W./Zeile, 3,42 s Standzeit.
- Conversion: IG/TikTok ohne Antwort (kein „foto ou PDF“ in der Caption); Preis in IG/TikTok erlaubt, weil er die Frage nicht beantwortet; LinkedIn B2B Zeile 1 mit UTM; Endcard ohne Preis.
**Runde 2**
- Fakten: c3-Preis braucht Richtung im selben Moment → Beleg „Português → inglês · tabela“ mit der Caption (Lehre 29-N2). Kein „a partir de“.
- Design: Belege auf y 672 (über dem Handy), Abstand zum Handy 56 px ≥ 48.
- Tempo: leere Bildschirme vermeiden (Seiten ab 7,0, Beleg-Zettel ab 24,0 sichtbar).
**Runde 3 (getrennt):** keine offenen Mängel in allen vier Blickwinkeln.

## Kritiker-Runden Video (nach dem Bau)
- V1 Design: Siegel (Pinho auf dunklem Bildschirm) unsichtbar → Areia-gefüllt und auf die Blätter gesetzt; Bildschirm 7,0–7,5 und 24,0–24,5 leer → Inhalte früher.
- V2 qa_frames: einziger Block `words` an der Loop-Naht 33,7–34,3 (21 Wörter Frame 0 mit 0,3 s Rest-Standzeit, Messartefakt der Pflicht-Variable) → schriftliche Ausnahme `maxNewWords: 22` mit Grund im Kommentar von reel.html; sonst 0 Blocks.
- V3 Ton: Pops −7…−10 dB RMS unter Musik → Gain 1,6 → 2,0; Klick GMB Spitze +5,1 dB → Gain 2,4 → 2,0 (+3,5 dB). Danach alle SFX Spitze ≤ +3,5 dB über Musik.
- V4 Kontaktbögen: alle Haupt- und GMB-Bögen angesehen (Ergebnis in reel35-texte.md).

## Abnahme 09.11. – Fix 35-A
- Beleg s4 „Opção no orçamento“ → „Original em papel: no cartório“ (Rechner `apo_hint_o`: Apostila im Original über das Orçamento nur bei digital ausgestelltem Dokument mit assinatura digital; Papier-Dokument vorher im Cartório). Nur Hauptfassung neu gerendert; Ton unverändert (audio.py identisch); GMB nicht betroffen (Szene 10,0–17,0 fehlt dort), gmb/reel.html nur textgleich gehalten.
