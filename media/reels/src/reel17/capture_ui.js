// Echte Rechner-Screens (Schritt 1) für Reel 17 – Playwright, iPhone-Viewport 390×844 @3x.
// pix-config wird gemockt (API aus der Sandbox nicht erreichbar); Schritt 1 zeigt keine Preise.
// Aufruf: node capture_ui.js   → shots/form_ar.png, shots/form_de.png (+ _full)
const {chromium}=require('/opt/node-tools/node_modules/playwright');
(async()=>{const px=process.env.HTTPS_PROXY;
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',proxy:px?{server:px}:undefined});
const d=await b.newPage({viewport:{width:900,height:1200}});
await d.setContent(`<body style="margin:0;background:#f4efe4"><div style="margin:60px;border:6px double #8a7a5a;height:1060px;padding:50px;box-sizing:border-box">${'<div style="height:14px;background:#cfc6b2;margin:34px 0;border-radius:7px"></div>'.repeat(16)}</div></body>`);
await d.screenshot({path:'shots/diploma.jpg',type:'jpeg'});
for(const [code,nome] of [['ar','Árabe'],['de','Alemão']]){
 const c=await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:3,isMobile:true,locale:'pt-BR'});
 const p=await c.newPage();
 const cap={ativo:true,express_max_pag:0,express_fix_cents:0,express48_max_pag:0,express48_fix_cents:0,normal_dias:0,longo_dias:0,max_pag_auto:0,limite_dia_pag:0,cutoff_hora:0,nome_pt:nome};
 await p.route('**/functions/v1/pix-config',r=>r.fulfill({status:200,contentType:'application/json',body:JSON.stringify({ok:true,agora:new Date().toISOString(),idiomas:{[code]:cap},precos:[{categoria:'documento',idioma:code,direcao:'to_pt',chave:'x',ordem:1,valor_cents:0},{categoria:'lauda',idioma:code,direcao:'to_pt',chave:'comum',valor_cents:0}],feriados:[],uso:{}})}));
 await p.goto('https://www.traduzme.com.br/orcamento-app/?lang=pt',{waitUntil:'networkidle',timeout:60000});
 await p.waitForTimeout(1500);
 await p.setInputFiles('#file','shots/diploma.jpg');
 await p.waitForTimeout(1500);
 await p.selectOption('#from',nome); await p.waitForTimeout(300);
 await p.selectOption('#to','Português'); await p.waitForTimeout(800);
 const card=await p.$('#card'); console.log(code,JSON.stringify(await card.boundingBox()));
 await p.evaluate(()=>window.scrollTo(0,0));
 await p.screenshot({path:`shots/form_${code}.png`});
 await p.screenshot({path:`shots/form_${code}_full.png`,fullPage:true});
 await c.close();}
await b.close();})().catch(e=>{console.error(e);process.exit(1)});
