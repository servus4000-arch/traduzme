// Echter Rechner-Screen (Schritt 1) für Karussell 01 – Playwright, iPhone-Viewport 390x844 @3x.
// pix-config wird gemockt (Supabase aus der Sandbox nicht erreichbar); Schritt 1 zeigt keine Preise.
const {chromium}=require('/opt/node-tools/node_modules/playwright');
(async()=>{const px=process.env.HTTPS_PROXY;
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',proxy:px?{server:px}:undefined});
const d=await b.newPage({viewport:{width:900,height:1200}});
await d.setContent(`<body style="margin:0;background:#f7f5ef"><div style="margin:60px;border:4px solid #b9b2a2;height:1060px;padding:50px;box-sizing:border-box">${'<div style="height:14px;background:#d6d0c2;margin:34px 0;border-radius:7px"></div>'.repeat(16)}</div></body>`);
await d.screenshot({path:'shots/antecedentes.jpg',type:'jpeg'});
const cases=[['en','Inglês','Português','Inglês','from_pt'],['es','Espanhol','Espanhol','Português','to_pt'],['ar','Árabe','Árabe','Português','to_pt']];
for(const [code,nome,from,to,dir] of cases){
 const c=await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:3,isMobile:true,locale:'pt-BR'});
 const p=await c.newPage();
 const cap={ativo:true,express_max_pag:0,express_fix_cents:0,express48_max_pag:0,express48_fix_cents:0,normal_dias:0,longo_dias:0,max_pag_auto:0,limite_dia_pag:0,cutoff_hora:0,nome_pt:nome};
 await p.route('**/functions/v1/**',r=>{ if(r.request().url().includes('pix-config')) return r.fulfill({status:200,contentType:'application/json',body:JSON.stringify({ok:true,agora:new Date().toISOString(),idiomas:{[code]:cap},precos:[{categoria:'documento',idioma:code,direcao:'to_pt',chave:'x',ordem:1,valor_cents:0},{categoria:'documento',idioma:code,direcao:'from_pt',chave:'x',ordem:1,valor_cents:0},{categoria:'lauda',idioma:code,direcao:'to_pt',chave:'comum',valor_cents:0},{categoria:'lauda',idioma:code,direcao:'from_pt',chave:'comum',valor_cents:0}],feriados:[],uso:{}})}); return r.abort();});
 await p.goto('https://www.traduzme.com.br/orcamento-app/?lang=pt',{waitUntil:'networkidle',timeout:60000});
 await p.waitForTimeout(1500);
 await p.setInputFiles('#file',{name:'antecedentes.jpg',mimeType:'image/jpeg',buffer:require('fs').readFileSync('shots/antecedentes.jpg')});
 await p.waitForTimeout(1500);
 await p.selectOption('#from',from); await p.waitForTimeout(300);
 await p.selectOption('#to',to); await p.waitForTimeout(800);
 const card=await p.$('#card'); console.log(code,JSON.stringify(await card.boundingBox()));
 await p.evaluate(()=>window.scrollTo(0,0));
 await p.screenshot({path:`shots/form_${code}.png`});
 await p.screenshot({path:`shots/form_${code}_full.png`,fullPage:true});
 console.log(await p.evaluate(()=>document.querySelector('#card').innerText));
 await c.close();}
await b.close();})().catch(e=>{console.error(e);process.exit(1)});
