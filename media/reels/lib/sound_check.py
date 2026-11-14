"""Objektive Sound-Analyse für den Sound-Kritiker: python3 sound_check.py audio.wav [abschnitt-zeiten...]
Gibt aus: Peak, RMS gesamt, RMS je 2 s, Bandbalance (Sub/Bass/Mitten/Präsenz/Höhen), Stereo-Breite,
Clipping-Anteil, Transienten/Sek. Richtwerte stehen unten im Ausdruck."""
import sys, wave, numpy as np
p=sys.argv[1]
w=wave.open(p); sr=w.getframerate(); n=w.getnframes(); x=np.frombuffer(w.readframes(n),'<i2').reshape(-1,w.getnchannels())/32768.0
m=x.mean(1); sd=(x[:,0]-x[:,1])/2
db=lambda v:20*np.log10(max(v,1e-9))
print(f'Dauer {n/sr:.1f}s  Peak {db(np.abs(x).max()):.1f} dBFS  RMS {db(np.sqrt((m**2).mean())):.1f} dB  Clip {(np.abs(x)>.985).mean()*100:.3f}%  Stereo-Breite (Side/Mid) {np.sqrt((sd**2).mean())/np.sqrt((m**2).mean()):.2f}')
F=np.abs(np.fft.rfft(m*np.hanning(len(m)))); f=np.fft.rfftfreq(len(m),1/sr)
bands=[('Sub 20-60',20,60),('Bass 60-250',60,250),('LowMid 250-800',250,800),('Mid 800-3k',800,3000),('Presence 3-8k',3000,8000),('Air 8-16k',8000,16000)]
tot=(F**2).sum()
print('Bandbalance (% Energie):',' | '.join(f'{nm} {100*(F[(f>=a)&(f<b)]**2).sum()/tot:.1f}' for nm,a,b in bands))
seg=int(2*sr); rows=[]
for i in range(0,len(m),seg):
    s=m[i:i+seg]
    if len(s)<sr//4: break
    e=np.abs(np.diff(np.convolve(np.abs(s),np.ones(256)/256,'same')[::256]))
    on=(e>e.mean()+2*e.std()).sum()/ (len(s)/sr)
    rows.append(f'{i/sr:4.0f}s {db(np.sqrt((s**2).mean())):6.1f}dB on/s {on:4.1f}')
print('Verlauf je 2 s:'); print('\n'.join(rows))
print('Richtwerte: Peak <= -0.3, RMS -10..-12, Clip 0, Breite 0.2-0.6, Sub+Bass 35-60 %, Presence+Air 5-15 %, Verlauf mit hörbaren Abschnitten (Break leiser), keine 2 s Stille außer gewollt, Ende ausgeblendet.')
