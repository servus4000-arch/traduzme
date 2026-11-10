# Reel 36 – „Certidão pro exterior: inteiro teor ou breve relato?“ (Di 17.11.2026)

Thema nach ENTSCHEIDEN (Lauf 10.11., marketing/lernen/social.md): **Certidão de nascimento português → espanhol**, Preisbeispiel **R$ 149 (breve relato) / R$ 169 (inteiro teor), tabela**. Score 17 (K2 N2 E1 B1 L3).
Format (Pflicht-Wechsel): **Dokument-Duell** – Held-Objekt Bühne 960 × 1080 mit zwei Certidões nebeneinander (Breve relato | Inteiro teor), Inhalt wechselt je Szene per Whip auf dem Schlag · Grund **Dark #1F3B35** · Musik `music.py` **lofi 120 BPM** (Raster E2: Erklär-Tisch/Dokumente → lofi).
R35 = Handy-Close-up / Névoa / pop · R34 = Dokument-Tisch / Pinho / funk · R33 = Kinetic-Type / Sálvia / lofi → Bildsprache, Grund und Musik anders als R35.
**Variable (Wochenfazit KW45, zweite Messung, gleich wie R35):** Dokument + Richtung + Preis in **Frame 0** als Etikett („Certidão de nascimento · português → espanhol · R$ 149 · breve relato“, 9 Wörter statt 11 bei R35, Lehre 35-1). Hook-Frage ist **nicht** die Preisfrage, sondern ein Kauf-Zweifel (welches Modell bestellen/übersetzen). Cover 1,0 s zeigt das Etikett.
Vorhersage: TikTok Ø Sehdauer +20 % gegenüber Median R28–R34 (72 h). Messung Fr 20.11. (Feiertag, ohne Post) bzw. Sa 21.11.2026.

## Preis-Einstufung (Lehre 33-5, vor dem Bau geprüft 10.11.2026)
| Prüfung | Befund |
|---|---|
| precos (SELECT `ativo and not placeholder`, es/from_pt) | `certidao de nascimento` **14900**, `certidao inteiro teor` **16900**, beide ohne extra_pag (Festpreis-Item, keine Lauda); certidão negativa 12900, lauda comum 11900 / técnica 13900 |
| analisar-Prompt (nucleo.ts v38) | „certidao inteiro teor: SOMENTE certidão BRASILEIRA … em INTEIRO TEOR: traz as palavras 'inteiro teor' … ou é a transcrição completa do assento … 2-3 páginas. A certidão brasileira normal (breve relato/modelo padrão de 1 página, mesmo com verso, averbações ou Apostila) continua no tipo da certidão“ → eine brasilianische Geburtsurkunde ist entweder `certidao de nascimento` (149) oder `certidao inteiro teor` (169); tecnico=false |
| pix-cob v51 `precoItem` | Item ohne extra_pag: Festpreis bis `PAUSCHAL_MAX_PAG = 4` Seiten pro Datei, darüber + Lauda comum je Seite → Inteiro teor mit 2–3 Seiten = 169 |
| Mindestauftrag (Preisregel r4, pix-cob) | custos es/from_pt: certidão EK 7000, inteiro teor EK 9000. Minimo = r9Acima(⌈(EK + 6000 + 100) / 0,94⌉) → 13937 → **14900** bzw. 16064 → **16900** = Tabelle → bei 1 Certidão kein Aufschlag, kein Rabatt unter die Tabelle möglich (Endpreis = MAX(…, Minimo)) |
| Ist-Preise precos_ia es/from_pt | 27.10. und 01.11. je 1 Certidão de nascimento: tabela 14900 = final 14900 ✓ |
| Ergebnis | Eine Certidão de nascimento português → espanhol kommt im Rechner mit **R$ 149** (breve relato) bzw. **R$ 169** (inteiro teor) heraus. Gezeigt wird nur das, immer mit Dokument + Richtung, „tabela“, nie „a partir de“. |

## Ablauf (120 BPM, Schlag 0,5 s; Szenen je 3,5 s)
| Zeit | Bild | Text (Bild) | Quelle |
|---|---|---|---|
| 0,0–2,95 | Bühne unten (Breve 1 Blatt | Inteiro teor Stapel, Fragezeichen pulsiert ab Frame 1), Etikett darüber | Hook „Certidão pro / exterior: / **inteiro teor** ou / **breve relato?**“ (8 W.) + Mitmach „Comenta INTEIRO ou BREVE“ + **Etikett** „Certidão de nascimento · português → espanhol · R$ 149 · breve relato“ | Q1 |
| 2,5 | Fragezeichen → Haken, Punch | – | – |
| 3,0–6,5 | Bühne steigt; beide Certidões mit Titel-Pillen „Breve relato“ / „Inteiro teor“, darunter Órgão (Säulen) mit Pfeilen, Haken 4,0 | „Quem pede define: / **pergunte antes.**“ · Beleg „Consulado, universidade, cartório“ · CTA-Chip ab 3,0 | Q6, Q3 |
| 6,5–10,0 | Breve relato groß, Ring 7,0, Kästen leuchten 8,0 | „Breve relato: / **o modelo resumido.**“ · Beleg „Campos em quadros“ | Q3 |
| 10,0–13,5 | Drei Seiten Inteiro teor fächern, Ring 11,0, Randvermerk 12,0 | „Inteiro teor: / **o registro completo.**“ · Beleg „Tudo o que consta no registro“ | Q3 |
| 13,5–17,0 | Pass (Form) + Inteiro teor + Globus, Haken-Stempel 15,0 | „Dupla cidadania? / **Em geral, inteiro teor.**“ · Beleg „Confirme com o consulado“ | Q3 |
| 17,0–20,5 | Beide Certidões mit leeren Preisschildern (18,0), Ring 19,0 | „Inteiro teor: R$ 169 / **breve relato: R$ 149**“ · Beleg „Português → espanhol · tabela“ (gleichzeitig) | Q1, Q2 |
| 20,5–24,0 | Drei Seiten mit Haken (21,0 / 22,0), Klammer = 1 Dokument (23,0) | „Envie todas / **as páginas.**“ · Beleg „Preço fixo por documento“ | Q4 |
| 24,0–27,5 | PDF wird unterschrieben, Globus, Lupe 25,5 | „O destino aceita / **PDF assinado?**“ · Beleg „Confirme antes com o destino“ | Q5 |
| 27,5–34,2 | Endcard Dark, Bühne unten (Bild-Reim auf den Hook) | „Certidão pro / exterior? / Envie a foto: / preço na hora.“ · „link na bio“ · traduzme.com.br · WhatsApp (61) 99803-8363 · **kein Preis** | Q6 |
| 34,2–34,5 | harter Schnitt auf Frame 0 (Loop) | Hook + Etikett | – |

GMB (27,5 s): ohne 13,5–17,0 (Dupla cidadania) und 20,5–24,0 (Todas as páginas); Preis-Szene bleibt. Chip „Preço na hora no site“, Endcard-Chip „no site“, Endcard 20,5–27,2, eigener Loop.

## Quellen
- **Q1** Supabase `precos` es/from_pt `certidao de nascimento` 14900 / `certidao inteiro teor` 16900 (SELECT 10.11.2026) + precos_ia 27.10./01.11. + Mindestauftrag Preisregel r4.
- **Q2** analisar-Prompt (Edge-Function v38, nucleo.ts) Einstufung breve relato / inteiro teor; pix-cob v51 `precoItem` (Festpreis bis 4 Seiten); Rechner-Typenliste „Certidão em inteiro teor“ (STD_LABEL, curl /orcamento-app/?lang=pt 10.11., HTTP 200).
- **Q3** Colégio Notarial do Brasil – SP, „Saiba a importância da certidão de inteiro teor“ (cnbsp.org.br, 25.07.2018, selbst geöffnet 10.11.2026): „Ela é composta por todos os elementos que constam no registro de nascimento da pessoa“, „utilizada em ocasiões específicas em que o documento convencional não é aceito“, „quando o cidadão brasileiro deseja solicitar dupla cidadania ou união estável em outro país“. Lei 6.015/1973 art. 19 („em inteiro teor, em resumo, ou em relatório“) über den eigenen Blog-Artikel /blog/traducao-certidao-de-nascimento zitiert (planalto.gov.br aus der Sandbox gesperrt). „Campos em quadros“ = sichtbares Merkmal des Breve-relato-Modells (eigener Blog-Artikel). → im Bild „Em geral“ + „Confirme com o consulado“.
- **Q4** Rechner pc1 „Documentos padrão (certidões, diplomas, CNH…): preço fixo por documento.“ + pc2 „Verso e Apostila (foto ou página) contam como parte do documento: sem custo extra.“ (curl 10.11.). Grenze 4 Seiten nur in Texten („certidão de até 4 páginas“, eigener Blog-Artikel), im Bild nicht nötig (Inteiro teor 2–3 Seiten).
- **Q5** REELS-REGELN-v2 #12 (Ziel im Ausland: „confirme se aceitam PDF assinado“) + Rechner-Info Apostila „a aceitação … varia conforme o país e o órgão de destino. Antes de pedir, confirme com quem vai receber (consulado, universidade, cartório)“ (curl 10.11.). Handlungsempfehlung.
- **Q6** Rechner fl1 „Foto ou PDF, quantos precisar.“ / fl2 „Valor e data de entrega na hora.“ / Rechner-Info Apostila „confirme com quem vai receber (consulado, universidade, cartório)“ (curl 10.11.).

Bewusst **nicht** verwendet: Zielländer (Annahme brasilianischer Übersetzungen in Spanien/Hispanoamerika nicht belegt), Gültigkeitsfristen, Apostila-Preise, Eil-Option, Via física, Kundenfälle.

## Kritiker-Runden Storyboard (getrennte Durchgänge, je ein fester Blickwinkel)
**Runde 1**
- Fakten: (a) Erstidee „Precisa de apostila?“ → zu nah an R35 (Apostila-Szene + Fix 35-A) → Kauf-Zweifel „inteiro teor ou breve relato?“, der direkt den Preis bestimmt (149 vs 169). (b) „Espanha pede inteiro teor“ nur aus eigenem Blog, Primärquelle (Konsulat) nicht erreichbar → kein Land im Bild, „Dupla cidadania: em geral, inteiro teor“ mit Colégio-Notarial-Beleg + „Confirme com o consulado“. (c) Erst-Beleg s3 „Com averbações“ → ersetzt durch Quelle-nahes „Tudo o que consta no registro“; s1 an Rechner-Wortlaut „consulado, universidade, cartório“ angeglichen.
- Design: (a) Dark-Grund → Hook Weiß, Captions Weiß auf Pinho-Box, Marker Areia/Dark, Etikett Papier/Dark (alle erlaubten Paare). (b) Bühne im Hook erst ab y 1236 (48 px unter dem Etikett). (c) Titel-Pillen auf dem Objekt nur in den zwei Gegenüberstellungs-Szenen.
- Hook/Tempo: 8 Wörter = Grenze; Antwort 3,0 s; Captions ≤ 4 W./Zeile, 3,42 s.
- Conversion: IG/TikTok ohne Antwort (kein „quem pede/depende do destino“, kein „dupla cidadania → inteiro teor“); Preise mit Dokument + Richtung beantworten die Frage nicht; LinkedIn UTM Zeile 1; Endcard ohne Preis.
**Runde 2**
- Fakten: c5 Preis braucht Richtung im selben Moment → Beleg „Português → espanhol · tabela“ gleichzeitig. „Preço fixo por documento“ wörtlich pc1.
- Design: Mitmach-Puls 0,035 → 0,012 und Titel-Pille rechts x 500 → 472 (qa_frames-Warnung `safe` x 915 / 908 bei Punch).
- Ton: SFX-Pegel nach Stem-Messung angepasst (whoosh 3,0 / 17,0, impact 7,0 / 19,0, click 25,5 leiser, pop 4,0 lauter).
**Runde 3 (getrennt):** keine offenen Mängel in allen vier Blickwinkeln (siehe Kontaktbögen-Prüfung in reel36-texte.md).
