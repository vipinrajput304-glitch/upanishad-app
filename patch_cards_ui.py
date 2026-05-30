from pathlib import Path

p = Path("index.html")
text = p.read_text(encoding="utf-8")

old = """.uc{display:flex;align-items:center;gap:14px;padding:14px 16px;margin:0 12px 10px;background:var(--b3);border-radius:16px;border:1px solid var(--bs);cursor:pointer;transition:all 0.2s;position:relative;overflow:hidden;}"""

new = """.uc{display:flex;align-items:center;gap:14px;padding:16px;margin:0 14px 12px;background:linear-gradient(145deg,rgba(255,255,255,0.055),rgba(201,168,76,0.045));border-radius:20px;border:1px solid rgba(201,168,76,0.16);cursor:pointer;transition:transform 0.18s ease,border-color 0.18s ease,background 0.18s ease;position:relative;overflow:hidden;box-shadow:0 10px 30px rgba(0,0,0,0.18);}"""

if old not in text:
    print("Card .uc CSS block not found")
else:
    text = text.replace(old, new)

old2 = """.uc:active{border-color:var(--br);background:var(--b4);}"""

new2 = """.uc:active{transform:scale(.985);border-color:rgba(201,168,76,0.38);background:rgba(201,168,76,0.10);}"""

if old2 in text:
    text = text.replace(old2, new2)

old3 = """.ci{width:50px;height:50px;border-radius:14px;display:flex;align-items:center;justify-content:center;font-size:24px;flex-shrink:0;background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.06);}"""

new3 = """.ci{width:54px;height:54px;border-radius:18px;display:flex;align-items:center;justify-content:center;font-size:25px;flex-shrink:0;background:rgba(255,255,255,0.055);border:1px solid rgba(201,168,76,0.14);box-shadow:inset 0 0 18px rgba(201,168,76,0.05);}"""

if old3 in text:
    text = text.replace(old3, new3)

old4 = """.cn{font-family:'Noto Sans Devanagari',serif;font-size:18px;color:var(--t);margin-bottom:2px;}"""

new4 = """.cn{font-family:'Noto Sans Devanagari',serif;font-size:19px;color:var(--t);margin-bottom:3px;letter-spacing:.2px;}"""

if old4 in text:
    text = text.replace(old4, new4)

old5 = """.ce{font-size:12px;color:var(--td);margin-bottom:3px;}.cd{font-size:11px;color:var(--tf);line-height:1.4;}"""

new5 = """.ce{font-size:12px;color:var(--td);margin-bottom:5px;}.cd{font-size:12px;color:var(--tf);line-height:1.5;}"""

if old5 in text:
    text = text.replace(old5, new5)

p.write_text(text, encoding="utf-8")
print("Card UI patch file created and applied.")
