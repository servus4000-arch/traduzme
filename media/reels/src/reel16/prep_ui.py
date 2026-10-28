# Bereitet die echten Rechner-Screenshots (capture_ui.js) fürs Reel vor:
#  ui_form_de.png : Schritt 1 (DE-Oberfläche), unten vor der Hinweiszeile zur automatischen Einordnung abgeschnitten (nicht im Bild),
#                   Sprachumschalter bis auf den aktiven DE-Knopf abgedeckt (keine Sprachliste im Bild).
#  ui_dados_de.png: Schritt "Daten" (DE), Zusammenfassung mit Lieferdatum unscharf (kein Datum/keine Mengenangabe lesbar).
from PIL import Image, ImageDraw, ImageFilter
a=Image.open('shots/de_1_full.png').convert('RGB')
bg=a.getpixel((20,300)); print('page bg',bg)
a=a.crop((0,0,1170,2485)); g=ImageDraw.Draw(a)
g.rectangle([575,30,1140,158],fill=bg)                     # ganzer Umschalter weg …
g.rounded_rectangle([826,42,935,146],radius=26,fill=(232,243,238))   # … dezenter Rahmen nur um DE
b=Image.open('shots/de_1_full.png').convert('RGB').crop((840,51,922,139)); a.paste(b,(840,51))  # echter DE-Knopf
a.save('ui_form_de.png')
d=Image.open('shots/de_3_full.png').convert('RGB').crop((0,860,1170,1800))
box=(93,1105-860,1066,1224-860); r=d.filter(ImageFilter.GaussianBlur(16)).crop(box)
m=Image.new('L',r.size,0); ImageDraw.Draw(m).rounded_rectangle([0,0,r.size[0]-1,r.size[1]-1],radius=28,fill=255); d.paste(r,box[:2],m)
d.save('ui_dados_de.png'); print(a.size,d.size)
