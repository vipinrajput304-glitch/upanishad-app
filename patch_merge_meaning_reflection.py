from pathlib import Path
import re

p = Path("index.html")
text = p.read_text(encoding="utf-8")

# 1) Tabs: पाठ | अर्थ | चिंतन
text = text.replace(
    "${['path','meaning','words','reflection'].map(t=>`<button class=\"tb ${t===CTB?'on':''}\" onclick=\"swTab('${t}')\">${t==='path'?'पाठ':t==='meaning'?'अर्थ':t==='words'?'शब्द':'चिंतन'}</button>`).join('')}",
    "${['path','meaning','reflection'].map(t=>`<button class=\"tb ${t===CTB?'on':''}\" onclick=\"swTab('${t}')\">${t==='path'?'पाठ':t==='meaning'?'अर्थ':'चिंतन'}</button>`).join('')}"
)

# 2) Merge अर्थ + शब्द into one meaning pane
meaning_words_pattern = re.compile(
    r"""<div class="pn \$\{CTB==='meaning'\?'on':''\}" id="p-meaning">.*?</div>\s*
<div class="pn \$\{CTB==='words'\?'on':''\}" id="p-words">.*?</div>\s*
(?=<div class="pn \$\{CTB==='reflection')""",
    re.S
)

new_meaning = """<div class="pn ${CTB==='meaning'?'on':''}" id="p-meaning">
  <div class="meaning-section">
    <div class="lbl" style="padding-top:2px">हिंदी अर्थ · HINDI</div>
    ${m.ws&&m.ws.length?`
    <div class="wnote">
      <div class="gnl">संस्कृत → हिंदी शब्दार्थ</div>
      <div class="wflow">
        ${m.ws.map((w,i)=>`<span class="wpair"><strong>${w.s}</strong><span class="dash"> — </span>${w.h}</span>${i<m.ws.length-1?'<span class="sep">॥</span>':''}`).join('')}
      </div>
    </div>`:''}
    <div class="mb2">
      <div class="ml" style="color:var(--green)">हिंदी भावार्थ</div>
      <div class="mhi">${m.hi}</div>
    </div>
  </div>

  <div class="meaning-section">
    <div class="lbl" style="padding-top:6px">English Meaning</div>
    ${m.ws&&m.ws.length?`
    <div class="wnote">
      <div class="gnl">Sanskrit → English word meaning</div>
      <div class="wflow en">
        ${m.ws.map((w,i)=>`<span class="wpair"><strong>${w.s}</strong><span class="dash"> — </span>${w.e}</span>${i<m.ws.length-1?'<span class="sep">॥</span>':''}`).join('')}
      </div>
    </div>`:''}
    <div class="mb2">
      <div class="ml" style="color:var(--g)">English full meaning</div>
      <div class="men">${m.en}</div>
    </div>
  </div>

  ${m.mt?`<div class="me"><strong style="color:var(--gd)">छन्द · Metre:</strong> ${m.mt}</div>`:''}
  ${m.gr?`<div class="gn"><div class="gnl">Grammatical Note</div><div class="gnt">${m.gr}</div></div>`:''}
</div>
"""

text, meaning_count = meaning_words_pattern.subn(new_meaning, text)

# 3) Replace चिंतन with scroll-based holistic layout
reflection_pattern = re.compile(
    r"""<div class="pn \$\{CTB==='reflection'\?'on':''\}" id="p-reflection">.*?</div>`;""",
    re.S
)

new_reflection = """<div class="pn ${CTB==='reflection'?'on':''}" id="p-reflection">
  ${m.insight?`
  <div class="gn">
    <div class="gnl">मुख्य संकेत · Key Insight</div>
    <div class="gnt">${m.insight}</div>
  </div>`:''}

  <div class="lbl" style="padding-top:6px">परंपरा दृष्टि · TRADITION VIEWS</div>
  ${trads.map(t=>{
    const c=m.cm[t]||{};
    const label=t==='advaita'?'अद्वैत':t==='vishisht'?'विशिष्टाद्वैत':'Integral View';
    return`<div class="cb on trad-card" style="background:${tbg[t]};border:1px solid ${tbd[t]}">
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

text, reflection_count = reflection_pattern.subn(new_reflection, text)

# 4) Add light CSS helpers
css_insert = """
.meaning-section{margin-bottom:14px;}
.trad-card{display:block!important;margin-bottom:12px;}
"""

if ".meaning-section{" not in text:
    text = text.replace(".wnote{", css_insert + "\n.wnote{")
    css_count = 1
else:
    css_count = 0

p.write_text(text, encoding="utf-8")

print("Merged अर्थ/शब्द and refined चिंतन layout")
print("Meaning merge replacements:", meaning_count)
print("Reflection replacements:", reflection_count)
print("CSS helper inserted:", css_count)
print()
print("VERIFY:")
fresh = p.read_text(encoding="utf-8")
for needle in [
    "'path','meaning','reflection'",
    "id=\"p-words\"",
    "संस्कृत → हिंदी शब्दार्थ",
    "हिंदी भावार्थ",
    "Sanskrit → English word meaning",
    "English full meaning",
    "मुख्य संकेत · Key Insight",
    "परंपरा दृष्टि · TRADITION VIEWS",
    "class=\"cb on trad-card\"",
    "मनन प्रश्न · REFLECTION QUESTIONS"
]:
    print(needle, "=>", needle in fresh)

print()
print("GIT STATUS:")
