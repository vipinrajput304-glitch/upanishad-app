from pathlib import Path

p = Path("index.html")
text = p.read_text(encoding="utf-8")

replacements = {
    ".mvb{padding:16px 14px 140px;}":
    ".mvb{padding:18px 14px 150px;max-width:720px;margin:0 auto;}",

    ".sk{background:linear-gradient(135deg,rgba(201,168,76,0.1),rgba(201,168,76,0.03));border:1px solid var(--br);border-radius:18px;padding:22px 18px;margin-bottom:14px;position:relative;overflow:hidden;}":
    ".sk{background:linear-gradient(135deg,rgba(201,168,76,0.12),rgba(201,168,76,0.035));border:1px solid rgba(201,168,76,0.22);border-radius:22px;padding:26px 20px;margin-bottom:16px;position:relative;overflow:hidden;box-shadow:0 14px 36px rgba(0,0,0,.20);}",

    ".skt{font-family:'Noto Sans Devanagari',serif;font-size:18px;color:var(--gl);line-height:2.2;text-align:center;white-space:pre-line;}":
    ".skt{font-family:'Noto Sans Devanagari',serif;font-size:20px;color:var(--gl);line-height:2.35;text-align:center;white-space:pre-line;letter-spacing:.2px;}",

    ".ro{font-family:'EB Garamond',serif;font-style:italic;font-size:13px;color:var(--td);text-align:center;line-height:1.8;margin-top:14px;padding-top:12px;border-top:1px solid rgba(255,255,255,0.05);}":
    ".ro{font-family:'EB Garamond',serif;font-style:italic;font-size:14px;color:var(--td);text-align:center;line-height:1.9;margin-top:16px;padding-top:14px;border-top:1px solid rgba(255,255,255,0.06);}",

    ".mhi{font-family:'Noto Sans Devanagari',serif;font-size:15px;line-height:2.1;color:var(--t);font-weight:300;}":
    ".mhi{font-family:'Noto Sans Devanagari',serif;font-size:16px;line-height:2.15;color:var(--t);font-weight:300;}",

    ".men{font-family:'EB Garamond',serif;font-style:italic;font-size:16px;line-height:1.85;color:var(--td);}":
    ".men{font-family:'EB Garamond',serif;font-style:italic;font-size:17px;line-height:1.9;color:var(--td);}",

    ".pt{position:fixed;bottom:0;left:0;right:0;background:rgba(8,7,5,0.96);backdrop-filter:blur(20px);border-top:1px solid var(--br);padding:12px 16px 22px;z-index:100;}":
    ".pt{position:fixed;bottom:0;left:0;right:0;background:rgba(8,7,5,0.97);backdrop-filter:blur(22px);border-top:1px solid rgba(201,168,76,0.22);padding:13px 16px 24px;z-index:100;box-shadow:0 -12px 34px rgba(0,0,0,.28);}",

    ".ptb{width:50px;height:50px;border-radius:50%;background:var(--b4);border:1px solid var(--br);color:var(--g);font-size:22px;cursor:pointer;display:flex;align-items:center;justify-content:center;transition:all 0.2s;flex-shrink:0;}":
    ".ptb{width:52px;height:52px;border-radius:50%;background:var(--b4);border:1px solid rgba(201,168,76,0.22);color:var(--g);font-size:23px;cursor:pointer;display:flex;align-items:center;justify-content:center;transition:all 0.2s;flex-shrink:0;}"
}

changed = 0
for old, new in replacements.items():
    if old in text:
        text = text.replace(old, new)
        changed += 1
    else:
        print("Not found:", old[:60])

p.write_text(text, encoding="utf-8")
print(f"Reading UI patch applied. Changes: {changed}")
