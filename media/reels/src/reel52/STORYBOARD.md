# Reel 52 – „Seu extrait francês mostra os pais?“ (Post Fr 04.12.2026, FR-Fall)

Acte de naissance **francês → português**, Etikett „R$ 119 na tabela“. Zweiter Bau nach Abnahme 52-A (erster Bau „Certidão em espanhol: só a tradução basta?“ abgelehnt: Doppelung R49). Format **Mural** (Pinnwand: Korkfläche in Pinho-Rahmen mit Pinnnadeln und Ablageleiste als Bühne; Szenenwechsel = **Blatt-Schnitt**: ein Papierblatt gleitet 0,10 s vor dem Schlag von rechts über den Kork, deckt die Fläche auf dem Schlag (harter Schnitt darunter) und ist bei +0,18 s links draußen), Grund **Areia #EEDECE**, Musik `music.py` **funk 120 BPM**, E, seed 52, Master v2 (Format/Farbe/Musik laut 52-A beibehalten). Szenen 3,5 s, Endcard Standard „Envie a foto: preço na hora.“, Etikett in Frame 0 (Standard seit R35), Mitmach-Pille „SIM, NÃO ou DEPENDE?“ (Standard-Pille, keine Knöpfe). Neue Variable (nicht im Bild): **TikTok-Caption Zeile 1 mit den französischen Originalbegriffen „copie intégrale“ und „extrait“**.

Pflichtwechsel ggü. Vorgängern (keine Variable): R51 Fichário/Sálvia/lofi, R50 Mala de viagem/Dark/bossa, R49 Envelope/Névoa/calm → Mural/Areia/funk.

## Thema (ENTSCHEIDEN 27.11.2026, Zeile in marketing/lernen/social.md)
- Auftrag 52-A: neues Thema ES/FR/IT (kein DE/EN/AR), aus Vorrat OFFEN N01–N24, sonst per ENTSCHEIDEN; Score ≥ 14; vor dem Storyboard jede Kernaussage und Szene gegen R20–R51 greppen; Lei 14.195 art. 26/27 § 2º I, CC 224 und „Lista … confirme“ nicht als Szene; Variante A (Impugnation) nicht.
- Vorrat geprüft und verworfen: N02 (alle Kernaussagen tabu), N06 (PF-FAQ zu PI 19/2021 widersprüchlich), N12 (Doppelung R49 → wieder OFFEN-gesperrt), N14 (Apostila/Legalisation Kern in R20/R22/R23/R26/R46; Kanada R44), N16 (Junta R27/R44/R50; art. 23 R49), N20 (Haiti: Port. 27/2021 verzichtet auf Übersetzung → gegen Verkauf, nah an Cuba), N24 (Casamento gesperrt).
- Schritt 1 (SELECT 27.11., read-only): pedidos status PAGO 30 T. – FR→PT „Acte de naissance“ bezahlt 30.10. (R$ 198, 1 Seite); analises 30 T. fr/certidao de nascimento 5 Uploads (eine Analyse 29.10. ausdrücklich „Acte de naissance, copie intégrale“).
- Kandidaten (Score = K×3 + N×2 + E×2 + B×2 + L):
  - **Acte de naissance FR→PT „Seu extrait francês mostra os pais?“ R$ 119 (K3 N1 E1 B0 L3 = 16) → gewählt**
  - Certidão em espanhol sem Pix (PayPal/Überweisung laut Rechner-FAQ) (K3 N0 E1 B1 L2 = 15) – nicht gewählt: R16 „Sem CPF“ deckt den Kern, Ablauf manuell per WhatsApp
  - N14 Québec FR – nicht bewertet: Kern (Apostila/Legalisation) ist Doppelung (Auftrag 52-A)
- Grund: einziger Kandidat ≥ 14 ohne Doppelung, echter Käufer-Zweifel (welche Fassung habe ich, zeigt sie die Eltern?), Primärquelle eindeutig (service-public F1427), Kaufnachweis FR-Geburtsurkunde. Erwartete Wirkung grob (Annahmen, nicht gemessen): 300 Aufrufe × 1 % Rechner × 10 % Kauf × R$ 119 ≈ R$ 36 je Reel (klein; B0 notiert).
- N1 geschätzt, nicht gemessen.

## Doppel-grep (vor dem Storyboard, gegen social/reels-log.md und social/reels/reel20–51-texte.md)
| Begriff / Kernaussage | Treffer | Bewertung |
|---|---|---|
| margem / marginal / menções | 0 | neu |
| filiação / filiation | R24 (anderer Zusammenhang) | neu als Kern |
| qualquer pessoa / qualquer um | 0 | neu |
| copie intégrale / extrait | 0 | neu |
| acte de naissance | R24, R31 (R31-Kern: übersetzen hier oder in Frankreich + Apostila) | anderer Lernpunkt |
| service-public | R37 (casier judiciaire) | andere Seite, anderes Dokument |
| Lei 14.195, CC 224, Lista/confirme als Szene | in R52 nicht verwendet | – |
| Preis-Szene „copie ou extrait: mesmo preço“ | Muster R41 | verworfen → Standard-Preisszene |

## Quellen
| Q | Aussage | Quelle | Wie geprüft |
|---|---|---|---|
| Q1 | Acte de naissance francês → português **R$ 119 na tabela** (Etikett 0–2,97; Bild 24,0) | Supabase `precos` `WHERE ativo AND NOT placeholder`: `fr / to_pt / certidao de nascimento` **11900**, extra_pag null | SELECT 27.11.2026 (read-only) |
| Q1b | Französische Geburtsurkunde (copie intégrale wie extrait) = Typ `certidao de nascimento`; Festpreis je Dokument bis 4 Seiten (Beleg „Preço fixo · até 4 páginas“) | Edge-Function `analisar` v48 („Classifique pela FUNÇÃO do documento“; Averbações/Verso/Apostila = Teil desselben Dokuments); echte Analyse 29.10. „Acte de naissance, copie intégrale … Ville de Nice“ → certidao de nascimento; `pix-cob` v62 `PAUSCHAL_MAX_PAG=4` | get_edge_function + SELECT analises 27.11.2026 |
| Q2 | Avec filiation: com os pais · „Pais no extrait · França“ (Bild 3,0) | service-public.gouv.fr F1427 „Acte de naissance : demande de copie intégrale ou d'extrait“ (Verified 14 August 2026): Extract with filiation = Zusammenfassung mit Angaben zur Person und zu den Eltern | WebFetch F1427?lang=en 27.11.2026, zweimal (service-public.fr vom Proxy gesperrt, Légifrance nicht erreichbar) |
| Q3 | Sans filiation: sem os pais · „Só nome, data e local“ (Bild 6,5) | F1427: Extract without parentage = nur Angaben zur Person (Name, Vornamen, Datum und Ort der Geburt) | wie Q2 |
| Q4 | Copie intégrale: todo o registro · „Reproduz todo o assento“ (Bild 10,0) | F1427: Full copy reproduziert den ganzen Registereintrag, inkl. Eltern | wie Q2 |
| Q5 | Menções à margem: nos três tipos · „Quando existem · França“ (Bild 13,5) | F1427 je Typ: „It indicates the marginal terms where they exist.“; die Seite nennt genau diese drei Typen (kein plurilinguales Extrait) | wie Q2 |
| Q6 | Com os pais: pedido restrito · „Ex.: titular, cônjuge, pais“ (Bild 17,0, nur Hauptfassung) | F1427: Full copy / extract with filiation nur Person (volljährig) oder gesetzl. Vertreter, Ehegatte/eingetragener Partner, Vorfahren/Nachkommen, gesetzlich befugte Berufsträger; andere (z. B. Onkel/Tante) erst nach 75 Jahren (Minderjährige 100) bzw. 25 Jahre nach dem Tod | wie Q2 |
| Q7 | Sans filiation: qualquer um pede · „Sem justificar o pedido“ (Bild 20,5) | F1427: „Any person may obtain a birth certificate without parentage, without having to justify its request.“ | wie Q2 |
| Q8 | Envie a foto: preço na hora (Endcard); Foto ou PDF; valor e data na hora; Pix; PDF com assinatura digital (Texte) | Rechner fl1–fl4 | curl /orcamento-app/ 27.11.2026 |
| – | Requisiten (Pinnwand, Extrait-Karte mit Eltern-Feld bzw. leerem Feld und Randspalte, Copie intégrale, Randmarker, Personen, Schloss, Menge, Preisschild ohne Zahl, Handy, Haken, Fragezeichen, Ring) | eigene SVG ohne Schrift, ohne Zahlen, ohne Wappen/Flaggen/Landkarte/Firmenlogo, kein Kundenfall | – |

**Bewusst nicht verwendet:** Apostila/Legalisation; Lei 14.195 und CC 224; welche Fassung ein brasilianischer Órgão verlangt (keine Primärquelle → in Texten nur „confirme no órgão“); „gratuit“ (Bestellung in Frankreich kostenlos, lenkt vom Kauf ab); SCEC Nantes; Lieferfristen; Empfehlungen (Lehre R45); Kundendaten.

## Ablauf (Designzeit; GMB lässt 17,0–20,5 weg, Endcard 5,0 s)
| Zeit | Text (Bild) | Beleg-Pille | Bild / Ereignis | SFX |
|---|---|---|---|---|
| 0–2,97 | Hook „Seu extrait / francês mostra / os pais?“ + Pille „SIM, NÃO ou DEPENDE?“ + Etikett „Acte de naissance · francês → português · R$ 119 · na tabela“ | – | Pinnwand, Extrait-Karte mit „?“; 2,5 zweite Karte (Eltern-Feld leer) gleitet daneben, Ring + Punch | pop 0,03 · stamp 2,5 |
| 3,0 | Avec filiation: / com os pais. | Pais no extrait · França | Blatt-Schnitt; Karte mit Eltern groß; 3,5 Marker über das Eltern-Feld; 5,5 Haken | whoosh · click 3,5 · pop 5,5 |
| 6,5 | Sans filiation: / sem os pais. | Só nome, data e local | Karte mit leerem Feld; 7,5 „?“ im Feld + Punch; 8,5 Haken | whoosh · stamp 7,5 · pop 8,5 |
| 10,0 | Copie intégrale: / todo o registro. | Reproduz todo o assento | hohes Blatt mit Randspalte; 10,5 Marker über alle Zeilen, 11,0 Punch; 12,5 Haken | whoosh · click 10,5 · stamp 11,0 · pop 12,5 |
| 13,5 | Menções à margem: / nos três tipos. | Quando existem · França | drei kleine Dokumente; 14,0 Randmarker, 14,5 Punch; 15,5 Haken | whoosh · click 14,0 · stamp 14,5 |
| 17,0 | Com os pais: / pedido restrito. | Ex.: titular, cônjuge, pais | Karte mit Eltern; 17,5 Familie gleitet heran; 18,5 Schloss springt auf | whoosh · click 17,5 · stamp 18,5 |
| 20,5 | Sans filiation: / qualquer um pede. | Sem justificar o pedido | Karte ohne Eltern; 21,5 Menge springt auf + Punch; 22,5 Haken | whoosh · stamp 21,5 · pop 22,5 |
| 24,0 | Francês, na tabela: / R$ 119 a certidão. | Preço fixo · até 4 páginas | Copie + Extrait; 24,5 Preisschild ohne Zahl gleitet heran, 25,5 Punch; 26,5 Haken | whoosh · click 24,5 · stamp 25,5 · pop 26,5 |
| 27,5–34,2 | Certidão / francesa? / Envie a foto: / preço na hora. + link na bio + traduzme.com.br + (61) 99803-8363 | – | Handy mit der Certidão, Haken 28,5 | stamp+hit 27,5 · pop 28,5 |
| 34,2 | Loop = Frame 0 | | | |

Lernpunkte (≥ 3 mit Warum): Ob die Eltern drauf sind, hängt von der Fassung ab (avec / sans filiation) → die copie intégrale gibt den ganzen Eintrag wieder → Randvermerke erscheinen in allen drei Fassungen, wenn es sie gibt → die Fassungen mit Eltern darf nur ein enger Kreis bestellen, die ohne Eltern jeder → Festpreis der Übersetzung.

## Kritiker-Runden (Storyboard)
- **Runde 1 Fakten (Lehre 52-1, exakter Wortlaut):** F1427 geöffnet; „família“ verworfen (Onkel/Tante ausgeschlossen) → „pedido restrito“, Beleg mit „Ex.:“ (Liste länger); „Menções à margem“ nur mit „Quando existem“. Runde 2: F1427 erneut geöffnet: genau drei Typen genannt, Randvermerk-Satz in allen drei → „nos três tipos“ hält; „qualquer um pede“ = „Any person … without having to justify“.
- **Runde 1 Doppelung:** grep oben; Preisszene als Standard („R$ 119 a certidão“), nicht „mesmo preço“ (R41).
- **Runde 1 Design:** Areia-Grund, Dark-Schrift; Hook passt mit 92 px in x ≤ 900 nur in der Kurzform „Seu extrait / francês mostra / os pais?“ („Acte de naissance:“ wäre zu breit).
- **Runde 1 Hook/Tempo (Lehre 51-A):** eine Frage, ein Gegenstand (die eigene Urkunde), Antwort ab 3,0 s; Etikett verrät nichts. Payoff 2,5 s.
- **Runde 1 Conversion (Lehre 51-B):** IG/TikTok ohne sinngemäße Antwort und ohne Typenzahl; Zeile 2 „Resposta no vídeo 👀“; YT/LinkedIn antworten mit Quelle; UTM reel52.
- **Runde 2 qa_frames:** Haupt und cut=gmb PASS (0 block, 0 warn).

## Kontaktbögen (nach dem letzten Render, 27.11.)
- Haupt 0–34,4 s und GMB 0–29,2 s ganz angesehen (10 fps): Safe Zone eingehalten, Blatt-Schnitt nur um die Schnitte, keine Doppelbelichtung, Captions wachsen Zeile für Zeile, keine leeren Pillen, kein leeres Bild; GMB springt bei 17,0 von „Menções à margem“ auf „Sans filiation: qualquer um pede.“ (Restrito-Szene fehlt wie geplant), Chip „Preço na hora no site“, Endcard „no site“; Loop kehrt in beiden Fassungen zum Hook zurück. Cover 1,0 s: Hook, Pille, Etikett lesbar. Kein Mangel gefunden. Hinweis: Extrait-Karte im Hook-Bild klein (≈ 170 px), gewollt (Etikett + Hook haben Vorrang).

## Ton
`music.py` funk 120 BPM, E, seed 52, Master v2, Ceiling −3,0 dBTP. stamp = Körper Hochpass 300 Hz + Präsenz-Schicht 1,8–4,2 kHz; **click mit eigener Präsenz-Schicht** (Lehre 52-2: 12 ms Rauschen 1–3,5 kHz, `CPRES` 5,0). 27 Ereignisse (0,78/s). Gains `GJ_MAIN`/`GJ_GMB` per `measure_sfx.py` (Ziel Breitband-20-ms-Spitze +3,5 dB, Fenster [t, t+0,45 s]; zusätzlich Spalte 1–3 kHz). Messwerte siehe social/reels/reel52-texte.md „Ton“.
