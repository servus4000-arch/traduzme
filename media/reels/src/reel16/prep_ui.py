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

# --- Abnahme 16-4/16-10: statt Handy-Zoom drei Ausschnitt-Karten (ganz in x 90–900, keine Dynamic Island) ---
f=Image.open('ui_form_de.png').convert('RGB')
f.crop((90,1572,790,1925)).save('ui_card_files.png')                      # nur die zwei Datei-Zeilen, groß (rechts angeschnitten, in der Karte ausgeblendet)
bgc=f.getpixel((20,250))
top=f.crop((30,30,1140,165)); tit=f.crop((30,305,1140,415))                # Logo + DE-Knopf, Titel (ohne Satz „geschätzten Preis")
h=Image.new('RGB',(1110,top.size[1]+20+tit.size[1]),bgc); h.paste(top,(0,0)); h.paste(tit,(0,top.size[1]+20)); h.save('ui_card_head.png')
dd=Image.open('ui_dados_de.png').convert('RGB'); bgd=dd.getpixel((60,600))
a1=dd.crop((85,135,800,220)); a2=dd.crop((85,610,925,730))
c=Image.new('RGB',(840,a1.size[1]+30+a2.size[1]),bgd); c.paste(a1,(0,0)); c.paste(a2,(0,a1.size[1]+30)); c.save('ui_card_cpf.png')
print('cards', Image.open('ui_card_files.png').size, h.size, c.size, bgc, bgd)
