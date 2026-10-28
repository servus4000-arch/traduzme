// Marker-Rechtecke für Panel B (pc1-Zeile) aus der Live-Seite (CSS-px, Viewport nach scrollIntoView)
const {chromium}=require('/opt/node-tools/node_modules/playwright');
(async()=>{const px=process.env.HTTPS_PROXY;
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',proxy:px?{server:px}:undefined});
const c=await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:3,isMobile:true,locale:'pt-BR'});
const p=await c.newPage();
await p.route('**/functions/v1/pix-config',r=>r.fulfill({status:200,contentType:'application/json',headers:{'access-control-allow-origin':'*'},body:JSON.stringify({ok:true,agora:new Date().toISOString(),idiomas:{es:{ativo:true,nome_pt:'Espanhol'}},precos:[],feriados:[],uso:{}})}));
await p.goto('https://www.traduzme.com.br/orcamento-app/?lang=pt',{waitUntil:'networkidle',timeout:60000});
await p.waitForTimeout(1200);
const r=await p.evaluate(()=>{const e=document.querySelector('.pricebox');e.scrollIntoView();
 const find=(root,s)=>{const w=document.createTreeWalker(root,NodeFilter.SHOW_TEXT);let n;while(n=w.nextNode()){const i=n.data.indexOf(s);if(i>=0){const rg=document.createRange();rg.setStart(n,i);rg.setEnd(n,i+s.length);return [...rg.getClientRects()].map(q=>[q.x,q.y,q.width,q.height])}}return null};
 return {cnh:find(e,'CNH…'),pf:find(e,'preço fixo por documento.'),dp:find(e,'Documentos padrão')}});
console.log(JSON.stringify(r));
await p.screenshot({path:'shots/pricebox.png'});
await b.close();})();
