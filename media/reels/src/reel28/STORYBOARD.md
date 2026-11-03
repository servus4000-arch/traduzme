# Reel 28 – „Certidão em espanhol: quanto custa?“ (Fr 06.11.2026, ersetzt Reel 24)

Thema nach marketing/ENTSCHEIDEN.md (Zeile lernen/social.md 02.11.: Kandidat A, Score 20 = K3 N2 E1 B1 L3). Kaufnachweis: ES→PT = meiste bezahlte Bestellungen 30 T. (3 von 5 ohne Tests). Hook = Suchfrage des Käufers mit konkretem Preisbeispiel (REELS-REGELN-v2 „Themen ab Di 03.11.“, Ben 02.11.).
Kern: Certidão de nascimento espanhol → português = **R$ 149 Listenpreis** (Tabelle), Preis final no site, na hora → vorher Wissen: em geral juramentada, feita no Brasil, Verso/Apostila ohne Aufpreis, mehrere Certidões in einem Pedido, Liste beim Órgão bestätigen.

- **Keine neue Test-Variable** (Lehre 4: Metricool-Messung der letzten 3 Reels fehlt). Bewährte Bausteine: Frage-Hook ≤ 6 Wörter in Frame 0, Quiz SIM/NÃO mit Karten + Payoff 2,5 s (R22/R26/R27), CTA-Chip ab 3,0 s, Endcard ≥ 6 s, Loop hart auf Frame 0. Der Preis im Bild ist Bens Themen-Regel vom 02.11., kein Test.
- **Bildsprache:** Preis-Etikett als Held-Objekt (Objekt-Close-up) + ein echter Rechner-Ausschnitt; nicht Dokument-mit-Siegel wie R22/R26. Grund **Pinho #376259** (R22 Dark 05.11., R26 Areia 07.11.). Musik `music.py` **pop 120 BPM** (R22 lofi, R26 calm).
- Mitmach: „Passa de R$ 200?“ + „Comenta:“ + Karten SIM/NÃO → Ein-Wort-Antwort. R$ 200 ist nur die Quiz-Schwelle (keine Preisbehauptung, kein Vergleich).
- Kein F6 (zuletzt R27, frühestens R31). Rechner-/Preis-Szenen 10,0–17,0 = 7,0 s von 24,0 s = 29 % (v3 #6 ≤ 30 %, Start ≥ 6 s). Ausnahme: Payoff 2,5–3,0 zeigt den Preis auf dem Etikett, weil die Hook die Preisfrage ist (Ben 02.11. „konkretes Preisbeispiel“; Raster A2 Payoff ≤ 3 s ist strenger).

## Quellen (nur was die Quelle trägt)
| Q | Quelle | Wortlaut / Inhalt | Geprüft |
|---|---|---|---|
| Q1 | Supabase `precos` (Projekt ypdvpytpajgkzglbzxwg), `WHERE ativo AND NOT placeholder AND idioma='es'` | `es|to_pt|certidao de nascimento` valor_cents **14900**; casamento/óbito/divórcio to_pt je 14900; inteiro teor 16900; certidão negativa 12900 (→ **kein „a partir de“** für „certidão“, nur „R$ 149 de tabela“ für Certidão de nascimento) | SELECT 02.11.2026 (MCP, read-only); deckt sich mit Memory preistabelle-live |
| Q2 | Memory preistabelle-live | „Endpreis kann unter der Liste liegen … Öffentlich nur Listenpreise oder live im Rechner geprüfte Beispiele“ → im Bild „de tabela“ + „Preço final: no site, na hora“ | gelesen 02.11. |
| Q3 | Rechner live /orcamento-app/?lang=pt, „Como o preço é calculado“ pc1/pc2 (Whitelist pc1–pc3) | pc1 „Documentos padrão (certidões, diplomas, CNH…): preço fixo por documento.“ · pc2 „Verso e Apostila (foto ou página) contam como parte do documento: sem custo extra.“ | Playwright **ohne Mock** 02.11. (Viewport 280 px, @3x) → shots/pc2_live.png (ganzes li, ungeschnitten) |
| Q4 | Rechner „Como funciona“ fl1/fl2 (Whitelist L1004–1005) | „Envie o documento – Foto ou PDF, quantos precisar.“ · „Preço em segundos – Valor e data de entrega na hora.“ | live (curl) 02.11. |
| Q5 | CC art. 224 (Whitelist 10-gegenkritik §3 P08, Abnahmen R23/R24) | Fremdsprachige Dokumente werden für Rechtswirkung im Land ins Portugiesische übersetzt → im Bild nur „em geral“ + „Regra geral: CC art. 224“ | Whitelist |
| Q6 | PF-FAQ (Whitelist 10 §3, Abnahme R26 selbst gelesen) | „De maneira geral … traduzidos“; „mesmo apostilados … tradutor juramentado … só pode ser feita no Brasil“ (CPC + Lei 14.195/2021) | Whitelist |
| Q7 | Abnahme R24 (normas CGJ-SP), R26 (PF/MJ) | Dokumentenliste hängt vom Órgão ab → „Confirme a lista com o órgão“ | Whitelist |

Nicht verwendet: „a partir de“, Endpreis-/Rabatt-Versprechen, Eil-Option, Papier-Versand, Apostila-Preise (PT→), Fristen, Sprachlisten, Kundenfälle, Technik-Angaben zur Übersetzung.

## Zeitachse Hauptfassung (31,0 s, 120 BPM, Schlag 0,5 s)
Text x 90–900, y 300–1500. Caption-Pillen ab y 320, CTA-Chip y 552, Objektzone y 680–1480, Beleg y 1384.

| Zeit | Szene / Held-Objekt + Handlung | Text im Bild | Q | Ton |
|---|---|---|---|---|
| 0,0–3,0 | **Frame 0 fertig:** ACTA DE NACIMIENTO (Requisite, ohne Daten) links, daran an einer Schnur das **Preis-Etikett** „Nascimento · ES → PT / R$ ???“ (Dokumenttyp + Richtung auch im Payoff, Fakten-Runde 1: „certidão“ allein wäre zu weit, negativa 129 / inteiro teor 169) (Ungereimtheit: Preis unbekannt), rechts Karten SIM/NÃO unter „Comenta:“. Etikett pendelt ab Frame 1. **2,5 Payoff:** NÃO Areia + Haken, SIM blass, Etikett dreht auf „R$ 149“, Punch | Hook „Certidão em / espanhol: / **quanto custa?**“ (5 W.) · Chip „Passa de R$ 200?“ · „Comenta:“ | Q1 | pop 0,03 · impact 2,5 |
| 3,0–6,5 | Acta fährt nach links, Pfeil, **Tradução** gleitet ein, Stempel 4,5 | „Para usar no Brasil: / **em geral, juramentada.**“ · Beleg „Regra geral: CC art. 224“ | Q5 | pop 3,0 · stamp 4,5 · pop 5,5 (Pfeil) |
| 6,5–10,0 | Acta + Apostille-Karte (ohne Schrift außer APOSTILLE) → Tradução mit BR-Siegel; 8,5 Haken | „Tradução feita / **no Brasil.**“ · Beleg „Em geral, mesmo apostilada · PF“ | Q6 | whoosh 6,5 · impact 8,5 |
| 10,0–13,5 | **Etikett groß** (≥ 70 % Breite): „CERTIDÃO DE NASCIMENTO / espanhol → português / R$ 149“; 11,0 Punch | „Tabela traduzme: / **R$ 149.**“ · Beleg „Preço final: no site, na hora“ | Q1, Q2, Q4 | whoosh 10,0 · impact 11,0 |
| 13,5–17,0 | **Echter Rechner-Ausschnitt** pc2 (weiße Karte 800 px); Mini-Stapel Frente/Verso/Apostila schiebt sich zu einem Blatt (15,0) | „Verso e apostila: / **sem custo extra.**“ | Q3 | whoosh 13,5 · pop 15,0 · stamp 15,5 |
| 17,0–20,5 | Drei Certidões (nur Linien) fallen nacheinander in einen Ordner/Upload-Tray (17,5 / 18,0 / 18,5), Haken 19,0 | „Mais de uma? / **Envie todas juntas.**“ · Beleg „Foto ou PDF, quantos precisar“ | Q4 | pop 17,5 · click 18,5 · impact 19,0 |
| 20,5–24,0 | Órgão-Gebäude + Checkliste, Lupe 22,0 | „Confirme a lista / **com o órgão.**“ · Beleg „Ex.: cartório ou Polícia Federal“ | Q7 | whoosh 20,5 · pop 22,0 |
| 24,0–30,7 | **Endcard** (Absender traduzme): Etikett klein mit „R$ 149“ | „Certidão em / espanhol? / **Preço no site.**“ · Chip „Preço na hora · link na bio“ · traduzme.com.br · (61) 99803-8363 | – | hit + stamp 24,0 |
| 30,7–31,0 | harter Schnitt auf Frame 0 | Hook | Loop | – |

Szenenwechsel 3,0/6,5/10,0/13,5/17,0/20,5/24,0 (3,0–3,5 s). Punches 2,5 · 8,5 · 11,0 · 15,5 · 19,0. CTA-Chip 3,0–24,0. Endcard 6,7 s.
Ducking: höchstens −4 dB (Faktor 0,631), nie zwei Ducks direkt hintereinander (Lehre 27-2): 13,5–16,95 und 20,5–23,95.

## GMB-Fassung (27,5 s)
Ohne 17,0–20,5 („Mais de uma?“). Chip „Preço na hora no site“, Endcard-Chip „Preço na hora no site“, kein „link na bio“. Endcard 20,5–27,2, Loop 27,2, END 27,5. Aus reel.html mit `GMB=1`.

## Kritiker-Runden
Siehe /mnt/project-files/social/reels/reel28-texte.md, „Prüfprotokoll“.
