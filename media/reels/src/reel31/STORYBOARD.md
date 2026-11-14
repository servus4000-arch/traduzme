# Reel 31 – „Certidão francesa: traduz aqui ou na França?“ (Mi 11.11.2026)

Thema nach marketing/ENTSCHEIDEN.md (Lauf 04.11., Zeile in marketing/lernen/social.md): **Certidão em francês → português, Preisbeispiel R$ 119 + „Apostila na França, tradução aqui“**.
Kaufnachweis (nur intern, nie öffentlich): pedidos 30 T. ohne Tests: Certidão de nascimento FR→PT bezahlt 30.10. (Acte de naissance, copie intégrale, 1 Seite, Tabelle R$ 119). Score **18** (K3 N1 E1 B1 L3), Kandidaten siehe lernen/social.md.
- **Abgrenzung:** R28 (Certidão ES, Preisquiz „Passa de R$ 200?“), R23 (Certidão ES „já apostilada: falta A ou B?“), R24 (Casamento FR, Reserve, nicht gepostet), R30 (CNH ES Verso). Neu hier: **Wo wird übersetzt?** (A/B-Frage AQUI/FRANÇA), Apostila-Ort nach Haager Übereinkommen art. 3º, Sprache Französisch, Bildsprache **Dokument-Reise** (Route-Bogen + Flugzeug), neuer Frame 0.
- Grund **Dark #1F3B35** (R30 Névoa, R28/R29 Pinho). Paare: Weiß auf Dark (Hook, Kontakt), Weiß auf Pinho-Pille (Captions, 6,9 : 1), Dark auf Areia (Marker, Chip, Belege), Dark auf Sálvia (Endcard-Chip), Dark auf Papier (Requisiten). Kein Weiß auf Sálvia/Névoa/Areia.
- Musik `lib/music.py` **bossa 120 BPM** (R30 funk, R29 lofi, R28 pop), Master v2, −14 LUFS.
- **Eine Variable (Lernlog 04.11.):** Endcard-Kopf = **Handlungsaufforderung** „Envie a foto: / preço na hora.“ statt Wiederholung der Antwort (R28–R30: „Preço no site.“ / „Depende.“ / „Verso incluído.“). Conversion-Variable, weil Social-Sitzungen KW45 unter Soll (02.11.: 2). Alles andere wie R30 (LinkedIn-Link Zeile 1, Quiz + Payoff 2,5 s, Chip ab 3 s, Endcard ≥ 6,5 s).

## Quellen (nur was die Quelle trägt)
| Q | Quelle | Wortlaut / Inhalt | Geöffnet |
|---|---|---|---|
| Q1 | Supabase `precos` (ypdvpytpajgkzglbzxwg) `WHERE ativo AND NOT placeholder` | `fr / to_pt / certidao de nascimento` **11900**; ebenso casamento, divórcio, inteiro teor, negativa je 11900; alle FR→PT-Dokumente ≥ 11900 | SQL read-only 04.11.2026 = Memory preistabelle-live („FR 119“) |
| Q2 | Polícia Federal, Dúvidas frequentes „É necessária a legalização e tradução…“ (gov.br/pf/…/e-necessaria-a-legalizacao-e) | „os documentos emitidos no exterior precisam ser legalizados e traduzidos“ · „No Brasil, documentos estrangeiros, mesmo apostilados, precisam ser traduzidos por tradutor juramentado para ter validade.“ · „Essa tradução só pode ser feita no Brasil“ (CPC art. 192, Lei 14.195/2021 art. 27) · Ausnahmen nur Mercosul/Uruguai/Argentina/Portarias (Frankreich nicht betroffen) | WebFetch 04.11.2026 (selbst geöffnet); Whitelist 10-gegenkritik §3 |
| Q3 | Convenção da Apostila, Decreto 8.660/2016 (camara.leg.br, Publicação Original) art. 3º | „…aposição da apostila … emitida pela autoridade competente do Estado no qual o documento é originado.“ | WebFetch 04.11.2026 (planalto.gov.br gesperrt, Câmara-Fassung gelesen) |
| Q4 | HCCH Status table Convention 12 (hcch.net, cid=41) | França: R 25-XI-1964, EIF 24-I-1965 · Brasil: A 2-XII-2015, EIF 14-VIII-2016 | WebFetch 04.11.2026 |
| Q5 | Rechner live /orcamento-app/?lang=pt „Como o preço é calculado“ | pc2 „Verso e Apostila (foto ou página) contam como parte do documento: sem custo extra.“ · pc1 „Documentos padrão (certidões, diplomas, CNH…): preço fixo por documento.“ | Playwright **ohne Mock** 04.11.2026 → shots/pc2_live.png (ungeschnitten) |
| Q6 | Rechner live „Como funciona“ | fl1 „Foto ou PDF, quantos precisar.“ · fl2 „Valor e data de entrega na hora.“ · fl3 „Pague por Pix“ · fl4 „PDF juramentado com assinatura digital.“ | curl 04.11.2026 |
| Q7 | Código Civil art. 224 | „Os documentos redigidos em língua estrangeira serão traduzidos para o português para ter efeitos legais no País.“ | Whitelist (10-gegenkritik §3, R16/R23/R28) |
| Q8 | Supabase `pedidos` (nur intern) | FR→PT Acte de naissance bezahlt 30.10. | SQL read-only 04.11.2026, Tests ausgeschlossen |

Nicht verwendet: „a partir de“, Endpreis-/Rabatt-Versprechen, Eil-Option, Papier-Versand, Fristen, Ländernamen außer França/Brasil, Sprachlisten, Kundenfälle, Zertifikats-Infrastruktur der Signatur, Behörden-Zuständigkeit in Frankreich (nicht selbst geprüft).

## Zeitachse Hauptfassung (31,0 s, 120 BPM, Schlag 0,5 s)
Text x 90–900, y 300–1500. Caption-Pillen ab y 320, CTA-Chip y 552, Objektzone y 700–1360, Beleg y 1384.

| Zeit | Held-Objekt + Handlung | Text im Bild | Q | Ton |
|---|---|---|---|---|
| 0,0–3,0 | **Frame 0 fertig:** Requisite „ACTE DE NAISSANCE“ (ohne Daten) schwebt + Karten AQUI / FRANÇA. **2,5 Payoff:** AQUI Areia + Haken, FRANÇA blass, Punch | Hook „Certidão / francesa: / traduz aqui / **ou na França?**“ (7 W.) · Chip „Comenta AQUI ou FRANÇA“ | Q2 | pop 0,03 · impact 2,5 |
| 3,0–6,0 | Route-Bogen, Flugzeug fliegt (Fahrt), 4,5 Blatt „TRADUÇÃO JURAMENTADA“ + Siegel am Zielpunkt | „Juramentada: / **feita no Brasil.**“ · Beleg „Em geral, mesmo apostilada · PF“ (Beleg +0,5 s) | Q2 | pop 3,0 · stamp 4,5 |
| 6,0–9,0 | Preis-Etikett „CERTIDÃO DE NASCIMENTO · francês → português · R$ 119“, Punch 7,0 | „Certidão em francês / **R$ 119**“ · Beleg „Para português · preço de tabela“ (gleichzeitig ab 6,0) | Q1 | whoosh 6,0 · impact 7,0 |
| 9,0–12,0 | Acte + Blatt „APOSTILLE“ schiebt daneben, Stempel 10,5 | „Apostila: / **feita na França.**“ · Beleg „Convenção da Apostila, art. 3º“ | Q3, Q4 | whoosh 9,0 · stamp 10,5 |
| 12,0–15,0 | Mini-Acte + Mini-Apostille, Haken 12,5 (Punch); **echter Rechner-Ausschnitt pc2** | „Página da apostila: / **sem custo extra.**“ · Beleg „Na traduzme: documento padrão“ | Q5 | whoosh 12,0 · impact 12,5 |
| 15,0–18,0 | Gebäude + Acte mit Haken 16,0, Punch 17,0 | „Pra valer no Brasil: / **em português.**“ · Beleg „Código Civil, art. 224“ | Q7 | whoosh 15,0 · stamp 16,0 · impact 17,0 |
| 18,0–21,0 | Handy mit zwei Bildern (Acte / Apostille), Haken 19,5 | „Envie tudo junto: / **foto ou PDF.**“ · Beleg „Certidão e apostila“ | Q6 fl1, Q5 | whoosh 18,0 · pop 19,5 |
| 21,0–24,0 | Pin + Gebäude + Lupe, Punch 22,0 | „Confirme a lista / **com o órgão.**“ · Beleg „Ex.: cartório ou PF“ | Vorsicht (Q2 nennt Ausnahmen) | whoosh 21,0 · impact 22,0 |
| 24,0–30,7 | **Endcard** (Absender traduzme), Acte klein | „Certidão / francesa? / **Envie a foto:** / **preço na hora.**“ · Chip „link na bio“ · traduzme.com.br · (61) 99803-8363 | Q6 fl1/fl2 (Variable) | hit + stamp 24,0 |
| 30,7–31,0 | harter Schnitt auf Frame 0 | Hook | Loop | – |

Szenenwechsel alle 3,0 s (0,33/s). Punches 2,5 · 7,0 · 12,5 · 17,0 · 22,0 (Abstand ≥ 4 s). CTA-Chip 3,0–24,0. Rechner-/Preis-Anteil 6–9 + 12–15 = 6 von 24 s = 25 % (≤ 30 %), Preis frühestens 6,0 s. Endcard 24,0–30,7 = 6,7 s.
Payoff 2,5 s zeigt nur die Antwort AQUI, keinen Preis. Endcard ohne Preis.

## GMB-Fassung (28,0 s)
Ohne 18,0–21,0 (Foto ou PDF). Chip „Preço na hora no site“, Endcard-Chip „no site“, kein „link na bio“. Endcard 21,0–27,7, Loop 27,7, END 28,0. gmb/reel.html = reel.html mit `GMB=1` und Pfaden `../`.

## Kritiker-Runden Storyboard (getrennte Durchgänge, je ein Blickwinkel)
| Runde | Fakten | Design | Hook/Tempo | Conversion/LinkedIn |
|---|---|---|---|---|
| 1 | (a) „feita no Brasil“ ist PF-Wortlaut („só pode ser feita no Brasil“), gilt für Verwendung im Brasil; Ausnahmen (Mercosul, Portarias) betreffen Frankreich nicht, trotzdem Beleg „Em geral …“ statt absolut. (b) „Apostila feita na França“ = Haager Übereinkommen art. 3º („Estado no qual o documento é originado“) + HCCH (FR Mitglied seit 1965, BR seit 2016); welche französische Stelle, wird **nicht** gesagt (nicht selbst geprüft). (c) Erster Entwurf S5 „em geral, traduzida“: CC 224 verlangt Übersetzung ins Portugiesische, nicht ausdrücklich juramentada → Zeile „em português.“ (das trägt die Quelle wörtlich). (d) Preis: Caption „Certidão em francês R$ 119“ stimmt für **jede** FR-Certidão (nascimento, casamento, divórcio, inteiro teor, negativa je 11900) → eindeutig; Etikett nennt nascimento + Richtung, Beleg „Para português“ gleichzeitig (Lehre 29-5/29-N2). (e) S7 „Confirme a lista com o órgão“ = Handlungsempfehlung, keine Tatsachenbehauptung. | Grund Dark: Weiß auf Dark ✓, Captions Weiß auf **Pinho**-Pille (Weiß auf Areia verboten), Marker Areia + Dark ✓. Requisiten aus R30 waren Dark gefüllt (Gebäude, Handy, Pin, Lupe) → auf Dark unsichtbar, umfärben (Areia/Sálvia/Papier). Flächenfarben je Frame: Dark, Pinho, Areia (+ Papier-Objekte, Sálvia nur Endcard-Chip statt Areia) ≤ 3. | Hook 6 W. (Certidão·francesa·traduz·aqui·ou·na·França = 7) → **7 W.** ≤ 8 ✓; Frame 0: Hook 7 + Chip 4 + Karten 2 + Requisit 3 = 16 > 12 → Requisiten-Titel und Karten per ignoreText (Präzedenz R28/R30). Payoff 2,5 ✓. | Chip ab 3,0; GMB ohne „link na bio“; LinkedIn bleibt Link in Zeile 1 (R30), neuer B2B-Fall (RH/Mobilität mit Mitarbeitenden aus Frankreich, Kanzleien Família internacional); IG/TikTok verraten AQUI nicht und nennen keinen Preis. |
| 2 | Alle Bildaussagen gegen Q1–Q7 gelesen: gedeckt. Kein „sempre/nunca“, kein „a partir de“, kein Superlativ. Endcard-Variable „Envie a foto: preço na hora.“ = fl1 + fl2. | Caption-Breiten am Video messen (qa_frames safe); Kerninfo Preis y ≤ 1250 (Etikett-Preis ≈ y 1060–1210). Mini-Titel bei Skala < 0,6 ausblenden (keine 20-px-Requisitenschrift). | Standzeit Caption 2,92 s ≥ max(1,8; 0,4 × 6 W.) ✓; ≤ 4 W./Zeile: „Tradução juramentada:“ 2 W., „Página da apostila:“ 3 W. ✓; Endcard 6,7 s ✓. | UTM reel31 je Kanal (youtube/linkedin/gmb). |
| 3 | keine offenen Mängel | keine offenen Mängel | keine offenen Mängel | keine offenen Mängel |
Video-Runden: /mnt/project-files/social/reels/reel31-texte.md, „Prüfprotokoll“.
