// 10-fps-Layoutprüfung: x-Grenzen an der Außenkante (Blase/Pille/Karte/Blatt), y >= 290, Überlappungen sichtbarer Elemente
const {chromium}=require('/opt/node-tools/node_modules/playwright');
const cut=process.argv[2]||'main';
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('file:///home/user/traduzme/media/reels/src/reel16/reel.html'+(cut==='gmb'?'?cut=gmb':''));await p.waitForFunction(()=>window.READY===true);
const res=await p.evaluate(()=>{
 const out=[]; const effO=e=>{let o=1;for(let n=e;n&&n!==document.body;n=n.parentElement){const cs=getComputedStyle(n);if(cs.display==='none'||cs.visibility==='hidden')return 0;o*=+cs.opacity;}return o;};
 const items=()=>{const L=[];
   document.querySelectorAll('.msg').forEach(m=>{m.querySelectorAll('.bub,.src,.name').forEach(x=>L.push([m.id+'.'+x.className,x]));});
   ['chipCta','chipTr','chipBio','url','wa','mit','cardA','cardB','cardC','doc','pt'].forEach(id=>L.push([id,document.getElementById(id)]));
   return L;};
 for(let f=0;f<Math.round(END*10);f++){const t=f/10; render(t); const V=[];
   for(const [n,e] of items()){const o=effO(e); if(o<0.05) continue; const r=e.getBoundingClientRect(); if(r.width<2) continue;
     if(r.bottom<0||r.top>1920) continue;
     V.push({n,o:+o.toFixed(2),l:Math.round(r.left),r:Math.round(r.right),t:Math.round(r.top),b:Math.round(r.bottom)});}
   const iss=[];
   for(const v of V){ if(v.l<88||v.r>902) iss.push(`X ${v.n} ${v.l}-${v.r}`); if(v.t<290) iss.push(`Y ${v.n} top ${v.t}`);}
   for(let i=0;i<V.length;i++)for(let j=i+1;j<V.length;j++){const a=V[i],c=V[j];
     const sameMsg=a.n.split('.')[0]===c.n.split('.')[0]&&a.n.startsWith('m_');
     if(sameMsg) continue;
     const ix=Math.min(a.r,c.r)-Math.max(a.l,c.l), iy=Math.min(a.b,c.b)-Math.max(a.t,c.t);
     if(ix>4&&iy>4) iss.push(`O ${a.n}(${a.o}) x ${c.n}(${c.o}) ${ix}x${iy}`);}
   if(iss.length) out.push(t.toFixed(1)+': '+iss.join(' | '));}
 return out;});
console.log(res.join('\n')); await b.close();})();
