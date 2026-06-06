# KENA_STYLE_NOTES.md

Style analysis based on ISHA (18 mantras), MANDUKYA (12 mantras), and AITAREYA (33 mantras).
Reference for bringing KENA up to house quality before editing index.html.

---

## 1. EXISTING HOUSE STYLE SUMMARY

### 1.1 Data Helpers

Three shorthand builders are defined at the top of index.html:

```js
const W=(s,h,e)=>({s,h,e});       // word-study entry
const D=(q,a)=>({q,a});            // deep-dive entry
const C=(hi,en,insight)=>({...}); // (used internally, not in main mantra arrays)
```

Every `ws` entry in ISHA/MANDUKYA/AITAREYA calls `W()`. Every `dp` entry calls `D()`.

### 1.2 Schema — Full Field List (in order as it appears)

| Field | Type | Notes |
|---|---|---|
| `id` | integer | 1-based, sequential within Upanishad |
| `adhyaya` | string | **Aitareya only**; omit for others |
| `sk` | string | Sanskrit; multi-line with `\n`. Uses `"..."` (regular string, not backtick) |
| `ro` | string | IAST romanisation; single line; pada separated by `·` (middle dot) |
| `hi` | string | Hindi translation; 1–3 flowing sentences |
| `en` | string | English translation; literary, precise; 1–3 sentences |
| `ws` | array | `[W("Sanskrit","Hindi","English"), ...]` — always uses `W()` helper |
| `gr` | string | Grammar/keyword note; uses `<strong>term</strong>` HTML tags |
| `mt` | string | Metre; full name + transliteration + syllable count + significance note |
| `cm` | object | Three tradition commentaries (see 1.4) |
| `dp` | array | Deep dives `[D("Emoji Title","HTML answer"), ...]` |

### 1.3 Field Conventions

**`sk`** — Regular double-quoted string. Line breaks with `\n`. Mantras separated by the
standard Vedic ॥ numeral. Example from ISHA 1:
```
"ईशावास्यमिदं सर्वं यत्किञ्च जगत्यां जगत् ।\nतेन त्यक्तेन भुञ्जीथा मा गृधः कस्यस्विद्धनम् ॥"
```

**`ro`** — Single string, pada separated by `·` (not `|`). Example:
```
"Īśāvāsyamidaṃ sarvaṃ yatkiñca jagatyāṃ jagat · tena tyaktena bhuñjīthā mā gṛdhaḥ kasyasviddhanam"
```

**`gr`** — Always wraps key Sanskrit terms in `<strong>`. Format:
- Opens with `<strong>KeyTerm</strong>` — grammatical form explained.
- Connects grammar to teaching meaning.
- Example: `"<strong>भुञ्जीथाः</strong> — Vidhi-liṅ mood: not a command but gentle permission — 'you may enjoy.'"`

**`mt`** — Full descriptor, never bare. Examples:
- Verse: `"Anuṣṭubh (अनुष्टुभ्) · 8 syllables per quarter · The most sacred Vedic metre"`
- Verse: `"Trishtubh (त्रिष्टुभ्) · 11 syllables per quarter"`
- Prose: `"Prose (गद्य) — Aitareya is written entirely in prose · Rigveda tradition"`
- Special: `"Mixed metres — death-time prayer"`

**`ws`** — Each entry is `W("Sanskrit","Hindi meaning","English meaning")`. Sanskrit is the
word as it appears or its base form. Hindi/English are concise but meaningful.
High-quality entries explain the grammatical nuance in the English column:
- `W("जिजीविषेत्","जीने की इच्छा करे","should wish to live")` — desiderative captured
- `W("विजुगुप्सते","घृणा नहीं करता","does not shrink, does not hate")` — root explained

**`gr`** — 2–4 sentences. Always starts with `<strong>key-word</strong>` — explanation.
Often cites Vedic grammatical form (Vidhi-liṅ, desiderative, causative, genitive chain).
Connects the grammar to the philosophical point.

**`dp`** — Array, 1–3 entries per mantra. Each `D(q,a)`:
- `q`: Short title with emoji at start, often a real question a reader would ask.
- `a`: HTML answer, 2–5 sentences. Uses `<strong>` for emphasis. May connect to
  other mantras, modern concepts, or cross-Upanishad comparisons.

### 1.4 Commentary (`cm`) — Structure

Three tradition keys: `advaita`, `vishisht`, `aurobindo`

Each has four sub-fields:

```js
advaita: {
  a: "शंकराचार्य · Adi Shankaracharya",   // bilingual full name — Sanskrit · English
  h: "Hindi commentary — 2–3 sentences",
  en: "English commentary — 2–3 sentences",
  ins: "One-line memorable insight/aphorism"
},
vishisht: {
  a: "रामानुजाचार्य · Ramanujacharya",
  h: "...", en: "...", ins: "..."
},
aurobindo: {
  a: "श्री अरविंद · Sri Aurobindo",
  h: "...", en: "...", ins: "..."
}
```

Key quality markers:
- `a` field is always bilingual: Hindi name · English name, not just the school name.
- `h` and `en` are not translations of each other — they may add different details.
- `ins` is a short aphorism, standalone quotable line. Often bold or italicised in spirit.
  Often addresses the reader directly ("Do not escape life — transform it").
- Each tradition is distinguished: Advaita uses neti-neti/jnana language; Vishishtadvaita
  uses bhakti/Lord language; Aurobindo uses evolution/supramental/transformation language.

---

## 2. CURRENT KENA QUALITY GAPS

All four KENA mantras share the same set of defects:

### Gap 1 — `ws` uses inline objects instead of `W()` helper  ❌ CRITICAL
```js
// KENA (wrong):
ws:[{s:'केन',h:'किसके द्वारा',e:'by whom'}, ...]

// House style (correct):
ws:[W("केन","किसके द्वारा","by whom — instrumental of kim"), ...]
```
The `W()` helper must be used. Additionally, the English column in KENA word study is bare
("by whom", "mind") rather than explaining grammatical nuance as ISHA/AITAREYA do.

### Gap 2 — `gr` has no `<strong>` HTML tags  ❌ CRITICAL
```js
// KENA (wrong):
gr:'Opening interrogative verse. The repeated "kena" shifts inquiry from outer instruments
    to the inner source that empowers them.'

// House style (correct):
gr:'<strong>केन</strong> (instrumental of kim) — repeated three times: ...'
```
Every key Sanskrit term must be wrapped in `<strong>`. Grammar notes must cite the
grammatical form name (vidhiliṅ, instrumental, genitive chain, past-passive-participle, etc.).

### Gap 3 — `mt` is bare `'Vedic verse'`  ❌ CRITICAL
```js
// KENA (wrong):
mt:'Vedic verse'

// House style (correct):
mt:"Anuṣṭubh (अनुष्टुभ्) · 8 syllables per quarter · Samaveda tradition"
```
Metre name, transliteration, syllable count, and a brief significance note are required.
REVIEW_NEEDED: Exact metre for each of the 4 Kena mantras must be verified against a
scholarly source. Tentative: mantras 1–2 appear to be Anushtubh or Trishtubh; mantras 3–4
are closer to Anushtubh. See section 3 for per-mantra notes.

### Gap 4 — Commentary `a` field is abbreviated school name  ❌ CRITICAL
```js
// KENA (wrong):
advaita:{ a:'Advaita', ... }
vishisht:{ a:'Vishishtadvaita', ... }
integral:{ a:'Integral View', ... }

// House style (correct):
advaita:{ a:"शंकराचार्य · Adi Shankaracharya", ... }
vishisht:{ a:"रामानुजाचार्य · Ramanujacharya", ... }
aurobindo:{ a:"श्री अरविंद · Sri Aurobindo", ... }
```

### Gap 5 — Third tradition key is `integral` instead of `aurobindo`  ❌ SCHEMA BUG
KENA uses `cm.integral` but all other Upanishads use `cm.aurobindo`. The rendering code
reads `cm.aurobindo` — so `cm.integral` will silently fail to render.
REVIEW_NEEDED: Confirm with rendering code which key is consumed. Fix to `aurobindo`.

### Gap 6 — `dp` (deep dives) is completely absent from all 4 mantras  ❌ MAJOR GAP
Every ISHA, MANDUKYA, and AITAREYA mantra has a `dp` array with 1–3 entries.
KENA has none. This is the most visible quality gap to a reader.

### Gap 7 — Commentary depth is shallow  ⚠️ QUALITY
KENA commentaries are 1 sentence each (`h` and `en`). House style uses 2–3 sentences that
build on each other. The `ins` fields in KENA are OK in length but lack the direct-address
quality of ISHA/MANDUKYA (e.g., "Every faculty is a doorway" is passable but generic).

### Gap 8 — `ro` pada separator uses `|` instead of `·`  ⚠️ MINOR
KENA uses standard IAST `|` (daṇḍa) as pada boundary. ISHA/MANDUKYA/AITAREYA use `·`.
REVIEW_NEEDED: Whether this is intentional (honoring IAST standard) or accidental
inconsistency. Recommend aligning to `·` for visual consistency with existing data.

### Gap 9 — `sk` uses backtick template literals instead of regular strings  ⚠️ MINOR
KENA: `sk:\`...\`` (backtick). Others: `sk:"..."` (double-quoted string).
Functionally equivalent, but inconsistent with style. Recommend normalising to `"..."`.

---

## 3. EXACT SCHEMA/FIELD USAGE NOTES FOR KENA

### 3.1 Metre — per mantra (REVIEW_NEEDED)

| Mantra | Sanskrit structure | Tentative metre |
|---|---|---|
| 1 | 4 lines, ~12 syllables each by surface count | REVIEW_NEEDED: Trishtubh (11) or Jagati (12)? Kena 1 line 1: `ke-ne-ṣi-taṃ pa-ta-ti pre-ṣi-taṃ ma-naḥ` = 12 syllables? Vedic sandhi complicates count. |
| 2 | 4 lines, similar to mantra 1 | REVIEW_NEEDED: Same. `śrotrasya śrotraṃ manaso mano yad` — count per line. |
| 3 | 2 lines | REVIEW_NEEDED: `na tatra cakṣur gacchati na vāg gacchati no manaḥ` appears to be 13 syllables in line 1. Possible Anushtubh with expansion. Some editions classify Kena 1.3 as prose. |
| 4 | 2 lines | REVIEW_NEEDED: Same as 3. Likely Anushtubh or close to it. |

**Action needed before editing:** Verify metre from a scholarly commentary or edition
(e.g., Gambhirananda's Kena Upanishad, or S. Radhakrishnan's edition).

### 3.2 Word study — quality bar

Each `ws` entry should explain grammatical form in the English column where meaningful:
- Root verb forms: `"by whom — instrumental of kim"`
- Past passive: `"impelled — past passive participle of iṣ"`
- Genitive chain: `"ear of the ear — genitive of śrotra"`
- Emphatic particle: `"'u' — Vedic emphatic particle"`

### 3.3 Commentary — `ins` field bar

The `ins` field must be an aphorism the reader can carry away. It should:
- Be one punchy sentence, standalone.
- Often address the reader directly ("You are...", "The X cannot...").
- Distinguish the three schools clearly.

Examples from ISHA that set the bar:
- Advaita: `"ब्रह्म सत्यं जगन्मिथ्या — but while in the world, see Brahman everywhere."`
- Aurobindo: `"Life is not an obstacle to God — life IS the field of God-realization."`

### 3.4 `dp` structure for Kena mantras

Suggested deep-dive topic areas per mantra:
- Mantra 1: Etymology of "kena", cross-reference to Aitareya's devas, the difference between
  मन and प्राण as questions, देवः meaning.
- Mantra 2: The genitive-chain device (ear-of-ear) as teaching method, what "धीराः" means,
  the meaning of अमृत in this context.
- Mantra 3: Why the teacher says "we do not know how to teach it", apophatic method
  in world traditions, अनुशिष्यात् and the limits of language.
- Mantra 4: The "known/unknown" paradox, connection to Isha 4 (manaso javīyaḥ), the
  शुश्रुम formula as guru-lineage acknowledgement (cf. Isha 10, 13).

---

## 4. REWRITTEN DRAFT — KENA MANTRA 1 (plain markdown, not JS)

This is a quality-target draft showing what the data should look like after revision.
Use this as the reference when editing index.html.

---

### id: 1

**sk:**
```
केनेषितं पतति प्रेषितं मनः
केन प्राणः प्रथमः प्रैति युक्तः ।
केनेषितां वाचमिमां वदन्ति
चक्षुः श्रोत्रं क उ देवो युनक्ति ॥ १ ॥
```

**ro:**
```
keneṣitaṃ patati preṣitaṃ manaḥ · kena prāṇaḥ prathamaḥ praiti yuktaḥ · keneṣitāṃ vācamimāṃ vadanti · cakṣuḥ śrotraṃ ka u devo yunakti
```
(Note: `·` replaces `|` for consistency with ISHA/MANDUKYA/AITAREYA pada-separator style.)

**hi:**
```
किसके द्वारा प्रेरित होकर मन अपने विषयों की ओर दौड़ता है?
प्राण किसके आदेश से सबसे पहले चलता है?
लोग यह वाणी किसकी इच्छाशक्ति से बोलते हैं?
कौन-सा देव आँख और कान को उनके कार्य में जोतता है?
```

**en:**
```
Willed by whom does the mind fall toward its objects?
By whom is the first vital force set in motion?
By whose will do people utter this speech?
What luminous power yokes the eye and ear to their work?
```
(REVIEW_NEEDED: "first vital force" — `prāṇaḥ prathamaḥ` could be "the breath, first among
the vital forces" [epithetic] or "the breath that moves first" [temporal]. Shankaracharya
takes it as epithetic. Flag for decision when editing.)

**ws (using W() helper):**
```js
W("केन","किसके द्वारा","by whom — instrumental of kim"),
W("इषितम्","प्रेरित / इच्छित","impelled, willed — past passive of iṣ (to impel)"),
W("पतति","गिरता है / जाता है","falls toward — the mind rushes at its objects"),
W("प्रेषितम्","भेजा गया","directed — pra+iṣ, sent forth with purpose"),
W("मनः","मन","mind"),
W("प्राणः प्रथमः","प्रथम प्राण","the first/chief vital force — prāṇa is primary among five"),
W("प्रैति","चला जाता है","goes forth — pra+eti, moves out"),
W("युक्तः","जोता हुआ","yoked, set to work — past passive of yuj (same root as yoga)"),
W("वाचम् इमाम्","यह वाणी","this very speech — imām is demonstrative, grounding the question"),
W("क उ देवः","कौन-सा देव?","what luminous being? — 'u' is Vedic emphatic; deva from div, to shine"),
W("युनक्ति","जोतता / नियुक्त करता है","yokes, puts to work — present of yuj; connects to yoga")
```

**gr:**
```
<strong>केन</strong> (instrumental of kim, 'by whom') appears three times in two lines — the repetition
is the teaching method: it hammers one question into all faculties at once.
<strong>इषितम् / प्रेषितम्</strong> — both past passive participles of iṣ — distinguish two degrees:
'impelled from within' vs 'directed from without', suggesting the source operates at
both levels. <strong>प्रैति</strong> = pra + eti — goes forth with force, not merely moves.
<strong>क उ देवः</strong> — the final line shifts the pronoun from 'kena' (instrumental) to
'kaḥ' (nominative) and adds <strong>देवः</strong> (from div, to shine) — not any external god but
the luminous principle that makes seeing and hearing possible.
<strong>युनक्ति</strong> = yokes (from युज्, root of yoga) — the senses are not self-propelling;
they are put to work by something else. The entire mantra is a single philosophical trap
that catches the meditator at every faculty.
```

**mt:**
```
REVIEW_NEEDED: Exact metre unconfirmed. Surface syllable count of pada 1 (keneṣitaṃ patati
preṣitaṃ manaḥ) gives ~12 syllables, suggesting Jagati or an irregular Trishtubh.
Some scholars classify Kena 1.1–1.2 as Trishtubh (11 syl/pada). Verify against
Gambhirananda or Radhakrishnan edition before setting final value.
Placeholder: "Trishtubh (त्रिष्टुभ्) · 11 syllables per quarter · Samaveda, Talavakāra Brāhmaṇa"
```

**cm:**

_advaita:_
```
a:  "शंकराचार्य · Adi Shankaracharya"
h:  "यह प्रारंभिक प्रश्न ही साधना की पूरी दिशा बदल देता है। मन, प्राण, वाणी, आँख, कान —
     सब किसी से प्रेरित हैं। शंकर कहते हैं: वह स्रोत साक्षी-चेतना है जो स्वयं न गति
     करती है, न बोलती है — पर सबको गति और वाणी देती है। इंद्रियों की ओर नहीं,
     इंद्रियों के स्रोत की ओर मुड़ो — यही केन की प्रथम शिक्षा है।"
en: "This opening question reorients the entire inquiry. Mind, Prana, speech, eye, ear —
     all are directed by something. That something, says Shankara, is the witness-consciousness:
     itself unmoved, unspoken, yet the mover and speaker behind everything. To turn
     from the instruments toward their source — this is Kena's first teaching."
ins: "The lamp cannot see its own flame. The question 'by whom' is the lamp turning to look."
```

_vishisht:_
```
a:  "रामानुजाचार्य · Ramanujacharya"
h:  "मन और इंद्रियाँ स्वतंत्र नहीं हैं — वे परमात्मा की अधिष्ठाता शक्ति से चलती हैं।
     जो जीव इस परतंत्रता को पहचानता है, वह अहंकार छोड़ता है और ईश्वर की शरण पाता है।
     'देवः' — वह शासक जो भीतर से जोतता है — वही ईश्वर है जो जीव का अन्तर्यामी है।"
en: "Mind and senses are not self-sovereign — they operate by the sustaining power of Ishvara.
     The soul that recognizes this dependence releases its ego-claim and discovers divine
     shelter. The 'luminous power' that yokes eye and ear is the indwelling Lord — the
     antaryāmin who dwells in every organ."
ins: "Dependence recognized is not weakness — it is the moment the soul finds its true master."
```

_aurobindo (key must be `aurobindo`, not `integral`):_
```
a:  "श्री अरविंद · Sri Aurobindo"
h:  "यह प्रश्न व्यक्ति को बाहर से भीतर की ओर मोड़ता है — surface instruments से उनके
     source की ओर। श्री अरविंद के लिए यह inquiry, ultimately, Supramental consciousness
     की खोज का पहला पड़ाव है: वह चेतना जो मन, प्राण और इंद्रियों को संचालित करती है
     पर स्वयं उनसे बाधित नहीं होती।"
en: "This question turns the seeker from surface to source — from the instruments to the
     consciousness that deploys them. For Sri Aurobindo this inquiry leads ultimately to
     the Supramental: the divine consciousness that organizes all human faculties without
     itself being limited by any of them."
ins: "Every faculty you use is a doorway. Step through it inward — and find the one who built the door."
```

**dp:**
```
D("❓ 'केन' — यह शब्द ही उपनिषद् का नाम क्यों?",
  "पूरी उपनिषद् एक ही प्रश्न में उतरती है: <strong>किसके द्वारा?</strong> 'कठ' मृत्यु से ज्ञान के बारे में है,
   'ईशावास्य' ईश्वर की व्यापकता के बारे में — पर केन एकमात्र उपनिषद् है जो प्रश्नवाचक से शुरू होती है।
   यह inquiry-based spirituality का प्राचीनतम model है: उत्तर नहीं, सही प्रश्न देना।")

D("🔗 ऐतरेय से केन का संबंध",
  "ऐतरेय ने बताया था: मन, प्राण, वाक्, चक्षु, श्रोत्र — सब cosmic देवगण हैं जो मनुष्य के
   शरीर में प्रवेश करते हैं। केन अगला प्रश्न पूछती है: <strong>इन देवगणों को किसने भेजा?</strong>
   ऐतरेय = शरीर में देवों का प्रवेश। केन = उन देवों के पीछे का प्रेरक। दोनों मिलकर complete picture बनाते हैं।")

D("🎯 'युनक्ति' — Yoga का मूल यहाँ है",
  "मंत्र का अंतिम शब्द <strong>युनक्ति</strong> — 'जोतता है' — युज् धातु से है, जिससे 'Yoga' बना है।
   इंद्रियाँ 'yoked' हैं — जैसे घोड़ा रथ से। कोई जोतने वाला है। <strong>Yoga का अर्थ है उस
   जोतने वाले को जानना — और अंततः उसी में विलीन होना।</strong> केन का पहला शब्द 'केन'
   और अंतिम शब्द 'युनक्ति' — यही उपनिषद् का arc है।")
```

---

## 5. REVIEW_NEEDED — CONSOLIDATED LIST

| # | Item | Location | Question |
|---|---|---|---|
| R1 | Metre for mantras 1–4 | All 4 mantras, `mt` field | Verify exact metre name from scholarly edition. Surface count suggests Trishtubh or Jagati for mantras 1–2; Anushtubh or prose for 3–4. |
| R2 | `ro` pada separator | All 4 mantras | Use `·` (house style) or keep `|` (IAST standard)? All three other Upanishads use `·`. Recommend `·`. |
| R3 | `aurobindo` vs `integral` key | All 4 mantras, `cm` | Rendering code reads `cm.aurobindo`. KENA uses `cm.integral`. This is a functional bug — integral commentary silently not rendered. Fix to `aurobindo`. |
| R4 | `prāṇaḥ prathamaḥ` translation | Mantra 1, `en` field | "first vital force" (epithetic, Shankara) vs "the breath that moves first" (temporal). Pick one and note in `gr`. |
| R5 | `sk` string style | All 4 mantras | Backtick template literals vs double-quoted strings. Normalise to `"..."` for consistency. |
| R6 | `en` translation of mantra 1 last line | Mantra 1, `en` | Current: "What shining principle connects the eye and the ear to their functions?" The word देवः means deity/luminous being. "connects" translates yunakti loosely — "yokes" is more precise. |
| R7 | Mantra 4 last line attribution | Mantra 4, `hi`/`en` | "पूर्वेषाम्" — "from the ancient teachers who explained it to us" — check whether `पूर्वेषाम्` is genitive plural of पूर्व (ancient ones) or a reference to a specific lineage. Cross-reference Isha 10 where the same शुश्रुम formula appears — same translation there can be model. |

---

*File created for planning only. Do not edit index.html until this review is complete.*
