import numpy as np, wave
SR=44100; DUR=39.5; N=int(SR*DUR)
L=np.zeros(N); R=np.zeros(N)
rng=np.random.default_rng(7)
BPM=120; B=60/BPM
def add(sig,t,gain=1.0,pan=0.0):
    i=int(t*SR);
    if i>=N: return
    s=sig[:N-i]*gain
    L[i:i+len(s)]+=s*(1-max(0,pan)); R[i:i+len(s)]+=s*(1+min(0,pan))
def env(n,a,d):
    e=np.ones(n); na=int(a*SR); e[:na]=np.linspace(0,1,na) if na>0 else 1
    e[na:]=np.exp(-np.arange(n-na)/(d*SR)); return e
def kick():
    n=int(.35*SR); t=np.arange(n)/SR
    f=48+110*np.exp(-t*28); ph=2*np.pi*np.cumsum(f)/SR
    return np.sin(ph)*np.exp(-t*7.5)*1.0
def clap():
    n=int(.25*SR); x=rng.standard_normal(n)
    e=np.zeros(n)
    for o in [0,.011,.022]:
        i=int(o*SR); e[i:]+=np.exp(-np.arange(n-i)/(SR*.03))
    # crude bandpass via diff
    y=np.diff(x,prepend=0)*e
    return y*.35
def hat(open_=False):
    n=int((.18 if open_ else .05)*SR); x=rng.standard_normal(n)
    y=np.diff(np.diff(x,prepend=0),prepend=0)
    return y*np.exp(-np.arange(n)/(SR*(.05 if open_ else .012)))*.06
def bass(freq,dur):
    n=int(dur*SR); t=np.arange(n)/SR
    s=np.sin(2*np.pi*freq*t)+.35*np.sign(np.sin(2*np.pi*freq*t))*.5
    return s*env(n,.004,.12)*.42
def pluck(freq,dur=.3,g=.16):
    n=int(dur*SR); t=np.arange(n)/SR
    s=np.sin(2*np.pi*freq*t)+.5*np.sin(4*np.pi*freq*t)+.2*np.sin(6*np.pi*freq*t)
    return s*env(n,.002,.09)*g
def chord(freqs,dur):
    n=int(dur*SR); t=np.arange(n)/SR; s=np.zeros(n)
    for f in freqs:
        for dt in (-.6,.6): s+=np.sin(2*np.pi*f*(1+dt/1200*10)*t)
    return s*env(n,.01,.18)*.035
def pop(f=900):
    n=int(.09*SR); t=np.arange(n)/SR
    return np.sin(2*np.pi*(f+f*1.5*np.exp(-t*60))*t)*np.exp(-t*45)*.35
def click():
    n=int(.03*SR); x=rng.standard_normal(n); return np.diff(x,prepend=0)*np.exp(-np.arange(n)/(SR*.004))*.35
def tick():
    n=int(.04*SR); t=np.arange(n)/SR; return np.sin(2*np.pi*2400*t)*np.exp(-t*120)*.18
def ding(f=1320):
    n=int(.5*SR); t=np.arange(n)/SR
    return (np.sin(2*np.pi*f*t)+.4*np.sin(2*np.pi*f*2.01*t))*np.exp(-t*7)*.16
def whoosh(d=.45):
    n=int(d*SR); x=rng.standard_normal(n);
    # moving lowpass via cumulative smoothing
    y=np.zeros(n); a=0;
    k=np.linspace(.02,.5,n)**1.5
    for i in range(n): a+= k[i]*(x[i]-a); y[i]=a
    e=np.sin(np.linspace(0,np.pi,n))**2
    return y*e*.5
def thud():
    n=int(.4*SR); t=np.arange(n)/SR
    return (np.sin(2*np.pi*(60+80*np.exp(-t*20))*t)*np.exp(-t*9)+rng.standard_normal(n)*np.exp(-t*40)*.3)*.8
def impact():
    return thud()*1.1

# progression (A minor-ish bright): F C G Am -> roots
prog=[(87.31,[349.2,440,523.3]),(65.41,[329.6,392,523.3]),(98.0,[392,493.9,587.3]),(110.0,[440,523.3,659.3])]
musicEnd=38.6
nbeats=int(DUR/B)
for b in range(nbeats):
    t=b*B
    if t>=musicEnd: break
    bar=b//4; ch=prog[bar%4]
    intro = t<1.0
    if not intro: add(kick(),t,1.0)
    if b%2==1 and t>=2.0: add(clap(),t,1.0)
    for k in range(2):
        tt=t+k*B/2
        if t>=1.0: add(hat(open_=(k==1)),tt,1.0, pan=.3 if k else -.3)
    for k in (1,3):
        if t>=4.0: add(hat(),t+k*B/4,.7,pan=-.2)
    # offbeat bass
    if t>=1.0: add(bass(ch[0],B*.45),t+B/2,1.0)
    if b%4==0 and t>=0: add(chord(ch[1],B*4),t,1.0)
    # pluck motif in sections s3..s5 and s6
    if 10.0<=t<28.5 or 28.5<=t<32:
        mel=[ch[1][2],ch[1][1],ch[1][2]*1.5/1.5,ch[1][0]*2]
        add(pluck(mel[b%4]*1.0),t+B*.75,.9,pan=.25)

# SFX
for i in range(14): add(tick(),0.5+i*0.1,.8)      # hook scramble
add(pop(700),2.0,1.0)
add(whoosh(.7),3.2,1.0)
for i in range(10): add(tick(),4.2+i*0.11,.7)
for x in (5.4,5.85,6.3): add(pop(1000),x,.9)
add(thud(),7.6,1.0)
for tb in (10.0,16.5,21.5,28.5,32.0): add(whoosh(.45),tb-.35,1.0)
W0,WD=11.3,0.65
for i in range(8): add(click(),W0+i*WD,1.0); add(pop(1200),W0+i*WD+.02,.5)
add(pop(800),17.0,1.0)
for i in range(5): add(ding(1175 if i%2 else 1320),17.7+i*.5,1.0)
for i in range(4): add(ding(1568),22.75+i*1.25+.25,.8); add(pop(900),22.5+i*1.25,.6)
for i in range(7): add(pop(1100 if i%2 else 850),28.75+i*0.5,.8)
add(impact(),32.0,1.0)

mix=np.stack([L,R],1)
# fade out tail
fo=int(38.4*SR); fe=int(39.4*SR)
mix[fo:fe]*=np.linspace(1,0,fe-fo)[:,None]; mix[fe:]=0
# soft clip + loudness
mix=np.tanh(mix*1.6)
rms=np.sqrt(np.mean(mix[:fo]**2)); target=10**(-11/20)
mix*=min(target/rms, .98/np.abs(mix).max())
mix=np.clip(mix,-1,1)
with wave.open('/tmp/claude-0/r09/audio.wav','wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((mix*32767).astype('<i2').tobytes())
print('rms dB',20*np.log10(np.sqrt(np.mean(mix**2))))
