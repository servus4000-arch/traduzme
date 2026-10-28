# Plan-Reel 2 (Datei traduzme_reel_11) – Do 29.10.2026 – "Lucas e o mestrado no Canadá" – TikTok, IG, YT (EDUCATION), LinkedIn
Plan-Version 3.1 (Inhalt R3 bestanden + Hinweise eingearbeitet; nach Runde 2: Inhalt, Design gemessen, Tempo). Länge 83,8 s, 1080x1920, 30 fps, 112 BPM.

## Was der Zuschauer mitnimmt (alles aus Blogpost traducao-juramentada-historico-escolar-e-diploma, 23.10.)
- Selbst übersetzen geht nicht: die WES recusa tradução feita pelo próprio candidato → man braucht eine richtige (juramentada) Übersetzung.
- L1 Erst die Anforderung des Zielorts lesen (WES: tradução literal e completa, palavra por palavra; incompleta é recusada).
- L2 Alle Seiten des Histórico zählen: Verso mit Text und Seite nur mit Stempel zählen mit (sonst unvollständig).
- L3 Diploma digital (RVDD): das PDF der Faculdade schicken, nicht drucken/scannen; die Übersetzung trägt den código de validação.
- L4 Diploma und Histórico im selben Pedido: gleiche Terminologie in beiden; Preis sofort, Pix, PDF digital signiert per E-Mail.

## Globale Design-Vorgaben (verbindlich)
- Ränder links 90, rechts 150 (Text max. 840 px breit). Nichts über y<220 (UI) oder y>1500.
- Zonen: Kopfleiste y 230–330 (4 Fortschrittspunkte Ø22, Abstand 18, aktiv Pinho, sonst Dunkel 25 %, ab S4); Textblock y 340–720 (Headline + Subline immer zusammen, Subline 36 px unter Headline); Bildbühne y 760–1480, Bodenlinie y 1480.
- Schrift Open Sans: Headline 88 px/800, Zeilenhöhe 1,08, Laufweite −1, max. 2 Zeilen; Subline 58 px/600, Zeilenhöhe 1,2, max. 3 Zeilen; Lesetext im Bild ≥ 44 px; Deko-Labels ≥ 34 px.
- Badge 1–4: Kreis Ø132 Pinho, Ziffer 76 px/800 weiß, links neben Headline (Headline-Einzug 160), Pop 0→1,12→1 in 350 ms.
- Lucas: feste Proportion (Kopf = 1/4), 6 px Kontur Dunkel, Bühnenscheibe Ø700 hinter ihm (Areia auf Pinho/Sálvia, Névoa auf Areia). Ganzkörper 820 px (S1, S8), Halbfigur 600 px links x 60–400 auf Bodenlinie in Lernszenen; Objekte rechts x 380–930, überlappen Lucas 40–80 px.
- Ebenen je Szene: Fläche, 2–3 Ton-in-Ton-Formen driften ±30 px/6 s (nie im Textblock), Bodenlinie, Figur+Objekt, Mikroanimationen (Blinzeln 2,5–3,5 s, Atmen 1→1,015/2 s, Float ±6 px). Kamera max. Scale 1,00→1,06 pro Szene, nur Bildebenen; Text bewegt sich nicht, solange er gelesen wird.
- Flach: keine Blur-Schatten; harte Schatten 0 14 px #1F3B35 15 %. Keine Verläufe, keine Emojis (Ahornblatt als SVG, Schweißtropfen Névoa).
- Kontrast: auf Areia/Névoa/Weiß Text Dunkel (Pinho nur ≥88 px); auf Sálvia nur Dunkel; auf Pinho/Dunkel Weiß oder Areia.
- Bewegung: Auftritte 350–600 ms, nichts Bildfüllendes < 300 ms, Text: 24 px hoch + Opacity in 400 ms, kein Tippeffekt bei > 5 Wörtern; nach jeder Zeile ≥ 1 s ohne neues Element. Übergänge 500 ms, story-motiviert (unten).
- Tempo-Regel: Einblendung 0,4 s, dann 0,4 s/Wort Lesen; ≥1 s Hinschauen pro Szene (am Anfang oder Ende); Zeile 2 erst, wenn Zeile 1 gelesen. Bildtexte, die nicht gelesen werden müssen, sind Platzhalter-Balken oder Deko (≤ 34 px Labels).
- Bau-Check: jedes Textelement getBoundingClientRect().bottom ≤ 720 (S7 ≤ 714); Headlines der Lernpunkte max. ~30 Zeichen (2 Zeilen à 88 px neben Badge); Kopfleiste-Punkte rechtsbündig an x 930.

## Szenen (Zeiten absolut; "a→b" = erscheint bei a, gelesen bis b)
S1 Hook 0,0–6,2 (Pinho, Areia-Scheibe, 3 Ahornblätter Sálvia)
- 0,0 Lucas (Ganzkörper 760 px, y 720–1480) springt rein, Brief 380×260 "APROVADO" + Ahornblatt (−8°).
- Text y 300–680: Kicker 64 px Areia "Vai estudar fora?" 0,4→2,0; Headline 80 px Weiß (3 Zeilen erlaubt) "4 coisas antes de traduzir diploma e histórico" 2,0→5,6. Halten bis 6,2.
→ 6,2–6,7 Brief fliegt in den Laptop-Bildschirm, Fläche Areia.
S2 Setup 6,2–12,8 (Areia)
- 6,7–9,8 Laptop zentriert, voll breit (840), Bildschirm y 820–1400; Mail: Absender-Logo "WES", Betreff 44 px "Envie as traduções: diploma e histórico." 7,0→9,8; Anhang-Chips "diploma" "histórico".
- 9,8 Kamera: Laptop skaliert auf 0,62 und rückt nach rechts (x 380–930), Lucas Halbfigur schiebt sich links rein. Sprechblase im Textblock (y 400–640, 58 px) "Fácil! Eu mesmo traduzo." 10,2→12,2, Pfeil nach unten zu Lucas, Grinsen. Halten bis 12,8.
→ 12,8–13,3 Plattenkratzer, Freeze, Wipe von oben zu Dunkel, 0,6 s Musikstille.
S3 Wendepunkt 12,8–22,0 (Dunkel)
- Lucas Halbfigur auf Pinho-Scheibe Ø700, Kontur Névoa, Freeze-Look Pinho/Névoa. Sprechblase knittert 13,3–13,7 und verschwindet.
- Headline 88 px Areia "Para a WES, não." 13,7→15,7
- Subline 58 px Weiß "A WES recusa tradução feita pelo próprio candidato." 15,7→19,3
- Zeile 3, 58 px Areia/800 "Precisa de tradutor juramentado." 19,3→21,3. Halten bis 22,0.
→ 22,0–22,5 Lupe kommt rein, Kreis-Wipe aus der Lupe zu Névoa.
S4 Lernpunkt 1 22,0–31,6 (Névoa)
- Badge 1 + Headline "Leia o que o destino exige." 22,8→25,6
- Subline "A WES pede tradução completa, palavra por palavra. Incompleta é recusada." 25,6→30,4
- Bild: Blatt 640×640 (x 290–930, y 800–1440) "Requisitos WES" mit Platzhalter-Balken; 26,0 Lupe Ø260 + Sálvia-Markierung (600 ms) über die einzige lesbare Zeile "tradução literal e completa" (44 px, einzeilig). Von Lucas nur Kopf + Hand mit Lupe unten links.
- 30,4–31,6 Gag: Lucas' Auge riesig hinter der Lupe.
→ 31,6–32,1 Blatt-Flip um Y, fächert zum Histórico auf.
S5 Lernpunkt 2 31,6–43,2 (Areia, Sálvia-Bühnenfläche unten)
- Badge 2 + Headline "Conte todas as páginas." 32,4→34,4
- Bild: 5 Blätter 240×340 gestaffelt (Versatz 150, x 90–930, y 900–1240), erscheinen 32,6 / 33,1 / 33,6 / 34,1 / 34,6 mit Ziffer 1–5 (96 px Pinho, y 780–880 auf Areia) + Ding: 1 frente, 2 VERSO, 3 frente, 4 VERSO, 5 só carimbo (Stempel Ø120).
- Subline "Verso com texto e página só com carimbo contam." 34,8→38,8; 35,2 Versos 2+4 leuchten auf, 36,6 Blatt 5 mit Stempel.
- 38,8 Crossfade Subline → "Pulou uma? Tradução incompleta." (Pinho-Akzent) 38,8→40,8
- 40,8–42,8 Gag (2,0 s): Blätter skalieren auf 0,8 nach oben, Lucas steigt von unten ein, zählt an überzeichneten Händen (1,3×). Halten bis 43,2.
→ 43,2–43,7 Blätter stapeln sich und gleiten in den Laptop.
S6 Lernpunkt 3 43,2–52,0 (Névoa)
- Badge 3 + Headline "Diploma digital? Mande o PDF." 44,0→46,4 (bei Überlauf Badge über die Headline)
- Subline "Impresso perde a validade. A tradução leva o código de validação." 46,4→51,2
- Bild: Laptop x 90–560, y 900–1200 mit Diploma-PDF + QR Ø180; Lucas als Brustbild hinter dem Laptop (≈420 px). Drucker 160 px rechts (x 700–860, y 900–1060) wird 46,8 durchgestrichen (14 px, 400 ms) und blendet aus; an seiner Stelle Blatt "TRADUÇÃO" 300×400 (x 630–930, y 880–1280); 48,6 Code-Chip "Código de validação" (44 px) fliegt vom Diploma auf das Blatt und landet auf 0,75. Halten bis 52,0.
→ 52,0–52,5 Laptop morpht zum Handy, Fläche Pinho.
S7 Lernpunkt 4 52,0–62,4 (Pinho; Text y 300–714)
- Badge 4 + Headline Weiß "Peça os dois juntos." 52,8→54,8
- Subline Areia Teil A "Disciplinas com o mesmo nome nos dois." 54,8→57,6, dann Crossfade zu Teil B "Preço na hora, Pix e PDF assinado por e-mail." 57,6→61,6
- Bild: Handy 500×760 (x 400–900, y 720–1480, Rahmen Dunkel, Bildschirm Areia, traduzme-Oberfläche); Lucas Halbfigur 560 px links auf Areia-Scheibe. 53,2 beide Datei-Chips (44 px) fliegen gleichzeitig rein + Häkchen; 55,2 im Handy kurz zwei Disciplinas-Zeilen mit gleichem Namen markiert (Deko); 58,0 Preis-Karte "●●●" 72 px; 58,8 Pix-Knopf gedrückt; 59,6 "Pago ✓" Ø200; 60,6 Mail-Symbol mit PDF + Siegel. Halten bis 62,4.
→ 62,4–62,9 "Pago ✓"-Kreis wächst als Kreis-Wipe zu Areia.
S8 Checkliste + Finish 62,4–76,8 (Areia, Himmel aus Névoa-Formen)
- Headline 88 px Dunkel "Checklist do Lucas:" 63,0→64,6
- Kopfzeile (Pinho-Fläche, Text 48 px/800 Areia, Linie darunter) "Tradutor juramentado" 64,6→66,2, darunter die 4 nummerierten Punkte (eine Spalte, Zeilen 72 px hoch, Abstand 14, Ziffer-Kreis Pinho + Text 48 px Dunkel, x 90–700, y 820–1180), je 1,6 s: "1 Exigência do destino" 66,2 · "2 Todas as páginas" 67,8 · "3 PDF da faculdade" 69,4 · "4 Os dois juntos" 71,0→72,6. Rechts (x 700–930) offener Koffer, bei jedem Häkchen springt ein kleines Dokument hinein.
- 72,6–73,2 Koffer klappt zu, Liste blendet aus; 73,2–74,2 Lucas Ganzkörper mit Koffer geht nach rechts, Flugzeug 360 px bei y 760 mit Sálvia-Kondensstreifen; Headline wechselt zu "Lucas embarcou. Agora é você." 73,8→76,2. Halten bis 76,8.
→ 76,8–77,3 Flugzeug zieht Pinho-Banner-Wipe übers Bild.
S9 Endcard 76,8–83,8 (Pinho), linksbündig x 90
- Elemente 77,3–78,3 nacheinander, dann ruhig 78,3–82,8 (4,5 s) + Ausklang 82,8–83,8.
- Kicker 48 px Areia "Tradução juramentada" (y 300–356) + Headline 80 px Weiß "Preço na hora no site." (y 380–553); Pill "traduzme.com.br" 640×132 Areia, 66 px/800 Dunkel (y 620–752); WHATSAPP-Label 32 px Sálvia + Nummer (61) 99803-8363 60 px/700 Weiß (y 820–930).
- Lucas klein (380 px) winkt rechts unten (x 680–930, y 1120–1480), Winken alle 2 s, nichts bewegt sich über den Kontaktdaten.
Gesamtlänge 83,8 s.

## Sound
112 BPM treibend (Kick jeder Schlag, Clap 2+4, Hats, Offbeat-Bass, Marimba-Motiv), Pop beim Hook, Mail-Ping, Plattenkratzer + 0,6 s Stille bei S3, Lupen-Whoosh, Ding je Blattzahl und je Checklisten-Häkchen, Stift-Strich beim Durchstreichen, Pix-Klick + Erfolgs-Ding, Koffer-Klack, Flugzeug-Whoosh, Ausklang. -11 dB RMS.

## Texte/Plattformen (nach Bau, Text-Prüfer)
TikTok ~10–12 Uhr locker; IG ~11 Uhr; YT ~16 Uhr Titel "Tradução juramentada de diploma e histórico: 4 cuidados antes de pedir", EDUCATION; LinkedIn 11 Uhr sachlich (Mobilidade internacional: o que conferir antes de traduzir diploma e histórico).

## v3.2 Bau-Korrekturen (Design R3, gemessen; Tempo R3; Inhalt R3 bestanden) – verbindlich, gehen vor den Szenenangaben oben
1. S3 Zeile 3 = "Só com tradutor juramentado." (einzeilig) 19,3→21,3.
2. S4 Subline per Crossfade: A "A WES pede tradução completa, palavra por palavra." 25,6→29,2 → B "Incompleta é recusada." 29,2→30,8; Augen-Gag 30,8–31,8; S4 endet 31,8 (alles danach +0,2 s, Endcard-Ende 84,0).
3. S6 Subline per Crossfade: A "Impresso perde a validade." 46,6→48,6 → B "A tradução leva o código de validação." 48,6→51,4 (Zeiten inkl. +0,2); Code-Chip landet auf 0,6.
4. Badge einheitlich in der Kopfleiste: Ø110, Ziffer 64 px, x 90, y 225–335; 4 Punkte rechtsbündig an x 930; Headlines volle Breite 840.
5. S7 Handy beginnt y 740 (500×740).
6. S8 Headline "Checklist do Lucas" (ohne Doppelpunkt, einzeilig y 340–435), Liste y 480–896; Bühne: Lucas Halbfigur 540 px (x 60–400) packt in offenen Koffer 420×300 (x 460–900, y 1180–1480); je Häkchen fliegt ein Mini-Dokument in den Koffer.
7. S9 Stapel mittig: Kicker y 470–526, Headline y 540–713, Pill y 790–922, WhatsApp y 990–1100; Lucas x 680–930, y 1100–1480.
Status: Inhalt bestanden (R3), Tempo bestanden mit Korrekturen (R3), Design bestanden mit diesen Korrekturen (R3). Prüfschleife Plan ok, 3 Runden.
