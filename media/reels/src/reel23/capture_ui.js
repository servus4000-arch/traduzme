// Reel 23: echte Rechner-Ausschnitte (Live-Seite traduzme.com.br/orcamento-app, iPhone-Viewport @3x, Playwright).
// pix-config wird gemockt (Supabase-API aus der Sandbox nicht erreichbar); Schritt 1 zeigt keine Preise. Texte kommen unverändert von der Live-Seite.
// Hochgeladen wird eine neutrale Platzhalter-Datei (keine echten Daten). Aufruf: node capture_ui.js
const {chromium}=require('/opt/node-tools/node_modules/playwright');
(async()=>{const px=process.env.HTTPS_PROXY;
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',proxy:px?{server:px}:undefined});
const d=await b.newPage({viewport:{width:640,height:860}});
await d.setContent(`<body style="margin:0;background:#eef0ec"><div style="margin:30px;height:800px;border-radius:20px;background:#fbfaf6;padding:50px;box-sizing:border-box">${'<div style="height:24px;background:#d5dad4;margin:0 0 34px;border-radius:12px"></div>'.repeat(14)}</div></body>`);
await d.screenshot({path:'shots/certidao.jpg',type:'jpeg'});
const c=await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:3,isMobile:true,locale:'pt-BR'});
const p=await c.newPage();
const code='es',nome='Espanhol';
const cap={ativo:true,express_max_pag:0,express_fix_cents:0,express48_max_pag:0,express48_fix_cents:0,normal_dias:0,longo_dias:0,max_pag_auto:0,limite_dia_pag:0,cutoff_hora:0,nome_pt:nome};
await p.route('**/functions/v1/pix-config',r=>r.fulfill({status:200,contentType:'application/json',headers:{'access-control-allow-origin':'*'},body:JSON.stringify({ok:true,agora:new Date().toISOString(),idiomas:{[code]:cap},precos:[{categoria:'documento',idioma:code,direcao:'to_pt',chave:'x',ordem:1,valor_cents:0},{categoria:'lauda',idioma:code,direcao:'to_pt',chave:'comum',valor_cents:0}],feriados:[],uso:{}})}));
await p.goto('https://www.traduzme.com.br/orcamento-app/?lang=pt',{waitUntil:'networkidle',timeout:60000});
await p.waitForTimeout(1500);
await p.setInputFiles('#file','shots/certidao.jpg');
await p.waitForTimeout(1500);
await p.selectOption('#from',nome); await p.waitForTimeout(300);
await p.selectOption('#to','Português'); await p.waitForTimeout(800);
const rects=await p.evaluate(()=>{const o={};for(const s of ['#card','#from','#to','#file','.flist','.file-list','#files','section.flow','section.pricebox']){const e=document.querySelector(s);if(e){const r=e.getBoundingClientRect();o[s]=[r.x,r.y+scrollY,r.width,r.height]}}return o});
console.log(JSON.stringify(rects));
console.log((await p.$eval('#card',e=>e.innerText)).replace(/\s+/g,' '));
await p.evaluate(()=>window.scrollTo(0,0));
await p.screenshot({path:'shots/form_es_full.png',fullPage:true});
// Flow-Schritt 4 + Trust-Zeile
for(const [sel,f] of [['section.flow','flow']]){const el=await p.$(sel); await el.scrollIntoViewIfNeeded(); await p.waitForTimeout(300); await el.screenshot({path:'shots/'+f+'.png'}); console.log(f,(await el.innerText()).replace(/\s+/g,' '));}
// FAQ "Preciso de Apostila de Haia?" zweiter Absatz
await p.evaluate(()=>abrirFaq()); await p.waitForTimeout(700);
const t8=await p.evaluate(()=>{const d=[...document.querySelectorAll('#pop .faq-l details')].find(x=>/Apostila de Haia/.test(x.querySelector('summary').textContent));d.open=true;d.scrollIntoView({block:'start'});const ps=d.querySelectorAll('.faq-a p');ps[1].id='p8b';return d.querySelector('summary').textContent+' || '+ps[1].textContent;});
console.log('faq', t8); await p.waitForTimeout(500);
await (await p.$('#p8b')).screenshot({path:'shots/faq_apostila.png'});
await b.close();})().catch(e=>{console.error(e);process.exit(1)});
