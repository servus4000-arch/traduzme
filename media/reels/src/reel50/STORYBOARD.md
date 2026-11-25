# Reel 50 – „Casou nos EUA: tradutor de lá serve?“ (Post Mi 02.12.2026, ersetzt R48)

Certidão de casamento **inglês → português**, Etikett „R$ 129 na tabela“. Format **Mala de viagem** (Koffer in Sálvia mit Griff, Pinho-Gurten, Eckschonern, Kofferanhänger ohne Schrift; Futter in Areia als Bühne; Szenenwechsel = **Zíper-Schnitt**: eine dunkle Reißverschluss-Bahn mit harter Kante fährt 0,10 s vor dem Schlag von links über das Futter, deckt es auf dem Schlag ganz (harter Schnitt darunter) und ist bei +0,18 s rechts draußen), Grund **Dark #1F3B35**, Musik `music.py` **bossa 120 BPM**, D, seed 50, Master v2. Szenen 3,5 s, Endcard Standard „Envie a foto: preço na hora.“, Etikett in Frame 0 (Standard seit R35), Mitmach-Pille „SIM ou NÃO?“ (Standard, keine Knöpfe). Neue Variable (nicht im Bild): **YouTube-Beschreibung kurz** (Antwort + 3 Punkte + Link statt 6–7 Punkte).

Pflichtwechsel (keine Variable): R49 Envelope/Névoa/calm, R48 Guichê/Dark/lofi (Entwurf, nicht gepostet), R47 Encruzilhada/Pinho/pop, R46 Mesa de carimbos/Areia/funk → Mala de viagem/Dark/bossa (letztes gepostetes Dark-Reel R42 am 25.11., letztes bossa R44 am 27.11. auf Sálvia).

## Thema (ENTSCHEIDEN 25.11.2026, Zeile in marketing/lernen/social.md)
- Schritt 1: pedidos 30 T. status PAGO (SELECT 25.11.): ES→PT CNH dominiert (gesperrt); EN→PT: **Certidão de casamento 17.11.** (2 Seiten), Konvolut Klinik-Belege 13.11., Studienunterlagen 17.11.; PT→EN Diploma/Histórico/Antecedentes (gesperrt); FR→PT Attestation/Acte/Casier (R49/R31/R37); DE→PT Geburtsurkunde/Meldebescheinigung 18./24.11.; IT keine bezahlte Bestellung. analises 30 T.: en certidao de casamento 1 (Florida, Certification of Marriage mit Apostila-Blatt, 17.11.), en certidao de nascimento 2 (Kalifornien, Florida), en procuracao 1 (UK, Immobilienverkauf); it nur drei „fac-símile“-Auszüge (Test). capacidade: it **ativo = true** (seit dem letzten Stand neu), zh aus. Messungen: keine fällig (R44 30.11., R45 01.12.); Fazit-Ordner nichts nach 13.11.; Lagebild Woche 46.
- Kandidaten (Score = K×3 + N×2 + E×2 + B×2 + L):
  - **A Certidão de casamento EN→PT „Casou nos EUA: tradutor de lá serve?“ R$ 129 (K3 N2 E1 B0 L2 = 17) → gewählt**
  - B Certidão italiana IT→PT (cidadania/registro) R$ 119 (K1 N3 E1 B0 L2 = 13 < 14) – raus: nur Test-Uploads, kein Kaufnachweis
  - C Procuração EN→PT (UK, Imóvel no Brasil) R$ 139 + 49/pág. (K2 N1 E1 B1 L2 = 14) – nicht gewählt: Score niedriger, Rechtslage (RTD/Notar) ohne geöffnete Primärquelle
  - D Certidão de nascimento EN→PT (EUA, filho nascido lá) R$ 129 (K2 N2 E1 B0 L2 = 14) – nicht gewählt: niedriger als A, gleiche Quelle (Res. 155) → Folge-Kandidat
  - E Meldebescheinigung DE→PT (K3 N1 E1 B1 L2 = 17) – nicht gewählt: Gleichstand, nicht „klar höher“ (Auftrag); bleibt Kandidat für den DE-Slot 03./04.12.
- Grund: EN mit Sofortpreis, bezahlter Auftrag zum Dokument, echter Kauf-Zweifel (billiger/näher beim Übersetzer in den USA?), Primärquelle eindeutig (Res. CNJ 155/2012 art. 2º § 1º), kein Duplikat zu R20–R49 (R40 = Habilitação in Brasilien mit Certidão ES; R23/R46 = Apostila/Legalisation – hier bewusst weggelassen, Lehre 42: keine Lernpunkte früherer Reels wiederholen).
- B = 0 (R$ 129 < 130). Erwartete Wirkung: N2 geschätzt, nicht gemessen (≈ 300 Suchen „transcrição/traslado de casamento no exterior“ × 3 % × 3 % × R$ 129 ≈ R$ 35/Monat + LinkedIn B2B Imigração/Família).

## Quellen
| Q | Aussage | Quelle | Wie geprüft |
|---|---|---|---|
| Q1 | Certidão de casamento inglês → português **R$ 129 na tabela** (Etikett 0–2,97; Bild 20,5) | Supabase `precos` `WHERE ativo AND NOT placeholder`: `en / to_pt / certidao de casamento` **12900**, extra_pag null | SELECT 25.11.2026 (read-only) |
| Q1b | Marriage certificate = Typ `certidao de casamento` (1–2 Seiten; Averbações/Apostila = Teile desselben Dokuments, ohne Aufpreis); Festpreis je Dokument bis 4 Seiten je Datei (Beleg „Preço fixo · até 4 páginas“) | Edge-Functions `analisar` v47 (Typenliste „marriage certificate/license … 1-2 páginas“), `pix-cob` v60 `PAUSCHAL_MAX_PAG=4`; Rechner-Badge „Preço fixo“ | get_edge_function 25.11.2026; curl /orcamento-app 25.11.2026 |
| Q2 | No traslado: tradutor de junta brasileira · Res. CNJ 155 · art. 2º, § 1º (Bild 3,0) | Resolução CNJ 155/2012 (compilada, Stand Res. 583/2024) art. 2º § 1º: Dokumente „deverão ser traduzidos por tradutor público juramentado, inscrito em junta comercial brasileira“; art. 13 a: „certidão estrangeira de casamento legalizada … e traduzida“ | WebFetch atos.cnj.jus.br/files/compilado1435392024100166fc08bbe1602.pdf 25.11.2026 (art. 2º ohne Revogado-/Redação-Vermerk) |
| Q3 | Certidão consular? Aí, sem tradução · art. 13, a (Bild 6,5) | art. 13 a: „certidão de assento de casamento emitida por autoridade consular brasileira **ou** certidão estrangeira de casamento legalizada … e traduzida“ → die Konsulats-Certidão ist die Alternative ohne Übersetzung | wie Q2 |
| Q4 | Traslado: 1º Ofício do seu domicílio · art. 1º (Bild 10,0) | art. 1º: Traslado „será efetuado no Livro "E" do 1º Ofício de Registro Civil de Pessoas Naturais da Comarca do domicílio“ | wie Q2 |
| Q5 | Sem domicílio aqui? 1º Ofício do DF · art. 13, c (Bild 13,5) | art. 13 c: „Na falta de domicílio no Brasil, o traslado deverá ser efetuado no 1º Ofício do Distrito Federal“ | wie Q2 |
| Q6 | Junto: sua certidão de nascimento · Em geral · art. 13, b (Bild 17,0, nur Hauptfassung) | art. 13 b: „certidão de nascimento do cônjuge brasileiro, ou certidão de casamento anterior com prova da sua dissolução“ → „Em geral“ wegen der Alternative | wie Q2 |
| Q7 | Lista completa? Confirme no cartório · As regras variam (Bild 24,0) | Rechner FAQ a8 „Como as regras variam, confirme sempre com o órgão de destino.“ (Whitelist a8); Res. 155 art. 13 nennt weitere Unterlagen (c, d) | curl /orcamento-app 25.11.2026 |
| Q8 | Envie a foto: preço na hora (Endcard); Foto ou PDF; valor e data na hora; Pix; PDF com assinatura digital (Texte) | Rechner fl1–fl4 | curl /orcamento-app 25.11.2026 |
| – | Requisiten (Koffer, Kofferanhänger, Certidão de casamento mit Ringen, Übersetzung mit Stempelkasten, Übersetzung mit Siegel, Konsulats-Certidão, Haus, Gebäude mit Säulen, Pfeil, Geburts-Certidão, Büroklammer, Preisschild ohne Zahl, Klemmbrett, Foto-Ecken) | eigene SVG ohne Schrift, ohne Zahlen, ohne Wappen/Flaggen/Landkarte/Firmenlogo, kein Kundenfall | – |

**Bewusst nicht verwendet:** Apostila/Legalisation (Lehren R39/R46, Lernpunkt R23/R46; im Text höchstens „legalizada ou apostilada“ als Wortlaut der Resolução in YT/LinkedIn ohne Leistungszusage); Regime de bens/Pacto antenupcial (§§ 2–5, zu komplex); Wirkung des Traslado (§ 11) als Rechtsrat; Fristen und Zusatzoptionen; Empfehlungen (Lehre R45); Kundendaten; „sem custo extra“.

## Ablauf (Designzeit; GMB lässt 17,0–20,5 weg, Endcard 5,0 s)
| Zeit | Text (Bild) | Beleg-Pille | Bild / Ereignis | SFX |
|---|---|---|---|---|
| 0–2,97 | Hook „Casou nos / EUA: tradutor / de lá serve?“ + Pille „SIM ou NÃO?“ + Etikett „Certidão de casamento · inglês → português · R$ 129 · na tabela“ | – | Koffer unten, Certidão schräg + Übersetzung „von dort“ mit Stempelkasten, „?“ daneben; 2,5 Ring um die Übersetzung + Punch; Requisiten über y 1490 | pop 0,03 · stamp 2,5 |
| 3,0 | No traslado: tradutor / de junta brasileira. | Res. CNJ 155 · art. 2º, § 1º | Zíper; Koffer steigt; Übersetzung von dort rutscht herein, blasst ab, Übersetzung mit Siegel davor; 5,5 Haken | whoosh · click 3,5 · pop 5,5 |
| 6,5 | Certidão consular? / Aí, sem tradução. | Res. CNJ 155 · art. 13, a | Konsulats-Certidão rückt 7,0 in die Mitte (Klick), 7,5 hebt sich + Punch; 8,5 Haken | whoosh · click 7,0 · stamp 7,5 · pop 8,5 |
| 10,0 | Traslado: 1º Ofício / do seu domicílio. | Res. CNJ 155 · art. 1º | Haus, Pfeil zeichnet sich 10,5, Gebäude 11,0 + Punch; 12,5 Haken | whoosh · stamp 11,0 · pop 12,5 |
| 13,5 | Sem domicílio aqui? / 1º Ofício do DF. | Res. CNJ 155 · art. 13, c | gestricheltes Haus blasst 14,0 ab (Klick), Gebäude 14,5 groß + Punch; 15,5 Haken | whoosh · click 14,0 · stamp 14,5 · pop 15,5 |
| 17,0 | Junto: sua certidão / de nascimento. | Em geral · art. 13, b | Certidão de casamento + Geburts-Certidão, Büroklammer 17,5; 19,0 Haken | whoosh · click 17,5 · pop 19,0 |
| 20,5 | Inglês, na tabela: / R$ 129 a certidão. | Preço fixo · até 4 páginas | Certidão + Preisschild ohne Zahl 21,5 + Punch; 22,5 Haken | whoosh · stamp 21,5 · pop 22,5 |
| 24,0 | Lista completa? / Confirme no cartório. | As regras variam | Klemmbrett, „?“ 25,5 + Stempel, Haken 26,5 | whoosh · stamp 25,5 · pop 26,5 |
| 27,5–34,2 | Casou nos / EUA? / Envie a foto: / preço na hora. + link na bio + traduzme.com.br + (61) 99803-8363 | – | Certidão gerade in Foto-Ecken + Haken 28,5 | stamp+hit 27,5 · pop 28,5 |
| 34,2 | Loop = Frame 0 | | | |

Lernpunkte (≥ 3 mit Warum): Übersetzung für den Traslado nur durch tradutor público juramentado einer brasilianischen Junta → Ausnahme: Certidão vom brasilianischen Konsulat braucht keine Übersetzung → Traslado im 1º Ofício des Wohnsitzes → ohne Wohnsitz in Brasilien 1º Ofício do DF → eigene Geburtsurkunde mitbringen (em geral) → Festpreis für die Certidão → Liste beim Cartório bestätigen.

## Kritiker-Runden (Storyboard)
- **Runde 1 Fakten:** Res. CNJ 155/2012 selbst geöffnet (compilada mit Res. 419/2021 und 583/2024; art. 1º, 2º, 13 ohne Revogado; Vermerke nur bei art. 13 § 3 ff.). Hook-Antwort „NÃO“ trägt art. 2º § 1º wörtlich („inscrito em junta comercial brasileira“); gilt für den Traslado (im Bild „No traslado:“), keine Aussage zu anderen Behörden. Konsulats-Alternative aus art. 13 a. „Em geral“ bei art. 13 b wegen der Alternative (casamento anterior + dissolução). Apostila weggelassen (Lehre 42, R23/R46). Preis 12900 mit „na tabela“, Einstufung aus analisar v47, Festpreis bis 4 Seiten (Lehre R41).
- **Runde 1 Design:** Dark-Grund → Hook Weiß mit Sálvia/Dark-Marker (Weiß/Dark, Dark/Sálvia), Captions Areia/Dark, Belege Papier/Dark, Chips Pinho/Weiß, Endcard Weiß/Dark. Held-Objekt Koffer 760 px = 70 % Breite. Hook-Requisiten über y 1490 (Lehre 48-1).
- **Runde 1 Hook/Tempo:** Hook 6 Wörter, Kauf-Zweifel, keine Preisfrage; Etikett nennt Dokument/Richtung/Preis und sagt nichts darüber, wer übersetzen darf → verrät SIM/NÃO nicht. Payoff 2,5 s (Ring), Antwort 3,0 s, 2. Lernpunkt 6,5 s.
- **Runde 1 Conversion:** IG/TikTok ohne Antwort (Regel 14), Zeile 2 „Resposta no vídeo 👀“; Endcard ohne Preis; CTA-Chip ab 3,0 s; YT/LinkedIn antworten mit Quelle; UTM reel50.
- **Runde 2:** „Junto: certidão de / nascimento sua.“ (holprig) → „Junto: sua certidão / de nascimento.“; Kontaktbogen: Gebäude überdeckte die Pfeilspitze (10,0–13,5) → Haus/Pfeil/Gebäude enger gestellt (Gebäude 0,68); Endcard-Certidão höher (lokal y 270).
- **Runde 3:** keine offenen Mängel am Storyboard.

## Fix nach Abnahme 25.11. (50-A, 50-1, nur Ton)
- 50-A: Hook-Payoff-stamp 2,5 s lag im Präsenzband 1,8–4,2 kHz nur +1,9 dB (GMB +1,6) über der Musik, weil der Tiefbass-Körper das Breitband-Limit +4 dB ausschöpfte. Fix in audio.py: stamp-Körper Hochpass 300 Hz (4. Ordnung), Präsenz-Schicht ×4,0 (2,5 s ×8,0), GJ_MAIN/GJ_GMB neu iteriert (Ziel Breitband-20-ms-Spitze ≈ +3,45 dB).
- Ergebnis Haupt (20-ms-Spitze, [t, t+0,45 s], Mix − Musik): stamp 2,5 Präsenz +7,0 / 0,3–8 kHz +4,1; 7,5 +21,7 / +4,3; 11,0 +20,7 / +6,8; 14,5 +12,2 / +6,4; 21,5 +10,1 / +4,6; 25,5 +15,3 / +6,4; 27,5 +10,9 / +4,7; Breitband alle 27 SFX +3,44 … +3,49 dB. GMB: 2,5 +6,9 / +4,1; 14,5 +12,1; 18,0 (= 21,5) +13,4; 24,0 (= Endcard) +13,8; Breitband +3,42 … +3,49 dB.
- 2,5 s erreicht ≥ +6, nicht ≥ +9: stärkere Präsenz (×14) hob das Band nur auf +7,6, weil die Präsenz-Schicht dann selbst das Breitband-Limit setzt (Musik an der Stelle präsenzreich).
- 50-5: Video nicht neu gerendert; Ton per Remux (`-c:v copy`, AAC 256k 48 kHz, faststart) in Haupt und GMB eingesetzt, Video-Stream bit-gleich (md5 des Videostreams vorher = nachher).
