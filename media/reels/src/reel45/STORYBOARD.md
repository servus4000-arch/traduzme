# Reel 45 – „Antecedentes da PF: vale quantos dias?“ (Post Sa 28.11.2026)

Antecedentes criminais (Certidão da Polícia Federal) **português → espanhol**, Etikett „R$ 119 na tabela“. Format **Bloco-calendário** (Abreißkalender, Blatt klappt über die Ringe weg), Grund **Névoa #BDCBCB**, Musik `music.py` **lofi 120 BPM**, A, seed 45, Master v2. Szenen 3,5 s, Endcard Standard „Envie a foto: preço na hora.“, Etikett in Frame 0 (Standard seit R35). Neue Variable (nicht im Bild): **Hashtag-Satz** (siehe social/reels/reel45-texte.md).

## Thema (ENTSCHEIDEN 20.11.2026, Zeile in marketing/lernen/social.md)
- Kaufnachweis: pedidos status PAGO 30 T. – PT→ES Certificado de Antecedentes da PF bezahlt am 14.11. (Auftrag mit Apostila no original); analises 30 T. idioma_origem pt / typ antecedentes criminais 5 Uploads. Keine Kundendaten im Reel.
- Kandidaten: **A Antecedentes da PF PT→ES „vale quantos dias?“ (K3 N1 E1 B0 L2 = 15) → gewählt** / B Antecedentes penales ES→PT (K3 N1 E1 B0 L2 = 15, Nähe R37/R26, Richtung →PT) / C Certidão de casamento ES→PT (K3 N1 E1 B1 L2 = 17, raus: Nähe R40 Casamento) / D Certidão de casamento PT→DE R$ 179 (K1 N1 E1 B1 L2 = 13 < 14).
- Grund: ES-Fall (jedes 3. Reel AR/DE/ES), Richtung PT→Fremdsprache (Auftrag), bezahlter Fall, Score ≥ 14; bei Gleichstand A vor B wegen Richtung und weil B Antecedentes-Winkel R26/R37 wiederholt. Kein Duplikat zu R20–R44 (R26/R37 = ausländische Antecedentes → Brasil; R36 = Certidão PT→ES).

## Quellen
| Q | Aussage | Quelle | Wie geprüft |
|---|---|---|---|
| Q1 | Antecedentes criminais português → espanhol **R$ 119 na tabela** (Etikett 0–2,97; Bild 20,5) | Supabase `precos` `WHERE ativo AND NOT placeholder`: `es / from_pt / antecedentes criminais` **11900**, extra_pag null, Kategorie documento (es/to_pt ebenfalls 11900) | SELECT 20.11.2026 (read-only) |
| Q1b | Einstufung: Certidão der PF = `antecedentes criminais`, 1–2 Seiten, Festpreis (bis 4 Seiten je Datei, Lehre R41) | Edge-Function `analisar` v40: „atestado/certidão de antecedentes criminais (Polícia Federal, Polícia Civil/SSP) … 1-2 páginas“ | get_edge_function 20.11.2026 |
| Q2 | Na PF, a certidão vale 90 dias · Para fins civis (Bild 3,0) | gov.br „Emitir Certidão de Antecedentes Criminais“: „Fornecida para fins civis, a Certidão emitida poderá ser impressa e terá a validade de 90 dias.“ / „Válido por 90 dia(s).“ | WebFetch gov.br/pt-br/servicos/emitir-certidao-de-antecedentes-criminais 20.11.2026 (selbst geöffnet) |
| Q2b | A PF emite só em português · Certidão da PF · gov.br (Bild 10,0) | dieselbe Seite: „A Certidão de Antecedentes Criminais emitida pela Polícia Federal é fornecida apenas em português.“ | WebFetch 20.11.2026 |
| Q2c | Em geral, vai com tradução e apostila (Bild 13,5) | dieselbe Seite: „Para saber se você precisa legalizar ou apostilar um documento, primeiramente identifique o país onde o documento foi emitido e para qual país o documento se destina. Se o seu documento foi emitido no Brasil e você irá usá-lo nos Estados Unidos, por exemplo, o seu documento deve ser traduzido e apostilado“ → nur „em geral“ + Beleg Konvention | WebFetch 20.11.2026 |
| Q3 | Apostila: países da Convenção (Beleg 13,5) · Lá fora, muitos pedem documento recente · Confirme no consulado (Bild 6,5) | Rechner Info-Pop-up „Apostila de Haia“ (Whitelist Info-Pop-ups): „… nos mais de 120 países da Convenção de Haia …“; „Para países fora da Convenção de Haia, é preciso legalização no consulado“; „o documento por baixo pode ter prazo próprio (por exemplo, antecedentes criminais costumam valer 90 dias), e muitos órgãos no exterior exigem documento e apostila recentes“; „confirme com quem vai receber (consulado, universidade, cartório)“ | curl /orcamento-app/?lang=pt 20.11.2026 (HTTP 200) |
| Q4 | Pra traduzir: foto ou PDF legível · Sem mandar o original (Bild 17,0, nur Hauptfassung) | Rechner Info „Tradução juramentada: como funciona“: „Preciso enviar o documento original? Não para a tradução: basta uma foto ou PDF legível.“ | curl 20.11.2026 |
| Q5 | Chega em PDF com assinatura digital · Confirme se aceitam PDF (Bild 24,0) · Envie a foto: preço na hora (Endcard) | Rechner fl4 „PDF juramentado com assinatura digital“, fl1/fl2 „Foto ou PDF“ / „Valor e data de entrega na hora“; REELS-REGELN-v2 Nr. 12 (Ziel im Ausland: PDF-Annahme bestätigen) | curl 20.11.2026; Wortlaut wie R44 |
| – | Requisiten (Kalender, Certidão mit rundem Emblem und Musterfeld, Mini-Monate, Sanduhr, Gebäude, Globus, Nadel, Siegel, Handy, Preisschild ohne Zahl, PDF) | eigene SVG ohne Schrift, ohne Zahlen, ohne Wappen/Flaggen, kein Kundenfall | – |

**Bewusst nicht verwendet:** ob die PDF-Certidão der PF eine digitale Apostila „no original“ bekommen kann (Rechner: nur bei Dokument mit assinatura digital; für die PF-PDF nicht geprüft → keine Aussage, Lehre R35-A/R44); wie lange ein bestimmtes Land die Certidão akzeptiert (keine Länderregel, nur „muitos pedem documento recente“ + „confirme no consulado“); Validar-Dienst der PF; Legalização im Detail; Lieferfristen, Urgência, Via física; Reihenfolge Apostila/Tradução (nur YT/LinkedIn mit Rechner-Wortlaut „o mais recomendado“).

## Ablauf (Designzeit; GMB lässt 17,0–20,5 weg, Endcard 5,0 s)
| Zeit | Text (Bild) | Beleg-Pille | Bild / Ereignis | SFX |
|---|---|---|---|---|
| 0–2,97 | Hook „Antecedentes / da PF: vale / quantos dias?“ + Mitmach „30, 90 ou 180?“ + Etikett „Antecedentes criminais · português → espanhol · R$ 119 na tabela“ | – | Kalender unten, Certidão schief, Sanduhr, „?“ pulsiert; 2,5 Sanduhr kippt + Ring + Punch (Payoff) | pop 0,03 · impact 2,5 |
| 3,0 | Na PF, a certidão / vale 90 dias. | Para fins civis · gov.br | Kalender steigt; 3,5 drei Mini-Monate; 4,0–5,0 füllen sich; 5,5 Haken | whoosh 3,0 · click 3,5 · pop 5,5 |
| 6,5 | Lá fora, muitos pedem / documento recente. | Confirme no consulado | Gebäude + Sanduhr; 7,0 Sand; 7,5 kippt + Punch; 8,5 Haken | whoosh · click 7,0 · impact 7,5 · pop 8,5 |
| 10,0 | A PF emite só / em português. | Certidão da PF · gov.br | Certidão groß; 11,5 Übersetzungsblatt gleitet heraus mit „?“; 12,5 Haken | whoosh · click 11,5 · pop 12,5 |
| 13,5 | Em geral, vai com / tradução e apostila. | Apostila: países da Convenção | Globus; 14,0 Nadel; 14,5 Siegel + Punch; 15,5 Haken | whoosh · click 14,0 · impact 14,5 · pop 15,5 |
| 17,0 | Pra traduzir: foto / ou PDF legível. | Sem mandar o original | Handy mit Certidão; 17,5 Auslöser-Blitz; 19,0 Haken | whoosh · click 17,5 · pop 19,0 |
| 20,5 | Pro espanhol: / R$ 119 na tabela. | Antecedentes · tabela | Certidão + Preisschild ohne Zahl 21,0; Punch 21,5; Haken 22,5 | whoosh · impact 21,5 · pop 22,5 |
| 24,0 | Chega em PDF com / assinatura digital. | Confirme se aceitam PDF | PDF, Unterschrift, Siegel 25,5, Haken 26,5 | whoosh · stamp 25,5 · pop 26,5 |
| 27,5–34,2 | Antecedentes / pro exterior? / Envie a foto: / preço na hora. + link na bio + traduzme.com.br + (61) 99803-8363 | – | Certidão gerade in Foto-Ecken + Haken (passt zu „Envie a foto“, Lehre 42-1) | stamp 27,5 · pop 28,5 |
| 34,2 | Loop = Frame 0 | | | |

Lernpunkte (≥ 3 mit Warum): 90 dias pela PF (gov.br) → Prazo des Ziels prüfen (muitos pedem recente) → PF nur Portugiesisch → darum Tradução (+ Apostila in Ländern der Convenção) → Foto/PDF reicht → Preis → PDF assinado, Annahme bestätigen.

## Kritiker-Runden (Storyboard, Bauer, getrennte Blickwinkel)
- **Runde 1 Fakten:** „vale 90 dias“ nur mit „Para fins civis · gov.br“ (Primärquelle-Wortlaut, Lehre R44: nicht pauschaler als die Quelle); Ausland nur „muitos pedem“ (Rechner-Wortlaut) + „Confirme no consulado“; „Em geral … tradução e apostila“ mit Konventions-Beleg (Lehre R39) – gov.br nennt die USA nur als Beispiel; keine Aussage zur Apostila no original der PF-PDF (Lehre R35-A); Preis 11900 Festpreis, keine Szene widerspricht (Lehre R41); keine Leistung ohne Quelle (Lehre R43/R44). Design: Névoa-Grund, Text Dark, Pillen Areia, Marker Sálvia/Pinho-Weiß, keine Weiß-auf-Névoa-Kombination. Hook/Tempo: Payoff 2,5 s (Sanduhr kippt), Antwort 3,0 s. Conversion: IG/TikTok dürfen „90“ nicht nennen.
- **Runde 2:** Etikett verrät die Zahl nicht (nur Dokument/Richtung/Preis) ✓; erste Fassung „Lá fora: confirme o prazo do destino“ war Ratschlag ohne Beleg → ersetzt durch Rechner-Wortlaut „muitos pedem documento recente“; GMB behält die Konventions- und Konsulats-Belege (Lehre R43-N2), streicht die Foto/PDF-Szene.
- **Runde 3:** keine offenen Mängel.

## Video-Kritik (nach Snapshots/Kontaktbögen)
- Runde 1: Requisiten lagen zu tief (Monate/Sanduhr im unteren UI-Bereich, Endcard-Certidão außerhalb 3:4) → alle Objekte auf dem Blatt ~140–180 px höher; Hook-Certidão + Sanduhr im 3:4-Ausschnitt.
- Weitere Runden: siehe reel45-texte.md „Prüfprotokoll B“.
