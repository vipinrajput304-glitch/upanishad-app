from pathlib import Path

p = Path("index.html")
text = p.read_text(encoding="utf-8")

replacements = {
    ":root{--g:#C9A84C;--gl:#E8C97A;--gd:#7A6130;--bg:#080705;--b3:#151209;--b4:#1c1710;--t:#E8DCC8;--td:#9A8A6A;--tf:#5A4A30;--br:rgba(201,168,76,0.18);--bs:rgba(201,168,76,0.08);--green:#52B788;--pu:#C084D4;--or:#C8956A;}":
    ":root{--g:#D6A84F;--gl:#F0D58A;--gd:#8D672D;--bg:#0B0804;--b3:#171109;--b4:#21180D;--t:#F1E6D0;--td:#C4B28A;--tf:#8B7650;--br:rgba(214,168,79,0.22);--bs:rgba(214,168,79,0.12);--green:#6F8F68;--pu:#B58AC8;--or:#A96D3A;}",

    "body{background:var(--bg);color:var(--t);font-family:'Crimson Pro',Georgia,serif;min-height:100vh;overflow-x:hidden;}":
    "body{background:var(--bg);color:var(--t);font-family:'Crimson Pro',Georgia,serif;min-height:100vh;overflow-x:hidden;}",

    "body::before{content:'';position:fixed;inset:0;background:radial-gradient(ellipse 80% 50% at 80% 10%,rgba(201,168,76,0.05),transparent 60%),radial-gradient(ellipse 60% 80% at 10% 90%,rgba(45,106,79,0.04),transparent 60%);pointer-events:none;z-index:0;}":
    "body::before{content:'';position:fixed;inset:0;background:radial-gradient(ellipse 70% 45% at 80% 8%,rgba(214,168,79,0.045),transparent 62%),radial-gradient(ellipse 55% 75% at 8% 92%,rgba(111,143,104,0.035),transparent 62%);pointer-events:none;z-index:0;}",

    ".lbl{font-size:10px;letter-spacing:3px;color:var(--tf);text-transform:uppercase;padding:0 16px 10px;}":
    ".lbl{font-size:12px;letter-spacing:2.4px;color:var(--gl);text-transform:uppercase;padding:4px 16px 12px;font-weight:600;text-shadow:0 0 14px rgba(214,168,79,.14);}",

    ".ls{font-size:12px;color:var(--td);margin-top:2px;}":
    ".ls{font-size:13px;color:var(--td);margin-top:3px;line-height:1.45;}",

    ".mi{display:flex;align-items:center;gap:12px;padding:13px 16px;margin:0 12px 8px;background:var(--b3);border-radius:14px;border:1px solid var(--bs);cursor:pointer;transition:all 0.2s;}":
    ".mi{display:flex;align-items:center;gap:12px;padding:15px 16px;margin:0 12px 10px;background:linear-gradient(145deg,rgba(241,230,208,.045),rgba(214,168,79,.035));border-radius:16px;border:1px solid rgba(214,168,79,.16);cursor:pointer;transition:all 0.2s;box-shadow:0 8px 22px rgba(0,0,0,.14);}",

    ".ms{font-family:'Noto Sans Devanagari',serif;font-size:14px;color:var(--td);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;}":
    ".ms{font-family:'Noto Sans Devanagari',serif;font-size:15px;color:#D8C9AA;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;line-height:1.55;}",

    ".sec-card{":
    ".sec-card{",

    ".sec-name{\n  font-family:'Noto Sans Devanagari',serif;\n  font-size:14px;\n  color:var(--t);\n  margin-bottom:3px;\n}":
    ".sec-name{\n  font-family:'Noto Sans Devanagari',serif;\n  font-size:15px;\n  color:var(--t);\n  margin-bottom:4px;\n  line-height:1.45;\n}",

    ".sec-range{\n  font-size:11px;\n  color:var(--td);\n}":
    ".sec-range{\n  font-size:12px;\n  color:var(--td);\n  letter-spacing:.3px;\n}"
}

changed = 0
for old, new in replacements.items():
    if old in text:
        text = text.replace(old, new)
        changed += 1
    else:
        if old != ".sec-card{":
            print("NOT FOUND:", old[:80])

text = text.replace(
""".toc-sub{
  font-size:12px;
  color:var(--td);
  line-height:1.45;
}""",
""".toc-sub{
  font-size:13px;
  color:var(--td);
  line-height:1.6;
}"""
)

text = text.replace(
""".toc-title{
  font-family:'Noto Sans Devanagari',serif;
  font-size:17px;
  color:var(--gl);
  margin-bottom:5px;
}""",
""".toc-title{
  font-family:'Noto Sans Devanagari',serif;
  font-size:18px;
  color:var(--gl);
  margin-bottom:6px;
  line-height:1.35;
}"""
)

text = text.replace(
""".sec-list{
  padding:0 16px 6px;
}""",
""".sec-list{
  padding:0 16px 10px;
}"""
)

p.write_text(text, encoding="utf-8")

print(f"Theme identity/readability patch applied. Replacements: {changed}")
print()
print("VERIFY:")
fresh = p.read_text(encoding="utf-8")
for needle in ["#0B0804", "#F1E6D0", "font-size:12px;letter-spacing:2.4px", "color:#D8C9AA", "box-shadow:0 8px 22px"]:
    print(needle, "=>", needle in fresh)

print()
print("GIT STATUS:")
