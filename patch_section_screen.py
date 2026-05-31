from pathlib import Path

p = Path("index.html")
text = p.read_text(encoding="utf-8")

# 1) Add a new section screen between overview list and mantra reading screen
section_screen = """</div>
<div class="sc" id="slist" style="padding-bottom:20px">
  <div class="lhdr">
    <div class="home-nav-row"><button class="bb" onclick="showList()">← उपनिषद्</button><button class="bb" onclick="showHome()">🏠 Home</button></div>
    <div class="lt"><div class="li" id="si"></div><div><div class="ln" id="snm"></div><div class="ls" id="smeta"></div></div></div>
  </div>
  <div id="sres"></div>
  <div class="lbl" style="padding-top:12px">इस खंड के मंत्र · SECTION MANTRAS</div>
  <div id="sm"></div>
</div>
<div class="sc" id="mvw">"""

if 'id="slist"' not in text:
    text = text.replace('</div>\n<div class="sc" id="mvw">', section_screen)

# 2) Add current section state
text = text.replace(
    "let CU=null,CMI=0,CTR='advaita',CTB='meaning';",
    "let CU=null,CS=null,CMI=0,CTR='advaita',CTB='meaning';"
)

# 3) Make reading back button context-aware
text = text.replace(
    '<button class="mb" onclick="showList()">← सूची</button>',
    '<button class="mb" onclick="backFromReading()">← सूची</button>'
)

# 4) Change section cards to open section screen instead of mantra directly
old_card = """<div class="sec-card" onclick="openM(${s.r[0]-1})"><div class="sec-num">${i+1}</div><div style="flex:1"><div class="sec-name">${s.t}</div><div class="sec-range">Mantras ${s.r[0]}–${s.r[1]}</div></div><div style="color:var(--tf)">›</div></div>"""
new_card = """<div class="sec-card" onclick="openSec(${i})"><div class="sec-num">${i+1}</div><div style="flex:1"><div class="sec-name">${s.t}</div><div class="sec-range">Mantras ${s.r[0]}–${s.r[1]}</div></div><div style="color:var(--tf)">›</div></div>"""
text = text.replace(old_card, new_card)

# 5) Add section screen functions before showList
helper = """
function openSec(i){
  CS=i;
  renderSection();
  showScr('slist');
}

function renderSection(){
  const u=CU,secs=SECTIONS[u.id]||[],sec=secs[CS],mt=MD[u.id]||[];
  if(!u||!sec)return;
  const start=sec.r[0],end=sec.r[1];
  document.getElementById('si').textContent=u.icon;
  document.getElementById('snm').textContent=secShortTitle(sec);
  document.getElementById('smeta').textContent=u.name+' उपनिषद् · Mantras '+start+'–'+end;
  document.getElementById('sres').innerHTML=`
    <div class="toc-card">
      <div class="toc-kicker">Section ${CS+1} · खंड ${CS+1}</div>
      <div class="toc-title">${sec.t}</div>
      <div class="toc-sub">${u.en} · ${u.veda} · इस खंड में मंत्र ${start} से ${end} तक हैं।</div>
      <div class="toc-actions">
        <button class="toc-btn" onclick="openM(${start-1})">ॐ Start Section</button>
      </div>
    </div>
  `;
  document.getElementById('sm').innerHTML=mt.slice(start-1,end).map((m,offset)=>{
    const idx=start-1+offset;
    return`<div class="mi" onclick="openM(${idx})">
      <div class="mn">${m.id}</div>
      <div style="flex:1;min-width:0"><div class="ms">मंत्र ${m.id} · ${m.sk.replace(/\\n/g,' ').substring(0,54)}…</div></div>
      <div style="color:var(--tf);font-size:14px">›</div>
    </div>`;
  }).join('');
}

function backFromReading(){
  if(CS!==null&&CS!==undefined){
    renderSection();
    showScr('slist');
  }else{
    showList();
  }
}
"""

if "function openSec(i)" not in text:
    text = text.replace("function showList(){renderList();showScr('ulist');}", helper + "\nfunction showList(){CS=null;renderList();showScr('ulist');}")
else:
    text = text.replace("function showList(){renderList();showScr('ulist');}", "function showList(){CS=null;renderList();showScr('ulist');}")

p.write_text(text, encoding="utf-8")

print("Section screen patch applied")
print()
print("VERIFY:")
fresh = p.read_text(encoding="utf-8")
for needle in ['id="slist"', 'function openSec(i)', 'function renderSection()', 'function backFromReading()', 'onclick="openSec(${i})"', "let CU=null,CS=null"]:
    print(needle, "=>", needle in fresh)

print()
print("GIT STATUS:")
