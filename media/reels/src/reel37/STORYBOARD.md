# Reel 37 – „Antecedentes da França: qual bulletin você pede?“ (Mi 18.11.2026)

Thema nach ENTSCHEIDEN (Lauf 11.11., marketing/lernen/social.md): **Antecedentes criminais francês → português** (Casier judiciaire, Bulletin nº 3), Preisbeispiel **R$ 119, tabela**. Score **15** (K3 N1 E1 B0 L2).
Format (Pflicht-Wechsel): **Quiz em 3 cartas** – Held-Objekt Bühne 960 × 1080 (Pinho) mit drei Karten „1 · 2 · 3“; je Szene schiebt sich der neue Bühneninhalt **von unten** herein (vertikaler Push auf dem Schlag, R36 hatte horizontalen Whip) · Grund **Areia #EEDECE** · Musik `music.py` **bossa 120 BPM**, Tonart G, seed 37.
R36 = Dokument-Duell / Dark / lofi 120 · R35 = Handy-Close-up / Névoa / pop 120 · R34 = Dokument-Tisch / Pinho / funk → Bildsprache, Grund und Musik anders als R35 und R36.
**Etikett (Standard seit R35, keine Variable mehr):** „Antecedentes criminais · francês → português · R$ 119“ in Frame 0 und im Cover 1,0 s. Hook = Kauf-Zweifel (welches Dokument bestellen und übersetzen lassen), **nicht** die Preisfrage. Das Etikett nennt keine Nummer → verrät die Antwort (nº 3) nicht.
**Eine neue Variable (berührt die ersten 3 s nicht):** **LinkedIn-Einstieg** – Zeile 1 = Kauf-Zweifel aus dem echten Fall als Frage an RH/Kanzleien („Colaborador ou cliente francês precisa de antecedentes criminais no Brasil: qual bulletin pedir?“) + UTM-Link in derselben Zeile; R30–R36 begannen mit einer Preis-Aussage. Video, Endcard („Envie a foto: preço na hora.“), IG/TikTok/YT unverändert im Aufbau.
Vorhersage: LinkedIn-Sitzungen `utm_campaign=reel37` (GA4, 72 h nach Post) **≥ +30 %** gegenüber dem Median reel30–reel36 im gleichen Alter; TikTok Ø Sehdauer ±15 % ggü. R35/R36 (Etikett gleich). Messung **Sa 21.11.2026**.

## Preis-Einstufung (Lehre 33-5, vor dem Bau geprüft 11.11.2026)
| Prüfung | Befund |
|---|---|
| precos (SELECT `ativo and not placeholder`, fr/to_pt) | `antecedentes criminais` **11900**, extra_pag null (Festpreis-Item); alle fr/to_pt-Dokumente 11900–12900, lauda comum 11900, técnica 13900 |
| analisar-Prompt (Edge-Function v39) | Typ „antecedentes criminais: atestado/certidão de antecedentes criminais …, certificado de antecedentes penales/judiciales, police clearance …; 1-2 páginas“; `MAX_PAG_ANEXO = 2` (Anhang wie Rückseite/Apostila ≤ 2 Seiten = Teil des Dokuments) → Bulletin nº 3 + Apostila-Blatt = 1 Dokument, tecnico=false |
| Echter Fall precos_ia 10.11.2026 14:04 | „Bulletin número 3 do Casier judiciaire national da França … seguido de folha de Apostila de Haia … 1 documento com Apostila“, 2 Seiten: tabela 11900 = final 11900, regra minimo 11900 (Mindestauftrag = Tabelle) |
| Ergebnis | Antecedentes criminais francês → português = **R$ 119** (tabela), Apostila-Blatt ohne Aufpreis. Im Bild nur „R$ 119“ mit Dokument + Richtung + „tabela“, nie „a partir de“. Endcard ohne Preis. |

## Ablauf (120 BPM, Schlag 0,5 s; Szenen je 3,5 s)
| Zeit | Bild | Text (Bild) | Quelle |
|---|---|---|---|
| 0,0–2,95 | Bühne unten: drei Karten „1 · 2 · 3“ wippen, Fragezeichen pulsiert ab Frame 1; Etikett darüber | Hook „Antecedentes / da França: / qual **bulletin** / **você pede?**“ (7 W.) + Mitmach „Comenta 1, 2 ou 3“ + **Etikett** „Antecedentes criminais · francês → português · R$ 119“ | Q1 |
| 2,5 | Karte 3 springt hoch (Haken + Punch), 1 und 2 blassen ab | – | Q2 |
| 3,0–6,5 | Bühne steigt (Push von unten); Karte 3 groß mit Person-Symbol und Haken 4,0, Karten 1/2 klein | „Nº 3: o único / **que você pede.**“ · Beleg „Ministério da Justiça da França“ · CTA-Chip ab 3,0 | Q2 |
| 6,5–10,0 | Karten 1 und 2 mit Pfeilen zum Gebäude (Órgão), Ring 7,0, Schloss 8,0 | „Nº 1 e nº 2: / **você não recebe.**“ · Beleg „Vão para juízes e órgãos“ | Q2 |
| 10,0–13,5 | Laptop mit Formular (Formen), Umschlag fliegt 11,0, Haken 12,0 | „Pedido online / **e gratuito.**“ · Beleg „service-public.fr“ | Q3 |
| 13,5–17,0 | Bulletin + Apostila-Blatt, Siegel-Stempel 15,0 | „Apostila: feita / **na França.**“ · Beleg „Em geral · antes da tradução“ | Q4 |
| 17,0–20,5 | Original → Pfeil → Übersetzung mit Siegel, Gebäude, Haken 19,0 | „No Brasil: tradução / **juramentada.**“ · Beleg „Ex.: naturalização · confirme“ | Q5 |
| 20,5–24,0 | Bulletin + Apostila mit Haken, Klammer = 1 Dokument, Preisschild ohne Zahl 23,0 | „Apostila conta / **como parte: R$ 119.**“ · Beleg „Francês → português · tabela“ | Q1, Q6 |
| 24,0–27,5 | PDF wird unterschrieben, Gebäude, Lupe 25,5 | „Chega em PDF com / **assinatura digital.**“ · Beleg „Confirme no órgão de destino“ | Q7 |
| 27,5–34,2 | Endcard Areia, Bühne unten (Bild-Reim auf den Hook) | „Antecedentes / da França? / **Envie a foto:** / **preço na hora.**“ · „link na bio“ · traduzme.com.br · WhatsApp (61) 99803-8363 · **kein Preis** | Q8 |
| 34,2–34,5 | harter Schnitt auf Frame 0 (Loop) | Hook + Etikett | – |

GMB (27,5 s): ohne 10,0–13,5 (online/gratuito) und 24,0–27,5 (PDF); Preis-Szene bleibt. Chip „Preço na hora no site“, Endcard-Chip „no site“, Endcard 20,5–27,2, eigener Loop.

## Quellen
- **Q1** Supabase `precos` fr/to_pt `antecedentes criminais` 11900, extra_pag null (SELECT 11.11.2026) + precos_ia 10.11.2026 (Bulletin nº 3 + Apostila, 2 S., tabela = final = minimo 11900).
- **Q2** justice.fr „Casier judiciaire : présentation des trois bulletins“ (Mis à jour le 20 octobre 2025, selbst geöffnet 11.11.2026): „Seule la personne condamnée (ou son représentant légal) peut demander le B3 du casier judiciaire.“ · „ne peut pas obtenir une copie du B1“ · „La personne condamnée ne peut pas solliciter une copie de son bulletin n°2.“ · „Seuls les juges, le procureur de la République et l'administration pénitentiaire peuvent se voir délivrer le bulletin n°1“ · „Le bulletin n°2 … peut être délivré aux autorités administratives“. Bildwort „Ministério da Justiça da França“ = Herausgeber justice.fr.
- **Q3** service-public.gouv.fr F1420 „Demande d'extrait de casier judiciaire (bulletin n°3)“ (selbst geöffnet 11.11.2026): „Dans tous les cas, cette démarche est gratuite.“ · „De manière générale, la demande doit être faite sur internet“ · „Le bulletin n°3 … peut vous être délivré quelle que soit votre nationalité.“
- **Q4** Rechner-Info Apostila P2 (curl /orcamento-app/?lang=pt 11.11.2026, HTTP 200): „Para documento estrangeiro não oferecemos apostila: ela é feita no país de origem, antes da tradução.“ + Polícia Federal, FAQ „É necessária a legalização e tradução …“ (gov.br/pf, selbst geöffnet 11.11.2026): Dokumente aus dem Ausland „precisam ser legalizados e traduzidos“, Apostila ersetzt die Legalisierung; Ausnahmen nur Mercosul/Bolívia/Chile/Uruguai/Argentina/Haiti/Ucrânia → „Em geral“.
- **Q5** Ministério da Justiça, „Lista de documentos de naturalização ordinária“ (gov.br/mj PDF, selbst geöffnet 11.11.2026), Punkt 6: „Atestado de antecedentes criminais ou documento equivalente emitido pelo país de origem … legalizado e traduzido, no Brasil, por tradutor público juramentado“ + PF-FAQ (Q4): apostilierte Dokumente brauchen weiter die tradução juramentada (CPC art. 192, Lei 14.195/2021 art. 27). Im Bild „Ex.: naturalização · confirme“.
- **Q6** Rechner pc2 „Verso e Apostila (foto ou página) contam como parte do documento: sem custo extra.“ (curl 11.11.2026).
- **Q7** Rechner fl4 „PDF juramentado com assinatura digital.“ (curl 11.11.2026) + Handlungsempfehlung „confirme no órgão de destino“ (Annahme des digital signierten PDF je Órgão nicht belegt).
- **Q8** Rechner fl1 „Foto ou PDF, quantos precisar.“ / fl2 „Valor e data de entrega na hora.“ (curl 11.11.2026).

Bewusst **nicht** verwendet: Gültigkeitsfristen (90 dias o. Ä.), Bearbeitungszeiten in Frankreich, Postweg, Zustellung per E-Mail, wo in Frankreich apostiliert wird (nur „na França“), Apostila-Preise, Eil-Option, Via física, Kundenfall/Kundendaten, PF-Residência-Listen (nur Naturalização als Beispiel mit Primärquelle).

## Kritiker-Runden Storyboard (getrennte Durchgänge, je ein fester Blickwinkel)
**Runde 1**
- Fakten: (a) Erstidee „A apostila paga à parte?“ → gleiche Antwort-Logik wie R30 („o verso paga à parte?“, pc2) → Kauf-Zweifel „qual bulletin você pede?“ mit französischer Primärquelle; pc2 bleibt nur als Preis-Szene. (b) „Nº 1 e nº 2 são só para juízes“ zu eng (B2 geht an Behörden) → „você não recebe“ + Beleg „Vão para juízes e órgãos“. (c) „PF exige antecedentes do país de origem“ ohne Liste geöffnet → Beispiel Naturalização (MJ-Liste Punkt 6) und „confirme“. (d) „Apostila é obrigatória“ zu absolut (Ausnahmen Mercosul usw.) → „Em geral“. (e) „gratuito“ nur mit service-public-Wortlaut.
- Design: (a) Areia-Grund → Hook Dark, Marker Sálvia/Dark, Captions Weiß auf Dark-Box, CTA- und Mitmach-Chip Weiß auf Pinho, Etikett/Belege Dark auf Papier (alle erlaubten Paare, kein Weiß auf Areia). (b) Kartenziffern im Hook: Glyphen-Unterkante ≤ y 1440 (< 1500). (c) Karten nebeneinander ohne Überlappung (kein `cut`).
- Hook/Tempo: 7 Wörter, Antwort-Bild 2,5 s, Antwort-Text 3,0 s; Captions ≤ 4 W./Zeile, 3,42 s.
- Conversion: IG/TikTok verraten die Nummer nicht (kein „nº 3“, kein „o único que você pede“); Preis mit Dokument + Richtung beantwortet die Frage nicht; LinkedIn-Einstieg = Variable; Endcard ohne Preis, gleich wie R31–R36.
**Runde 2**
- Fakten: c6 „R$ 119“ braucht Richtung im selben Moment → Beleg „Francês → português · tabela“. c7 „assinatura digital“ wörtlich fl4. Beleg s4 „Em geral · antes da tradução“ (Rechner-Wortlaut „antes da tradução“).
- Design: Etikett 3 Zeilen wie R36 (744 × 264), Text rechts ≤ 872; Beleg-Pillen ≤ 44 px × ~30 Zeichen (≤ 810 px Breite).
- Hook/Tempo: Frame 0 = 7 + 4 + 7 Wörter + Kartenziffern 3 = 21 → qa-Ausnahme `maxNewWords 22` wie R35/R36 (nur Loop-Naht).
**Runde 3 (getrennt):** keine offenen Mängel im Storyboard.
**Nach dem Rendern (Video-Runden):** qa_frames `safe` x 921/909 bei „tradução juramentada.“ / „com assinatura digital.“ → Zeilen umgebrochen; Loop-SSIM 0,970 → Karten-Wippen bei t = 0 auf 0 (danach 0,996); SFX-Spitzen bis +10 dB (click/pop/whoosh) → Gains gesenkt, danach ≤ +3,7 dB. Danach qa_check Haupt + GMB Exit 0.
