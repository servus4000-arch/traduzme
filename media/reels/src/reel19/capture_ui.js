// Reel 19: echter Screenshot der Rechner-FAQ "Preciso de Apostila de Haia?" (faq_a8) – Live-Seite, iPhone-Viewport @3x.
// pix-config wird gemockt (Proxy-Sandbox erreicht Supabase nicht); FAQ-Text kommt unverändert aus der Live-Seite.
const {chromium}=require('/opt/node-tools/node_modules/playwright');
(async()=>{const px=process.env.HTTPS_PROXY;
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',proxy:px?{server:px}:undefined});
const c=await b.newContext({viewport:{width:+(process.env.VW||390),height:844},deviceScaleFactor:3,isMobile:true,locale:'pt-BR',ignoreHTTPSErrors:false});
const p=await c.newPage();
await p.route('**/functions/v1/pix-config',r=>r.fulfill({status:200,contentType:'application/json',body:JSON.stringify({ok:true,agora:new Date().toISOString(),idiomas:{},precos:[],feriados:[],uso:{}})}));
await p.goto('https://www.traduzme.com.br/orcamento-app/?lang=pt',{waitUntil:'domcontentloaded',timeout:60000});
await p.waitForTimeout(2500);
await p.evaluate(()=>abrirFaq());
await p.waitForTimeout(600);
const ok=await p.evaluate(()=>{const d=document.querySelectorAll('#pop .faq-l details');const x=d[7];x.open=true;x.scrollIntoView({block:'start'});return x.querySelector('summary').textContent+' || '+x.querySelector('.faq-a').textContent;});
console.log(ok);
await p.waitForTimeout(500);
await p.screenshot({path:'shots/faq8_view.png'});
const box=await p.$('#pop .faq-l details:nth-child(8)'); const bb=await box.boundingBox(); console.log(JSON.stringify(bb));
await box.screenshot({path:'shots/faq8.png'});
// Wort-Rechtecke der zwei Belegstellen (fuer Marker im Reel), relativ zur details-Box, CSS-px
const hl=await p.evaluate(()=>{const d=document.querySelectorAll('#pop .faq-l details')[7];const R=d.getBoundingClientRect();const a=d.querySelector('.faq-a p');
 const txt=a.firstChild; const s=txt.textContent; const out={};
 for(const [k,ph] of [['h1','apostilado em cartório antes da tradução'],['h2','a tradução juramentada recebe uma apostila própria, que você pode incluir direto no orçamento']]){
  const i=s.indexOf(ph); const r=document.createRange(); r.setStart(txt,i); r.setEnd(txt,i+ph.length);
  out[k]=[...r.getClientRects()].map(q=>[q.left-R.left,q.top-R.top,q.width,q.height].map(v=>Math.round(v*10)/10));}
 out.box=[R.width,R.height]; return out;});
require('fs').writeFileSync('shots/faq8_rects.json',JSON.stringify(hl)); console.log(JSON.stringify(hl));
await b.close();})().catch(e=>{console.error(e);process.exit(1)});
