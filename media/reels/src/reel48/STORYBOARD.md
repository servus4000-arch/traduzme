# Reel 48 – „Certidão egípcia: tradução simples serve?“ (Post Mi 02.12.2026)

Certidão de nascimento **árabe → português**, Etikett „R$ 299 na tabela“. Format **Guichê** (Schalter-Fenster mit Pinho-Rahmen, Markise, Ablage Areia; Szenenwechsel = Rollladen-Schnitt: Rollladen fällt 0,10 s vor dem Schlag, Schnitt auf dem Schlag, oben bei +0,18 s), Grund **Dark #1F3B35**, Musik `music.py` **lofi 120 BPM**, F, seed 48, Master v2. Szenen 3,5 s, Endcard Standard „Envie a foto: preço na hora.“, Etikett in Frame 0 (Standard seit R35), Mitmach-Pille „SIM ou NÃO?“. Neue Variable (nicht im Bild): **TikTok-Postzeit 18:30 SP statt ~11:20 SP** (siehe social/reels/reel48-texte.md).

## Thema (ENTSCHEIDEN 24.11.2026, Zeile in marketing/lernen/social.md)
- Kaufnachweis: analises 30 T. – zwei Uploads ägyptischer Geburtsurkunden AR (16.11., 23.11., je 1 Seite); keine bezahlte AR-Bestellung in 30 T. → K2. Keine Kundendaten im Reel.
- Kandidaten: **A Certidão egípcia AR→PT „tradução simples serve?“ (K2 N1 E1 B2 L2 = 16) → gewählt** / B Certidão de casamento PT→FR R$ 119 (K3 N1 E1 B0 L2 = 15) / C PT→DE-Familienpaket (20, raus: Annahme in Deutschland nicht belegt) / D Führerschein DE (raus: CNH gesperrt) / E Antecedentes Líbano (raus: Legalisation).
- Grund: Sprachquote AR/DE, Score ≥ 14, kein Duplikat, kein CNH/Apostila/Legalisation.

## Quellen
| Q | Aussage | Quelle | Wie geprüft |
|---|---|---|---|
| Q1 | Certidão de nascimento árabe → português **R$ 299 na tabela** (Etikett 0–2,97; Bild 20,5) | Supabase `precos` `WHERE ativo AND NOT placeholder`: `ar / to_pt / certidao de nascimento` **29900**, extra_pag null | SELECT 24.11.2026 (read-only) |
| Q1b | Ausländische Certidão = `certidao de nascimento`, nie inteiro teor; Festpreis bis 4 Seiten („Preço fixo · até 4 páginas“) | Edge-Functions `analisar` v40 (SABER_TIPOS), `pix-cob` v56 `PAUSCHAL_MAX_PAG=4` | get_edge_function 24.11.2026 |
| Q2 | Em geral, não: vale a juramentada · Lei 14.195/2021 · art. 26 (Bild 3,0) | Lei 14.195/2021 art. 26 I (Übersetzung von Dokumenten, die vor Behörden/Cartórios vorgelegt werden, ist Aufgabe des tradutor público) | WebFetch Câmara (www2.camara.leg.br, normaatualizada) 24.11.2026 |
| Q3 | Pra valer no Brasil: em português · Código Civil · art. 224 (Bild 6,5) | CC art. 224 „Os documentos redigidos em língua estrangeira serão traduzidos para o português para ter efeitos legais no País.“ | Whitelist (R31-Beleg) |
| Q4 | Fé pública? Só com tradutor público · Em geral · Lei 14.195, art. 27 (Bild 10,0) | art. 27 caput und § 1 (keine Übersetzung hat fé pública ohne tradutor público; Ausnahmen I–IV → „Em geral“) | WebFetch Câmara 24.11.2026 |
| Q5 | Registro por idioma: tradutor de árabe · Lei 14.195/2021 · art. 23 (Bild 13,5) | art. 23: Habilitation und Registrierung je Sprache → Folgerung „tradutor de árabe“ | WebFetch Câmara 24.11.2026 |
| Q6 | Órgão pode pedir o original junto · Lei 14.195 · art. 27, § 2º (Bild 17,0, nur Hauptfassung) | art. 27 § 2º: Vermutung schließt Vorlage des Originals mit der Übersetzung nicht aus | WebFetch Câmara 24.11.2026 |
| Q7 | Lista de documentos? Confirme no órgão · Cada órgão tem a sua (Bild 24,0) | Rechner FAQ a8 „Como as regras variam, confirme sempre com o órgão de destino.“ | Rechner-Quelltext 24.11.2026 |
| Q8 | Envie a foto: preço na hora (Endcard) | Rechner fl1 „Foto ou PDF, quantos precisar.“, fl2 „Valor e data de entrega na hora.“ | Rechner-Quelltext 24.11.2026 |
| – | Requisiten (Guichê, Certidão mit Raster ohne Schrift, einfaches Blatt, Übersetzungsblatt mit Siegel, Pfeil, Ausweis-Karte mit Reitern, Büroklammer, Preisschild ohne Zahl, Klemmbrett, Foto-Ecken) | eigene SVG ohne Schrift, ohne Zahlen, ohne Wappen/Flaggen/Landkarte, keine nachgemachte arabische Schrift, kein Kundenfall | – |

planalto war nicht erreichbar (Proxy 403) → Lei 14.195 über die Câmara-Fassung gelesen.

**Bewusst nicht verwendet:** Apostila/Legalisation; Wege ohne Übersetzung; Transliteration von Namen; Lieferfristen, Urgência, Via física (Regel 12); Empfehlungen (Lehre R45).

## Ablauf (Designzeit; GMB lässt 17,0–20,5 weg, Endcard 5,0 s)
| Zeit | Text (Bild) | Beleg-Pille | Bild / Ereignis | SFX |
|---|---|---|---|---|
| 0–2,97 | Hook „Certidão / egípcia: / tradução / simples serve?“ + Pille „SIM ou NÃO?“ + Etikett „Certidão de nascimento · árabe → português · R$ 299 · na tabela“ | – | Guichê unten, Certidão + einfaches Blatt, „?“ über dem Blatt; 2,5 Ring um das einfache Blatt + Punch | pop 0,03 · stamp 2,5 |
| 3,0 | Em geral, não: / vale a juramentada. | Lei 14.195/2021 · art. 26 | Rollladen; Guichê steigt; einfaches Blatt wird Übersetzung mit Siegel; 5,5 Haken | whoosh · click 3,5 · pop 5,5 |
| 6,5 | Pra valer no Brasil: / em português. | Código Civil · art. 224 | Certidão → Pfeil (7,5 Punch) → Blatt PT; 8,5 Haken | whoosh · click 7,0 · stamp 7,5 · pop 8,5 |
| 10,0 | Fé pública? Só com / tradutor público. | Em geral · Lei 14.195, art. 27 | Übersetzungsblatt, Siegel 11,0 + Punch, Unterschrift; 12,5 Haken | whoosh · stamp 11,0 · pop 12,5 |
| 13,5 | Registro por idioma: / tradutor de árabe. | Lei 14.195/2021 · art. 23 | Ausweis-Karte, Reiter 14,0, mittlerer Reiter leuchtet 14,5 + Punch; 15,5 Haken | whoosh · click 14,0 · stamp 14,5 · pop 15,5 |
| 17,0 | Órgão pode pedir / o original junto. | Lei 14.195 · art. 27, § 2º | Original + Übersetzung mit Büroklammer 17,5; 19,0 Haken | whoosh · click 17,5 · pop 19,0 |
| 20,5 | Do árabe, na tabela: / R$ 299 a certidão. | Preço fixo · até 4 páginas | Certidão + Preisschild ohne Zahl 21,5 + Punch; 22,5 Haken | whoosh · stamp 21,5 · pop 22,5 |
| 24,0 | Lista de documentos? / Confirme no órgão. | Cada órgão tem a sua | Klemmbrett mit leeren Kästchen, „?“ 25,5 + Stempel, Haken 26,5 | whoosh · stamp 25,5 · pop 26,5 |
| 27,5–34,2 | Certidão / em árabe? / Envie a foto: / preço na hora. + link na bio + traduzme.com.br + (61) 99803-8363 | – | Certidão in Foto-Ecken + Haken 28,5 | stamp+hit 27,5 · pop 28,5 |
| 34,2 | Loop = Frame 0 | | | |

Lernpunkte (≥ 3 mit Warum): Dokument muss auf Português vorliegen, um in Brasilien zu wirken → vor Behörden übersetzt der tradutor público → nur seine Übersetzung hat in der Regel fé pública → Registrierung je Sprache (árabe) → Original kann zusätzlich verlangt werden → Festpreis je Certidão → Dokumentenliste beim Órgão prüfen.

## Kritiker-Runden
- Runde 1 (Fakten/Design/Hook/Conversion): Lei 14.195 selbst über die Câmara-Fassung geöffnet; „Em geral“ bei fé pública, „Confirme no órgão“ als eigene Szene; Preis nur mit „na tabela“, Endcard ohne Preis; Hook = Kauf-Zweifel (günstigerer Weg), IG/TikTok verraten die Antwort nicht.
- Runde 2: Marker-Puls des Hooks ragte über die Safe Zone (x 907) → Puls auf 0,03 begrenzt; Requisiten zu klein → vergrößert; Haken in den Szenen 17,0 / 20,5 / 24,0 lagen in der unteren UI-Zone → nach oben versetzt.
- Runde 3: keine offenen Mängel (Kontaktbögen Haupt 0–34,4 s und GMB 0–29,2 s, qa_frames PASS).
