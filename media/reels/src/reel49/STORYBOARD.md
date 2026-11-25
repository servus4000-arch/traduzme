# Reel 49 – „Carta de emprego: tradução simples serve?“ (Post Do 26.11.2026, ersetzt R43)

Declaração de emprego (Carta de emprego / Attestation d'emploi) **francês → português**, Etikett „R$ 119 na tabela“. Format **Envelope** (großer Briefumschlag in Pinho mit Luftpost-Streifen-Rand in Sálvia/Areia und Briefmarken-Form ohne Schrift; Papier-Einlage als Bühne; Szenenwechsel = **Klappen-Schnitt**: die Umschlag-Klappe fällt 0,10 s vor dem Schlag über die Einlage, deckt sie auf dem Schlag ganz (harter Schnitt darunter) und ist bei +0,18 s wieder oben), Grund **Névoa #BDCBCB**, Musik `music.py` **calm 120 BPM mit leisem Lofi-Puls** (wie R26), A, seed 49, Master v2. Szenen 3,5 s, Endcard Standard „Envie a foto: preço na hora.“, Etikett in Frame 0 (Standard seit R35), Mitmach-Pille „SIM ou NÃO?“ (Standard, keine Knöpfe). Neue Variable (nicht im Bild): **TikTok-Postzeit 18:30 SP statt ~11:20 SP** (übernommen von R48, dort nicht gemessen, weil R48 nicht gepostet wird).

Pflichtwechsel (keine Variable): R48 Guichê/Dark/lofi, R47 Encruzilhada/Pinho/pop, R42 (25.11.) Visor da câmera/Dark/funk, R44 (27.11.) Pasta/Sálvia/bossa → Envelope/Névoa/calm.

## Thema (ENTSCHEIDEN 25.11.2026, Zeile in marketing/lernen/social.md)
- Schritt 1: pedidos 30 T. status PAGO (SELECT 25.11.): ES→PT CNH dominiert (gesperrt), FR: FR→PT „Attestation“ 14.11. (1 S.), FR→PT 1-Seiten-Dok. 11.11., FR→PT Casier 10.11. (R37), FR→PT Acte de naissance 30.10. (R31-Nähe), PT→FR Certidão de casamento mit Apostila digital 19.11.; IT keine bezahlte Bestellung; DE→PT Geburtsurkunde + Meldebescheinigung 24.11. analises 30 T. FR: zwei „Attestation d'emploi“ (Universität in Montréal, 12.11./14.11., typ declaracao simples, 1 S.), Atestado einer Botschaft (16.11.), Relevé de notes, CIEC-Auszug; IT nur drei Auszüge als „fac-símile“ (Test). Messungen: keine fällig (R40 72 h erst 26.11.); Fazit-Ordner nichts nach 13.11.
- Kandidaten (Score = K×3 + N×2 + E×2 + B×2 + L):
  - **A Carta de emprego FR→PT „tradução simples serve?“ R$ 119 (K3 N1 E1 B0 L2 = 15) → gewählt**
  - B Certidão de casamento PT→FR mit Apostila digital (K3 N1 E1 B0 L2 = 15) – raus: Kern „Apostila do original traduzida junto“ = R39-Lernpunkt; Annahme der brasilianischen Übersetzung in Frankreich nicht belegt (Lehre R46/R47)
  - C Acte de naissance FR→PT (Haiti/Líbano/Nice) (K3 N1 E1 B0 L2 = 15) – raus: Nähe R31 (Certidão FR), Haiti = Legalisation direkt nach R46
  - D Certidão IT→PT / cidadania PT→IT (K1 N3 E1 B0 L2 = 13 < 14) – raus: kein Kaufnachweis (nur Test-Uploads), Konsulate nehmen digitale Übersetzungen teils nicht an (Memory italienisch-markt)
  - E Meldebescheinigung DE→PT (K3 N1 E1 B1 L2 = 17) – nicht gewählt: Auftrag „R49 bevorzugt Francês oder Italiano, sonst EN“ (DE nicht im Pool); als Kandidat für den DE-Slot 02.12. notiert
  - F Certidão de casamento EN→PT (K3 N1 E1 B0 L2 = 15) – nur Rückfall (EN)
- Grund: FR mit Sofortpreis (capacidade fr ativo), Kaufnachweis zum Dokument, Kauf-Zweifel „ist doch nur ein Brief einer Firma – reicht eine einfache Übersetzung?“, kein Duplikat zu R20–R47 (R48-Inhalt Lei 14.195 laut Auftrag in anderer Sprache wiederverwendbar; neues Dokument, neues Held-Objekt, neue Szene „Qualquer documento: carta também.“).
- B = 0 (R$ 119 < 130). Erwartete Wirkung: N1 geschätzt, nicht gemessen (≈ 100 Suchen × 3 % × 3 % × R$ 119 ≈ R$ 11/Monat + LinkedIn B2B RH/Mobilidade).

## Quellen
| Q | Aussage | Quelle | Wie geprüft |
|---|---|---|---|
| Q1 | Declaração de emprego francês → português **R$ 119 na tabela** (Etikett 0–2,97; Bild 20,5) | Supabase `precos` `WHERE ativo AND NOT placeholder`: `fr / to_pt / declaracao simples` **11900**, extra_pag null | SELECT 25.11.2026 (read-only) |
| Q1b | Carta/declaração de emprego = Typ `declaracao simples` („declaração curta de 1 página … declaração de vínculo/emprego, employment letter“), Festpreis je Dokument bis 4 Seiten je Datei; Rechner-Label „Declaração simples“, Badge „Preço fixo“ | Edge-Functions `analisar` v47 (Typenliste), `pix-cob` v60 `PAUSCHAL_MAX_PAG=4`; Rechner-Quelltext /orcamento-app | get_edge_function 25.11.2026; curl 25.11.2026 |
| Q2 | Órgão ou cartório: em geral, não · Lei 14.195/2021 · art. 26 (Bild 3,0) | art. 26 caput „São atividades privativas do tradutor (…) público:“, I „traduzir qualquer documento que tenha de ser apresentado em outro idioma perante pessoa jurídica de direito público interno ou perante serviços notariais e de registro de notas ou de títulos e documentos“; p. ú. (ad hoc, agente público) → „Em geral“ | WebFetch planalto 25.11.2026 (keine Revogado-/Redação-Vermerke bei art. 23, 26, 27) |
| Q3 | Qualquer documento: carta também · Art. 26, I: „qualquer documento“ (Bild 6,5) | art. 26 I Wortlaut „qualquer documento que tenha de ser apresentado …“ (Kontext: vor Órgão/Cartório, Szene davor) | wie Q2 |
| Q4 | Fé pública? Só com tradutor público · Em geral · Lei 14.195, art. 27 (Bild 10,0) | art. 27 § 1º „Nenhuma tradução terá fé pública se não for realizada por tradutor (…) público, exceto …“ (4 Ausnahmen → „Em geral“) | wie Q2 |
| Q5 | Registro por idioma: tradutor de francês · Lei 14.195/2021 · art. 23 (Bild 13,5) | art. 23 „poderá habilitar-se e registrar-se para um ou mais idiomas estrangeiros“; art. 26 p. ú. I „habilitado para o idioma“ | wie Q2 |
| Q6 | O original vai junto com a tradução · Lei 14.195 · art. 27, § 2º (Bild 17,0, nur Hauptfassung) | art. 27 § 2º I: „A presunção … não afasta: I – a obrigação de o documento na língua original acompanhar a sua respectiva tradução“ → Pflicht (Lehre 48-A) | wie Q2 |
| Q7 | Lista de documentos? Confirme no órgão · Cada órgão tem a sua (Bild 24,0) | Rechner FAQ a8 „Como as regras variam, confirme sempre com o órgão de destino.“ (Whitelist a8) | curl /orcamento-app 25.11.2026 |
| Q8 | Envie a foto: preço na hora (Endcard); Foto ou PDF; valor e data na hora; Pix; PDF com assinatura digital (Texte) | Rechner fl1 „Foto ou PDF, quantos precisar.“, fl2 „Valor e data de entrega na hora.“, fl3 „Pague por Pix“, fl4 „PDF juramentado com assinatura digital …“ | curl /orcamento-app 25.11.2026 |
| – | Requisiten (Umschlag, Carta mit Briefkopf-Band/Logo-Kreis/Zeilen/Unterschrift/Ring-Stempel, einfaches Blatt, Übersetzungsblatt mit Siegel, Dokumenten-Fächer (Certidão-Raster, Diplom-Querformat mit Band, Carta), Ausweis-Karte mit Reitern, Büroklammer, Preisschild ohne Zahl, Klemmbrett, Foto-Ecken) | eigene SVG ohne Schrift, ohne Zahlen, ohne Wappen/Flaggen/Landkarte/Firmenlogo, kein Kundenfall | – |

**Bewusst nicht verwendet:** Zweck der Carta (INSS, Visto, Residência, Revalidação) – keine Primärquelle geöffnet, keine Behörde behaupten; Apostila/Legalisation (Lehre R39/R46); Kanada/Québec/Frankreich als Herkunft im Bild; Lieferfristen und Zusatzoptionen; Empfehlungen (Lehre R45); Kundendaten; „sem custo extra“.

## Ablauf (Designzeit; GMB lässt 17,0–20,5 weg, Endcard 5,0 s)
| Zeit | Text (Bild) | Beleg-Pille | Bild / Ereignis | SFX |
|---|---|---|---|---|
| 0–2,97 | Hook „Carta de / emprego: / tradução / simples serve?“ + Pille „SIM ou NÃO?“ + Etikett „Declaração de emprego · francês → português · R$ 119 · na tabela“ | – | Umschlag unten, Carta schräg + einfaches Blatt, „?“ rechts neben dem einfachen Blatt; 2,5 Ring um das einfache Blatt + Punch; Requisiten über y 1490 (Lehre 48-1) | pop 0,03 · stamp 2,5 |
| 3,0 | Órgão ou cartório: / em geral, não. | Lei 14.195/2021 · art. 26 | Klappe; Umschlag steigt; einfaches Blatt rutscht herein, blasst ab, Übersetzung mit Siegel davor; 5,5 Haken | whoosh · click 3,5 · pop 5,5 |
| 6,5 | Qualquer documento: / carta também. | Art. 26, I: „qualquer documento“ | Fächer aus drei Dokumenten (Certidão, Diplom, Carta); 7,0 Fächer öffnet (Klick), 7,5 Carta hebt sich + Punch; 8,5 Haken | whoosh · click 7,0 · stamp 7,5 · pop 8,5 |
| 10,0 | Fé pública? Só com / tradutor público. | Em geral · Lei 14.195, art. 27 | Übersetzungsblatt groß, Siegel 11,0 + Punch, Unterschrift; 12,5 Haken | whoosh · stamp 11,0 · pop 12,5 |
| 13,5 | Registro por idioma: / tradutor de francês. | Lei 14.195/2021 · art. 23 | Ausweis-Karte, Reiter 14,0, mittlerer Reiter 14,5 + Punch; 15,5 Haken | whoosh · click 14,0 · stamp 14,5 · pop 15,5 |
| 17,0 | O original vai / junto com a tradução. | Lei 14.195 · art. 27, § 2º | Carta + Übersetzung, Büroklammer 17,5; 19,0 Haken | whoosh · click 17,5 · pop 19,0 |
| 20,5 | Francês, na tabela: / R$ 119 a declaração. | Declaração curta · 1 página | Carta + Preisschild ohne Zahl 21,5 + Punch; 22,5 Haken | whoosh · stamp 21,5 · pop 22,5 |
| 24,0 | Lista de documentos? / Confirme no órgão. | Cada órgão tem a sua | Klemmbrett, „?“ 25,5 + Stempel, Haken 26,5 | whoosh · stamp 25,5 · pop 26,5 |
| 27,5–34,2 | Carta em / francês? / Envie a foto: / preço na hora. + link na bio + traduzme.com.br + (61) 99803-8363 | – | Carta gerade in Foto-Ecken + Haken 28,5 | stamp+hit 27,5 · pop 28,5 |
| 34,2 | Loop = Frame 0 | | | |

Lernpunkte (≥ 3 mit Warum): vor Órgão/Cartório übersetzt der tradutor público → das gilt für jedes Dokument, auch eine Firmen-Carta → nur seine Übersetzung hat in der Regel fé pública → Registrierung je Sprache (francês) → das Original geht per Gesetz mit → Festpreis für die kurze Declaração → Dokumentenliste beim Órgão prüfen.

## Kritiker-Runden (Storyboard)
- **Runde 1 Fakten:** Lei 14.195 selbst auf planalto geöffnet (art. 22–27, Vermerke nur „Vide ADI 7196“ bei art. 22 p. ú.). art. 26 I nennt Órgão (pessoa jurídica de direito público interno) und Cartórios de notas/RTD → „Órgão ou cartório: em geral, não.“ mit „Em geral“, weil p. ú. Ausnahmen kennt und Registro Civil nicht wörtlich genannt ist. Szene 6,5 zitiert „qualquer documento“ wörtlich, steht direkt nach der Órgão/Cartório-Szene (kein Satz „jede Carta braucht juramentada“ ohne Kontext). Original-Szene als Pflicht (48-A). Preis 11900 mit „na tabela“; Einstufung declaracao simples aus analisar v47; kein Gesamt-/Ab-Preis. Kein Zweck der Carta genannt (keine Quelle).
- **Runde 1 Design:** Névoa-Grund → Hook Dark mit Pinho-Marker/Weiß (Weiß/Pinho, Dark/Névoa), Captions Areia/Dark mit Sálvia-Marker, Belege Papier/Dark mit Pinho-Rand (Schema R45). Held-Objekt Umschlag 760 px = 70 % Breite. Hook-Requisiten über y 1490 (Lehre 48-1): Umschlag im Hook höher, Etikett kompakter (744 × 248 statt 292), Requisiten 0,58–0,62 skaliert.
- **Runde 1 Hook/Tempo:** Hook 6 Wörter, Kauf-Zweifel (günstigerer Weg), keine Preisfrage; Etikett nennt Dokument/Richtung/Preis, sagt nichts zu simples/juramentada → verrät SIM/NÃO nicht. Payoff 2,5 s (Ring), Antwort 3,0 s, 2. Lernpunkt 6,5 s. Szenen 3,5 s.
- **Runde 1 Conversion:** IG/TikTok ohne Antwort (Regel 14), Zeile 2 „Resposta no vídeo 👀“; Endcard ohne Preis; CTA-Chip ab 3,0 s; YT/LinkedIn antworten mit Quelle; UTM reel49.
- **Runde 2:** „Pra órgão ou cartório:“ (22 Zeichen) und „Do francês, na tabela:“ zu breit für die Safe Zone → „Órgão ou cartório:“ / „Francês, na tabela:“. Hook „Carta de emprego em francês: …“ (7 Wörter, 5 Zeilen) drückte Pille/Etikett unter y 1250 → Hook ohne „em francês“ (Sprache steht im Etikett und auf der Endcard). Beleg 6,5 als Zitat statt Paragraphen-Nummer allein (zeigt, woher „qualquer“ kommt).
- **Runde 3:** keine offenen Mängel am Storyboard.
