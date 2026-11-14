# Reel 27 – „Juramentado em Brasília: só do DF?“ (Mo 09.11.2026)

Thema: REELS-REGELN-v2, Themen-Priorität Punkt 5 „Tradutor juramentado em Brasília? Nem precisa sair de casa“ (lokaler Such-Winkel, auch GMB).
Kern: Der Tradutor muss nicht aus der Junta do DF sein (Lei 14.195/2021, art. 24) → Pedido komplett online in 4 Schritten (echte „Como funciona“-Zeilen des Rechners) → PDF mit assinatura digital, em geral gleichwertig zu Papier → „confirme se o órgão aceita PDF“.
- **Kein Standort-Claim:** kein Büro in Brasília, keine Adresse. traduzme sitzt in São Paulo (feste-fakten-ben), nur die WhatsApp-Nummer hat DDD 61. Das Reel sagt nur, dass man aus Brasília online bestellt.
- Format **F6 „Do celular ao PDF“** (erstmals; D8 Werbe-Anteil für F6 ausgesetzt, ≤ 32 s). Held-Objekte: Tradução (Hook/Lei), Haus (Casa), Handy mit echten Rechner-Zeilen (Schritte), PDF + Papier (Validade), Órgão-Gebäude (Confirme).
- ES-Fall nur angedeutet: im Schritt 1 wird eine „ACTA DE NACIMIENTO“ (Spanisch, Requisite ohne Daten) fotografiert. Kein Kundenfall behauptet.
- Grund **Dark #1F3B35** (R26 Areia, R25 Névoa). Hook Weiß auf Dark, Marker Areia/Dark; Captions Areia-Pillen mit Dark-Text, Marker Pinho/Weiß; Chips Sálvia/Dark; Belege Névoa/Dark.
- Musik `lib/music.py` **funk 120 BPM** (R26 calm, R25 bossa), Master v2, Schlag 0,5 s.

## Neue Variable (genau eine, Schritt 0)
**Hook-Typ „lokaler Such-Hook“**: Ortsname + Suchbegriff („Juramentado em Brasília“) in der Hook-Frage, statt Dokument-Quiz ohne Ort (R26 „Atestado em árabe: vale direto?“). Gleich wie R26: Quiz SIM/NÃO mit Karten im Frame 0, Payoff 2,5 s, kein Serien-Rahmen (R27 ist keine Serienfolge).
Mitläufer (Routine-Rotation, keine Test-Variable): Format F6, Farbe Dark, Musik funk.
**Vorhersage (72 h nach Post 09.11., Messung Do 12.11.2026):** TikTok-Aufrufe ≥ +30 % gegenüber dem Median der letzten 6 Reels (Suche bringt Zusatz-Views); TikTok Ø Sehdauer ±15 %; GMB-Videoaufrufe falls Metricool sie liefert (bisher null → nur notieren).

## Quellen (nur was die Quelle trägt)
| Q | Quelle | Wortlaut / Inhalt | Geöffnet |
|---|---|---|---|
| Q1 | Lei nº 14.195/2021, art. 24 – zitiert im eigenen Blog „Tradução juramentada em Brasília (DF)“ (traduzme-site origin/main 49dfec8, Stand 28.10.2026) + Fakten-Whitelist 10-gegenkritik §3 P14 „Myth outro estado: Grün (L1011, FAQ a1, Lei 14.195/2021)“ | Blog: „o tradutor não precisa estar matriculado na Junta Comercial do DF: pelo artigo 24 da mesma lei, quem cumpre os requisitos pode ‚atuar em qualquer Estado e no Distrito Federal‘“; FAQ Blog: „mantendo registro só na junta do seu domicílio“ | Blog per git show 02.11.2026; planalto.gov.br aus der Sandbox gesperrt (curl 403, WebFetch „Acesso negado“) |
| Q2 | Rechner live /orcamento-app/?lang=pt, „Como funciona“ (Whitelist L1004–1007) | „1 Envie o documento – Foto ou PDF, quantos precisar. 2 Preço em segundos – Valor e data de entrega na hora. 3 Pague por Pix – Confirmação automática, a tradução começa. 4 Receba por e-mail – PDF juramentado com assinatura digital.“ | Playwright 02.11.2026, **ohne Mock** (shots/step*_c.png) |
| Q3 | Rechner, Kopf (Whitelist L998) | „Tradução juramentada online · 100% digital.“ | Quelltext origin/main + live 02.11. |
| Q4 | Rechner-FAQ a7 (Whitelist) | „Não [precisa enviar o original]. Basta uma foto nítida ou um PDF legível do documento inteiro …“ | Quelltext origin/main 02.11. |
| Q5 | Rechner-FAQ a6 (Whitelist, **ohne** Zertifikats-Teil) | „A tradução é entregue em PDF com assinatura digital …, verificável por QR Code. No Brasil, ela tem a mesma validade jurídica de uma tradução em papel.“ / „Alguns órgãos, principalmente no exterior, ainda pedem a via em papel.“ | Quelltext origin/main 02.11. |
| Q6 | Blog Brasília (wie Q1): STJ verlangt bei Homologação Übersetzung in Papier | Grund, warum im Bild „Em geral“ + „Confirme se o órgão aceita PDF“ stehen (kein Via-física-Versprechen) | wie Q1 |

Nicht verwendet: Adresse/Büro in Brasília, Fristen, Preise, Eil-Option, Papier-Versand, Apostila-Kosten, Zertifikats-Infrastruktur, Sprachlisten, Kundenfälle.

## Zeitachse Hauptfassung (32,0 s, 120 BPM)
Text x 90–900, y 300–1500. Caption-Pillen ab y 320, CTA-Chip y 552, Objektzone y 680–1484, Beleg y 1384.

| Zeit | Szene / Held-Objekt + Handlung | Text im Bild | Q | Ton |
|---|---|---|---|---|
| 0,0–3,0 | **Frame 0 fertig:** Tradução-Dokument (≥ 540 px breit) mit gestricheltem Pin „DF?“ auf dem Siegel (Ungereimtheit), Karten SIM/NÃO rechts. Pin wippt ab Frame 1. **2,5 Payoff:** NÃO wird Areia mit Haken, SIM blass, Pin fällt, Punch | Hook „Juramentado / em Brasília: / **só do DF?**“ (6 W.; „DF?“-Pin + Doku-Titel per qa ignoreText vom Wortzähler ausgenommen) · Mitmach „Comenta: SIM ou NÃO“ | Q1 | pop 0,03 · impact 2,5 |
| 3,0–6,0 | Tradução mittig groß, Siegel stempelt 4,5 | „Não precisa ser / **da Junta do DF.**“ · Beleg „Lei 14.195/2021, art. 24“ | Q1 | pop 3,0 · stamp 4,5 |
| 6,0–9,0 | Haus mit gestrichelter Route zum Bürogebäude; 7,0 Route mit X durchgestrichen; 7,5 Handy leuchtet im Fenster (Punch) | „Nem precisa / **sair de casa.**“ · Beleg „Pedido 100% digital“ | Q3 | whoosh 6,0 · stamp 7,0 · impact 7,5 |
| 9,0–11,5 | **Handy**, echte Zeile 1; ES-Urkunde „ACTA DE NACIMIENTO“ wird fotografiert (Blitz 10,0) | „Foto ou PDF / **do documento.**“ · Beleg „Sem enviar o original · FAQ“ | Q2, Q4 | whoosh 9,0 · click 10,0 |
| 11,5–14,0 | Handy, echte Zeile 2; Kalender + Balken ohne Zahlen, Punch 12,0 | „Preço e data / **na hora.**“ | Q2 | pop 11,5 · impact 12,0 |
| 14,0–16,5 | Handy, echte Zeile 3; Tipp 14,5, Haken 15,0 | „Pague / **por Pix.**“ | Q2 | click 14,5 · pop 15,0 |
| 16,5–19,0 | Handy, echte Zeile 4; Umschlag, PDF gleitet heraus, Punch 17,0 | „PDF assinado / **por e-mail.**“ | Q2 | whoosh 16,5 · impact 17,0 |
| 19,0–22,0 | PDF (Siegel, QR-Andeutung, Unterschrift) + Papierblatt (gleiten zusammen ein), Gleichheitszeichen 21,0 (Punch) | „Em geral, vale / **como papel.**“ · Beleg „No Brasil · FAQ traduzme“ | Q5 | whoosh 19,0 · pop 19,5 · stamp 21,0 |
| 22,0–25,0 | Órgão-Gebäude, PDF fährt hin, Lupe/Fragezeichen 23,5 | „Confirme se o / **órgão aceita PDF.**“ · Beleg „Alguns pedem papel · FAQ“ | Q5, Q6 | whoosh 22,0 · pop 23,5 |
| 25,0–31,7 | **Endcard** (Absender traduzme), Mini-Handy | „Juramentada / em Brasília? / **Pelo celular.**“ · Chip · traduzme.com.br · (61) 99803-8363 | – (CTA) | hit + stamp 25,0 |
| 31,7–32,0 | harter Schnitt auf Frame 0 | Hook | Loop | – |

Szenenwechsel: 3/6/9/11,5/14/16,5/19/22/25 = 9 in 25 s (0,36/s). Punches 2,5 · 7,5 · 12,0 · 17,0 · 21,0. CTA-Chip „Preço na hora · link na bio“ 3,0–25,0. Rechner-/Kauf-Anteil 9–19 s = 10 s von 25 s (40 %, F6-Ausnahme D8, Start ≥ 6 s). Endcard 25,0–31,7 = 6,7 s (voll ab 25,12).

## GMB-Fassung (29,0 s)
Ohne 19,0–22,0 (Validade). Chip „Preço na hora no site“, kein „link na bio“. Endcard 22,0–28,7, Loop-Schnitt 28,7, END 29,0. Gebaut aus reel.html (`GMB=1`, Pfade `../`).

## Kritiker-Runden
Siehe /mnt/project-files/social/reels/reel27-texte.md, „Prüfprotokoll“ (Storyboard-Runde 2, Video-Runde V5 und Text-Runde 3: keine offenen Mängel; Kritiker = Selbst-Durchgänge).
