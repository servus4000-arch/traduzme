// Reel 23: Live-FAQ „Preciso de Apostila de Haia?“ Absatz 2 bei Viewport 345 (DPR 3): Screenshot shots/faq_p345.png + Zeilen-Rechtecke der zwei Marker-Stellen. faq_l36.png = Zeilen 3–6 (y 124–377 px). Aufruf: node faq_rects.js 345
const {chromium}=require('/opt/node-tools/node_modules/playwright');
(async()=>{const px=process.env.HTTPS_PROXY; const W=+process.argv[2]||320;
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',proxy:px?{server:px}:undefined});
const c=await b.newContext({viewport:{width:W,height:844},deviceScaleFactor:3,isMobile:true,locale:'pt-BR'});
const p=await c.newPage();
await p.route('**/functions/v1/pix-config',r=>r.fulfill({status:200,contentType:'application/json',body:JSON.stringify({ok:true,agora:new Date().toISOString(),idiomas:{},precos:[],feriados:[],uso:{}})}));
await p.goto('https://www.traduzme.com.br/orcamento-app/?lang=pt',{waitUntil:'domcontentloaded',timeout:60000});
await p.waitForTimeout(2500);
await p.evaluate(()=>abrirFaq()); await p.waitForTimeout(700);
const r=await p.evaluate(()=>{const d=[...document.querySelectorAll('#pop .faq-l details')].find(x=>/Apostila de Haia/.test(x.querySelector('summary').textContent));d.open=true;d.scrollIntoView({block:'start'});const P=d.querySelectorAll('.faq-a p')[1];P.id='p8b';const base=P.getBoundingClientRect();const tn=P.firstChild;const txt=P.textContent;
 const cs=getComputedStyle(P);
 const out={w:base.width,h:base.height,fs:cs.fontSize,lh:cs.lineHeight,txt,parts:{}};
 for(const s of ['a tradução para o português não precisa de apostila','Como as regras variam, confirme']){const i=txt.indexOf(s);const rg=document.createRange();rg.setStart(tn,i);rg.setEnd(tn,i+s.length);out.parts[s]=[...rg.getClientRects()].map(q=>[q.left-base.left,q.top-base.top,q.width,q.height].map(v=>+v.toFixed(1)));}
 return out;});
await p.waitForTimeout(400);
await (await p.$('#p8b')).screenshot({path:'shots/faq_p345.png'});
console.log(JSON.stringify(r)); await b.close();})();
