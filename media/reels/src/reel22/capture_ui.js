// Reel 22: echte Screenshots der Rechner-Seite (Live, iPhone-Viewport @3x): Block "Como funciona" (fl1–fl4)
// und Zeile pc2 "Verso e Apostila … sem custo extra" aus "Como o preço é calculado". Keine Preise auf diesen Blöcken.
// pix-config wird gemockt (Sandbox erreicht Supabase nicht); die Texte kommen unverändert von der Live-Seite.
const {chromium}=require('/opt/node-tools/node_modules/playwright');
(async()=>{const px=process.env.HTTPS_PROXY;
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',proxy:px?{server:px}:undefined});
const c=await b.newContext({viewport:{width:+(process.env.VW||300),height:844},deviceScaleFactor:3,isMobile:true,locale:'pt-BR'});
const p=await c.newPage();
await p.route('**/functions/v1/pix-config',r=>r.fulfill({status:200,contentType:'application/json',body:JSON.stringify({ok:true,agora:new Date().toISOString(),idiomas:{},precos:[],feriados:[],uso:{}})}));
await p.goto('https://www.traduzme.com.br/orcamento-app/?lang=pt',{waitUntil:'domcontentloaded',timeout:60000});
await p.waitForTimeout(2500);
for(const [sel,f] of [['section.flow','flow'],['section.pricebox','price']]){
  const el=await p.$(sel); await el.scrollIntoViewIfNeeded(); await p.waitForTimeout(300);
  console.log(f, JSON.stringify(await el.boundingBox()), (await el.innerText()).replace(/\s+/g,' '));
  await el.screenshot({path:'shots/'+f+'.png'});
}
// Wort-Rechtecke der pc2-Zeile (relativ zur pricebox, CSS-px)
const r=await p.evaluate(()=>{const box=document.querySelector('section.pricebox').getBoundingClientRect();const li=document.querySelector('[data-i18n-html="pc2"]').getBoundingClientRect();
 const fl=[...document.querySelectorAll('section.flow li')].map(e=>{const q=e.getBoundingClientRect();return [q.left,q.top,q.width,q.height]});const fb=document.querySelector('section.flow').getBoundingClientRect();
 return {pc2:[li.left-box.left,li.top-box.top,li.width,li.height],price:[box.width,box.height],flow:[fb.width,fb.height],flowLi:fl.map(a=>[a[0]-fb.left,a[1]-fb.top,a[2],a[3]])};});
require('fs').writeFileSync('shots/rects.json',JSON.stringify(r)); console.log(JSON.stringify(r));
// FAQ a8, zweiter Absatz ("Documento estrangeiro para usar no Brasil? …")
await p.evaluate(()=>abrirFaq()); await p.waitForTimeout(700);
const t8=await p.evaluate(()=>{const d=document.querySelectorAll('#pop .faq-l details')[7];d.open=true;d.scrollIntoView({block:'start'});const ps=d.querySelectorAll('.faq-a p');ps[1].id='p8b';return d.querySelector('summary').textContent+' || '+ps[1].textContent;});
console.log('faq8', t8); await p.waitForTimeout(500);
const e8=await p.$('#p8b'); await e8.screenshot({path:'shots/faq8b.png'});
await b.close();})().catch(e=>{console.error(e);process.exit(1)});
