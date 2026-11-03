// Reel 30 – echter Rechner-Ausschnitt „Como o preço é calculado“ (pc1–pc3), live ohne Mock, 03.11.2026.
// Aufruf: node capture_ui.js  (schreibt n_pc1.png … n_pc3.png + n_pc_sec.png ins aktuelle Verzeichnis)
// Verwendet im Video: nur pc2 → shots/pc2_live.png (ganze Zeile, ungeschnitten). Viewport 280 px @3x.
const {chromium}=require('/opt/node-tools/node_modules/playwright');
(async()=>{const px=process.env.HTTPS_PROXY;
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',proxy:px?{server:px}:undefined});
const c=await b.newContext({viewport:{width:280,height:653},deviceScaleFactor:3,isMobile:true,locale:'pt-BR'});
const p=await c.newPage();
await p.goto('https://www.traduzme.com.br/orcamento-app/?lang=pt',{waitUntil:'domcontentloaded',timeout:60000});
await p.waitForTimeout(4000);
const lis=await p.$$('li[data-i18n-html="pc1"], li[data-i18n-html="pc2"], li[data-i18n-html="pc3"]');
const all=await p.$$('section li');
for(const sel of ['pc1','pc2','pc3']){const el=await p.$(`[data-i18n-html="${sel}"]`); if(!el){console.log('no',sel);continue;}
 const li=await el.evaluateHandle(e=>e.closest('li')); await li.asElement().scrollIntoViewIfNeeded(); await p.waitForTimeout(300);
 console.log(sel,(await li.asElement().innerText()).replace(/\s+/g,' '),JSON.stringify(await li.asElement().boundingBox()));
 await li.asElement().screenshot({path:`n_${sel}.png`});}
const h=await p.$('#pc_h, [data-i18n="pc_h"]'); if(h){console.log('H',await h.innerText()); const sec=await h.evaluateHandle(e=>e.closest('section')); await sec.asElement().screenshot({path:'n_pc_sec.png'});}
await b.close();})().catch(e=>{console.error(e);process.exit(1)});
