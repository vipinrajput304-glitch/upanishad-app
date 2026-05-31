from pathlib import Path

p = Path("index.html")
text = p.read_text(encoding="utf-8")

old = """function goM(dir){
  try{stopSp();}catch(e){}
  const mt=MD[CU.id]||[],nx=CMI+dir;
  if(nx<0||nx>=mt.length)return;
  CMI=nx;CTB='meaning';
  const b=document.getElementById('mvb');
  b.style.cssText='transition:opacity 0.15s,transform 0.15s;opacity:0;transform:translateX('+(dir>0?'40px':'-40px')+')';
  setTimeout(()=>{
    renderMV();
    b.style.transform='translateX('+(dir>0?'-30px':'30px')+')';b.style.opacity='0';
    setTimeout(()=>{b.style.cssText='transition:opacity 0.2s,transform 0.2s;opacity:1;transform:translateX(0)';document.getElementById('mvw').scrollTo({top:0,behavior:'smooth'});},30);
  },160);
}"""

new = """function goM(dir){
  try{stopSp();}catch(e){}
  const mt=MD[CU.id]||[],nx=CMI+dir;
  if(nx<0||nx>=mt.length)return;

  const curM=mt[CMI],nextM=mt[nx];
  const curSec=getSec(CU.id,curM.id),nextSec=getSec(CU.id,nextM.id);
  const changedSection=curSec&&nextSec&&curSec!==nextSec;

  CMI=nx;CTB='meaning';
  const b=document.getElementById('mvb');
  b.style.cssText='transition:opacity 0.15s,transform 0.15s;opacity:0;transform:translateX('+(dir>0?'40px':'-40px')+')';
  setTimeout(()=>{
    renderMV();
    if(changedSection){
      toast((dir>0?'नया खंड आरंभ: ':'पिछला खंड: ')+secShortTitle(nextSec));
    }
    b.style.transform='translateX('+(dir>0?'-30px':'30px')+')';b.style.opacity='0';
    setTimeout(()=>{b.style.cssText='transition:opacity 0.2s,transform 0.2s;opacity:1;transform:translateX(0)';document.getElementById('mvw').scrollTo({top:0,behavior:'smooth'});},30);
  },160);
}"""

if old not in text:
    print("ERROR: goM block not found")
else:
    text = text.replace(old, new)
    p.write_text(text, encoding="utf-8")
    print("Section transition notice patch applied")

print()
print("VERIFY:")
for needle in ["changedSection", "नया खंड आरंभ", "पिछला खंड"]:
    print(needle, "=>", needle in p.read_text(encoding="utf-8"))

print()
print("GIT STATUS:")
