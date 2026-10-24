import sys; sys.path.insert(0,'/home/user/traduzme/media/reels/lib'); from sound import *
ST={'s1':0,'f1':5.8,'f2':17.3,'f3':26.4,'f4':36.3,'s6':46.0,'s7':52.3}; END=59.3
Q={1:dict(cd=[5.9,6.5,7.1],res=7.7,rs=8.2,hit=False,pills=[4.1,4.5,4.9]),2:dict(cd=[3.9,4.5,5.1],res=5.7,rs=6.2,hit=False,pills=None),
   3:dict(cd=[4.7,5.3,5.9],res=6.5,rs=7.0,hit=True,pills=None),4:dict(cd=[4.3,4.8,5.3],res=5.8,rs=6.4,hit=False,pills=None)}
song=Song(style='phonk',dur=END,key='E',seed=13)
song.section(0,'intro'); song.section(0.8,'drop')
hits=[]
for n,q in Q.items():
    s0=ST['f%d'%n]; song.section(s0+q['cd'][0],'break'); T=s0+q['res']+.15; song.section(T,'drop'); hits.append(T)
song.section(ST['s6'],'break'); song.section(ST['s6']+.6,'drop'); song.section(ST['s7']+5.6,'outro')
hits.append(ST['s6']+.75)
song.hits=hits
song.build()
for T in hits:
    song.put('kick',song.kick(1.3),T,1.0); song.kicks.append(T); song.put('bass',song.bass_note(song.root,song.B*1.5,'808'),T,1.0)
sf=song.sfx
# Hook
sf('pop',0.0,.7,f=900); sf('pop',.15,.8,f=700); sf('buzz',.8,.9); sf('buzz',3.0,.8)
for k,s0 in ST.items():
    if s0>0: sf('whoosh',s0-.05,.9,d=.6)
for n,q in Q.items():
    s0=ST['f%d'%n]
    sf('pop',s0+.2,.7,f=800)
    if q['pills']:
        for i,a in enumerate(q['pills']): sf('pop',s0+a,.7,f=900+150*i)
    else:
        for i in range(3): sf('pop',s0+.35+i*.08,.5,f=900+150*i)
    for i,a in enumerate(q['cd']): sf('tick',s0+a,.8+.2*i)
    sf('buzz',s0+q['cd'][0],.8); sf('pop',s0+q['cd'][0]+.3,.6,f=1200)
    T=s0+q['res']+.15; sf('impact',T,.8)
    sf('correct' if q['hit'] else 'boing',T+.05,.8)
    sf('ding',s0+q['res']+.05,.6,f=1568)
    if q['hit']: sf('pop',s0+q['res']+.3,.8,f=1300); sf('riser',s0+q['res']-.6,.4,d=.6)
    song.duck(s0+q['cd'][0],q['res']-q['cd'][0]+.15,.3)
sf('pop',ST['s6']+.6,.8); sf('impact',ST['s6']+.75,.5)
for i in range(4): sf('pop',ST['s7']+.5+i*.2,.5,f=900+80*i)
print('rms',song.write('/tmp/claude-0/r13/audio.wav',fade=(END-1.2,END-.2)))
