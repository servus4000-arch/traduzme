// Panel B v2 (Abnahme 21-5): nur der erste Punkt „Documentos padrão … preço fixo por documento“ aus der Live-Seite,
// schmaler Viewport (320 CSS-px), damit die Schrift nach dem Einpassen auf 810 px ≥ 40 px wirkt. Marker-Rechtecke relativ zum Element.
const {chromium}=require('/opt/node-tools/node_modules/playwright');
(async()=>{const px=process.env.HTTPS_PROXY;
const b=await chromium.launch({executablePath:process.env.CHR||'/opt/pw-browsers/chromium',proxy:px?{server:px}:undefined});
const c=await b.newContext({viewport:{width:320,height:700},deviceScaleFactor:3,isMobile:true,locale:'pt-BR'});
const p=await c.newPage();
await p.route('**/functions/v1/pix-config',r=>r.fulfill({status:200,contentType:'application/json',headers:{'access-control-allow-origin':'*'},body:JSON.stringify({ok:true,agora:new Date().toISOString(),idiomas:{es:{ativo:true,nome_pt:'Espanhol'}},precos:[],feriados:[],uso:{}})}));
await p.goto('https://www.traduzme.com.br/orcamento-app/?lang=pt',{waitUntil:'networkidle',timeout:60000});
await p.waitForTimeout(1200);
const r=await p.evaluate(()=>{const box=document.querySelector('.pricebox'); box.scrollIntoView();
 const li=[...box.querySelectorAll('li')].find(l=>l.textContent.includes('Documentos padrão')); li.id='liCap';
 const L=li.getBoundingClientRect(); const fs=getComputedStyle(li).fontSize;
 const find=s=>{const w=document.createTreeWalker(li,NodeFilter.SHOW_TEXT);let n;while(n=w.nextNode()){const i=n.data.indexOf(s);if(i>=0){const rg=document.createRange();rg.setStart(n,i);rg.setEnd(n,i+s.length);return [...rg.getClientRects()].map(q=>[q.x-L.x,q.y-L.y,q.width,q.height])}}return null};
 return {li:[L.x,L.y,L.width,L.height],fs,cnh:find('CNH…'),pf:find('preço fixo por documento.'),text:li.textContent.trim()}});
console.log(JSON.stringify(r));
await p.locator('#liCap').screenshot({path:'shots/panelB2.png'});
await b.close();})();
