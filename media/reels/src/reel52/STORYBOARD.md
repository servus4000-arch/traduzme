# Reel 52 – „Certidão em espanhol: só a tradução basta?“ (Post Fr 04.12.2026, ES-Fall)

Certidão de nascimento **espanhol → português**, Etikett „R$ 149 na tabela“. Format **Mural** (Pinnwand: Korkfläche in Pinho-Rahmen mit Pinnnadeln und Ablageleiste als Bühne; Szenenwechsel = **Blatt-Schnitt**: ein Papierblatt gleitet 0,10 s vor dem Schlag von rechts über den Kork, deckt die Fläche auf dem Schlag (harter Schnitt darunter) und ist bei +0,18 s links draußen), Grund **Areia #EEDECE** (radialer Verlauf), Musik `music.py` **funk 120 BPM**, E, seed 52, Master v2. Szenen 3,5 s, Endcard Standard „Envie a foto: preço na hora.“, Etikett in Frame 0 (Standard seit R35), Mitmach-Pille „SIM ou NÃO?“ (Standard-Pille, keine Knöpfe). Neue Variable (nicht im Bild): **TikTok-Caption Zeile 1 nennt drei Herkunftsländer** („Certidão de nascimento do México, da Colômbia ou da Venezuela: …“) statt nur „em espanhol“.

Pflichtwechsel (keine Variable): R51 Fichário/Sálvia/lofi, R50 Mala de viagem/Dark/bossa, R49 Envelope/Névoa/calm → Mural/Areia/funk.

## Thema (ENTSCHEIDEN 27.11.2026, Zeile in marketing/lernen/social.md)
- Auftrag: nur Vorrat N01–N24 (Status OFFEN), nur ES/FR/IT; kein Alemão/Inglês/Árabe; gesperrt Divórcio, Casamento/Traslado, CNH, Antecedentes, Diploma, Carta de emprego, Certidão de Cuba und alles aus R20–R51. Score ≥ 14.
- Schritt 1 (SELECT 27.11., read-only): pedidos status PAGO 30 T. – ES→PT Certidões de nascimento bezahlt 14.11. (R$ 409), 18.11. (R$ 329), 20.11. (R$ 300); analises 30 T. es/certidao de nascimento 13 Uploads; keine ES-Procuração-Uploads. Metricool nur gelesen (Best Time IG Freitag: 10 h höchster Wert) – nichts geplant.
- Kandidaten (Score = K×3 + N×2 + E×2 + B×2 + L):
  - **N12 Certidão de nascimento ES→PT „só a tradução basta?“ R$ 149 (K3 N1 E1 B2 L2 = 19) → gewählt**
  - N06 Certidão sem apostila (roh 19) – raus: nah an R46 (Cuba/Legalisation), Risiko Portaria/Apostila (Lehre 42)
  - N14 Québec FR (≈ 17) – nicht gewählt: B niedrig, kein bezahlter FR-Auftrag
  - N02 Procuração argentina (K0, ≈ 11) – unter 14
  - N16 – kein Dokument; N20 Haiti – nah an Cuba; N24 IT – Casamento gesperrt
- Grund: höchster Score mit frischem Kaufnachweis (drei bezahlte ES-Geburtsurkunden in 30 T.), echter Kauf-Zweifel (muss das Original mit zum Cartório?), Primärquelle eindeutig (Lei 14.195/2021 art. 27 § 2º I = Pflicht), kein Duplikat zu R20–R51.
- N1 geschätzt, nicht gemessen.

## Quellen
| Q | Aussage | Quelle | Wie geprüft |
|---|---|---|---|
| Q1 | Certidão de nascimento espanhol → português **R$ 149 na tabela** (Etikett 0–2,97; Bild 20,5) | Supabase `precos` `WHERE ativo AND NOT placeholder`: `es / to_pt / certidao de nascimento` **14900**, extra_pag null | SELECT 27.11.2026 (read-only) |
| Q1b | Ausländische Geburtsurkunde = Typ `certidao de nascimento`; Festpreis je Dokument bis 4 Seiten (Beleg „Preço fixo · até 4 páginas“) | Edge-Function `analisar` v48 („acta/partida/registro civil de nacimiento (México, Argentina, Colômbia, Espanha, Cuba...)“; „inteiro teor“ nur brasilianische Certidões; Verso/Apostila = Teil des Dokuments); `pix-cob` v62 `PAUSCHAL_MAX_PAG=4`; Rechner pc1 „preço fixo por documento“ | get_edge_function 27.11.2026; curl /orcamento-app/ 27.11.2026 |
| Q2 | Não: o original vai junto · Lei 14.195 · art. 27, § 2º, I (Bild 3,0) | Lei 14.195/2021 art. 27 § 2º: „A presunção (…) não afasta: I – a obrigação de o documento na língua original acompanhar a sua respectiva tradução“ | WebFetch camara.leg.br (norma atualizada) 27.11.2026; planalto per curl vom Proxy gesperrt |
| Q3 | Juramentada: presume-se fiel · art. 27, caput (Bild 6,5) | art. 27 caput: „Presumem-se fiéis e exatas as traduções realizadas por tradutor (…) público“ | wie Q2 |
| Q4 | Cartório, em geral: tradutor público · art. 26, I (Bild 10,0) | art. 26 I: privativ, „traduzir qualquer documento que tenha de ser apresentado em outro idioma perante pessoa jurídica de direito público interno ou perante serviços notariais e de registro de notas ou de títulos e documentos“; „em geral“ wegen parágrafo único (ad hoc / agente público) | wie Q2 |
| Q5 | Pra valer no Brasil: em português · Código Civil art. 224 (Bild 13,5) | CC art. 224 „Os documentos redigidos em língua estrangeira serão traduzidos para o português para ter efeitos legais no País.“ (ohne Änderungsvermerk) | WebFetch planalto.gov.br l10406compilada 27.11.2026 |
| Q6 | A fidelidade pode ser impugnada · art. 27, § 2º, II (Bild 17,0, nur Hauptfassung) | art. 27 § 2º II: „a possibilidade de ente público ou qualquer interessado impugnar (…) a fidedignidade ou a exatidão da tradução“ | wie Q2 |
| Q7 | Lista do cartório: confirme antes · Em geral · confirme no órgão (Bild 24,0) | **Keine Primärquelle** zur Dokumentenliste einzelner Cartórios → nur Vorbehalt, keine Aussage, was ein Cartório verlangt | – |
| Q8 | Envie a foto: preço na hora (Endcard); Foto ou PDF; valor e data na hora; Pix; PDF com assinatura digital (Texte) | Rechner fl1 „Foto ou PDF, quantos precisar.“, fl2 „Valor e data de entrega na hora.“, fl3 „Pague por Pix“, fl4 „PDF juramentado com assinatura digital …“ | curl /orcamento-app/ 27.11.2026 |
| – | Requisiten (Pinnwand, Certidão estrangeira mit Zierrahmen und Siegel ohne Wappen, Tradução mit Pinho-Kopfband und Stempelkasten, Clip, Waage, Gebäude mit Säulen, Pfeil, Lupe, Preisschild ohne Zahl, Checkliste, Handy, Haken, Fragezeichen, Ring) | eigene SVG ohne Schrift, ohne Zahlen, ohne Wappen/Flaggen/Landkarte/Firmenlogo, kein Kundenfall | – |

**Bewusst nicht verwendet:** Apostila und Legalisation (Lehre 42, R23/R39/R46; traduzme apostiliert nur brasilianische Originale); ob ein digitales Original genügt (keine Primärquelle); welche Unterlagen ein bestimmtes Cartório verlangt; Länderregeln; Lieferfristen und Zusatzoptionen; Empfehlungen (Lehre R45); „sem custo extra“; Kundendaten.

## Ablauf (Designzeit; GMB lässt 17,0–20,5 weg, Endcard 5,0 s)
| Zeit | Text (Bild) | Beleg-Pille | Bild / Ereignis | SFX |
|---|---|---|---|---|
| 0–2,97 | Hook „Certidão em / espanhol: só a / tradução basta?“ + Pille „SIM ou NÃO?“ + Etikett „Certidão de nascimento · espanhol → português · R$ 149 · na tabela“ | – | Pinnwand unten, Tradução allein mit „?“; 2,5 Original gleitet dahinter, Clip schnappt, Ring + Punch | pop 0,03 · stamp 2,5 |
| 3,0 | Não: o original / vai junto. | Lei 14.195 · art. 27, § 2º, I | Blatt-Schnitt; Paar mit Clip groß; 3,5 Clip zieht nach; 5,5 Haken | whoosh · click 3,5 · pop 5,5 |
| 6,5 | Juramentada: / presume-se fiel. | Lei 14.195 · art. 27, caput | Tradução links, 7,5 Waage springt auf + Punch; 8,5 Haken | whoosh · stamp 7,5 · pop 8,5 |
| 10,0 | Cartório, em geral: / tradutor público. | Lei 14.195 · art. 26, I | Gebäude mit Säulen, 10,5 Tradução gleitet darunter, 11,0 Punch; 12,5 Haken | whoosh · click 10,5 · stamp 11,0 · pop 12,5 |
| 13,5 | Pra valer no Brasil: / em português. | Código Civil · art. 224 | Original links, 14,0 Pfeil zeichnet sich, 14,5 Tradução springt auf + Punch; 15,5 Haken | whoosh · click 14,0 · stamp 14,5 |
| 17,0 | A fidelidade pode / ser impugnada. | Lei 14.195 · art. 27, § 2º, II | Lupe fährt 17,5 über die Tradução, 18,5 „?“ + Stempel, Lupe schwebt weiter | whoosh · click 17,5 · stamp 18,5 |
| 20,5 | Espanhol, na tabela: / R$ 149 a certidão. | Preço fixo · até 4 páginas | Paar mit Clip + Preisschild ohne Zahl 21,5 + Punch; 22,5 Haken | whoosh · stamp 21,5 · pop 22,5 |
| 24,0 | Lista do cartório: / confirme antes. | Em geral · confirme no órgão | Gebäude + Checkliste, Lupe 24,5, „?“ 25,5 + Stempel, Haken 26,5 | whoosh · click 24,5 · stamp 25,5 · pop 26,5 |
| 27,5–34,2 | Certidão em / espanhol? / Envie a foto: / preço na hora. + link na bio + traduzme.com.br + (61) 99803-8363 | – | Handy mit der Certidão auf dem Bildschirm, Haken 28,5 | stamp+hit 27,5 · pop 28,5 |
| 34,2 | Loop = Frame 0 | | | |

Lernpunkte (≥ 3 mit Warum): Das Original geht mit (Pflicht, art. 27 § 2º I) → die juramentada gilt als treu (caput) → für Cartório in der Regel tradutor público (art. 26 I) → Rechtswirkung in Brasilien nur auf Portugiesisch (CC 224) → Treue kann angefochten werden (§ 2º II) → Festpreis der Übersetzung → Liste des Cartórios vorher bestätigen.

## Kritiker-Runden (Storyboard)
- **Runde 1 Fakten:** Lei 14.195/2021 art. 26/27 selbst geöffnet (camara.leg.br, norma atualizada; planalto per curl gesperrt), CC art. 224 auf planalto. „Vai junto“ = „acompanhar“ (Pflicht, nicht Empfehlung). „Em geral“ bei art. 26 wegen parágrafo único. Preis 14900 mit „na tabela“, Einstufung aus analisar v48, Festpreis bis 4 Seiten (Lehre R41). Apostila weggelassen (Lehre 42). Keine Aussage zur Liste einzelner Cartórios (nur „confirme antes“).
- **Runde 1 Design:** Areia-Grund → Hook/Endcard Dark-Schrift, Marker Sálvia; Captions Dark-Pillen mit weißer Schrift, Marker Sálvia/Dark; Belege Papier mit Pinho-Rand; Chip Pinho/Weiß. Held-Objekt Pinnwand 700 px breit. Hook-Requisiten auf der Korkfläche.
- **Runde 1 Hook/Tempo:** Hook 7 Wörter, Kauf-Zweifel („só a tradução basta?“), keine Preisfrage; Etikett nennt nur Dokument/Richtung/Preis → verrät die Antwort nicht. Payoff 2,5 s (Original gleitet hinter die Tradução + Clip + Ring), Antwort ab 3,0 s.
- **Runde 1 Conversion:** IG/TikTok ohne Antwort (Regel 14), Zeile 2 „Resposta no vídeo 👀“; Endcard ohne Preis; CTA-Chip ab 3,0 s; YT/LinkedIn antworten mit Quelle; UTM reel52.
- **Runde 2:** qa_frames BLOCK safe: Hook „tradução basta?“ bis x 971 und Caption „Tradução juramentada:“ bis x 913 → Hook 104 → 92 px, letter-spacing −3 px; Caption „Juramentada:“. Danach PASS (Haupt + cut=gmb).
- **Runde 3 (Kontaktbögen):** Waage (6,5) und Tradução in der Cartório-Szene (10,0) zu klein, Lupen-Szene (17,0) fast still → Waage größer, Tradução 0,56, Lupe schwebt nach 18,3 weiter. Neu gerendert, keine offenen Mängel.
- **Variable:** zuerst IG-Postzeit abends geplant → verworfen (Metricool IG Freitag: 10 h bester Slot, 18 h deutlich schwächer) → TikTok-Caption mit drei Ländern.

## Ton
`music.py` funk 120 BPM, E, seed 52, Master v2, Ceiling −3,0 dBTP. stamp = Körper Hochpass 300 Hz + Präsenz-Schicht 1,8–4,2 kHz im selben Ereignis (Lehren 49-1/50-A). 27 Ereignisse (0,78/s). Gains `GJ_MAIN`/`GJ_GMB` per `measure_sfx.py --iter 6` (Ziel Breitband-20-ms-Spitze +3,5 dB, Fenster [t, t+0,45 s]). Messwerte siehe social/reels/reel52-texte.md „Ton“.
