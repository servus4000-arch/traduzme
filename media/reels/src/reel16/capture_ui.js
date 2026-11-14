// Echte Rechner-Screenshots (traduzme.com.br/orcamento-app) für Reel 16.
// Die Preis-API (pix-config) ist aus der Sandbox nicht erreichbar -> nur IM BROWSER gemockt, damit das Formular rendert.
// Preise/Datum erscheinen im Reel nie lesbar (unscharf). Live-Seite unverändert.
const {chromium}=require('/opt/node-tools/node_modules/playwright');
const fs=require('fs');fs.mkdirSync('shots',{recursive:true});
(async()=>{const px=process.env.HTTPS_PROXY;
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',proxy:px?{server:px}:undefined});
// Dummy-Urkunde (Vektor, keine echten Daten)
const d=await b.newPage({viewport:{width:900,height:1200}});
await d.setContent(`<body style="margin:0;background:#f4efe4;font-family:serif"><div style="margin:60px;border:6px double #8a7a5a;height:1060px;padding:50px;box-sizing:border-box"><h1 style="text-align:center;letter-spacing:4px">HEIRATSURKUNDE</h1>${'<div style="height:14px;background:#cfc6b2;margin:28px 0;border-radius:7px"></div>'.repeat(14)}</div></body>`);
await d.screenshot({path:'shots/heiratsurkunde.jpg',type:'jpeg'});
await d.setContent(`<body style="margin:0;background:#f4efe4;font-family:serif"><div style="margin:60px;border:6px solid #8a7a5a;height:1060px;padding:50px;box-sizing:border-box"><h1 style="text-align:center;letter-spacing:4px">APOSTILLE</h1><p style="text-align:center;font-style:italic">(Convention de La Haye du 5 octobre 1961)</p>${'<div style="height:14px;background:#cfc6b2;margin:28px 0;border-radius:7px"></div>'.repeat(12)}</div></body>`);
await d.screenshot({path:'shots/heiratsurkunde-apostille.jpg',type:'jpeg'});
const lang=process.argv[2]||'de';
const c=await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:3,isMobile:true,locale:lang==='de'?'de-DE':'pt-BR'});
const p=await c.newPage();
p.on('console',m=>{if(m.type()==='error')console.log('console:',m.text().slice(0,200))});
let real=false;
await p.route('**/functions/v1/pix-config',async r=>{
  try{const resp=await r.fetch({timeout:8000}); if(resp.status()===200){real=true;console.log('API echt');return r.fulfill({response:resp});} console.log('API status',resp.status(),'-> Mock');}catch(e){console.log('API nicht erreichbar -> Mock');}
  const cap={ativo:true,express_max_pag:0,express_fix_cents:0,express48_max_pag:0,express48_fix_cents:0,normal_dias:3,longo_dias:5,max_pag_auto:30,limite_dia_pag:100,cutoff_hora:18,nome_pt:'Alemão',fisica_ativa:false};
  r.fulfill({status:200,contentType:'application/json',body:JSON.stringify({ok:true,agora:new Date().toISOString(),idiomas:{de:cap},precos:[{categoria:'documento',idioma:'de',direcao:'to_pt',chave:'certidao de casamento',ordem:1,valor_cents:100},{categoria:'lauda',idioma:'de',direcao:'to_pt',chave:'comum',valor_cents:100}],feriados:[],uso:{}})});
});
await p.goto('https://www.traduzme.com.br/orcamento-app/?lang='+lang,{waitUntil:'networkidle',timeout:60000});
await p.waitForTimeout(1500);
await p.screenshot({path:`shots/${lang}_0_top.png`});
await p.screenshot({path:`shots/${lang}_0_full.png`,fullPage:true});
await p.setInputFiles('#file',['shots/heiratsurkunde.jpg','shots/heiratsurkunde-apostille.jpg']);
await p.waitForTimeout(2000);
await p.selectOption('#from','Alemão'); await p.waitForTimeout(300);
await p.selectOption('#to','Português'); await p.waitForTimeout(800);
await p.evaluate(()=>window.scrollTo(0,0));
await p.screenshot({path:`shots/${lang}_1_full.png`,fullPage:true});
const card=await p.$('#card'); console.log('card',JSON.stringify(card?await card.boundingBox():null));
const ids=await p.$$eval('button',bs=>bs.filter(b=>b.offsetParent).map(b=>(b.id||'')+':'+b.textContent.trim().slice(0,30)));console.log(ids.join(' | '));
// Preis berechnen
const calc=await p.$('#calc')||await p.$('button.cta');
await p.click('text=/Preis berechnen|Calcular preço/'); await p.waitForTimeout(4000);
await p.screenshot({path:`shots/${lang}_2_full.png`,fullPage:true});
fs.writeFileSync(`shots/${lang}_dom2.html`,await p.content());
try{await p.click('text=/^\\s*(Weiter|Continuar)\\s*$/',{timeout:5000}); await p.waitForTimeout(1500);
await p.screenshot({path:`shots/${lang}_3_full.png`,fullPage:true});
await p.click('#opt-estr'); await p.waitForTimeout(700);
await p.screenshot({path:`shots/${lang}_4_full.png`,fullPage:true});}catch(e){console.log('weiter fail',e.message.slice(0,200))}
await b.close();})().catch(e=>{console.error(e);process.exit(1)});
