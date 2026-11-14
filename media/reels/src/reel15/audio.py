import sys; sys.path.insert(0,'/home/user/traduzme/media/reels/lib'); from music import Track
OUT=sys.argv[1] if len(sys.argv)>1 else '/tmp/claude-0/r15/audio.wav'
ST={'s1':0,'s2':3.8,'e1':8.4,'e2':14.2,'e3':18.2,'e4':23.6,'e5':30.0,'rec':34.6,'end':39.2}; END=45.0
STOP=ST['e4']+.8
tr=Track(style='pop',dur=END,key='A',seed=15,bpm=120)
tr.section(0,'soft'); tr.section(ST['s2'],'main'); tr.section(STOP,'break'); tr.section(ST['e4']+1.3,'main'); tr.section(44.0,'outro')
for t in (ST['e1']+.05,ST['e4']+1.3,ST['rec']+.05): tr.hit(t)
sf=tr.sfx; ev=tr.ev
for k in range(8): ev['drums'].append((.25+k*.5,37,50,.05))            # Uhr-Ticks (Side-Stick), nur im Hook
ev['drums'].append((.3,75,72,.1))                                        # Knopf der Stoppuhr
for k in ('s2','e1','e2','e3','e4','e5','rec','end'): sf('whoosh',ST[k]-.05,.32,d=.5)
sf('scratch',ST['s2']+1.75,.45); tr.duck(ST['s2']+1.7,.4,.7)                                            # Kratzer-Stop
ev['drums'].append((ST['s2']+2.4,77,70,.1))                             # Laptop zu
sf('pop',ST['e1']+1.45,.7,f=600)                                        # Upload
ev['drums'].append((ST['e1']+3.8,75,56,.1))                              # Chip valor certo
ev['drums'].append((ST['e2']+1.2,75,68,.1))                              # Tap Inglês
sf('riser',ST['e3']+.2,.22,d=1.0)                                        # Analyse
for i in range(3): ev['drums'].append((ST['e3']+1.55+i*.3,76,50+4*i,.1)) # frente/verso/apostila
ev['drums'].append((STOP,75,80,.1)); sf('click',STOP,.4)                 # STOPP
ev['drums'].append((ST['e5']+.9,75,66,.1))                               # Tap Pix
root,ch=tr.chord_notes(int((ST['e5']+1.4)//(4*tr.B))); v=tr.voicing(ch)
for j,n in enumerate(v[-2:]): ev['chord'].append((ST['e5']+1.4+j*.04,n+12,72,.8))   # Pagamento confirmado
for i in range(4): ev['drums'].append((ST['rec']+.4+i*.7,76,56+4*i,.1))  # Recap-Haken
print('LUFS',tr.write(OUT,lufs=-14.2,fade=(END-1.0,END-.1)))
