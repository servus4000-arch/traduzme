# Reel 29 – „Diploma em espanhol: precisa traduzir?“ (Mo 09.11.2026, ersetzt R27 Brasília)

Thema nach marketing/ENTSCHEIDEN.md (Kandidat C, Score 17, Zeile lernen/social.md 02.11.): Diploma + Histórico em espanhol für Revalidação/Reconhecimento, tradução juramentada + Preis. Kaufnachweis ES→PT = meiste bezahlte Bestellungen (30 T.).
- **Wendung nach Faktenprüfung:** Die Primärquellen sagen, dass Spanisch bei Revalidação/Reconhecimento **in der Regel keine Übersetzung braucht** (Res. CNE/CES nº 2/2024, art. 4º §§ 6º–7º; UFMG und UFSC dispensieren ES). Ein Reel „ES-Diplom braucht juramentada“ wäre falsch. Deshalb ist die ehrliche Antwort der Mitmach-Frage **DEPENDE**: em geral dispensa → a universidade pode exigir (justificativa em ato próprio; ex.: UFSC pede no decorrer) → concurso/conselho: confirme → wenn verlangt: tradutor juramentado do Brasil, PDF assinado (ex.: UFMG) → Preis.
- **Mercosul:** Die PF-Liste der Abkommen (Dec. 6.975/2009, 5.852/2006, 5.851/2006, 9.089/2017, 6.736/2009) betrifft Legalisierung von Dokumenten für Migration, ARCU-SUL nur die tramitação simplificada (Res. 2/2024 art. 9º § 3º). Keine dieser Quellen regelt die Übersetzung → im Bild nicht erwähnt.
- Format Dokument-Tisch (Held-Objekte: Diploma, Universidade, Processo, Edital, Tradução, PDF, Rechner-Ausschnitt, Histórico-Seiten). Grund **Pinho #376259** (R26 Areia, R27 Dark). Musik `lib/music.py` **lofi 120 BPM** (R27 funk, R26 calm). Hook Weiß auf Pinho mit Areia-Marker; Captions Areia-Pillen mit Dark-Text, Marker Dark/Weiß; Chips Sálvia/Dark; Belege Névoa/Dark.
- **Keine neue Test-Variable** (Lehre 4: Metricool-Messung der letzten 3 Reels fehlt). Quiz-Karten (SIM/NÃO/DEPENDE) + Payoff 2,5 s wie R26/R27.

## Quellen (nur was die Quelle trägt)
| Q | Quelle | Wortlaut / Inhalt | Geöffnet |
|---|---|---|---|
| Q1 | Resolução CNE/CES nº 2, de 19/12/2024 (DOU 20/12/2024), PDF abmes.org.br/arquivos/legislacoes/Resolucao-cne-ces-002-2024-12-19.pdf (gov.br-PDF rces002_24 nur mit Captcha) | art. 4º § 6º „Caberá à universidade pública revalidadora solicitar, quando julgar necessário, a tradução da documentação prevista no caput.“ § 7º „O disposto no parágrafo anterior não se aplica às línguas francas … tais como o inglês, o francês e o espanhol; … o afastamento dessa excepcionalidade deverá ser justificado pela universidade em ato próprio.“ art. 20 §§ 7º–8º gleich für Reconhecimento. Revogiert Res. CNE/CES nº 1/2022 (dort art. 7º §§ 4º–5º gleichlautend). | WebFetch 02.11.2026 |
| Q2 | UFSC/DAE, „Relação de Documentos para Revalidação de Diploma de Medicina“ versão 05 (11/2025), dae.paginas.ufsc.br | Observação 02: tradução juramentada da documentação inicial „só é solicitada para documentos em línguas estrangeiras que não sejam o inglês, o francês e o espanhol“; „Já no decorrer do processo, a comissão revalidadora pode vir a solicitar a tradução juramentada de qualquer documento apensado a este.“ | WebFetch 02.11.2026 |
| Q3 | UFMG Prograd, Revalidação de diplomas (ufmg.br/prograd/revalidacao-de-diplomas/) | „Dispensamos a tradução dos documentos emitidos originalmente em português, galego, espanhol ou inglês.“ · „ser feita por tradutor … público matriculado em Junta Comercial de um estado brasileiro“ · „Não aceitamos traduções feitas no exterior …“ · „se for eletrônica, estar assinada pelo tradutor com certificado digital …, com autenticidade verificável.“ · Protokoll nur über Plataforma Carolina Bori (MEC) | WebFetch 02.11.2026 |
| Q4 | Supabase `precos` (ypdvpytpajgkzglbzxwg) `WHERE ativo AND NOT placeholder AND idioma='es'`, 02.11.2026 = Memory preistabelle-live | `es|to_pt|diploma superior` 15900 · `es|to_pt|historico escolar` 15900 + extra_pag 7500 (updated 15.10.2026) | SQL 02.11.2026 |
| Q5 | Rechner live /orcamento-app/?lang=pt, Box „Como o preço é calculado“ | „Documentos padrão (certidões, diplomas, CNH…): preço fixo por documento. Ver lista“ | Playwright 02.11.2026 **ohne Mock** (capture_ui.js, VW=286 → shots/ui_preco.png). pix-config aus der Sandbox nicht erreichbar → keine Sprachfelder, kein Preis im Screenshot |

Nicht verwendet: Preise für Zusatzoptionen, Fristen, Sprachlisten, Ländernamen, Mercosul-Abkommen, CPC/CC-Artikel, Kundenfälle, „a partir de“.

## Zeitachse Hauptfassung (34,0 s, 120 BPM, Schlag 0,5 s)
Text x 90–900, y 300–1500. Caption-Pillen ab y 320, CTA-Chip y 552, Objektzone y 690–1360, Beleg y 1384.

| Zeit | Held-Objekt + Handlung | Text im Bild | Q | Ton |
|---|---|---|---|---|
| 0,0–3,0 | **Frame 0 fertig:** Diploma „TÍTULO“ (Requisite, ES-Anmutung, Histórico dahinter) + Karten SIM / NÃO / DEPENDE, Diplom wackelt ab Frame 1. **2,5 Payoff:** DEPENDE Areia mit Haken, SIM/NÃO blass, Punch | Hook „Diploma em / espanhol: / precisa / **traduzir?**“ (5 W.) · Chip „Comenta a sua resposta“ | Q1 | pop 0,03 · impact 2,5 |
| 3,0–6,0 | Diplom mittig, Stempel mit Haken 4,5 | „Revalidação: em geral, / **espanhol dispensa.**“ · Beleg „Res. CNE/CES nº 2/2024, art. 4º“ | Q1 | pop 3,0 · stamp 4,5 |
| 6,0–9,0 | Universidade; 7,5 Blase mit Übersetzungsblatt + „?“ (Punch) | „Mas a universidade / **pode exigir.**“ · Beleg „Confirme com a sua universidade“ | Q1 (§ 7º) | whoosh 6,0 · impact 7,5 |
| 9,0–12,0 | Processo-Ordner, Fortschritt läuft, 10,5 Blase „pede depois“ | „Ex.: UFSC, a comissão / **pode pedir depois.**“ · Beleg „Ex.: UFSC · Medicina“ | Q2 | whoosh 9,0 · stamp 10,5 |
| 12,0–15,0 | Edital-Checkliste, Lupe; Haken 12,5 (Punch) und 13,5 | „Concurso ou conselho? / **Confirme a regra.**“ · Beleg „No edital ou no órgão“ | – (keine Tatsachenaussage) | whoosh 12,0 · impact 12,5 · click 13,5 |
| 15,0–18,0 | Tradução juramentada, Siegel 16,0, Punch 17,0 | „Se pedirem: tradutor / **juramentado.**“ · Beleg „Feito no Brasil · ex.: UFMG“ | Q3 | whoosh 15,0 · stamp 16,0 · impact 17,0 |
| 18,0–21,0 | PDF mit Unterschrift + QR-Andeutung, Haken 19,5 | „PDF com assinatura / **digital? UFMG aceita.**“ · Beleg „Ex.: UFMG · assinatura verificável“ | Q3 | whoosh 18,0 · pop 19,5 |
| 21,0–24,0 | **Echter Rechner-Ausschnitt** (harter Schnitt, sofort deckend) + Mini-Diplom → Pfeil → Mini-Tradução, Punch 22,0 | „Diploma em espanhol / **R$ 159**“ · Beleg „Para português · preço de tabela“ | Q4, Q5 | whoosh 21,0 · impact 22,0 |
| 24,0–27,0 | Histórico-Seiten fächern auf (25,0 / 26,0, je „+“-Marke), Punch 26,0 | „Histórico: R$ 159 / **+ R$ 75/página extra**“ · Beleg „Espanhol para português · tabela“ | Q4 | whoosh 24,0 · pop 25,0 · impact 26,0 |
| 27,0–33,7 | **Endcard** (Absender traduzme), Mini-Diplom | „Diploma em / espanhol? / **Depende.**“ · Chip · traduzme.com.br · (61) 99803-8363 | – (CTA) | hit + stamp 27,0 |
| 33,7–34,0 | harter Schnitt auf Frame 0 | Hook | Loop | – |

Szenenwechsel alle 3,0 s (0,33/s). Punches 2,5 · 7,5 · 12,5 · 17,0 · 22,0 · 26,0 (Abstand ≥ 4 s). CTA-Chip 3,0–27,0. Preis/Rechner-Anteil 21–27 s = 6 von 27 s = 22 % (≤ 30 %, Start ≥ 6 s). Endcard voll 27,12–33,7 = 6,6 s.

## GMB-Fassung (28,0 s)
Ohne 9,0–12,0 (UFSC) und 18,0–21,0 (PDF). Chip/Endcard „Preço na hora no site“, kein „link na bio“. Endcard 21,0–27,7, Loop 27,7, END 28,0. gmb/reel.html = reel.html mit `GMB=1` und Pfaden `../`.

## Kritiker-Runden
Protokoll: /mnt/project-files/social/reels/reel29-texte.md, „Prüfprotokoll“.
