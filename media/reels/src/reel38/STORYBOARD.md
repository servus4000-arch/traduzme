# Reel 38 – „Boletim alemão: a tradução muda a nota?“ (Do 19.11.2026)

**Thema (ENTSCHEIDEN, Score 16):** Boletim escolar (Zeugnis) alemão → português. Kauf-Zweifel der Eltern: Ändert die Übersetzung die deutsche Note (1 = beste Note)? Antwort im Video: NÃO, die Ziffer bleibt; die Schule vergleicht.
**Etikett Frame 0 (Standard seit R35):** „Boletim escolar · alemão → português · R$ 179 + R$ 80 por página extra“. Ein Preis + Seitenzuschlag, nennt weder SIM noch NÃO, keine Note → legt die Antwort nicht nahe. Hook-Frage = Kauf-Zweifel, nicht die Preisfrage.
**Variable (genau eine, berührt die ersten 3 s und den LinkedIn-Einstieg nicht):** Mitte gestrafft – 7 Szenen à 3,0 s statt 3,5 s, Loop-Punkt 30,7 s statt 34,2 s (R37). Hook (0–3,0 s), Etikett, Endcard (6,7 s), Mitmach-Form (SIM/NÃO) und LinkedIn-Einstieg (Frage + UTM in Zeile 1 wie R37) bleiben.
**Pflichtwechsel:** Format Zeugnis-Close-up mit Wisch-Übersetzung (Papierbogen auf Sálvia, Mask-Reveal mit harter Kante von links) statt Quiz em 3 cartas (R37) / Dokument-Duell (R36); Grund Sálvia #97B9A8 (R37 Areia, R36 Dark); Musik funk 120 BPM, A, seed 38 (R37 bossa, R36 lofi).

## Ablauf (Designzeit, 120 BPM, Schlag 0,5 s)

| Zeit | Bild (Held-Objekt Papierbogen) | Text im Bild | Beleg-Pille | Quelle |
|---|---|---|---|---|
| 0,0–3,0 | Bogen unten: Notenkästchen „1“ → Pfeil → gestricheltes Kästchen mit „?“ (pulsiert). 2,5 s Payoff: Kästchen zeigt „1“ (Pinho), Gleichheitszeichen, Haken, Punch | Hook „Boletim / alemão: a / tradução / muda a nota?“ (7 W.) · Chip „Comenta SIM ou NÃO“ · Etikett | – | Q1 (Etikett) |
| 3,0–6,0 | Bogen steigt; Original-Zeugnis (1 · 2 · 1) = Übersetzung (1 · 2 · 1, Siegel); Haken 4,0 | „NÃO: a nota / fica igual.“ | Lei 14.195/2021, art. 27 | Q4 |
| 6,0–9,0 | Skala: „1“ (Pinho) … „6“; Ring auf der 1 (7,0 Punch), Stern + 6 blasst ab (8,0) | „Na Alemanha: / 1 = sehr gut.“ | Em geral · ex.: NRW | Q5 |
| 9,0–12,0 | Zeile Original „1“ → Pfeil → Zeile Übersetzung „1“ (9,5), Siegel 10,0, Haken 10,5 | „Na tradução: / 1 (muito bom).“ | Exemplo · número igual | Q4 (Beispiel) |
| 12,0–15,0 | Zeugnis · Schule · Waage kippt (13,0 Punch), Haken 14,0 | „Quem compara: / a escola.“ | LDB, art. 23 e 24 | Q6 |
| 15,0–18,0 | Drei Schulen mit verschiedenen Checklisten, Lupe fährt, Haken 16,0 | „Regras: da sua / rede de ensino.“ | Confirme na escola | Q6 |
| 18,0–21,0 | Vier Seiten fächern auf, Klammer + Preisschild ohne Zahl (19,0 Punch), Haken 20,0 | „4 páginas: / R$ 419 na tabela.“ | Boletim · alemão → português | Q1, Q2, Q3 |
| 21,0–24,0 | PDF, Unterschrift zeichnet sich (21,5), Schule, Lupe (22,5) | „Chega em PDF com / assinatura digital.“ | Confirme se aceitam PDF | Q7 |
| 24,0–30,7 | Endcard (harter Schnitt), Bogen in Hook-Pose (Loop-Reim) | „Boletim / alemão? / Envie a foto: / preço na hora.“ · link na bio · traduzme.com.br · (61) 99803-8363 | – | Q8 |
| 30,7–31,0 | Loop: Frame 0 | – | – | – |

GMB (≤ 30 s): ohne 9,0–12,0 („Na tradução: 1 (muito bom).“), harter Schnitt, Chip „Preço na hora no site“, Endcard-Chip „no site“ → 28,0 s Datei (Loop-Punkt 27,7 s).
Preis-/Rechner-Szenen vor der Endcard: 18,0–21,0 = 3 s von 24 s = 12,5 % (≤ 30 %, ab 6 s). Captions je 2,92 s ≥ max(1,8; 0,4 × Wörter).

## Quellen (Whitelist oder selbst geöffnet 12.11.2026)

| Nr. | Aussage | Quelle | Wie geprüft |
|---|---|---|---|
| Q1 | Boletim escolar alemão → português R$ 179, + R$ 80 je weitere Seite (Etikett, Texte) | Supabase `precos` (ypdvpytpajgkzglbzxwg) `WHERE ativo AND NOT placeholder`: `de / to_pt / boletim` valor_cents 17900, extra_pag_cents 8000 | SELECT 12.11.2026 (read-only) |
| Q2 | Boletim wird pro Seite berechnet; Folgeseiten = Seiten dieses Dokuments | Edge-Function `analisar` v40, nucleo.ts: „boletim“: „boletim escolar / report card de um período, com notas por matéria; 1-2 páginas, cobrado por página“; „páginas seguintes de histórico escolar, boletim ou procuração: contam como páginas desse documento“; Folgeseite = `#cont` (Preis je weitere Seite) | get_edge_function 12.11.2026 |
| Q3 | 4 páginas = R$ 419 na tabela (179 + 3 × 80) | Rechnung aus Q1; precos_ia 10.11.2026 (de → português): Zeugnis Grundschule 4 Seiten, `preco_tabela_reais` 419 | SELECT 12.11.2026; Kundenfall nicht öffentlich |
| Q4 | Tradução fiel: a nota fica igual (Ziffer wird nicht umgerechnet) | Lei 14.195/2021, art. 27 caput: „Presumem-se fiéis e exatas as traduções realizadas por tradutor [público]“; art. 28: Strafen für Übersetzung „incompleta, imprecisa, errada ou fraudulenta“ | camara.leg.br Lei 14.195 normaatualizada, WebFetch 12.11.2026 (planalto aus der Sandbox gesperrt) |
| Q5 | Na Alemanha: 1 = sehr gut (Skala 1–6), „em geral“, „ex.: NRW“ | Schulministerium NRW „Wie kommt eine Zeugnisnote zustande?“: Notenstufen „sehr gut (1)“ … „ungenügend (6)“, Grundsätze § 48 SchulG NRW. Einschränkung: AO-GS NRW § 6 – Schuleingangsphase beschreibt Lernentwicklung, Noten erst ab Versetzungszeugnis in Klasse 3 → „em geral“ (Oberstufe nicht geprüft, nicht erwähnt) | WebFetch 12.11.2026 (schulministerium.nrw, bass.schule.nrw) |
| Q6 | Quem compara: a escola; regras da rede de ensino; confirme na escola | LDB (Lei 9.394/1996) art. 23 § 1º: „A escola poderá reclassificar os alunos, inclusive quando se tratar de transferências entre estabelecimentos situados no País e no exterior“; art. 24, II, c: „mediante avaliação feita pela escola … conforme regulamentação do respectivo sistema de ensino“ | camara.leg.br, WebFetch 12.11.2026 |
| Q6b | (nur YT/LinkedIn) Rede pública: matrícula de estudante migrante não pode ser negada por falta de tradução juramentada | Res. CNE/CEB nº 1/2020, art. 1º § 3º, I (Ausbleiben der „tradução juramentada de documentação comprobatória de escolaridade anterior“ ist kein Hindernis); § 5º Avaliação/classificação | WebFetch 12.11.2026 (anec.org.br, Abdruck der Resolução) |
| Q7 | Chega em PDF com assinatura digital · Confirme se aceitam PDF | Rechner fl4 „PDF juramentado com assinatura digital.“ + Handlungsempfehlung | curl /orcamento-app/?lang=pt 12.11.2026 (HTTP 200) |
| Q8 | Envie a foto: preço na hora (Endcard); Valor e data na hora, Pix (LinkedIn) | Rechner fl1 „Foto ou PDF, quantos precisar.“, fl2 „Valor e data de entrega na hora.“, fl3 „Pague por Pix“ | curl 12.11.2026 |
| – | Requisiten (Notenkästchen, Zeugnis-Karten, Skala, Stern, Schule, Waage, Checklisten, Seiten, Klammer, Preisschild, PDF, Lupe, Siegel) | eigene SVG ohne Daten, kein Kundenfall; einzige Schrift auf dem Objekt = Notenziffern 1/2/6 | – |

Bewusst **nicht** verwendet: Apostila für Schulunterlagen (keine Quelle für Schulen), Notenumrechnung in 0–10 (keine einheitliche Regel), Fristen, Eil-Option, Via física, Kundenfall/Kundendaten, Sprachlisten, Aussage „Tradução é obrigatória pra matrícula“ (Res. CNE/CEB 1/2020 sagt für Migranten das Gegenteil → nur in YT/LinkedIn offen benannt).

## Kritiker-Runden Storyboard (Bauer, getrennte Blickwinkel)

**Runde 1**
- Fakten: „Na Alemanha: 1 = sehr gut“ absolut → Schuleingangsphase (ohne Noten, AO-GS NRW § 6) widerspricht → Beleg „Em geral · ex.: NRW“. „Quem compara: a escola“ gedeckt durch LDB art. 23 § 1º; Rolle der Secretaria offen → eigene Szene „Regras: da sua rede de ensino.“ + „Confirme na escola“ (art. 24 II c). Res. CNE/CEB 1/2020 kippt jede Aussage „precisa traduzir pra matrícula“ → im Video keine Pflicht-Aussage, in YT/LinkedIn offen erwähnt. Zitat art. 27 ohne Sperrwort (Berufsbezeichnung gekürzt auf „tradutor público“).
- Design: Etikett 3 Zeilen + Seitenzuschlag; Ziffern im Hook müssen y ≤ 1500 bleiben (nur eine Notenzeile sichtbar). Sálvia: nur Dark-Text, Marker Areia statt Sálvia.
- Hook/Tempo: 7 Wörter, Payoff 2,5 s im Bild (Kästchen zeigt „1“ + Gleich), Antwort-Text 3,0 s. 3,0-s-Szenen = Variable; Captions ≤ 5 Wörter → Standzeit 2,92 s ≥ 2,0 s.
- Conversion: Preis-Szene ab 18 s (≤ 30 %); Endcard ohne Preis; LinkedIn-Einstieg bleibt Frage (R37-Variable nicht anfassen).

**Runde 2**
- Fakten: „4 páginas: R$ 419 na tabela“ → Endpreis kann darunter liegen (Rechner-Regel) → „na tabela“ bleibt Pflicht; Dokument + Richtung im selben Frame über Beleg „Boletim · alemão → português“. Beispiel „1 (muito bom)“ als „Exemplo“ markiert.
- Design: Waage/Schule ohne Schrift; Stern als SVG; keine Flagge, keine Sprachliste.
- Hook/Tempo: Wisch 0,22 s mit Kante, alte Ebene rechts der Kante (keine Überblendung); Punch 2,5/7/13/19 (≤ 1 je 4 s).
- Conversion: Mitmach SIM/NÃO bleibt (keine zweite Variable).

**Runde 3 (getrennt): keine offenen Mängel.**
