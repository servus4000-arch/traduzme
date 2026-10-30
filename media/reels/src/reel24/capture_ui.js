// Reel 24: echte Rechner-Ausschnitte (Live-Seite traduzme.com.br/orcamento-app, iPhone-Viewport @3x, Playwright).
// pix-config wird gemockt (Supabase-API aus der Sandbox nicht erreichbar), nur damit das Formular rendert. Gezeigte Ausschnitte
// (Titel, Sprachfelder, „Como funciona“ Schritt 4) enthalten keine gemockten Werte. Hochgeladen wird eine neutrale Platzhalter-Datei.
const {chromium}=require('/opt/node-tools/node_modules/playwright');
(async()=>{const px=process.env.HTTPS_PROXY;
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',proxy:px?{server:px}:undefined});
const c=await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:3,isMobile:true,locale:'pt-BR'});
const p=await c.newPage();
const code='fr',nome='Francês';
const cap={ativo:true,express_max_pag:0,express_fix_cents:0,express48_max_pag:0,express48_fix_cents:0,normal_dias:0,longo_dias:0,max_pag_auto:0,limite_dia_pag:0,cutoff_hora:0,nome_pt:nome};
await p.route('**/functions/v1/pix-config',r=>r.fulfill({status:200,contentType:'application/json',headers:{'access-control-allow-origin':'*'},body:JSON.stringify({ok:true,agora:new Date().toISOString(),idiomas:{[code]:cap},precos:[{categoria:'documento',idioma:code,direcao:'to_pt',chave:'x',ordem:1,valor_cents:0},{categoria:'lauda',idioma:code,direcao:'to_pt',chave:'comum',valor_cents:0}],feriados:[],uso:{}})}));
await p.goto('https://www.traduzme.com.br/orcamento-app/?lang=pt',{waitUntil:'networkidle',timeout:60000});
await p.waitForTimeout(1500);
await p.setInputFiles('#file','shots/certidao.jpg'); await p.waitForTimeout(1500);
await p.selectOption('#from',nome); await p.waitForTimeout(300);
await p.selectOption('#to','Português'); await p.waitForTimeout(800);
console.log('CARD:',(await p.$eval('#card',e=>e.innerText)).replace(/\s+/g,' '));
// Struktur der Sprachfelder
console.log(await p.evaluate(()=>{const o=[];for(const s of ['#from','#to']){let e=document.querySelector(s);const r=e.getBoundingClientRect();o.push(s+' '+JSON.stringify([r.x,r.y+scrollY,r.width,r.height]));const l=document.querySelector('label[for="'+s.slice(1)+'"]')||e.closest('label')||e.parentElement.querySelector('label');if(l){const q=l.getBoundingClientRect();o.push(' label '+l.textContent.trim()+' '+JSON.stringify([q.x,q.y+scrollY,q.width,q.height]))}}
 const h=[...document.querySelectorAll('#card h1,#card h2,#card h3,#card .ttl,#card legend')].map(x=>{const q=x.getBoundingClientRect();return x.tagName+' '+x.textContent.trim().slice(0,60)+' '+JSON.stringify([q.x,q.y+scrollY,q.width,q.height])});return o.concat(h).join('\n')}));
await p.evaluate(()=>window.scrollTo(0,0));
await p.screenshot({path:'shots/form_fr_full.png',fullPage:true});
const fl=await p.$('section.flow'); await fl.scrollIntoViewIfNeeded(); await p.waitForTimeout(300);
console.log('FLOW:',(await fl.innerText()).replace(/\s+/g,' '));
console.log(await p.evaluate(()=>{const f=document.querySelector('section.flow');return [...f.querySelectorAll('*')].filter(e=>e.children.length===0&&e.textContent.trim()).map(e=>{const q=e.getBoundingClientRect();return e.tagName+'.'+e.className+' '+e.textContent.trim().slice(0,70)+' '+JSON.stringify([q.x,q.y+scrollY,q.width,q.height].map(Math.round))}).join('\n')}));
// FAQ-Texte (Wortlaut) für die Quellen-Tabelle
await p.evaluate(()=>abrirFaq()); await p.waitForTimeout(700);
console.log(await p.evaluate(()=>[...document.querySelectorAll('#pop .faq-l details')].filter(d=>/original|Apostila|validade/.test(d.querySelector('summary').textContent)).map(d=>d.querySelector('summary').textContent+' :: '+d.querySelector('.faq-a').textContent.replace(/\s+/g,' ')).join('\n')));
await b.close();})().catch(e=>{console.error(e);process.exit(1)});
