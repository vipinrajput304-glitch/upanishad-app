from pathlib import Path

p = Path("index.html")
text = p.read_text(encoding="utf-8")

old = """  <div class="lbl" style="padding-top:12px">सभी मंत्र · ALL MANTRAS</div>
  <div id="lm"></div>"""

new = """  <div class="toc-card">
    <div class="toc-kicker">Full Index · संपूर्ण सूची</div>
    <div class="toc-title">सभी मंत्र अनुभागवार देखें</div>
    <div class="toc-sub">अगले चरण में यहाँ अलग स्क्रीन खुलेगी, जिसमें अध्याय/खंड के अनुसार सभी मंत्र दिखेंगे।</div>
    <div class="toc-actions">
      <button class="toc-btn" onclick="toast('All Mantras screen next step')">सभी मंत्र देखें</button>
    </div>
  </div>
  <div id="lm" style="display:none"></div>"""

if old not in text:
    print("All mantras block not found")
else:
    text = text.replace(old, new)
    p.write_text(text, encoding="utf-8")
    print("Raw all-mantras list hidden from overview")
