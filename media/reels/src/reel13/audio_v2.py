import sys; sys.path.insert(0,'/home/user/traduzme/media/reels/lib'); from music import Track
STYLE=sys.argv[1] if len(sys.argv)>1 else 'funk'; OUT=sys.argv[2] if len(sys.argv)>2 else '/tmp/claude-0/r13m/audio.wav'
ST={'s1':0,'f1':5.8,'f2':17.3,'f3':26.4,'f4':36.3,'s6':46.0,'s7':52.3}; END=59.3
Q={1:dict(cd=[5.9,6.5,7.1],res=7.7,hit=False,pills=[4.1,4.5,4.9]),2:dict(cd=[3.9,4.5,5.1],res=5.7,hit=False,pills=None),
   3:dict(cd=[4.7,5.3,5.9],res=6.5,hit=True,pills=None),4:dict(cd=[4.3,4.8,5.3],res=5.8,hit=False,pills=None)}
tr=Track(style=STYLE,dur=END,key='D',seed=13)
tr.section(0,'intro'); tr.section(0.8,'main')
for n,q in Q.items():
    s0=ST['f%d'%n]; tr.section(s0+q['cd'][0]-.2,'soft'); T=s0+q['res']+.05; tr.section(T,'main'); tr.hit(T)
tr.section(ST['s6'],'soft'); tr.section(ST['s6']+.6,'main'); tr.hit(ST['s6']+.75); tr.section(ST['s7']+5.6,'outro')
sf=tr.sfx
sf('pop',0.0,.5,f=700)
for k,s0 in ST.items():
    if s0>0: sf('whoosh',s0-.05,.45,d=.6)
for n,q in Q.items():
    s0=ST['f%d'%n]
    if q['pills']:
        for i,a in enumerate(q['pills']): sf('pop',s0+a,.45,f=700+80*i)
    for i,a in enumerate(q['cd']): tr.ev['drums'].append((s0+a,76,64+6*i,.1))   # Woodblock, ohne Humanisierung
    T=s0+q['res']+.05
    if q['hit']:
        for j,n in enumerate(tr.voicing(tr.chord_notes(int(T//(4*tr.B)))[1])): tr.add('chord',T+j*.04,n+12,80,1.0)   # 'richtig' = Arpeggio im laufenden Akkord
    else: sf('boing',T,.8)
    tr.duck(s0+q['cd'][0]-.2,q['res']-q['cd'][0]+.8,.6)
sf('pop',ST['s6']+.6,.5,f=700)
print(STYLE,'LUFS',tr.write(OUT,fade=(END-1.2,END-.2)))
