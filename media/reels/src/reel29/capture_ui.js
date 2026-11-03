// Reel 29: echte Rechner-Ausschnitte (Live-Seite, iPhone @3x), OHNE Mock. Nur statischer Text: Box „Como o preço é calculado“.
const {chromium}=require('/opt/node-tools/node_modules/playwright');
(async()=>{const px=process.env.HTTPS_PROXY;
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',proxy:px?{server:px}:undefined});
const c=await b.newContext({viewport:{width:+(process.env.VW||390),height:844},deviceScaleFactor:3,isMobile:true,locale:'pt-BR'});
const p=await c.newPage();
await p.goto('https://www.traduzme.com.br/orcamento-app/?lang=pt',{waitUntil:'domcontentloaded',timeout:60000});
await p.waitForTimeout(5000);
const pb=await p.$('.pricebox'); await pb.scrollIntoViewIfNeeded(); await p.waitForTimeout(400);
console.log('PRICEBOX:',(await pb.innerText()).replace(/\s+/g,' '));
await pb.screenshot({path:'pricebox.png'});
const kids=await pb.$$(':scope > *'); let i=0;
for(const k of kids){i++; const bb=await k.boundingBox(); console.log(i,(await k.innerText()).replace(/\s+/g,' ').slice(0,100),JSON.stringify(bb)); await k.screenshot({path:`pb${i}.png`});}
await b.close();})().catch(e=>{console.error(e);process.exit(1)});
