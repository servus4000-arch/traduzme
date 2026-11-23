# Reel 47 – „Divórcio na Alemanha: vai pro STJ?“ (Post Di 01.12.2026)

Sentença de divórcio **alemão → português**, Etikett „R$ 159 por lauda na tabela“. Format **Encruzilhada** (Wegweiser-Tafel mit Weggabel: links Haus/Cartório, rechts Gericht mit Waage; Szenenwechsel = Wegweiser-Wisch: Pfeilschild fährt 0,10 s vor dem Schlag ein, Schnitt auf dem Schlag, fährt bis +0,18 s hinaus), Grund **Pinho #376259**, Musik `music.py` **pop 120 BPM**, C, seed 47, Master v2. Szenen 3,5 s, Endcard Standard „Envie a foto: preço na hora.“, Etikett in Frame 0 (Standard seit R35). Neue Variable (im Bild): **Mitmach als zwei Antwort-Knöpfe „SIM“ | „NÃO“** statt einer Pille „SIM ou NÃO?“ (siehe social/reels/reel47-texte.md).

## Thema (ENTSCHEIDEN 23.11.2026, Zeile in marketing/lernen/social.md)
- Kaufnachweis: pedidos status PAGO 30 T. – Sentença de divórcio EN→PT bezahlt 17.11. (mehrseitig, je Lauda); DE-Scheidungsurteile nur als Such-/Upload-Signal (K1). Keine Kundendaten im Reel.
- Kandidaten: **A Divórcio na Alemanha „vai pro STJ?“ DE→PT R$ 159/Lauda (K1 N2 E1 B3 L2 = 17) → gewählt** / B Divórcio EN→PT (K3 N2 E1 B3 L0, raus: Sprachquote – mindestens jedes 2. Reel AR/DE, R44–R46 ohne) / C Führungszeugnis DE→PT (K2 N1 E1 B1 L2 = 14, raus: Nähe R37/R26/R45) / D PT→DE Familienpaket (20, raus: Annahme in Deutschland nicht belegt, OLG Sachsen/Bamberg) / E Antecedentes Líbano AR→PT (16, raus: Legalisation direkt nach R46, Nähe R20/R26).
- Grund: DE (Quote), B = 3 (Sentença mehrseitig je Lauda), Score ≥ 14, kein Duplikat zu R20–R46, kein CNH/Apostila/Legalisation.

## Quellen
| Q | Aussage | Quelle | Wie geprüft |
|---|---|---|---|
| Q1 | Sentença de divórcio alemão → português **R$ 159 por lauda na tabela** (Etikett 0–2,97; Bild 20,5) | Supabase `precos` `WHERE ativo AND NOT placeholder`: `de / to_pt / tecnica` **15900**, extra_pag null (daneben `de/to_pt/certidao de divorcio` 16900 Festpreis, `comum` 14900) | SELECT 23.11.2026 (read-only) |
| Q1b | Einstufung: „Sentença longa de divórcio = outro (técnico)“, Gerichtstexte = técnico, `outro` je Lauda | Edge-Function `analisar` v40 | get_edge_function 23.11.2026 |
| Q2 | Nem sempre: depende da sentença · Sentença estrangeira · STJ (Bild 3,0) · Consensual e simples? Direto no cartório · Em geral · averbação · STJ (Bild 6,5) · Guarda, pensão, bens? Passa pelo STJ · Homologação · STJ (Bild 10,0) | STJ „Sentença estrangeira“ (www.stj.jus.br/sites/portalp/Processos/Sentenca-Estrangeira, Stände 09/11/2021 und 06/10/2025): divórcio consensual simples ou puro (nur Auflösung) braucht keine Homologation, Averbação direkt im cartório de registro civil (Provimento 53 CNJ); mit guarda, alimentos oder partilha ist die Homologation „continua necessária“ | WebFetch 23.11.2026 (selbst geöffnet) |
| Q3 | Nos dois: tradução juramentada · Em geral · STJ e TJMG (Bild 13,5) | TJMG (publ. 18/03/2016, akt. 24/06/2017): averbação direta für divórcio consensual simples ou puro mit „tradução oficial juramentada“; CPC art. 961 §5, Provimento 53/2016; STJ-Seite: Übersetzung durch tradutor juramentado | WebFetch 23.11.2026 |
| Q3b | Tradutor juramentado de Junta Comercial · Regra do STJ (Bild 17,0, nur Hauptfassung) | STJ-Seite: „A tradução deve ser feita por tradutor juramentado por uma junta comercial.“ | WebFetch 23.11.2026 |
| Q4 | PDF assinado serve? Confirme no órgão · Cartório ou STJ (Bild 24,0) | STJ-Seite „documentação traduzida deve ser entregue em papel“ (Kontext unklar → **offen**, deshalb nur Frage + Confirme); Rechner FAQ a8 „Como as regras variam, confirme sempre com o órgão de destino.“; REELS-REGELN-v2 Punkt 12 | WebFetch / Rechner-Quelltext 23.11.2026 |
| Q5 | Envie a foto: preço na hora (Endcard); „Texto especial“ | Rechner fl1 „Foto ou PDF, quantos precisar.“, fl2 „Valor e data de entrega na hora.“; Badge „Texto especial“ | Rechner-Quelltext 23.11.2026 |
| – | Requisiten (Tafel, Weggabel, Haus mit Tür, Gericht mit Waage, Sentença, Übersetzungsblatt, Junta-Gebäude, Laudas-Fächer, Preisschild ohne Zahl, Handy, Papier, Foto-Ecken) | eigene SVG ohne Schrift, ohne Zahlen, ohne Wappen/Flaggen/Landkarte, kein Kundenfall | – |

planalto (CPC) und CNJ (Provimento 53) waren nicht erreichbar → nur über STJ/TJMG zitiert.

**Bewusst nicht verwendet:** Apostila/Legalisation der deutschen Sentença (Legalisationsthema direkt nach R46 gesperrt; TJMG nennt 2016/2017 noch „chancela consular“); Kosten/Fristen/Anwaltspflicht der Homologation; deutsches Scheidungsrecht; „papel obrigatório“ als Aussage; Gesamtpreis (Laudas unbekannt); Lieferfristen; Empfehlungen (Lehre R45).

## Ablauf (Designzeit; GMB lässt 17,0–20,5 weg, Endcard 5,0 s)
| Zeit | Text (Bild) | Beleg-Pille | Bild / Ereignis | SFX |
|---|---|---|---|---|
| 0–2,97 | Hook „Divórcio na / Alemanha: vai / pro STJ?“ + Knöpfe „SIM“ „NÃO“ + Etikett „Sentença de divórcio · alemão → português · R$ 159 por lauda na tabela“ | – | Tafel unten, Sentença schräg an der Gabel, „?“ pulsiert; 2,5 Ring um die Gabel + Punch | pop 0,03 · stamp 2,5 |
| 3,0 | Nem sempre: / depende da sentença. | Sentença estrangeira · STJ | Wisch; Tafel steigt; 3,5 linker Weg leuchtet, 4,5 rechter; 5,5 Haken | whoosh · click 3,5 · pop 5,5 |
| 6,5 | Consensual e simples? / Direto no cartório. | Em geral · averbação · STJ | Sentença fährt zum Haus (7,0), 7,5 Tür öffnet + Punch, 8,5 Haken | whoosh · click 7,0 · stamp 7,5 · pop 8,5 |
| 10,0 | Guarda, pensão, bens? / Passa pelo STJ. | Homologação · STJ | Sentença fährt zum Gericht; Marken 11,0/11,5/12,0; 12,5 Haken | whoosh · click 11,0 · pop 12,5 |
| 13,5 | Nos dois: tradução / juramentada. | Em geral · STJ e TJMG | Übersetzungsblatt gleitet heraus 14,0; Siegel 14,5 + Punch; 15,5 Haken | whoosh · click 14,0 · stamp 14,5 · pop 15,5 |
| 17,0 | Tradutor juramentado / de Junta Comercial. | Regra do STJ | Unterschrift wird gezogen 17,5; Junta-Gebäude 18,0; 19,0 Haken | whoosh · click 17,5 · pop 19,0 |
| 20,5 | Do alemão, na tabela: / R$ 159 por lauda. | Sentença · texto especial | Laudas-Fächer, Preisschild ohne Zahl 21,5 + Punch, Haken 22,5 | whoosh · stamp 21,5 · pop 22,5 |
| 24,0 | PDF assinado serve? / Confirme no órgão. | Cartório ou STJ | Handy ab dem Schnitt (24,5 springt auf), Papier 25,0, „?“ 25,5 + Stempel, Haken 26,5 | whoosh · stamp 25,5 · pop 26,5 |
| 27,5–34,2 | Divórcio / alemão? / Envie a foto: / preço na hora. + link na bio + traduzme.com.br + (61) 99803-8363 | – | Sentença gerade in Foto-Ecken + Haken (Lehre 42-1) | stamp 27,5 · pop 28,5 |
| 34,2 | Loop = Frame 0 | | | |

Lernpunkte (≥ 3 mit Warum): ob STJ nötig ist, hängt vom Inhalt ab → nur Auflösung (consensual simples) geht direkt ins Cartório → mit Guarda/Alimentos/Partilha Homologation im STJ → in beiden Wegen tradução juramentada → STJ verlangt Junta-Comercial-Übersetzer → Preis je Lauda → Form (PDF/Papier) beim Órgão prüfen.

## Kritiker-Runden
- Runde 1 (Fakten/Design/Hook/Conversion): Quellen selbst geöffnet (STJ, TJMG); „em geral“ + „Confirme no órgão“; kein Gesamtpreis; Hook-Frage Kauf-Zweifel; IG/TikTok ohne Antwort.
- Runde 2: Hook-Bild im 3:4-Ausschnitt zu tief → hochgesetzt; Captions x 962/921 über Safe Zone → gekürzt; Junta-Gebäude 1,1×; leere Tafel 24,2–24,4 → Handy ab Schnitt; Endcard-Haken angeschnitten → tiefer; Szene 2 ließ „consensual“ weg → „Consensual e simples?“ (STJ-Wortlaut).
- Runde 3: keine offenen Mängel (Kontaktbögen Haupt 0–34,4 s und GMB 0–29,2 s, qa_frames PASS).
