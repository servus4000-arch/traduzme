// Reel 20: echte Rechner-Screens (Schritt 1, Árabe -> Português) – Live-Seite, iPhone-Viewport 390x844 @3x.
// pix-config gemockt (API aus der Sandbox nicht erreichbar); Schritt 1 zeigt keine Preise.
const {chromium}=require('/opt/node-tools/node_modules/playwright');
(async()=>{const px=process.env.HTTPS_PROXY;
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',proxy:px?{server:px}:undefined});
const d=await b.newPage({viewport:{width:900,height:1200}});
await d.setContent(`<body style="margin:0;background:#f4efe4"><div style="margin:60px;border:6px double #8a7a5a;height:1060px;padding:50px;box-sizing:border-box">${'<div style="height:14px;background:#cfc6b2;margin:34px 0 34px 120px;border-radius:7px"></div>'.repeat(16)}</div></body>`);
await d.screenshot({path:'shots/certidao.jpg',type:'jpeg'});
const code='ar',nome='Árabe';
const c=await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:3,isMobile:true,locale:'pt-BR'});
const p=await c.newPage();
const cap={ativo:true,express_max_pag:0,express_fix_cents:0,express48_max_pag:0,express48_fix_cents:0,normal_dias:0,longo_dias:0,max_pag_auto:0,limite_dia_pag:0,cutoff_hora:0,nome_pt:nome};
await p.route('**/functions/v1/pix-config',r=>r.fulfill({status:200,contentType:'application/json',body:JSON.stringify({ok:true,agora:new Date().toISOString(),idiomas:{[code]:cap},precos:[{categoria:'documento',idioma:code,direcao:'to_pt',chave:'x',ordem:1,valor_cents:0},{categoria:'lauda',idioma:code,direcao:'to_pt',chave:'comum',valor_cents:0}],feriados:[],uso:{}})}));
await p.goto('https://www.traduzme.com.br/orcamento-app/?lang=pt',{waitUntil:'networkidle',timeout:60000});
await p.waitForTimeout(1500);
await p.screenshot({path:'shots/top.png'});
await p.setInputFiles('#file','shots/certidao.jpg');
await p.waitForTimeout(1500);
await p.selectOption('#from',nome); await p.waitForTimeout(300);
await p.selectOption('#to','Português'); await p.waitForTimeout(800);
await p.evaluate(()=>window.scrollTo(0,0));
await p.screenshot({path:'shots/form_ar.png'});
await p.screenshot({path:'shots/form_ar_full.png',fullPage:true});
const rects=await p.evaluate(()=>{const o={};for(const s of ['#card','#from','#to','#file']){const e=document.querySelector(s);if(e){const r=e.getBoundingClientRect();o[s]=[r.left,r.top+scrollY,r.width,r.height];}}
 const btn=[...document.querySelectorAll('button')].find(x=>/Calcular/.test(x.textContent)); if(btn){const r=btn.getBoundingClientRect();o.btn=[r.left,r.top+scrollY,r.width,r.height,btn.textContent.trim()];}
 const ia=[...document.querySelectorAll('*')].filter(e=>e.children.length==0&&/\bIA\b/.test(e.textContent)).map(e=>{const r=e.getBoundingClientRect();return [e.textContent.trim().slice(0,80),r.top+scrollY,r.height]}); o.ia=ia; return o;});
console.log(JSON.stringify(rects,null,1));
await b.close();})().catch(e=>{console.error(e);process.exit(1)});
