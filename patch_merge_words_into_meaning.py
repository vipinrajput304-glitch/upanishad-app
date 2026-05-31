from pathlib import Path
import re

p = Path("index.html")
text = p.read_text(encoding="utf-8")

# 1) Tabs: remove शब्द tab only
old_tabs = """${['path','meaning','words','reflection'].map(t=>`<button class="tb ${t===CTB?'on':''}" onclick="swTab('${t}')">${t==='path'?'पाठ':t==='meaning'?'अर्थ':t==='words'?'शब्द':'चिंतन'}</button>`).join('')}"""
new_tabs = """${['path','meaning','reflection'].map(t=>`<button class="tb ${t===CTB?'on':''}" onclick="swTab('${t}')">${t==='path'?'पाठ':t==='meaning'?'अर्थ':'चिंतन'}</button>`).join('')}"""

if old_tabs not in text:
    print("ERROR: tabs block not found")
else:
    text = text.replace(old_tabs, new_tabs)
    print("Tabs updated")

# 2) Replace meaning + words panes with one merged meaning pane
old_block = """<div class="pn ${CTB==='meaning'?'on':''}" id="p-meaning">
  <div class="mb2"><div class="ml" style="color:var(--green)">हिंदी अर्थ</div><div class="mhi">${m.hi}</div></div>
  <div class="mb2"><div class="ml" style="color:var(--g)">English Meaning</div><div class="men">${m.en}</div></div>
  ${m.mt?`<div class="me"><strong style="color:var(--gd)">छन्द · Metre:</strong> ${m.mt}</div>`:''}
</div>
<div class="pn ${CTB==='words'?'on':''}" id="p-words">
  ${m.ws&&m.ws.length?`
  <div class="wnote">
    <div class="gnl">संस्कृत → हिंदी</div>
    <div class="wflow">
      ${m.ws.map((w,i)=>`<span class="wpair"><strong>${w.s}</strong><span class="dash"> — </span>${w.h}</span>${i<m.ws.length-1?'<span class="sep">॥</span>':''}`).join('')}
    </div>
  </div>
  <div class="wnote">
    <div class="gnl">Sanskrit → English</div>
    <div class="wflow en">
      ${m.ws.map((w,i)=>`<span class="wpair"><strong>${w.s}</strong><span class="dash"> — </span>${w.e}</span>${i<m.ws.length-1?'<span class="sep">॥</span>':''}`).join('')}
    </div>
  </div>
  ${m.gr?`<div class="gn"><div class="gnl">Grammatical Note</div><div class="gnt">${m.gr}</div></div>`:''}`
  :'<p style="padding:20px;text-align:center;color:var(--tf)">Coming soon</p>'}
</div>"""

new_block = """<div class="pn ${CTB==='meaning'?'on':''}" id="p-meaning">
  <div class="meaning-section">
    <div class="lbl" style="padding-top:2px">हिंदी अर्थ · HINDI</div>
    ${m.ws&&m.ws.length?`
    <div class="wnote">
      <div class="gnl">संस्कृत → हिंदी शब्दार्थ</div>
      <div class="wflow">
        ${m.ws.map((w,i)=>`<span class="wpair"><strong>${w.s}</strong><span class="dash"> — </span>${w.h}</span>${i<m.ws.length-1?'<span class="sep">॥</span>':''}`).join('')}
      </div>
    </div>`:''}
    <div class="mb2"><div class="ml" style="color:var(--green)">हिंदी भावार्थ</div><div class="mhi">${m.hi}</div></div>
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
    <div class="mb2"><div class="ml" style="color:var(--g)">English full meaning</div><div class="men">${m.en}</div></div>
  </div>

  ${m.mt?`<div class="me"><strong style="color:var(--gd)">छन्द · Metre:</strong> ${m.mt}</div>`:''}
  ${m.gr?`<div class="gn"><div class="gnl">Grammatical Note</div><div class="gnt">${m.gr}</div></div>`:''}
</div>"""

if old_block not in text:
    print("ERROR: meaning/words block not found")
else:
    text = text.replace(old_block, new_block)
    print("Meaning and words panes merged")

# 3) Small CSS helper
css = ".meaning-section{margin-bottom:14px;}"
if ".meaning-section{" not in text:
    text = text.replace(".wnote{", css + "\n.wnote{")
    print("Meaning section CSS inserted")
else:
    print("Meaning section CSS already exists")

p.write_text(text, encoding="utf-8")

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
    "id=\"p-reflection\""
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
