from pathlib import Path

p = Path("index.html")
text = p.read_text(encoding="utf-8")

helper = """
function getSec(uid,mid){
  const secs=SECTIONS[uid]||[];
  return secs.find((s,i)=>mid>=s.r[0]&&mid<=s.r[1])||null;
}
function getSecIndex(uid,mid){
  const secs=SECTIONS[uid]||[];
  return secs.findIndex(s=>mid>=s.r[0]&&mid<=s.r[1]);
}
function secShortTitle(sec){
  if(!sec)return 'सामान्य पाठ';
  return sec.t.split('·')[0].trim();
}
"""

if "function getSec(uid,mid)" not in text:
    text = text.replace("function renderMV(){", helper + "\nfunction renderMV(){")

old = """  document.getElementById('mu').textContent=u.name+' उपनिषद्';
  document.getElementById('mm').textContent='मंत्र '+m.id+' of '+u.total;"""

new = """  const sec=getSec(u.id,m.id),secNo=getSecIndex(u.id,m.id)+1;
  document.getElementById('mu').textContent=u.name+' उपनिषद्';
  document.getElementById('mm').textContent=(sec?('खंड '+secNo+' · '+secShortTitle(sec)+' · '):'')+'मंत्र '+m.id+' of '+u.total;"""

if old not in text:
    print("Reading header lines not found")
else:
    text = text.replace(old, new)

old2 = """  document.getElementById('ptl').textContent=u.name+' — मंत्र '+m.id;"""

new2 = """  document.getElementById('ptl').textContent=u.name+' — '+(sec?secShortTitle(sec)+' · ':'')+'मंत्र '+m.id;"""

if old2 in text:
    text = text.replace(old2, new2)

p.write_text(text, encoding="utf-8")
print("Reading section header patch applied")
