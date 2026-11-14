// LinkedIn-Dokument: gleiche Folien als PDF (Vektortext), Folie 9 mit /orcamento statt "link na bio".
const {chromium}=require('/opt/node-tools/node_modules/playwright');
(async()=>{
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
const p=await b.newPage({viewport:{width:1080,height:1350}});
await p.goto('file://'+__dirname+'/carousel.html');
await p.evaluate(()=>document.fonts.ready);
await p.evaluate(()=>{
 document.getElementById('ctaChipT').textContent='Preço na hora no site';
 const u=document.getElementById('ctaUrl'); u.textContent='traduzme.com.br/orcamento'; u.parentElement.style.fontSize='54px';
 const st=document.createElement('style'); st.textContent='@page{size:1080px 1350px;margin:0} html,body{background:none} .slide+.slide{margin-top:0} .slide{break-after:page}';
 document.head.appendChild(st);});
const chk=await p.evaluate(()=>{const s=document.getElementById('s9').getBoundingClientRect(); return [...document.querySelectorAll('#s9 .row,#ctaChip')].map(e=>Math.round(e.scrollWidth)+' '+Math.round(s.right-e.getBoundingClientRect().right)+' right-gap')});
console.log(chk);
const s9=await p.$('#s9'); await s9.screenshot({path:'out/slide_09_linkedin.png'});
await p.pdf({path:'out/carousel01_antecedentes_linkedin.pdf',width:'1080px',height:'1350px',printBackground:true,pageRanges:'1-9'});
await b.close();})();
