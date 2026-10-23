const {chromium}=require('/opt/node-tools/node_modules/playwright');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('file://'+__dirname+'/reel.html');await p.evaluate(()=>document.fonts.ready);
const mode=process.argv[2];
if(mode==='snap'){for(const t of process.argv.slice(3)){await p.evaluate(t=>render(+t),t);await p.screenshot({path:`snap_${t}.png`});}}
else{const fps=30,end=87.1;const fs=require('fs');fs.mkdirSync('frames',{recursive:true});
for(let i=0;i<Math.round(end*fps);i++){await p.evaluate(t=>render(t),i/fps);await p.screenshot({path:`frames/f${String(i).padStart(5,'0')}.jpg`,type:'jpeg',quality:93});}}
await b.close();})();
