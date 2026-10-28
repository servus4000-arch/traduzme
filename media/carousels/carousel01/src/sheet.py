from PIL import Image; import glob,sys
fs=sorted(glob.glob('out/slide_*.png')); w,h=360,450
sh=Image.new('RGB',(w*5+60,h*2+30),'#666')
for i,f in enumerate(fs):
    im=Image.open(f).convert('RGB').resize((w,h)); sh.paste(im,(10+(i%5)*(w+10),10+(i//5)*(h+10)))
sh.save('out/contact_sheet.png')
