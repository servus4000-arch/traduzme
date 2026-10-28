# Reel 22 – „Sua certidão do exterior já tem apostila?“ (Do 05.11.2026)

Thema Nr. 2 aus REELS-REGELN-v2 „Themen-Priorität aus Zahlen“ (Apostila-Cluster: meiste Impressionen, 0 Klicks).
Fortsetzung von Reel 19 (BR → exterior: Reihenfolge). Hier: **documento estrangeiro já apostilado → Brasil**: was fehlt noch,
Apostila-Seite mitschicken, alles in einem Upload, PDF assinado.
**Fall im Bild: Árabe** (Koordinator 28.10.: AR/DE mind. jedes 2. Reel) – Geburtsurkunde aus Marokko („رسم الولادة“, Kopf
„المملكة المغربية“), Vektor ohne Daten. Marokko: Apostille-Konvention in Kraft seit 14.08.2016 (HCCH-Statustabelle cid=41);
einziger Einspruch gegen den Beitritt: Deutschland (treatydatabase.overheid.nl) → zwischen Brasilien und Marokko gilt die Apostila.
Espanhol nur als zweites Beispiel in der Caption. Keine Via física, keine Urgência.

- **Serie:** „Veio de fora #1“ (Design-Regeln v3 Nr. 10, 16-viral §3; Koordinator 28.10.: Reel 22 = #1). Badge „VEIO DE FORA · #1“
  (Areia, Dark-Kontur 6 px, 54 px/800, Radius 16, −3°) im Hook-Bild 0–3,0 s, im Loop-Bild und in der Endcard. Badge steht bei x 128 / y 340
  statt x 90 / y 300, damit es auch auf dem Stinger-Höhepunkt (×1,12, −6°) innerhalb x 90–900 / y 300 bleibt; Hook 32 px darunter (y 480).
  Stinger ab Frame 1 (Frame 0 fertig): Badge 1→1,12→1, −3°→−6°→−3° in 0–0,4 s, Kamera-Push der Objektwelt +3 % bis 0,6 s, SFX stamp 0,03.
  Im Loop-Bild kein Stinger (letztes Bild = erstes Bild).
- **Format:** „Mito ou fato?“-Variante als Quiz „SIM ou NÃO?“ (3 Fragen, Countdown 3-2-1). Held-Objekt in jeder Szene: marokkanische Urkunde,
  Apostille, Tradução, PDF-Datei, Lupe, echte Rechner-Ausschnitte. Kein Chat, Split, POV, keine Figur.
- **Grund:** Dark #1F3B35. **Musik:** music.py `lofi` 120 BPM, Master v2.
- **Bewusst getestete Variable:** Countdown-Ratepause in jeder Frage.
- **Länge:** 36,0 s (v3-Ziel 32–36 s); GMB 27,5 s (ohne Frage 1 und Mitmach; Chip „Preço na hora no site“; Endcard ohne „link na bio“; eigener Loop).
  Umsetzung: reel.html/audio.py rechnen in Designzeit; SKIP-Liste lässt je Frage 0,5 s Ruhe vor dem Countdown, 0,5 s im Mitmach und 1,0 s
  Endcard-Standzeit weg (Abstände 0,5 s → alle Schläge bleiben im Raster). Hintergrund/Atmen laufen in Echtzeit (kein Ruck an Skips).
- **Raster (8 px):** Text x 96–900. Badge y 340, Hook y 480 (104 px), Tag y 304, Szenen-Headline y 400 (84 px, ≤ 2 Zeilen), Chip y 672 (54 px),
  Pillen y 800, Bildzone y 944–1496, Beleg-Pillen y 1408 (44 px).
- **Zoom-Punch (v3 Nr. 4):** Objektwelt 1,00→1,06→1,00 in 0,22 s + genau 1 impact auf dem Schlag bei 3,0 / 8,0 / 13,5 / 19,0 s (Abstand ≥ 5 s).
- **Rechner-Anteil (v3 Nr. 6):** pc2-Ausschnitt 14,0–16,35 + „Como funciona“ 22,0–27,85 = 8,2 s von 31,0 s vor der Endcard = 26 %, erst ab 14,0 s.
  FAQ-a8-Ausschnitt (19,5–21,7) zählt als Wissens-Beleg (Regel zur Apostila, kein Preis/Kauf).

## Zeitachse Hauptfassung (Echtzeit)

| Zeit (s) | Bild / Handlung | Text im Bild | Quelle |
|---|---|---|---|
| 0,0–3,0 | Frame 0 fertig: Badge + marokkanische Geburtsurkunde (arab.) mit angehefteter „APOSTILLE“; Stinger 0–0,6 | **VEIO DE FORA · #1** · **Sua certidão do exterior já tem apostila?** | Thema 15-themen-leistung §4 Rang 2 |
| 3,0–5,5 | Zoom-Punch; „TRADUÇÃO JURAMENTADA“ gleitet neben die Urkunde; Beleg-Pille 3,5 | **Falta a tradução juramentada.** · „Regra geral: Código Civil, art. 224“ | CC art. 224 (planalto); Rechner Info-Popup Apostila; „Regra geral“ wegen PF-Ausnahmen (nur Caption) |
| ab 3,0 | CTA-Chip bis 31,0 | Preço na hora · link na bio | Ben-Regel |
| 5,5–8,0 | Pergunta 1 de 3 · Pillen 6,0 · Countdown 6,5/7,0/7,5 | **A apostila já traduz o texto?** | – |
| 8,0–11,0 | Reveal NÃO + Punch; Lupe aufs Siegel; Beleg 8,5 | **Não: confirma só quem assinou.** · „Fonte: Decreto 8.660/2016, art. 5“ | Decreto 8.660/2016 art. 5; HCCH-Merkblatt (cnj.jus.br) |
| 11,0–13,5 | Pergunta 2 de 3 · Urkunde + „+“ + Apostille | **Manda a página da apostila junto?** | – |
| 13,5–16,5 | Reveal SIM + Punch; beide Blätter werden zur Datei „certidao.pdf“; 14,0 echter Rechner-Ausschnitt pc2 | **Sim: num upload, sem custo extra.** | Rechner pc2, pc1, up_tips |
| 16,5–19,0 | Pergunta 3 de 3 · Tradução mit leerem Feld „apostila ?“ | **A tradução precisa de apostila aqui?** | – |
| 19,0–22,0 | Reveal NÃO + Punch; Feld füllt sich mit Text; 19,5 FAQ-a8-Ausschnitt, Marker 20,0/20,5 | **Em geral, não: confira no órgão.** | Rechner FAQ a8 |
| 22,0–25,0 | Echter Screenshot „Como funciona“ Schritte 1–2 | **Foto ou PDF: preço e data na hora.** | Rechner fl1_d, fl2_d |
| 25,0–28,0 | Fahrt zu Schritt 3–4 | **Pix e PDF assinado por e-mail.** | Rechner fl3, fl4 |
| 28,0–31,0 | Mitmach + Urkunde (echte Inhaltsfrage, Ein-Wort-Antwort = Land) | **Sua certidão é de qual país?** + **Comenta só o país** | v3 Nr. 7 |
| 31,0–35,5 | Endcard: Badge-Stempel, Urkunde + Tradução klein | **Preço na hora no site.** · link na bio · traduzme.com.br · (61) 99803-8363 (4,5 s) | Ben-Regel |
| 35,5–36,0 | Schnitt auf das Hook-Bild (Loop, ohne Stinger) | Badge + Hook | Raster D6 |

## Sound (lofi 120 BPM, v3-Grammatik)
stamp 0,03 (Stinger) · impact 3,0 / 8,0 / 13,5 / 19,0 (Payoff/Auflösungen, 4×) · whoosh je Frage-Start + Rechner (4×) · pop Pillen/Belege/Mitmach/link na bio ·
Woodblock 3-2-1 + Musik 'soft' in den Ratepausen · Endcard: Musik-Hit + stamp (Badge). Ø ≈ 0,5 SFX/s.

## Bewusst NICHT im Bild
Preise, Sprachlisten, Fristen, Sperrlisten-Begriffe (REELS-REGELN-v2 Nr. 11), Zertifikats-Norm, Behörden-Anforderungen ohne Quelle,
Aussagen zu digitalen Apostilas fremder Länder, Länderlisten, Via física/Urgência.

## Kritiker-Runden Storyboard
| Runde | Rolle | Mängel | Fix |
|---|---|---|---|
| 1 | Fakten | „falta **só** a tradução“ zu absolut (Registro em RTD je nach Uso, PF-Ausnahmen); „Pix automático“ verwechselbar mit BCB-Produkt | Beleg „Regra geral: Código Civil, art. 224“, Ausnahmen in Caption; „Pix e PDF assinado por e-mail“ |
| 1 | Design | 3 Karten in der Payoff-Szene → Gefahr angeschnittener Titel | Apostille nur über dem Linienbereich; qa_frames `cut` |
| 1 | Hook/Tempo | Lernpunkt Frage 1 spät | Payoff 3,0 s mit Quelle ist erster Lernpunkt |
| 1 | Conversion | Rechner erst ab 24 s | echter pc2-Screenshot schon ab 15 s |
| 2 | Raster (neu 28.10.) | Hook 92 px < 104; Szenen-Headline 3 Zeilen (B3 ≤ 2); Chip 44 < 54 px; lofi 90 BPM < 100 (E2); Standzeit Hook 2,33 s < 2,8 s (C4); 8-px-Raster | Hook 104 px, Szenentexte auf 2 Zeilen gekürzt, Chip 54 px, 120 BPM mit 0,5-s-Raster, Hook 3,0 s, Positionen auf 8 px |
| 2 | Fakten | „Não: só confirma a assinatura“ lässt Funktion/Siegel weg | „Não: confirma só quem assinou“ (Unterschrift + Funktion, Art. 5) |
| 2 | Koordinator | Fall auf Árabe umstellen, Marokko per HCCH prüfen | erledigt (s. o.) |
| 3 | alle, getrennt | keine offenen Mängel | – |
| 4 | Koordinator (v3) | Serie „Veio de fora #1“, Stinger, Zoom-Punch, SFX-Grammatik (whoosh 7× > 4×), Länge 39 s > 36 s | Badge + Stinger, Punch 4×, whoosh auf 4 reduziert, impact statt Musik-Hit, Skips → 36,0 s |
| 4 | Design (qa_frames) | Badge auf Stinger-Höhepunkt außerhalb y 300 / x 90; Endcard-Nummer kollidierte mit zurückfahrender Urkunde | Badge x 128 / y 340, Hook y 480; Endcard blendet 38,12–38,24 (Design) aus, Endcard-Objekte 40 px tiefer |
