import numpy as np, wave
SR=44100; DUR=29.0; N=int(SR*DUR)
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

# progression
prog=[(87.31,[349.2,440,523.3]),(65.41,[329.6,392,523.3]),(98.0,[392,493.9,587.3]),(110.0,[440,523.3,659.3])]
musicEnd=28.4
nbeats=int(DUR/B)
for b in range(nbeats):
    t=b*B
    if t>=musicEnd: break
    bar=b//4; ch=prog[bar%4]
    brk = 8.9<=t<9.6   # Pause vor dem Stempel
    if brk: continue
    if t>=0.0: add(kick(),t,1.0)
    if b%2==1 and t>=1.0: add(clap(),t,1.0)
    for k in range(2):
        if t>=0.5: add(hat(open_=(k==1)),t+k*B/2,1.0,pan=.3 if k else -.3)
    for k in (1,3):
        if t>=3.2: add(hat(),t+k*B/4,.7,pan=-.2)
    add(bass(ch[0],B*.45),t+B/2,1.0)
    if b%4==0: add(chord(ch[1],B*4),t,1.0)
    if 12.8<=t<23.8:
        mel=[ch[1][2],ch[1][1],ch[1][2],ch[1][0]*2]
        add(pluck(mel[b%4]),t+B*.75,.9,pan=.25)

# SFX
for x in (0.1,0.9,1.6,2.3): add(pop(800),x,1.0)
for tb in (3.2,9.0,12.8,20.4,23.8): add(whoosh(.45),tb-.35,1.0)
for i in range(15): add(tick(),4.2+i*0.107,.8)
for i in range(6): add(pluck(1046.5*(1.122**(i%3)),.4,.22),6.1+i*.18,1.0,pan=(-.4 if i%2 else .4))
add(pop(600),6.85,.9); add(pop(600),7.25,.9)
add(thud(),9.6,1.2); add(impact(),9.62,1.0)
add(pop(900),9.85,.7)
add(pop(800),13.0,.8)
for i in range(3): add(ding(1320 if i!=1 else 1175),14.3+i*1.4,1.0)
add(click(),21.7,1.0); add(pop(1200),21.72,.6)
add(ding(1568),22.4,1.0)
for i in range(5): add(pop(900+80*i),23.85+i*.08,.5)

mix=np.stack([L,R],1)
fo=int(27.9*SR); fe=int(28.9*SR)
mix[fo:fe]*=np.linspace(1,0,fe-fo)[:,None]; mix[fe:]=0
mix=np.tanh(mix*1.6)
rms=np.sqrt(np.mean(mix[:fo]**2)); target=10**(-11/20)
mix*=min(target/rms, .98/np.abs(mix).max())
mix=np.clip(mix,-1,1)
with wave.open('/tmp/claude-0/r10/audio.wav','wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((mix*32767).astype('<i2').tobytes())
print('rms dB',20*np.log10(np.sqrt(np.mean(mix**2))))
