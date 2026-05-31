from pathlib import Path
import re

p = Path("index.html")
text = p.read_text(encoding="utf-8")

old = """<div class="pn ${CTB==='reflection'?'on':''}" id="p-reflection">
  <div class="lbl" style="padding-top:2px">व्याख्या · COMMENTARY</div>
  <div class="tt">
    ${trads.map(t=>`<button class="tbt ${tcls[t]} ${CTR===t?'on':''}" onclick="swTr('${t}')">${tnames[t]}</button>`).join('')}
  </div>
  ${trads.map(t=>{const c=m.cm[t]||{};return`<div class="cb ${CTR===t?'on':''}" id="cb-${t}" style="background:${tbg[t]};border:1px solid ${tbd[t]}"><div class="cba" style="color:${tcol[t]}">${c.a||''}</div><div class="chi">${c.h||''}</div><div class="cen">${c.en||''}</div>${c.ins?`<div class="ci2" style="color:${tcol[t]};border-color:${tcol[t]}">${c.ins}</div>`:''}</div>`;}).join('')}
  <div class="lbl" style="padding-top:12px">गहराई · DEEP REFLECTION</div>
  ${m.dp&&m.dp.length?m.dp.map((d,i)=>`<div class="di" id="di${i}"><div class="dq" onclick="tD(${i})"><div class="dqt">${d.q}</div><div class="da2">▼</div></div><div class="da"><div class="dai">${d.a}</div></div></div>`).join('')
  :'<p style="padding:20px;text-align:center;color:var(--tf)">Coming soon</p>'}
</div>`;"""

new = """<div class="pn ${CTB==='reflection'?'on':''}" id="p-reflection">
  <div class="lbl" style="padding-top:2px">परंपरा दृष्टि · TRADITION VIEWS</div>
  ${trads.map(t=>{
    const c=m.cm[t]||{};
    const label=t==='advaita'?'अद्वैत':t==='vishisht'?'विशिष्टाद्वैत':'Integral View';
    return `<div class="cb on trad-card" style="background:${tbg[t]};border:1px solid ${tbd[t]}">
      <div class="cba" style="color:${tcol[t]}">${c.a||''} · ${label}</div>
      <div class="chi">${c.h||''}</div>
      <div class="cen">${c.en||''}</div>
      ${c.ins?`<div class="ci2" style="color:${tcol[t]};border-color:${tcol[t]}">${c.ins}</div>`:''}
    </div>`;
  }).join('')}
  <div class="lbl" style="padding-top:12px">मनन प्रश्न · REFLECTION QUESTIONS</div>
  ${m.dp&&m.dp.length?m.dp.map((d,i)=>`<div class="di" id="di${i}"><div class="dq" onclick="tD(${i})"><div class="dqt">${d.q}</div><div class="da2">▼</div></div><div class="da"><div class="dai">${d.a}</div></div></div>`).join('')
  :'<p style="padding:20px;text-align:center;color:var(--tf)">Coming soon</p>'}
</div>`;"""

if old not in text:
    print("ERROR: reflection block not found")
else:
    text = text.replace(old, new)
    print("Reflection block replaced")

css = ".trad-card{display:block!important;margin-bottom:12px;}"
if ".trad-card{" not in text:
    text = text.replace(".meaning-section{margin-bottom:14px;}", ".meaning-section{margin-bottom:14px;}\n" + css)
    print("Trad card CSS inserted")
else:
    print("Trad card CSS already exists")

p.write_text(text, encoding="utf-8")

print()
print("VERIFY:")
fresh = p.read_text(encoding="utf-8")
for needle in [
    "परंपरा दृष्टि · TRADITION VIEWS",
    "class=\"cb on trad-card\"",
    "मनन प्रश्न · REFLECTION QUESTIONS",
    "class=\"tt\"",
    "onclick=\"swTr",
    "id=\"cb-${t}\""
]:
    print(needle, "=>", needle in fresh)

print()
print("Extracting script for syntax check")
m = re.search(r"<script>(.*)</script>", fresh, re.S)
if not m:
    print("ERROR: script block not found")
else:
    Path("upanishad_app_check.js").write_text(m.group(1), encoding="utf-8")
    print("Script extracted")
