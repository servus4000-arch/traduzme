import sys; sys.path.insert(0,'/home/user/traduzme/media/reels/lib'); from sound import *
S2,S3,S4,S5,S6,S7=5.4,17.0,28.6,40.2,47.8,58.8; END=65.8
P={S2:(3.4,5.0,5.8),S3:(3.8,4.6,5.2),S4:(3.4,4.4,5.0)}   # Blase gelesen, Stempel, Wechsel
song=Song(style='funk',dur=END,key='A',seed=12)
song.section(0,'intro'); song.section(1.0,'drop')
for s0,(rd,stp,sw) in P.items():
    song.section(s0+rd,'break'); song.section(s0+stp+.15,'drop')
song.section(S5,'drop'); song.section(S6,'break'); song.section(S6+2.0,'drop'); song.section(S7+5.6,'outro')
song.hits=[s0+stp+.15 for s0,(rd,stp,sw) in P.items()]
song.build()
for s0,(rd,stp,sw) in P.items():
    T=s0+stp+.15; song.put('kick',song.kick(1.3),T,1.0); song.kicks.append(T); song.put('bass',song.bass_note(song.root,song.B*1.5,'808'),T,1.0)
sf=song.sfx
for x in (0.1,0.25,0.4): sf('pop',x,.8,f=800)
sf('pop',1.2,.7,f=1000); sf('impact',3.5,.6); sf('pop',3.55,.8,f=700)
for s0 in (S2,S3,S4,S5,S6,S7): sf('whoosh',s0-.05,.9,d=.6)
for s0,(rd,stp,sw) in P.items():
    sf('pop',s0+.6,.8,f=900); sf('tick',s0+rd+.2,.8); sf('tick',s0+rd+.6,.8)
    sf('stamp',s0+stp+.15,1.1); sf('impact',s0+stp+.15,.7); song.duck(s0+rd,stp-rd+.15,.25)
    sf('whoosh',s0+sw,.7,d=.45); (sf('ding',s0+sw+.7,.7,f=1568) if s0!=S4 else None)
sf('crumple',S2+8.4,.8)
for i in range(8): sf('tick',S3+5.9+i*.3,.6)
sf('pop',S3+8.2,.7)
sf('whoosh',S4+5.5,.9,d=.6); sf('ding',S4+6.7,.8,f=1760); sf('whoosh',S4+7.6,.6,d=.4)
sf('pop',S5+.4,.7); sf('typing',S5+3.0,.7,d=.4); sf('pop',S5+3.4,.8); sf('pop',S5+3.7,.6,f=1200); sf('pop',S5+4.2,.8,f=1100); sf('click',S5+5.5,1.0); sf('cash',S5+5.8,1.0)
sf('whoosh',S6+1.7,.6,d=.5); sf('pop',S6+2.2,.8)
for x in (2.4,4.5,7.3): sf('ding',S6+x,.7,f=1318)
for i in range(3): sf('pop',S6+9.7+i*.2,.6,f=1000+120*i)
sf('correct',S6+10.0,.8)
for i in range(4): sf('pop',S7+.5+i*.2,.5,f=900+80*i)
print('rms',song.write('/tmp/claude-0/r12/audio.wav',fade=(END-1.2,END-.2)))
