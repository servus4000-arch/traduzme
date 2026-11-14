// Reel 27: echte Rechner-Ausschnitte (Live-Seite traduzme.com.br/orcamento-app, iPhone-Viewport @3x, Playwright).
// Gezeigt wird nur statischer Seitentext („Como funciona“ Schritte 1–4). pix-config (Supabase) ist aus der Sandbox nicht
// erreichbar und wird NICHT gemockt: keine Preise, keine Sprachliste, keine gemockten Werte im Bild.
const {chromium}=require('/opt/node-tools/node_modules/playwright');
(async()=>{const px=process.env.HTTPS_PROXY;
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',proxy:px?{server:px}:undefined});
const c=await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:3,isMobile:true,locale:'pt-BR'});
const p=await c.newPage();
await p.goto('https://www.traduzme.com.br/orcamento-app/?lang=pt',{waitUntil:'domcontentloaded',timeout:60000});
await p.waitForTimeout(4000);
const fl=await p.$('section.flow'); await fl.scrollIntoViewIfNeeded(); await p.waitForTimeout(500);
console.log('FLOW:',(await fl.innerText()).replace(/\s+/g,' '));
const items=await p.$$('section.flow li, section.flow .step, section.flow ol > *');
console.log('items',items.length);
let i=0; for(const it of items){i++; const t=(await it.innerText()).replace(/\s+/g,' '); const bb=await it.boundingBox(); console.log(i,t,JSON.stringify(bb)); await it.screenshot({path:`shots/step${i}.png`});}
await fl.screenshot({path:'shots/flow_full.png'});
// Danach (Python/PIL): Zuschnitt step{i}.png → step{i}_c.png, y 22…h−6; Breite 780 px (Schritte 1, 2, 4) bzw. 870 px (Schritt 3, längste Zeile),
// damit die UI-Schrift im Handy (Anzeigebreite 790 px) möglichst ≥ 40 px wirkt. Rohbilder step{i}.png werden nicht committet.
await b.close();})().catch(e=>{console.error(e);process.exit(1)});
