from pathlib import Path

p = Path("index.html")
text = p.read_text(encoding="utf-8")

extra_css = """
.sacred-row{
  display:flex;
  justify-content:center;
  align-items:center;
  gap:14px;
  margin-bottom:10px;
  color:rgba(232,201,122,.72);
  font-size:15px;
  letter-spacing:4px;
}
.sacred-line{
  width:54px;
  height:1px;
  background:linear-gradient(90deg,transparent,rgba(201,168,76,.55),transparent);
}
.mantra-chip{
  display:inline-flex;
  align-items:center;
  justify-content:center;
  margin:14px auto 0;
  padding:7px 13px;
  border-radius:999px;
  color:rgba(232,201,122,.86);
  background:rgba(201,168,76,.075);
  border:1px solid rgba(201,168,76,.16);
  font-family:'Noto Sans Devanagari',serif;
  font-size:12px;
  letter-spacing:.6px;
}
.home-nav-row{
  display:flex;
  justify-content:space-between;
  align-items:center;
  gap:10px;
  margin-bottom:12px;
}
.home-mini{
  min-width:44px;
}
"""

if ".sacred-row{" not in text:
    text = text.replace("</style>", extra_css + "\n</style>")

old_header = """    <div class="om">ॐ</div>
    <div class="ht">उपनिषद् ज्ञान कोश</div>
    <div class="hs">Upanishad Wisdom Library</div>
    <div class="hd">Sanskrit · Hindi · English · Built-in Chanting</div>
    <div class="hero-note">शांत अध्ययन के लिए एक सरल ग्रंथालय — मंत्र, अर्थ, शब्द-विच्छेद और चिंतन एक ही स्थान पर।</div>"""

new_header = """    <div class="sacred-row"><span class="sacred-line"></span><span>॥ ॐ ॥</span><span class="sacred-line"></span></div>
    <div class="om">ॐ</div>
    <div class="ht">उपनिषद् ज्ञान कोश</div>
    <div class="hs">Upanishad Wisdom Library</div>
    <div class="hd">श्रुति · ध्यान · ज्ञान</div>
    <div class="mantra-chip">असतो मा सद्गमय · तमसो मा ज्योतिर्गमय</div>
    <div class="hero-note">शांत अध्ययन के लिए एक सरल ग्रंथालय — मंत्र, अर्थ, शब्द-विच्छेद और चिंतन एक ही स्थान पर।</div>"""

if old_header in text:
    text = text.replace(old_header, new_header)
else:
    print("Header block not found")

text = text.replace(
    '<button class="bb" onclick="showHome()">← वापस</button>',
    '<div class="home-nav-row"><button class="bb" onclick="showHome()">← वापस</button><button class="bb" onclick="showHome()">🏠 Home</button></div>'
)

text = text.replace(
    '<button class="mb" onclick="showList()">← सूची</button>',
    '<div style="display:flex;gap:8px;align-items:center"><button class="mb" onclick="showList()">← सूची</button><button class="mb home-mini" onclick="showHome()">🏠</button></div>'
)

p.write_text(text, encoding="utf-8")
print("Header authenticity and home buttons patch created/applied")
