import sys; sys.path.insert(0,'/home/user/traduzme/media/reels/lib'); from music import Track
OUT=sys.argv[1] if len(sys.argv)>1 else '/tmp/claude-0/r14/audio.wav'
ST={'s1':0,'s2':4.4,'e1':8.0,'e2':15.8,'e2b':23.6,'e3':28.0,'e4':34.4,'bon':41.2,'rec':45.8,'end':50.6}; END=57.8
tr=Track(style='lofi',dur=END,key='F',seed=14)
tr.section(0,'soft'); tr.section(4.4,'main'); tr.section(ST['bon'],'soft'); tr.section(ST['rec'],'main'); tr.section(ST['end']+1.5,'outro')
for k in ('e1','e4','rec'): tr.hit(ST[k]+.25)
sf=tr.sfx; ev=tr.ev
ev['drums'].append((0.33,75,70,.1))                                   # Klick auf "Pagar" (Claves, weich)
for i in range(3): ev['drums'].append((.8+i*.3,76,52,.1))             # Fragezeichen
for k in ('s2','e1','e2','e2b','e3','e4','bon','rec','end'): sf('whoosh',ST[k]-.05,.35,d=.5)
def chime(t):   # Häkchen = Akkordtöne aus dem laufenden Takt, eine Oktave höher
    root,ch=tr.chord_notes(int(t//(4*tr.B))); v=tr.voicing(ch)
    for j,n in enumerate(v[-2:]): ev['chord'].append((t+j*.05,n+12,74,.8))
for t in (ST['e1']+1.2,ST['e2b']+2.9,ST['e3']+4.7,ST['e4']+3.0): chime(t)
for i in range(4): ev['drums'].append((ST['rec']+.7+i*.4,76,58+4*i,.1))   # Recap-Häkchen
ev['drums'].append((ST['e1']+.3,75,55,.1))                              # Push
for i in range(3): ev['drums'].append((ST['e2']+1.0+i*.6,76,78,.1))     # Seiten zählen
ev['drums'].append((ST['e2']+3.3,77,66,.1))                             # +1 Seite
ev['drums'].append((ST['e2b']+1.9,75,64,.1)); sf('pop',ST['e2b']+2.6,.45,f=500)   # Auswahl, Siegel
for k in range(7): ev['drums'].append((ST['e3']+.6+k*.18,37,48,.05))    # Tippen (Side-Stick)
for i in range(1,4): ev['drums'].append((ST['e4']+3.45+i*.45,76,58,.1)) # Kalender-Häkchen
sf('pop',ST['bon']+3.1,.4,f=400)
print('LUFS',tr.write(OUT,fade=(END-1.0,END-.1)))
