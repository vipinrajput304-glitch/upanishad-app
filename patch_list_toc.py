from pathlib import Path

p = Path("index.html")
text = p.read_text(encoding="utf-8")

extra_css = """
.toc-card{
  margin:12px 16px;
  padding:16px;
  border-radius:18px;
  background:linear-gradient(145deg,rgba(201,168,76,.09),rgba(255,255,255,.035));
  border:1px solid rgba(201,168,76,.18);
}
.toc-kicker{
  font-size:10px;
  letter-spacing:2.5px;
  color:var(--tf);
  text-transform:uppercase;
  margin-bottom:7px;
}
.toc-title{
  font-family:'Noto Sans Devanagari',serif;
  font-size:17px;
  color:var(--gl);
  margin-bottom:5px;
}
.toc-sub{
  font-size:12px;
  color:var(--td);
  line-height:1.45;
}
.toc-actions{
  display:flex;
  gap:8px;
  margin-top:12px;
}
.toc-btn{
  flex:1;
  border:1px solid rgba(201,168,76,.22);
  background:rgba(201,168,76,.08);
  color:var(--gl);
  border-radius:14px;
  padding:10px 12px;
  font-family:'Noto Sans Devanagari',serif;
  font-size:13px;
}
.sec-list{
  padding:0 16px 6px;
}
.sec-card{
  display:flex;
  align-items:center;
  gap:12px;
  margin-bottom:10px;
  padding:14px;
  border-radius:16px;
  background:rgba(255,255,255,.035);
  border:1px solid rgba(201,168,76,.12);
  cursor:pointer;
}
.sec-num{
  width:38px;
  height:38px;
  border-radius:13px;
  display:flex;
  align-items:center;
  justify-content:center;
  color:#080705;
  background:linear-gradient(135deg,var(--gl),var(--g));
  font-weight:600;
  flex-shrink:0;
}
.sec-name{
  font-family:'Noto Sans Devanagari',serif;
  font-size:14px;
  color:var(--t);
  margin-bottom:3px;
}
.sec-range{
  font-size:11px;
  color:var(--td);
}
"""
if ".toc-card{" not in text:
    text = text.replace("</style>", extra_css + "\n</style>")

section_js = """
const SECTIONS={
  isha:[
    {t:'आरंभिक दृष्टि · Divine Presence',r:[1,1]},
    {t:'कर्म, त्याग और आत्मा · Action & Self',r:[2,8]},
    {t:'विद्या और अविद्या · Knowledge & Ignorance',r:[9,14]},
    {t:'अंतिम प्रार्थना · Final Prayer',r:[15,18]}
  ],
  mandukya:[
    {t:'ॐ और आत्मा · OM & Self',r:[1,2]},
    {t:'चेतना की चार अवस्थाएँ · Four States',r:[3,7]},
    {t:'अ, उ, म और मौन · A-U-M & Silence',r:[8,12]}
  ],
  aitareya:[
    {t:'सृष्टि-विचार · Creation',r:[1,10]},
    {t:'आत्मा का प्रवेश · Entry of Self',r:[11,20]},
    {t:'प्रज्ञानं ब्रह्म · Consciousness is Brahman',r:[21,33]}
  ]
};
"""

if "const SECTIONS={" not in text:
    text = text.replace("const MD={isha:ISHA,mandukya:MAND,aitareya:AITA};", "const MD={isha:ISHA,mandukya:MAND,aitareya:AITA};\n"+section_js)

old = """function renderList(){
  const u=CU,prog=gP(),last=prog[u.id]??0,mt=MD[u.id]||[];
  document.getElementById('li').textContent=u.icon;
  document.getElementById('ln').textContent=u.name+' उपनिषद्';
  document.getElementById('ls').textContent=u.en+' · '+u.veda+' · '+u.total+' mantras';
  document.getElementById('lres').innerHTML=last>0&&mt.length>last?
    `<div class="res" onclick="openM(${last})"><div class="ri">📖</div><div class="rt"><div class="rl">Last read — continue from</div><div class="rm">मंत्र ${mt[last].id}</div></div><div class="ra">›</div></div>`:'';
  document.getElementById('lm').innerHTML=mt.map((m,i)=>{
    const done=i<last,cur=i===last;
    return`<div class="mi ${cur?'cur':''}" onclick="openM(${i})">
      <div class="mn ${done?'dn':''} ${cur?'cr':''}">${done?'✓':m.id}</div>
      <div style="flex:1;min-width:0"><div class="ms">${m.sk.replace(/\\n/g,' ').substring(0,58)}…</div></div>
      <div style="color:var(--tf);font-size:14px">›</div></div>`;
  }).join('');
}"""

new = """function renderList(){
  const u=CU,prog=gP(),last=prog[u.id]??0,mt=MD[u.id]||[],secs=SECTIONS[u.id]||[];
  document.getElementById('li').textContent=u.icon;
  document.getElementById('ln').textContent=u.name+' उपनिषद्';
  document.getElementById('ls').textContent=u.en+' · '+u.veda+' · '+u.total+' mantras';

  const resumeIdx=last>0?Math.min(last,mt.length-1):0;
  document.getElementById('lres').innerHTML=`
    <div class="toc-card">
      <div class="toc-kicker">Resume · पुनः आरंभ</div>
      <div class="toc-title">${last>0?'मंत्र '+mt[resumeIdx].id+' से जारी रखें':'पहले मंत्र से आरंभ करें'}</div>
      <div class="toc-sub">${last>0?'आपकी पिछली पढ़ाई यहाँ तक सुरक्षित है।':'इस उपनिषद् का अध्ययन क्रम से शुरू करें।'}</div>
      <div class="toc-actions">
        <button class="toc-btn" onclick="openM(${resumeIdx})">📖 Continue</button>
        <button class="toc-btn" onclick="openM(0)">ॐ Start</button>
      </div>
    </div>
    ${secs.length?'<div class="lbl">अध्याय / खंड · SECTIONS</div><div class="sec-list">'+secs.map((s,i)=>`<div class="sec-card" onclick="openM(${s.r[0]-1})"><div class="sec-num">${i+1}</div><div style="flex:1"><div class="sec-name">${s.t}</div><div class="sec-range">Mantras ${s.r[0]}–${s.r[1]}</div></div><div style="color:var(--tf)">›</div></div>`).join('')+'</div>':''}
  `;

  document.getElementById('lm').innerHTML=mt.map((m,i)=>{
    const done=i<last,cur=i===last;
    return`<div class="mi ${cur?'cur':''}" onclick="openM(${i})">
      <div class="mn ${done?'dn':''} ${cur?'cr':''}">${done?'✓':m.id}</div>
      <div style="flex:1;min-width:0"><div class="ms">मंत्र ${m.id} · ${m.sk.replace(/\\n/g,' ').substring(0,46)}…</div></div>
      <div style="color:var(--tf);font-size:14px">›</div></div>`;
  }).join('');
}"""

if old not in text:
    print("renderList block not found")
else:
    text = text.replace(old, new)

p.write_text(text, encoding="utf-8")
print("TOC and resume patch applied")
