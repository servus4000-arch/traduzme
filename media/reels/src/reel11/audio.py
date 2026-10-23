import numpy as np, wave
SR=44100; DUR=87.1; N=int(SR*DUR)
L=np.zeros(N); R=np.zeros(N)
rng=np.random.default_rng(7)
BPM=112; B=60/BPM
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


def scratch():
    n=int(.45*SR); t=np.arange(n)/SR; x=rng.standard_normal(n)
    f=np.abs(np.sin(2*np.pi*7*t))*1800+200; ph=2*np.pi*np.cumsum(f)/SR
    return (np.sin(ph)*.5+np.diff(x,prepend=0)*.4)*np.exp(-t*3)*.5
def boing():
    n=int(.5*SR); t=np.arange(n)/SR; f=220+180*np.sin(2*np.pi*9*t)*np.exp(-t*4)+t*200
    return np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-t*5)*.35
def crumple():
    n=int(.4*SR); x=rng.standard_normal(n); e=(rng.random(n)<.02)*1.0
    e=np.convolve(e,np.exp(-np.arange(400)/60),'same'); return np.diff(x,prepend=0)*e*.5
def marimba(f,g=.18):
    n=int(.45*SR); t=np.arange(n)/SR
    return (np.sin(2*np.pi*f*t)+.3*np.sin(2*np.pi*f*4*t)*np.exp(-t*30))*np.exp(-t*9)*g
prog=[(87.31,[349.2,440,523.3]),(98.0,[392,493.9,587.3]),(110.0,[440,523.3,659.3]),(65.41,[329.6,392,523.3])]
musicEnd=86.1
nbeats=int(DUR/B)
for b in range(nbeats):
    t=b*B
    if t>=musicEnd: break
    if 12.75<=t<13.45: continue   # Stille beim Wendepunkt
    bar=b//4; ch=prog[bar%4]
    soft = t<0.5
    add(kick(),t,.9)
    if b%2==1: add(clap(),t,.85)
    for k in range(2): add(hat(open_=(k==1)),t+k*B/2,.9,pan=.3 if k else -.3)
    for k in (1,3):
        if t>=6.2: add(hat(),t+k*B/4,.6,pan=-.2)
    add(bass(ch[0],B*.45),t+B/2,1.0)
    if b%4==0: add(chord(ch[1],B*4),t,1.0)
    if t>=6.2 and not (12.8<=t<22.0):
        mel=[ch[1][2]*2,ch[1][1]*2,ch[1][0]*2,ch[1][1]*2]
        if b%2==0: add(marimba(mel[(b//2)%4]),t+B*.5,1.0,pan=.25)
# SFX (Szenenstarts v3.2: s4 22.0, s5 32.7, s6 44.3, s7 53.7, s8 65.1, s9 80.1)
S4,S5,S6,S7,S8,S9=22.0,32.7,44.3,53.7,65.1,80.1
for x in (0.0,0.25,0.4,2.0): add(pop(800),x,.9)
for tb in (6.2,S4,S5,S6,S7,S8,S9): add(whoosh(.45),tb-.3,1.0)
add(ding(1760),7.0,.8); add(ding(2093),7.12,.6)
add(pop(1000),10.2,.9)
add(scratch(),12.75,1.2)
add(crumple(),13.3,1.0)
add(thud(),15.9,.6); add(thud(),16.2,.6)
for x in (13.7,15.7,19.3): add(pop(700),x,.7)
add(pop(800),S4+.8,.8); add(whoosh(.4),S4+3.6,.7); add(tick(),S4+4.2,1.0); add(boing(),S4+9.5,1.0)
add(pop(800),S5+.8,.8)
for i in range(5): add(ding(1046.5*(2**(i*2/12))),S5+1.0+i*.5,.9)
add(ding(1568),S5+3.6,.7); add(ding(1760),S5+5.0,.7); add(pop(900),S5+9.5,.7)
for i in range(5): add(tick(),S5+10.2+i*.22,1.2)
add(pop(800),S6+.8,.8); add(pop(600),S6+1.2,.7); add(crumple(),S6+5.0,.8); add(pop(900),S6+5.4,.7); add(whoosh(.6),S6+5.9,.8); add(ding(1568),S6+6.7,.9)
add(pop(800),S7+.8,.8); add(whoosh(.5),S7+1.2,.8); add(ding(1320),S7+2.2,.7); add(ding(1568),S7+2.4,.7); add(ding(1175),S7+3.2,.6)
add(pop(900),S7+6.7,.8); add(click(),S7+7.9,1.2); add(ding(1568),S7+8.3,1.0); add(ding(2093),S7+8.45,.9); add(pop(1000),S7+9.5,.8)
add(pop(800),S8+.6,.8)
for i,x in enumerate((2.2,3.8,5.4,7.0,8.6)): add(ding(1175+i*90),S8+x,.8); add(thud(),S8+x+1.1,.25)
add(thud(),S8+10.7,.6); add(click(),S8+10.75,1.0); add(whoosh(1.4),S8+10.8,1.0); add(pop(900),S8+13.8,.8); add(ding(1568),S8+14.0,.6)
for i in range(5): add(pop(900+80*i),S9+.5+i*.2,.5)
mix=np.stack([L,R],1)
fo=int(85.9*SR); fe=int(86.9*SR)
mix[fo:fe]*=np.linspace(1,0,fe-fo)[:,None]; mix[fe:]=0
mix=np.tanh(mix*1.6)
rms=np.sqrt(np.mean(mix[:fo]**2)); target=10**(-11/20)
mix*=min(target/rms, .89/np.abs(mix).max())
mix=np.clip(mix,-1,1)
with wave.open('/tmp/claude-0/r11/audio.wav','wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((mix*32767).astype('<i2').tobytes())
print('rms dB',20*np.log10(np.sqrt(np.mean(mix[:fo]**2))))
