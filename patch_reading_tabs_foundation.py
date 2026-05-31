from pathlib import Path
import re

p = Path("index.html")
text = p.read_text(encoding="utf-8")

# 1) Make पाठ / path the default tab everywhere
text = text.replace("CTB='meaning'", "CTB='path'")

# 2) Move Sanskrit + chanting player into new पाठ tab and update tab labels
pattern = re.compile(
    r"document\.getElementById\('mvb'\)\.innerHTML=`\n"
    r"(?P<pathcontent><div class=\"sk\">.*?</div>\n<div class=\"ap\">.*?</div>)\n"
    r"<div class=\"tabs\">\n"
    r"\s*\$\{\['meaning','words','commentary','depth'\]\.map\(t=>`<button class=\"tb \$\{t===CTB\?'on':''\}\" onclick=\"swTab\('\$\{t\}'\)\">"
    r"\$\{t==='meaning'\?'अर्थ':t==='words'\?'शब्द':t==='commentary'\?'व्याख्या':'गहराई'\}</button>`\)\.join\(''\)\}\n"
    r"</div>",
    re.S
)

def replace_tabs(m):
    pathcontent = m.group("pathcontent")
    return """document.getElementById('mvb').innerHTML=`
<div class="tabs">
  ${['path','meaning','words','reflection'].map(t=>`<button class="tb ${t===CTB?'on':''}" onclick="swTab('${t}')">${t==='path'?'पाठ':t==='meaning'?'अर्थ':t==='words'?'शब्द':'चिंतन'}</button>`).join('')}
</div>
<div class="pn ${CTB==='path'?'on':''}" id="p-path">
""" + pathcontent + """
</div>"""

text, tab_replacements = pattern.subn(replace_tabs, text)

# 3) Merge commentary + depth into चिंतन / reflection pane
old_reflection = """<div class="pn ${CTB==='commentary'?'on':''}" id="p-commentary">
  <div class="tt">
    ${trads.map(t=>`<button class="tbt ${tcls[t]} ${CTR===t?'on':''}" onclick="swTr('${t}')">${tnames[t]}</button>`).join('')}
  </div>
  ${trads.map(t=>{const c=m.cm[t]||{};return`<div class="cb ${CTR===t?'on':''}" id="cb-${t}" style="background:${tbg[t]};border:1px solid ${tbd[t]}"><div class="cba" style="color:${tcol[t]}">${c.a||''}</div><div class="chi">${c.h||''}</div><div class="cen">${c.en||''}</div>${c.ins?`<div class="ci2" style="color:${tcol[t]};border-color:${tcol[t]}">${c.ins}</div>`:''}</div>`;}).join('')}
</div>
<div class="pn ${CTB==='depth'?'on':''}" id="p-depth">
  ${m.dp&&m.dp.length?m.dp.map((d,i)=>`<div class="di" id="di${i}"><div class="dq" onclick="tD(${i})"><div class="dqt">${d.q}</div><div class="da2">▼</div></div><div class="da"><div class="dai">${d.a}</div></div></div>`).join('')
  :'<p style="padding:20px;text-align:center;color:var(--tf)">Coming soon</p>'}
</div>`;"""

new_reflection = """<div class="pn ${CTB==='reflection'?'on':''}" id="p-reflection">
  <div class="lbl" style="padding-top:2px">व्याख्या · COMMENTARY</div>
  <div class="tt">
    ${trads.map(t=>`<button class="tbt ${tcls[t]} ${CTR===t?'on':''}" onclick="swTr('${t}')">${tnames[t]}</button>`).join('')}
  </div>
  ${trads.map(t=>{const c=m.cm[t]||{};return`<div class="cb ${CTR===t?'on':''}" id="cb-${t}" style="background:${tbg[t]};border:1px solid ${tbd[t]}"><div class="cba" style="color:${tcol[t]}">${c.a||''}</div><div class="chi">${c.h||''}</div><div class="cen">${c.en||''}</div>${c.ins?`<div class="ci2" style="color:${tcol[t]};border-color:${tcol[t]}">${c.ins}</div>`:''}</div>`;}).join('')}
  <div class="lbl" style="padding-top:12px">गहराई · DEEP REFLECTION</div>
  ${m.dp&&m.dp.length?m.dp.map((d,i)=>`<div class="di" id="di${i}"><div class="dq" onclick="tD(${i})"><div class="dqt">${d.q}</div><div class="da2">▼</div></div><div class="da"><div class="dai">${d.a}</div></div></div>`).join('')
  :'<p style="padding:20px;text-align:center;color:var(--tf)">Coming soon</p>'}
</div>`;"""

if old_reflection in text:
    text = text.replace(old_reflection, new_reflection)
    reflection_replacements = 1
else:
    reflection_replacements = 0
    print("WARNING: old commentary/depth block not found")

p.write_text(text, encoding="utf-8")

print("Reading tabs foundation patch applied")
print("Tab block replacements:", tab_replacements)
print("Reflection merge replacements:", reflection_replacements)
print()
print("VERIFY:")
fresh = p.read_text(encoding="utf-8")
for needle in ["CTB='path'", "'path','meaning','words','reflection'", "id=\"p-path\"", "id=\"p-reflection\"", "पाठ", "चिंतन", "id=\"p-depth\""]:
    print(needle, "=>", needle in fresh)

print()
print("GIT STATUS:")
