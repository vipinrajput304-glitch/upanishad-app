from pathlib import Path

p = Path("index.html")
text = p.read_text(encoding="utf-8")

old_words_block = """<div class="pn ${CTB==='words'?'on':''}" id="p-words">
  ${m.ws&&m.ws.length?`
  <div class="wh"><span>संस्कृत</span><span>हिंदी</span><span>English</span></div>
  ${m.ws.map(w=>`<div class="wr"><div class="ws">${w.s}</div><div class="whi">${w.h}</div><div class="we">${w.e}</div></div>`).join('')}
  ${m.gr?`<div class="gn"><div class="gnl">Grammatical Note</div><div class="gnt">${m.gr}</div></div>`:''}`
  :'<p style="padding:20px;text-align:center;color:var(--tf)">Coming soon</p>'}
</div>"""

new_words_block = """<div class="pn ${CTB==='words'?'on':''}" id="p-words">
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

if old_words_block not in text:
    print("ERROR: old words block not found")
else:
    text = text.replace(old_words_block, new_words_block)
    print("Words block replaced with flowing layout")

css_insert = """
.wnote{background:var(--b3);border:1px solid rgba(214,168,79,.16);border-radius:16px;padding:16px 16px;margin-bottom:12px;}
.wflow{font-family:'Noto Sans Devanagari',serif;font-size:15px;line-height:2;color:var(--t);}
.wflow.en{font-family:'EB Garamond',serif;font-size:16px;line-height:1.9;color:var(--td);}
.wpair{display:inline;}
.wpair strong{font-family:'Noto Sans Devanagari',serif;color:var(--gl);font-weight:600;}
.dash{color:var(--tf);}
.sep{color:rgba(214,168,79,.42);padding:0 7px;}
"""

if ".wnote{" not in text:
    text = text.replace(".gn{", css_insert + "\n.gn{")
    print("Flow word CSS inserted")
else:
    print("WARNING: .wnote CSS already exists, not inserting duplicate")

p.write_text(text, encoding="utf-8")

print()
print("VERIFY:")
fresh = p.read_text(encoding="utf-8")
for needle in ["संस्कृत → हिंदी", "Sanskrit → English", "class=\"wflow\"", "class=\"sep\">॥</span>", ".wnote{", ".wflow.en"]:
    print(needle, "=>", needle in fresh)

print()
print("GIT STATUS:")
