from pathlib import Path

p = Path("index.html")
text = p.read_text(encoding="utf-8")

replacements = {
    ".wh{display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px;padding:4px 12px 8px;font-size:9px;color:var(--tf);letter-spacing:2px;text-transform:uppercase;}":
    ".wh{display:none;}",

    ".wr{display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px;padding:11px 12px;margin-bottom:7px;background:var(--b3);border:1px solid rgba(255,255,255,0.04);border-radius:12px;align-items:start;}":
    ".wr{display:block;padding:14px 15px;margin:0 0 10px;background:var(--b3);border:1px solid rgba(214,168,79,.16);border-radius:14px;}",

    ".ws{font-family:'Noto Sans Devanagari',serif;font-size:14px;color:var(--g);}":
    ".ws{font-family:'Noto Sans Devanagari',serif;font-size:18px;color:var(--gl);line-height:1.55;margin-bottom:5px;}",

    ".whi{font-size:12px;color:var(--td);line-height:1.5;}":
    ".whi{font-family:'Noto Sans Devanagari',serif;font-size:14px;color:var(--t);line-height:1.65;margin-bottom:3px;}",

    ".we{font-size:11px;font-family:'EB Garamond',serif;font-style:italic;color:var(--tf);line-height:1.5;}":
    ".we{font-size:14px;font-family:'EB Garamond',serif;font-style:normal;color:var(--td);line-height:1.55;}"
}

changed = 0
for old, new in replacements.items():
    if old in text:
        text = text.replace(old, new)
        changed += 1
    else:
        print("NOT FOUND:", old[:80])

p.write_text(text, encoding="utf-8")

print(f"Word cards mobile patch applied. Replacements: {changed}")
print()
print("VERIFY:")
fresh = p.read_text(encoding="utf-8")
for needle in [".wh{display:none;}", ".wr{display:block", "font-size:18px;color:var(--gl)", "font-style:normal;color:var(--td)"]:
    print(needle, "=>", needle in fresh)

print()
print("GIT STATUS:")
