// Rendert jede .slide als PNG (1080x1350) + DOM-Prüfung (Überlauf, Schriftgrößen, Ränder) + PDF.
const {chromium}=require('/opt/node-tools/node_modules/playwright');
const fs=require('fs');
(async()=>{
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
const p=await b.newPage({viewport:{width:1080,height:1350},deviceScaleFactor:1});
await p.goto('file://'+__dirname+'/carousel.html');
await p.evaluate(()=>document.fonts.ready);
await p.waitForTimeout(500);
const rep=await p.evaluate(()=>{
 const out=[];
 document.querySelectorAll('.slide').forEach(s=>{
  const sr=s.getBoundingClientRect();
  s.querySelectorAll('*').forEach(el=>{
   if(el.closest('svg')&&el.tagName!=='svg')return;
   const r=el.getBoundingClientRect(); if(!r.width)return;
   const cls=el.className&&el.className.baseVal!==undefined?'svg':el.className;
   const id=s.id+' '+el.tagName+'.'+cls;
   // overflow of text boxes
   if(el.scrollWidth>el.clientWidth+1&&getComputedStyle(el).overflow!=='hidden'&&el.tagName!=='svg') out.push('SCROLLW '+id+' '+el.scrollWidth+'>'+el.clientWidth);
   const decorative=el.matches('.docill,.docill *,.swipe,.swipe *');
   if(!decorative&&(r.left<sr.left+80-0.5||r.right>sr.right-80+0.5||r.top<sr.top+80-0.5||r.bottom>sr.bottom-80+0.5)) out.push('MARGIN '+id+' L'+Math.round(r.left-sr.left)+' R'+Math.round(sr.right-r.right)+' T'+Math.round(r.top-sr.top)+' B'+Math.round(sr.bottom-r.bottom));
   // text font sizes
   for(const n of el.childNodes){ if(n.nodeType===3&&n.textContent.trim()){ const fs=parseFloat(getComputedStyle(el).fontSize); if(fs<34) out.push('FONT<34 '+id+' '+fs+' "'+n.textContent.trim()+'"'); } }
  });
  // line counts for h2/body
  s.querySelectorAll('h2,.body,.hook').forEach(el=>{const lh=parseFloat(getComputedStyle(el).lineHeight); out.push('INFO '+s.id+' '+el.tagName+' lines='+Math.round(el.getBoundingClientRect().height/lh)+' bottom='+Math.round(el.getBoundingClientRect().bottom-sr.top));});
  s.querySelectorAll('h2,.body,.hook,.sub,.save span,.row').forEach(el=>{const rg=document.createRange(); rg.selectNodeContents(el); const rs=[...rg.getClientRects()].filter(r=>r.width>2); if(!rs.length)return; const maxB=Math.max(...rs.map(r=>r.bottom)); const last=rs.filter(r=>r.bottom>maxB-4); const w=Math.max(...last.map(r=>r.right))-Math.min(...last.map(r=>r.left)); if(rs.length>1&&w<200) out.push('ORPHAN '+s.id+' '+el.tagName+' lastline='+Math.round(w)+'px'); const R=Math.max(...rs.map(r=>r.right)); if(R>sr.right-80+0.5) out.push('TEXT>MARGIN '+s.id+' '+el.tagName+' right='+Math.round(R-sr.left));});
  const f=s.querySelector('.foot,.save'); if(f){const prev=f.previousElementSibling; out.push('INFO '+s.id+' gap-before-foot='+Math.round(f.getBoundingClientRect().top-prev.getBoundingClientRect().bottom));}
 });
 return out;});
console.log(rep.join('\n'));
fs.mkdirSync('out',{recursive:true});
const slides=await p.$$('.slide');
for(let i=0;i<slides.length;i++){await slides[i].screenshot({path:`out/slide_${String(i+1).padStart(2,'0')}.png`});}
await b.close();})().catch(e=>{console.error(e);process.exit(1)});
