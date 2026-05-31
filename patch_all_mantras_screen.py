from pathlib import Path

p = Path("index.html")
text = p.read_text(encoding="utf-8")

# 1) Insert All Mantras screen after section screen
all_screen = """</div>
<div class="sc" id="alist" style="padding-bottom:20px">
  <div class="lhdr">
    <div class="home-nav-row"><button class="bb" onclick="showList()">← उपनिषद्</button><button class="bb" onclick="showHome()">🏠 Home</button></div>
    <div class="lt"><div class="li" id="ai"></div><div><div class="ln" id="anm"></div><div class="ls" id="ameta"></div></div></div>
  </div>
  <div class="toc-card">
    <div class="toc-kicker">Full Index · संपूर्ण सूची</div>
    <div class="toc-title">सभी मंत्र अनुभागवार</div>
    <div class="toc-sub">पूरे उपनिषद् को खंडों के अनुसार देखें और किसी भी मंत्र पर सीधे जाएँ।</div>
  </div>
  <div id="am"></div>
</div>
<div class="sc" id="mvw">"""

if 'id="alist"' not in text:
    text = text.replace('</div>\n<div class="sc" id="mvw">', all_screen)

# 2) Replace temporary All Mantras toast button with real function
text = text.replace(
    '<button class="toc-btn" onclick="toast(\'All Mantras screen next step\')">सभी मंत्र देखें</button>',
    '<button class="toc-btn" onclick="openAllMantras()">सभी मंत्र देखें</button>'
)

# 3) Add functions before openSec
helper = """
function openAllMantras(){
  CS=null;
  renderAllMantras();
  showScr('alist');
}

function renderAllMantras(){
  const u=CU,secs=SECTIONS[u.id]||[],mt=MD[u.id]||[];
  if(!u)return;
  document.getElementById('ai').textContent=u.icon;
  document.getElementById('anm').textContent=u.name+' उपनिषद्';
  document.getElementById('ameta').textContent=u.en+' · '+u.veda+' · '+u.total+' mantras';
  document.getElementById('am').innerHTML=secs.map((sec,si)=>{
    const start=sec.r[0],end=sec.r[1];
    const items=mt.slice(start-1,end).map((m,offset)=>{
      const idx=start-1+offset;
      return`<div class="mi" onclick="openM(${idx})">
        <div class="mn">${m.id}</div>
        <div style="flex:1;min-width:0"><div class="ms">मंत्र ${m.id} · ${m.sk.replace(/\\n/g,' ').substring(0,54)}…</div></div>
        <div style="color:var(--tf);font-size:14px">›</div>
      </div>`;
    }).join('');
    return`
      <div class="lbl" style="padding-top:${si===0?'4px':'16px'}">खंड ${si+1} · ${secShortTitle(sec)}</div>
      <div class="sec-list">${items}</div>
    `;
  }).join('');
}
"""

if "function openAllMantras()" not in text:
    text = text.replace("function openSec(i){", helper + "\nfunction openSec(i){")

p.write_text(text, encoding="utf-8")

print("All Mantras grouped screen patch applied")
print()
print("VERIFY:")
fresh = p.read_text(encoding="utf-8")
for needle in ['id="alist"', 'function openAllMantras()', 'function renderAllMantras()', 'onclick="openAllMantras()"', 'सभी मंत्र अनुभागवार']:
    print(needle, "=>", needle in fresh)

print()
print("GIT STATUS:")
