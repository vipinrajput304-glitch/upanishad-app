from pathlib import Path

p = Path("index.html")
text = p.read_text(encoding="utf-8")

replacements = {
    ".hdr{text-align:center;padding:44px 20px 28px;border-bottom:1px solid var(--br);background:linear-gradient(180deg,rgba(201,168,76,0.07),transparent);}":
    ".hdr{text-align:center;padding:44px 20px 28px;border-bottom:1px solid var(--br);background:rgba(23,17,9,.55);}",

    ".uc{display:flex;align-items:center;gap:14px;padding:16px;margin:0 14px 12px;background:linear-gradient(145deg,rgba(255,255,255,0.055),rgba(201,168,76,0.045));border-radius:20px;border:1px solid rgba(201,168,76,0.16);cursor:pointer;transition:transform 0.18s ease,border-color 0.18s ease,background 0.18s ease;position:relative;overflow:hidden;box-shadow:0 10px 30px rgba(0,0,0,0.18);}":
    ".uc{display:flex;align-items:center;gap:14px;padding:16px;margin:0 14px 12px;background:var(--b3);border-radius:16px;border:1px solid rgba(214,168,79,.18);cursor:pointer;transition:transform 0.18s ease,border-color 0.18s ease,background 0.18s ease;position:relative;overflow:hidden;box-shadow:none;}",

    ".ci{width:54px;height:54px;border-radius:18px;display:flex;align-items:center;justify-content:center;font-size:25px;flex-shrink:0;background:rgba(255,255,255,0.055);border:1px solid rgba(201,168,76,0.14);box-shadow:inset 0 0 18px rgba(201,168,76,0.05);}":
    ".ci{width:50px;height:50px;border-radius:14px;display:flex;align-items:center;justify-content:center;font-size:23px;flex-shrink:0;background:rgba(214,168,79,.06);border:1px solid rgba(214,168,79,.20);box-shadow:none;}",

    ".lhdr{padding:20px 16px 16px;background:linear-gradient(135deg,rgba(201,168,76,0.07),transparent);border-bottom:1px solid var(--br);}":
    ".lhdr{padding:20px 16px 16px;background:rgba(23,17,9,.70);border-bottom:1px solid var(--br);}",

    ".mi{display:flex;align-items:center;gap:12px;padding:15px 16px;margin:0 12px 10px;background:linear-gradient(145deg,rgba(241,230,208,.045),rgba(214,168,79,.035));border-radius:16px;border:1px solid rgba(214,168,79,.16);cursor:pointer;transition:all 0.2s;box-shadow:0 8px 22px rgba(0,0,0,.14);}":
    ".mi{display:flex;align-items:center;gap:12px;padding:15px 16px;margin:0 12px 10px;background:var(--b3);border-radius:14px;border:1px solid rgba(214,168,79,.18);cursor:pointer;transition:all 0.2s;box-shadow:none;}",

    ".sk{background:linear-gradient(135deg,rgba(201,168,76,0.12),rgba(201,168,76,0.035));border:1px solid rgba(201,168,76,0.22);border-radius:22px;padding:26px 20px;margin-bottom:16px;position:relative;overflow:hidden;box-shadow:0 14px 36px rgba(0,0,0,.20);}":
    ".sk{background:var(--b4);border:1px solid rgba(214,168,79,.22);border-radius:18px;padding:26px 20px;margin-bottom:16px;position:relative;overflow:hidden;box-shadow:none;}",

    ".sk::before{content:'';position:absolute;top:0;left:0;right:0;height:2px;background:linear-gradient(90deg,transparent,var(--g),transparent);}":
    ".sk::before{content:'॥';position:absolute;top:8px;left:0;right:0;height:auto;background:none;color:rgba(214,168,79,.38);font-size:13px;text-align:center;letter-spacing:8px;}",

    ".ap{background:linear-gradient(135deg,rgba(201,168,76,0.08),rgba(201,168,76,0.02));border:1px solid var(--br);border-radius:18px;padding:18px 16px;margin-bottom:14px;position:relative;overflow:hidden;}":
    ".ap{background:var(--b3);border:1px solid var(--br);border-radius:16px;padding:18px 16px;margin-bottom:14px;position:relative;overflow:hidden;}",

    ".ap::before{content:'';position:absolute;top:0;left:0;right:0;height:2px;background:linear-gradient(90deg,transparent,var(--g),transparent);}":
    ".ap::before{content:'';position:absolute;top:0;left:18px;right:18px;height:1px;background:rgba(214,168,79,.32);}",

    ".apb{width:52px;height:52px;border-radius:50%;flex-shrink:0;background:linear-gradient(135deg,var(--g),var(--gd));border:none;cursor:pointer;font-size:20px;display:flex;align-items:center;justify-content:center;box-shadow:0 4px 20px rgba(201,168,76,0.35);transition:transform 0.15s;}":
    ".apb{width:52px;height:52px;border-radius:50%;flex-shrink:0;background:var(--g);border:1px solid rgba(240,213,138,.28);cursor:pointer;font-size:20px;display:flex;align-items:center;justify-content:center;box-shadow:none;transition:transform 0.15s;}",

    ".tb.on{background:linear-gradient(135deg,rgba(201,168,76,0.2),rgba(201,168,76,0.07));color:var(--gl);outline:1px solid rgba(201,168,76,0.25);}":
    ".tb.on{background:rgba(214,168,79,.12);color:var(--gl);outline:1px solid rgba(214,168,79,.28);}",

    ".pt{position:fixed;bottom:0;left:0;right:0;background:rgba(8,7,5,0.97);backdrop-filter:blur(22px);border-top:1px solid rgba(201,168,76,0.22);padding:13px 16px 24px;z-index:100;box-shadow:0 -12px 34px rgba(0,0,0,.28);}":
    ".pt{position:fixed;bottom:0;left:0;right:0;background:rgba(11,8,4,0.98);backdrop-filter:blur(10px);border-top:1px solid rgba(214,168,79,.24);padding:13px 16px 24px;z-index:100;box-shadow:none;}",

    ".ptn{background:linear-gradient(135deg,var(--g),var(--gd));color:#000;border-color:transparent;width:54px;height:54px;}":
    ".ptn{background:var(--g);color:#0B0804;border-color:rgba(240,213,138,.25);width:54px;height:54px;}",

    "background:linear-gradient(135deg,var(--gl),var(--g));\n  box-shadow:0 12px 34px rgba(201,168,76,.18);":
    "background:var(--g);\n  box-shadow:none;",

    "background:linear-gradient(90deg,transparent,rgba(201,168,76,.55),transparent);":
    "background:rgba(214,168,79,.38);",

    "background:linear-gradient(145deg,rgba(201,168,76,.09),rgba(255,255,255,.035));":
    "background:var(--b3);",

    "background:linear-gradient(135deg,var(--gl),var(--g));":
    "background:var(--g);"
}

changed = 0
for old, new in replacements.items():
    if old in text:
        text = text.replace(old, new)
        changed += 1
    else:
        print("NOT FOUND:", old[:90])

p.write_text(text, encoding="utf-8")

print(f"De-gloss manuscript theme patch applied. Replacements: {changed}")
print()
print("VERIFY:")
fresh = p.read_text(encoding="utf-8")
for needle in ["box-shadow:none", "background:var(--b3)", "content:'॥'", "backdrop-filter:blur(10px)", "background:var(--g);"]:
    print(needle, "=>", needle in fresh)

print()
print("GIT STATUS:")
