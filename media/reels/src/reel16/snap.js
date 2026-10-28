// Render für Reel 16 (PNG-Frames, parallel). Aufruf:
//   node snap.js frames [main|gmb] [outDir]      -> outDir/f00000.png …  (END aus reel.html)
//   node snap.js snap [main|gmb] t1 t2 …          -> qa/snap_<cut>_<t>.png
const {chromium}=require('/opt/node-tools/node_modules/playwright');
const fs=require('fs'),path=require('path');
(async()=>{const mode=process.argv[2]||'frames', cut=process.argv[3]||'main';
const url='file://'+__dirname+'/reel.html'+(cut==='gmb'?'?cut=gmb':'');
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
const open=async()=>{const p=await b.newPage({viewport:{width:1080,height:1920},deviceScaleFactor:1}); await p.goto(url); await p.waitForFunction(()=>window.READY===true); return p;};
if(mode==='snap'){const p=await open(); fs.mkdirSync(path.join(__dirname,'qa'),{recursive:true});
  for(const t of process.argv.slice(4)){await p.evaluate(t=>render(t),+t); await p.screenshot({path:path.join(__dirname,'qa',`snap_${cut}_${t}.png`)});}}
else{const out=process.argv[4]||path.join(__dirname,'frames_'+cut); fs.rmSync(out,{recursive:true,force:true}); fs.mkdirSync(out,{recursive:true});
  const p0=await open(); const end=await p0.evaluate(()=>END); const n=Math.round(end*30); const J=+(process.env.JOBS||4);
  const pages=[p0]; for(let j=1;j<J;j++) pages.push(await open());
  let next=0; await Promise.all(pages.map(async p=>{while(true){const i=next++; if(i>=n)break;
    await p.evaluate(t=>render(t),i/30); await p.screenshot({path:path.join(out,`f${String(i).padStart(5,'0')}.png`)});}}));
  console.log(`${n} Frames (${end}s, ${cut}) -> ${out}`);}
await b.close();})().catch(e=>{console.error(e);process.exit(1)});
