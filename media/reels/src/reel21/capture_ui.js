// Echter Rechner-Screen (Schritt 1) für Reel 21 – Playwright, iPhone-Viewport 390×844 @3x.
// pix-config wird gemockt (Supabase-API aus der Sandbox über den Proxy nicht erreichbar); Schritt 1 zeigt keine Preise.
// Hochgeladen wird eine neutrale Platzhalter-Karte (keine echten Daten). Aufruf: node capture_ui.js → shots/form_es.png (+ _full)
const {chromium}=require('/opt/node-tools/node_modules/playwright');
(async()=>{const px=process.env.HTTPS_PROXY;
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',proxy:px?{server:px}:undefined});
const d=await b.newPage({viewport:{width:900,height:570}});
await d.setContent(`<body style="margin:0;background:#e9eef2"><div style="margin:30px;height:510px;border-radius:28px;background:#d9e3ea;padding:40px;box-sizing:border-box"><div style="width:210px;height:270px;background:#b8c6d0;border-radius:14px;float:left"></div>${'<div style="height:22px;background:#a9b9c4;margin:30px 0 30px 250px;border-radius:11px"></div>'.repeat(6)}</div></body>`);
await d.screenshot({path:'shots/licencia.jpg',type:'jpeg'});
const c=await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:3,isMobile:true,locale:'pt-BR'});
const p=await c.newPage();
const code='es',nome='Espanhol';
const cap={ativo:true,express_max_pag:0,express_fix_cents:0,express48_max_pag:0,express48_fix_cents:0,normal_dias:0,longo_dias:0,max_pag_auto:0,limite_dia_pag:0,cutoff_hora:0,nome_pt:nome};
await p.route('**/functions/v1/pix-config',r=>r.fulfill({status:200,contentType:'application/json',headers:{'access-control-allow-origin':'*'},body:JSON.stringify({ok:true,agora:new Date().toISOString(),idiomas:{[code]:cap},precos:[{categoria:'documento',idioma:code,direcao:'to_pt',chave:'x',ordem:1,valor_cents:0},{categoria:'lauda',idioma:code,direcao:'to_pt',chave:'comum',valor_cents:0}],feriados:[],uso:{}})}));
await p.goto('https://www.traduzme.com.br/orcamento-app/?lang=pt',{waitUntil:'networkidle',timeout:60000});
await p.waitForTimeout(1500);
await p.setInputFiles('#file','shots/licencia.jpg');
await p.waitForTimeout(1500);
await p.selectOption('#from',nome); await p.waitForTimeout(300);
await p.selectOption('#to','Português'); await p.waitForTimeout(800);
const card=await p.$('#card'); console.log('card',JSON.stringify(await card.boundingBox()));
const rects=await p.evaluate(()=>{const o={};for(const s of ['#card','#from','#to','#file','button[type=submit]','.btn-calc','#calc','.flist','.file-list','#files']){const e=document.querySelector(s);if(e){const r=e.getBoundingClientRect();o[s]=[r.x,r.y+scrollY,r.width,r.height]}}return o});
console.log(JSON.stringify(rects));
await p.evaluate(()=>window.scrollTo(0,0));
await p.screenshot({path:`shots/form_${code}.png`});
await p.screenshot({path:`shots/form_${code}_full.png`,fullPage:true});
await c.close(); await b.close();})().catch(e=>{console.error(e);process.exit(1)});
