from pathlib import Path

p = Path("index.html")
text = p.read_text(encoding="utf-8")

extra_css = """
.hero-note{
  margin:18px auto 0;
  max-width:330px;
  color:var(--td);
  font-size:15px;
  line-height:1.65;
  text-align:center;
}
.hero-actions{
  display:grid;
  grid-template-columns:1fr;
  gap:10px;
  padding:0 16px;
  margin:18px 0 10px;
}
.hero-btn{
  width:100%;
  border:none;
  border-radius:18px;
  padding:15px 16px;
  font-family:'Noto Sans Devanagari',serif;
  font-size:15px;
  cursor:pointer;
  transition:transform .18s ease, border-color .18s ease, background .18s ease;
}
.hero-btn:active{
  transform:scale(.98);
}
.hero-primary{
  color:#080705;
  background:linear-gradient(135deg,var(--gl),var(--g));
  box-shadow:0 12px 34px rgba(201,168,76,.18);
}
.hero-secondary{
  color:var(--gl);
  background:rgba(201,168,76,.08);
  border:1px solid var(--br);
}
.section-hint{
  padding:0 16px 12px;
  color:var(--td);
  font-size:13px;
  line-height:1.5;
}
"""

if ".hero-note{" not in text:
    text = text.replace("</style>", extra_css + "\n</style>")

old = """  <div class="hdr">
    <div class="om">ॐ</div>
    <div class="ht">उपनिषद् ज्ञान कोश</div>
    <div class="hs">Upanishad Wisdom Library</div>
    <div class="hd">Sanskrit · Hindi · English · Built-in Chanting</div>
  </div>
  <div class="sbar">"""

new = """  <div class="hdr">
    <div class="om">ॐ</div>
    <div class="ht">उपनिषद् ज्ञान कोश</div>
    <div class="hs">Upanishad Wisdom Library</div>
    <div class="hd">Sanskrit · Hindi · English · Built-in Chanting</div>
    <div class="hero-note">शांत अध्ययन के लिए एक सरल ग्रंथालय — मंत्र, अर्थ, शब्द-विच्छेद और चिंतन एक ही स्थान पर।</div>
  </div>
  <div class="hero-actions">
    <button class="hero-btn hero-primary" onclick="document.getElementById('cards').scrollIntoView({behavior:'smooth'})">अध्ययन शुरू करें · Start Reading</button>
    <button class="hero-btn hero-secondary" onclick="document.getElementById('cards').scrollIntoView({behavior:'smooth'})">उपनिषद् देखें · Explore Library</button>
  </div>
  <div class="sbar">"""

if old in text:
    text = text.replace(old, new)
else:
    print("Header block not found")

old2 = """  <div class="lbl">चुनें · SELECT UPANISHAD</div>
  <div id="cards"></div>"""

new2 = """  <div class="lbl">चुनें · SELECT UPANISHAD</div>
  <div class="section-hint">जिस उपनिषद् से आरंभ करना चाहें, उसे चुनें। आपकी पढ़ाई की प्रगति इसी उपकरण में सुरक्षित रहेगी।</div>
  <div id="cards"></div>"""

if old2 in text and "आपकी पढ़ाई की प्रगति" not in text:
    text = text.replace(old2, new2)

p.write_text(text, encoding="utf-8")
print("Home UI patch file executed successfully")
