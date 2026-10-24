"""traduzme Reel-Sound-Baukasten (Ben 24.10.2026: "Sounds deutlich besser").
Nutzung:
    import sys; sys.path.insert(0,'/home/user/traduzme/media/reels/lib'); from sound import *
    S = Song(style='funk', dur=45.0, key='A', seed=3)
    S.section(0,'intro'); S.section(1.0,'drop'); S.section(12.8,'break'); S.section(14.0,'drop'); S.section(41,'outro')
    S.build()                      # Musik
    S.sfx('whoosh',6.2); S.sfx('pop',7.0) ...   # Effekte synchron zu Animationen
    S.write('/tmp/x/audio.wav')    # Master: Sidechain, Hall, Lautheit -11 dB RMS, Fade am Ende
Stile: funk (Funk carioca/Tamborzão 130), pophouse (122), lofi (88, Swing), phonk (140, Cowbell, light), afro (108).
Benötigt numpy + scipy (pip install scipy, falls fehlt).
"""
import numpy as np, wave
from scipy.signal import fftconvolve, butter, sosfilt

SR = 44100
NOTE = {'C':0,'C#':1,'D':2,'D#':3,'E':4,'F':5,'F#':6,'G':7,'G#':8,'A':9,'A#':10,'B':11}
def hz(m): return 440.0*2**((m-69)/12)

STYLES = {
 'funk':     dict(bpm=130, swing=0.0, prog=[0,0,-4,-2], minor=True,  drums='tamborzao', bass='808',  lead='pluck', pad=True),
 'pophouse': dict(bpm=122, swing=0.0, prog=[0,-4,-2,3], minor=True,  drums='house',     bass='saw',  lead='pluck', pad=True),
 'lofi':     dict(bpm=88,  swing=0.12,prog=[0,5,-2,3],  minor=False, drums='boom',      bass='sub',  lead='keys',  pad=True),
 'phonk':    dict(bpm=140, swing=0.0, prog=[0,0,-4,-5], minor=True,  drums='phonk',     bass='808',  lead='bell',  pad=False),
 'afro':     dict(bpm=108, swing=0.06,prog=[0,-4,-2,-5],minor=True,  drums='afro',      bass='sub',  lead='marimba',pad=True),
}

class Song:
    def __init__(s, style='pophouse', dur=40.0, key='A', seed=1, bpm=None):
        s.st = dict(STYLES[style]); s.style = style
        if bpm: s.st['bpm'] = bpm
        s.dur = dur; s.N = int(SR*dur); s.rng = np.random.default_rng(seed)
        s.root = 45 + NOTE[key]          # A2 = 45
        s.B = 60.0/s.st['bpm']
        s.bus = {k: np.zeros((s.N,2)) for k in ('kick','drums','bass','music','lead','sfx')}
        s.sections = []; s.kicks = []
    # ---------- helpers ----------
    def section(s, t, kind): s.sections.append((t,kind)); s.sections.sort()
    def kind_at(s, t):
        k='drop'
        for (a,kk) in s.sections:
            if t+s.B*.5>=a: k=kk
        return k
    def put(s, bus, sig, t, g=1.0, pan=0.0):
        if bus in ('kick','bass') and any(-.06<t-h<.25 and abs(t-h)>1e-6 for h in getattr(s,'hits',())): return
        i = int(t*SR)
        if i >= s.N or i < 0: return
        x = sig[:s.N-i]*g
        if x.ndim == 1:
            l = x*np.sqrt(0.5*(1-pan)); r = x*np.sqrt(0.5*(1+pan)); x = np.stack([l,r],1)*1.414
        s.bus[bus][i:i+len(x)] += x
    def env(s, n, a=0.003, d=0.2, sus=0.0):
        e = np.ones(n); na = max(1,int(a*SR)); e[:na] = np.linspace(0,1,na)
        e[na:] = sus + (1-sus)*np.exp(-np.arange(n-na)/(d*SR)); return e
    def lp(s, x, fc, order=2):
        sos = butter(order, min(fc, SR*0.45), 'low', fs=SR, output='sos'); return sosfilt(sos, x, axis=0)
    def hp(s, x, fc, order=2):
        sos = butter(order, fc, 'high', fs=SR, output='sos'); return sosfilt(sos, x, axis=0)
    def bp(s, x, lo, hi):
        sos = butter(2, [lo, hi], 'band', fs=SR, output='sos'); return sosfilt(sos, x, axis=0)
    def saw(s, f, n, detune=0.0):
        t = np.arange(n)/SR; ph = (f*(1+detune)*t + s.rng.random()) % 1.0
        return 2*ph-1
    # ---------- instruments ----------
    def kick(s, hard=1.0):
        n=int(.42*SR); t=np.arange(n)/SR
        f=45+140*np.exp(-t*30)*hard; ph=2*np.pi*np.cumsum(f)/SR
        body=np.sin(ph)*np.exp(-t*6.5); click=s.hp(s.rng.standard_normal(n)*np.exp(-t*400),1500)*.25
        return np.tanh((body+click)*1.6)*.95
    def snare(s):
        n=int(.3*SR); t=np.arange(n)/SR
        tone=np.sin(2*np.pi*190*t)*np.exp(-t*25)*.5
        nz=s.bp(s.rng.standard_normal(n),1200,8000)*np.exp(-t*16)*.7
        return tone+nz
    def clap(s):
        n=int(.3*SR); e=np.zeros(n)
        for o in (0,.009,.019,.03):
            i=int(o*SR); e[i:]+=np.exp(-np.arange(n-i)/(SR*(.012 if o<.03 else .09)))
        return s.bp(s.rng.standard_normal(n),900,6000)*e*.55
    def hat(s, op=False):
        n=int((.22 if op else .05)*SR); t=np.arange(n)/SR
        x=s.hp(s.rng.standard_normal(n),7000,4)
        return x*np.exp(-t*(14 if op else 90))*.28
    def rim(s):
        n=int(.06*SR); t=np.arange(n)/SR
        return (np.sin(2*np.pi*1700*t)+.6*np.sin(2*np.pi*820*t))*np.exp(-t*80)*.35
    def conga(s, f=220):
        n=int(.25*SR); t=np.arange(n)/SR; ff=f*(1+.5*np.exp(-t*60))
        return np.sin(2*np.pi*np.cumsum(ff)/SR)*np.exp(-t*14)*.5
    def cowbell(s, f=560):
        n=int(.3*SR); t=np.arange(n)/SR
        x=np.sign(np.sin(2*np.pi*f*t))+np.sign(np.sin(2*np.pi*f*1.48*t))
        return s.bp(x,500,4000)*np.exp(-t*9)*.18
    def shaker(s):
        n=int(.07*SR); t=np.arange(n)/SR
        return s.hp(s.rng.standard_normal(n),5000)*np.sin(np.pi*t/t[-1])*.12
    def bass_note(s, m, dur, kind):
        n=int(dur*SR); t=np.arange(n)/SR; f=hz(m)
        if kind=='808':
            ff=f*(1+.6*np.exp(-t*40)); x=np.sin(2*np.pi*np.cumsum(ff)/SR)
            x=np.tanh(x*4.0)*s.env(n,.002,dur*1.2,.0)
        elif kind=='saw':
            x=s.saw(f,n)+s.saw(f,n,.004); ev=np.exp(-t*12); x=(s.lp(x,1300)*ev+s.lp(x,320)*(1-ev))*.6 + np.sin(2*np.pi*f*t)*.7
            x=x*s.env(n,.004,.18,.35)
        else:
            x=np.sin(2*np.pi*f*t)+.15*np.sin(4*np.pi*f*t); x=x*s.env(n,.01,.4,.5)
        rel=min(n,int(.02*SR)); x[-rel:]*=np.linspace(1,0,rel)
        return x*.55
    def chord_pad(s, ms, dur):
        n=int(dur*SR); out=np.zeros(n)
        for m in ms:
            f=hz(m)
            for d in (-.006,0,.006): out+=s.saw(f,n,d)
        out=s.lp(out,1400)*s.env(n,.25,dur*2,.8)
        rel=min(n,int(.15*SR)); out[-rel:]*=np.linspace(1,0,rel)
        return out*.035
    def stab(s, ms, dur=.22):
        n=int(dur*SR); t=np.arange(n)/SR; out=np.zeros(n)
        for m in ms:
            for d in (-.004,.004): out+=s.saw(hz(m),n,d)
        ev=np.exp(-t*6); return (s.lp(out,2800)*ev+s.lp(out,400)*(1-ev))*np.exp(-t*9)*.06
    def pluck(s, m, dur=.35):           # Karplus-Strong
        f=hz(m); n=int(dur*SR); p=max(2,int(SR/f))
        buf=s.rng.uniform(-1,1,p); out=np.zeros(n)
        for i in range(n):
            out[i]=buf[i%p]; buf[i%p]=.5*(buf[i%p]+buf[(i+1)%p])*.996
        return s.lp(out,5000)*.45
    def keys(s, m, dur=.5):
        n=int(dur*SR); t=np.arange(n)/SR; f=hz(m)
        x=np.sin(2*np.pi*f*t+.8*np.sin(2*np.pi*f*t)*np.exp(-t*6))
        return x*np.exp(-t*4)*.22
    def bell(s, m, dur=.6):
        n=int(dur*SR); t=np.arange(n)/SR; f=hz(m)
        x=np.sin(2*np.pi*f*t+1.3*np.sin(2*np.pi*f*3.5*t)*np.exp(-t*8))
        return x*np.exp(-t*5)*.10
    def marimba(s, m, dur=.4):
        n=int(dur*SR); t=np.arange(n)/SR; f=hz(m)
        return (np.sin(2*np.pi*f*t)+.3*np.sin(2*np.pi*f*4*t)*np.exp(-t*30))*np.exp(-t*9)*.3
    # ---------- arrangement ----------
    def scale(s):
        return [0,2,3,5,7,8,10] if s.st['minor'] else [0,2,4,5,7,9,11]
    def chord(s, deg_root):
        r=s.root+12+deg_root; third=3 if s.st['minor'] and deg_root in (0,5,7,-4,-5) else 4
        if deg_root in (-2,3,-9): third=4
        return [r, r+third, r+7, r+12]
    def build(s, hook=None):
        st=s.st; B=s.B; nb=int(s.dur/B)+1
        # hook melody: 2 bars, scale degrees (index in scale, octave offset)
        sc=s.scale()
        hook = hook or [(4,0),(None,0),(2,0),(4,0),(5,0),(4,0),(2,0),(None,0),(1,0),(None,0),(2,0),(0,0),(None,0),(None,0),(2,0),(None,0)]
        d0=0; prev=None
        for b in range(nb):
            t0=b*B
            if t0>=s.dur: break
            k=s.kind_at(t0); bar=b//4; beat=b%4
            if k=='drop' and prev!='drop': d0=b
            prev=k
            ch_root=st['prog'][bar%len(st['prog'])]
            sw=lambda i: (st['swing']*B/2 if i%2==1 else 0)
            # --- pad / chords
            if beat==0 and st['pad'] and k in ('drop','break','intro','outro'):
                g={'intro':.8,'break':1.3,'drop':1.0,'outro':.9}[k]
                pl=s.chord_pad(s.chord(ch_root), B*4); pr=s.chord_pad(s.chord(ch_root), B*4)
                s.put('music', np.stack([pl,pr],1), t0, g)
            if k=='outro' and t0>s.dur-B*2: continue
            # --- drums
            if k in ('drop','outro'):
                s.drums(st['drums'], t0, beat, b, sw)
            elif k=='intro':
                if beat in (0,2): s.put('drums', s.hat(), t0, .6, .2)
            elif k=='break':
                if beat==0: s.put('drums', s.rim(), t0, .5)
            # --- bass
            if k in ('drop','outro'):
                br=s.root+ch_root
                if st['bass']=='808':
                    if beat==0: s.put('bass', s.bass_note(br,B*1.5,'808'), t0, 1.0)
                    if beat==2: s.put('bass', s.bass_note(br,B*.75,'808'), t0+B*.5, .8)
                    if beat==3 and bar%2==1: s.put('bass', s.bass_note(br+12,B*.4,'808'), t0+B*.5, .6)
                else:
                    s.put('bass', s.bass_note(br+(12 if st['bass']=='saw' else 0),B*.45,st['bass']), t0+B*.5, 1.0)
            # --- stabs (house)
            if st['drums']=='house' and k=='drop' and beat in (1,3):
                s.put('music', s.stab(s.chord(ch_root)), t0+B*.5, 1.0)
            # --- lead hook (16 steps of 8th notes over 2 bars), only on drop, every other 2-bar phrase
            if k=='drop' and ((b-d0)//8)%2==0:
                for half in (0,1):
                    step=((b-d0)%8)*2+half
                    deg,octv=hook[step%len(hook)]
                    if deg is None: continue
                    m=s.root+24+sc[deg%7]+12*(octv+deg//7)
                    tt=t0+half*B/2+sw(half)
                    inst=st['lead']
                    sig={'pluck':s.pluck,'keys':s.keys,'bell':s.bell,'marimba':s.marimba}[inst](m)
                    s.put('lead', sig, tt, 1.0, pan=.45 if half else -.45)
                    s.put('lead', sig*.35, tt+B*.75, 1.0, pan=-.6 if half else .6)  # Delay-Echo
        # risers into each drop after a break/intro
        for (t,kind) in s.sections:
            if kind=='drop' and t>0.5: s.sfx('riser', t-1.2)
    def drums(s, kind, t0, beat, b, sw):
        B=s.B
        if kind=='house':
            s.put('kick', s.kick(), t0); s.kicks.append(t0)
            if beat in (1,3): s.put('drums', s.clap(), t0, .9)
            s.put('drums', s.hat(op=True), t0+B/2, .7, .3)
            s.put('drums', s.hat(), t0+B/4, .5, -.3); s.put('drums', s.hat(), t0+3*B/4, .5, -.3)
        elif kind=='tamborzao':   # funk carioca: K . . K | . . K . with tamborzão percussion
            pat16=[1,0,0,1, 0,0,1,0, 1,0,0,1, 0,0,1,0]
            for i in range(4):
                st=((beat*4)+i)%16; tt=t0+i*B/4
                if pat16[st]: s.put('kick', s.kick(1.2), tt, .95); s.kicks.append(tt)
                if st in (4,12): s.put('drums', s.snare(), tt, .8)
                if st in (2,7,10,15): s.put('drums', s.conga(260 if st%2 else 200), tt, .8, pan=.35 if st%2 else -.35)
                if i%2==1: s.put('drums', s.shaker(), tt, 1.0, .4)
        elif kind=='boom':
            if beat in (0,) or (beat==2 and b%2==1): s.put('kick', s.kick(.8), t0); s.kicks.append(t0)
            if beat in (1,3): s.put('drums', s.snare(), t0, .7)
            for i in range(2): s.put('drums', s.hat(), t0+i*B/2+sw(i), .45, .2)
        elif kind=='phonk':
            if beat in (0,2): s.put('kick', s.kick(1.1), t0); s.kicks.append(t0)
            if beat in (1,3): s.put('drums', s.clap(), t0, .7)
            for i in range(4): s.put('drums', s.hat(), t0+i*B/4, .4, .25)
            s.put('drums', s.cowbell(560 if beat%2 else 700), t0+B*.5, .8, -.2)
        elif kind=='afro':
            if beat in (0,2) or (beat==3): s.put('kick', s.kick(.9), t0+ (B*.5 if beat==3 else 0)); s.kicks.append(t0)
            if beat in (1,3): s.put('drums', s.rim(), t0+B*.25, .8)
            for i in range(4): s.put('drums', s.shaker(), t0+i*B/4, 1.0, .3)
            if beat==2: s.put('drums', s.conga(240), t0+B*.75, .7, -.3)
    # ---------- SFX ----------
    def sfx(s, kind, t, g=1.0, pan=0.0, **kw):
        n=lambda d:int(d*SR)
        if kind=='pop':
            f=kw.get('f',900); m=n(.09); tt=np.arange(m)/SR
            x=np.sin(2*np.pi*np.cumsum(f+f*1.5*np.exp(-tt*60))/SR)*np.exp(-tt*45)*.4
        elif kind=='click':
            m=n(.03); x=s.hp(s.rng.standard_normal(m),2000)*np.exp(-np.arange(m)/(SR*.004))*.5
        elif kind=='tick':
            m=n(.04); tt=np.arange(m)/SR; x=np.sin(2*np.pi*2600*tt)*np.exp(-tt*120)*.25
        elif kind=='ding':
            f=kw.get('f',1320); m=n(.7); tt=np.arange(m)/SR
            x=(np.sin(2*np.pi*f*tt)+.4*np.sin(2*np.pi*f*2.01*tt)+.15*np.sin(2*np.pi*f*3.02*tt))*np.exp(-tt*6)*.18
        elif kind=='whoosh':
            d=kw.get('d',.5); m=n(d); x=s.rng.standard_normal(m)
            fc=np.linspace(300,6000,m)**1.0; y=np.zeros(m); a=0.0
            k=np.clip(fc/SR*6.28,0,1)
            for i in range(m): a+=k[i]*(x[i]-a); y[i]=a
            x=y*np.sin(np.linspace(0,np.pi,m))**2*.55
        elif kind=='riser':
            d=kw.get('d',1.2); m=n(d); tt=np.arange(m)/SR
            nz=s.hp(s.rng.standard_normal(m),2000)*(tt/d)**2*.25
            tone=np.sin(2*np.pi*np.cumsum(200+1800*(tt/d)**2)/SR)*(tt/d)**2*.08
            x=nz+tone
        elif kind=='impact':
            m=n(1.2); tt=np.arange(m)/SR
            x=np.sin(2*np.pi*np.cumsum(40+90*np.exp(-tt*12))/SR)*np.exp(-tt*3)*.9 + s.lp(s.rng.standard_normal(m),900)*np.exp(-tt*6)*.5
        elif kind=='scratch':
            m=n(.45); tt=np.arange(m)/SR; f=np.abs(np.sin(2*np.pi*7*tt))*1800+200
            x=(np.sin(2*np.pi*np.cumsum(f)/SR)*.5+s.hp(s.rng.standard_normal(m),1500)*.4)*np.exp(-tt*3)*.5
        elif kind=='boing':
            m=n(.5); tt=np.arange(m)/SR; f=220+180*np.sin(2*np.pi*9*tt)*np.exp(-tt*4)+tt*200
            x=np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-tt*5)*.4
        elif kind=='buzz':      # wrong answer
            m=n(.35); tt=np.arange(m)/SR; x=s.lp(np.sign(np.sin(2*np.pi*110*tt))+np.sign(np.sin(2*np.pi*116*tt)),1800)*np.exp(-tt*4)*.18
        elif kind=='correct':   # right answer: two-note chime
            x=np.zeros(n(.8))
            for j,f in enumerate((1318.5,1975.5)):
                i=n(.09*j); tt=np.arange(len(x)-i)/SR; x[i:]+=np.sin(2*np.pi*f*tt)*np.exp(-tt*5)*.2
        elif kind=='typing':
            d=kw.get('d',1.0); x=np.zeros(n(d))
            for tt0 in np.arange(0,d-.05,.085):
                i=n(tt0+s.rng.uniform(0,.02)); m=n(.02); x[i:i+m]+=s.hp(s.rng.standard_normal(m),3000)*np.exp(-np.arange(m)/(SR*.003))*.35
        elif kind=='cash':
            x=np.zeros(n(.9))
            for j,f in enumerate((2093,2637,3136)):
                i=n(.05*j); tt=np.arange(len(x)-i)/SR; x[i:]+=np.sin(2*np.pi*f*tt)*np.exp(-tt*7)*.15
        elif kind=='stamp':
            m=n(.35); tt=np.arange(m)/SR
            x=np.sin(2*np.pi*np.cumsum(70+120*np.exp(-tt*40))/SR)*np.exp(-tt*14)*.9+s.lp(s.rng.standard_normal(m),2500)*np.exp(-tt*30)*.6
        elif kind=='crumple':
            m=n(.4); e=(s.rng.random(m)<.02)*1.0; e=np.convolve(e,np.exp(-np.arange(400)/60),'same')
            x=s.hp(s.rng.standard_normal(m),1000)*e*.5
        else: raise ValueError(kind)
        s.put('sfx', x, t, g, pan)
    def duck(s, t, d=1.0, depth=.15):
        """Musik kurz leiser (z. B. Wendepunkt / Stille)."""
        s.ducks=getattr(s,'ducks',[]); s.ducks.append((t,d,depth))
    # ---------- master ----------
    def reverb(s, x, decay=1.4, wet=.18):
        m=int(decay*SR); t=np.arange(m)/SR
        ir=s.rng.standard_normal((m,2))*np.exp(-t*6.9/decay)[:,None]; ir=s.lp(ir,6000); ir/=np.sqrt((ir**2).sum(0))
        y=np.stack([fftconvolve(x[:,c],ir[:,c])[:len(x)] for c in (0,1)],1)
        return x*(1-wet)+y*wet*2.2
    def write(s, path, target_db=-11.0, fade=(None,None)):
        N=s.N
        s.kicks=[k for k in s.kicks if not any(-.06<k-h<.25 and abs(k-h)>1e-6 for h in getattr(s,'hits',()))]
        # sidechain envelope from kicks
        sc=np.ones(N); L=int(s.B*.55*SR); curve=1-.62*np.exp(-np.arange(L)/(SR*.07))
        for k in s.kicks:
            i=int(k*SR)
            if i<N: m=min(L,N-i); sc[i:i+m]=np.minimum(sc[i:i+m],curve[:m])
        music=s.reverb(s.bus['music']*1.0,2.2,.35)+s.reverb(s.bus['lead']*1.8,1.3,.22)
        music=music*sc[:,None]; bass=s.bus['bass']*sc[:,None]**.7
        drums=s.reverb(s.bus['drums'],.8,.10)
        sfx=s.reverb(s.bus['sfx'],.9,.12)
        mix=s.bus['kick']*.6+drums*1.25+bass*.35+music*1.9+sfx*1.15
        mix=mix+.7*s.bp(mix-sfx*1.15,1000,6000)   # Handy-Lautsprecher: Präsenz anheben
        for (t,d,depth) in getattr(s,'ducks',[]):
            a=int(t*SR); b=min(N,int((t+d)*SR))
            if a<N:
                g=np.full(b-a,depth); r=min(len(g),int(.08*SR)); g[:r]=np.linspace(1,depth,r); g[-r:]=np.linspace(depth,1,r)
                nonsfx=(mix-sfx*1.15)[a:b]; mix[a:b]=nonsfx*g[:,None]+sfx[a:b]*1.15
        mix=s.hp(mix,28)
        fo=int((fade[0] or s.dur-1.3)*SR); fe=int((fade[1] or s.dur-.25)*SR)
        mix[fo:fe]*=np.linspace(1,0,fe-fo)[:,None]; mix[fe:]=0
        mix=np.tanh(mix*1.6)/np.tanh(1.6)
        rms=np.sqrt(np.mean(mix[:fo]**2)); g=10**(target_db/20)/max(rms,1e-9)
        mix*=min(g,.89/np.abs(mix).max()); mix=np.clip(mix,-1,1)
        with wave.open(path,'wb') as w:
            w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((mix*32767).astype('<i2').tobytes())
        return 20*np.log10(np.sqrt(np.mean(mix[:fo]**2)))
