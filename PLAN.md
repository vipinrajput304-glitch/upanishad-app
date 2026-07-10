# Upanishad Content Generation Plan

## Workflow
- Content is generated as JSON files in `content/`
- Each file = one Upanishad section (~8–15 mantras)
- Merge into `index.html` using `merge_content.py` only after all files for an Upanishad are done
- JSON files stay in git permanently as source of truth

## Resume Instruction (paste at start of any new session)
```
Check content/ folder for existing JSON files.
Generate the next PENDING file from PLAN.md.
Do NOT read or touch index.html.
Commit and push the new JSON file when done.
```

## The 10 Principal Upanishads

| # | Upanishad | Total Mantras | Structure | Status |
|---|---|---|---|---|
| 1 | Isha | 18 | 1 section | ✅ In app (complete) |
| 2 | Kena | ~35 | 4 Parts | ✅ All JSON done (1–4 in app, 5–35 in content/) |
| 3 | Katha | ~119 | 6 Vallis | ❌ Not started |
| 4 | Prashna | ~67 | 6 Questions | ❌ Not started |
| 5 | Mundaka | ~64 | 6 Khandas | ❌ Not started |
| 6 | Mandukya | 12 | 1 section | ✅ In app (complete) |
| 7 | Taittiriya | ~48 | 3 Vallis | ❌ Not started |
| 8 | Aitareya | 33 | 3 Adhyayas | ✅ In app (complete) |
| 9 | Chandogya | ~154 | 8 Prapathakas | ❌ Not started |
| 10 | Brihadaranyaka | ~190 | 6 Adhyayas | ❌ Not started |

**Total: ~810 mantras | In app: 67 | Remaining: ~743**

## File List & Status

### Kena (ids 1–35, app already has 1–4)
| File | Mantras | Content | Status |
|---|---|---|---|
| `content/kena_p1b.json` | 5–8 | Verse section Part 1 remainder (paradox of knowing, immortality) | ✅ DONE |
| `content/kena_p2.json` | 9–16 | Prose Part 2 — Brahman's victory; Yaksha tests Agni & Vayu | ✅ DONE |
| `content/kena_p3.json` | 17–28 | Prose Part 3 — Indra approaches; Uma Haimavati teaches | ✅ DONE |
| `content/kena_p4.json` | 29–35 | Prose Part 4 — conclusion, lightning metaphor, teaching | ✅ DONE |

### Katha (ids 1–119)
| File | Mantras | Content | Status |
|---|---|---|---|
| `content/katha_1_1.json` | 1–29 | Adhyaya 1 Valli 1 — Nachiketa's three boons | ✅ DONE |
| `content/katha_1_2.json` | 1–25 | Adhyaya 1 Valli 2 — What is beyond the senses | ✅ DONE |
| `content/katha_1_3.json` | 1–17 | Adhyaya 1 Valli 3 — Chariot metaphor, self-knowledge | ✅ DONE |
| `content/katha_2_1.json` | 1–15 | Adhyaya 2 Valli 1 — The city of eleven gates | ⏳ NEXT |
| `content/katha_2_2.json` | 1–15 | Adhyaya 2 Valli 2 — The Cosmic Person | ❌ PENDING |
| `content/katha_2_3.json` | 1–17 | Adhyaya 2 Valli 3 — The Yoga of the Self | ❌ PENDING |

### Prashna (ids 1–67)
| File | Mantras | Content | Status |
|---|---|---|---|
| `content/prashna_q1.json` | 1–16 | Question 1 — Who sustains the world? | ❌ PENDING |
| `content/prashna_q2.json` | 1–13 | Question 2 — How many gods in man? | ❌ PENDING |
| `content/prashna_q3.json` | 1–12 | Question 3 — Whence is Prana born? | ❌ PENDING |
| `content/prashna_q4.json` | 1–11 | Question 4 — What sleeps and what is awake? | ❌ PENDING |
| `content/prashna_q5.json` | 1–7 | Question 5 — OM meditation | ❌ PENDING |
| `content/prashna_q6.json` | 1–8 | Question 6 — The sixteen-part Person | ❌ PENDING |

### Mundaka (ids 1–64)
| File | Mantras | Content | Status |
|---|---|---|---|
| `content/mundaka_1_1.json` | 1–9 | Mundaka 1 Khanda 1 — Two kinds of knowledge | ❌ PENDING |
| `content/mundaka_1_2.json` | 1–13 | Mundaka 1 Khanda 2 — Raft of sacrifice | ❌ PENDING |
| `content/mundaka_2_1.json` | 1–10 | Mundaka 2 Khanda 1 — The cosmic Person | ❌ PENDING |
| `content/mundaka_2_2.json` | 1–11 | Mundaka 2 Khanda 2 — The knower of Brahman | ❌ PENDING |
| `content/mundaka_3_1.json` | 1–10 | Mundaka 3 Khanda 1 — Two birds on one tree | ❌ PENDING |
| `content/mundaka_3_2.json` | 1–11 | Mundaka 3 Khanda 2 — Satyameva Jayate | ❌ PENDING |

### Taittiriya (ids 1–48)
| File | Mantras | Content | Status |
|---|---|---|---|
| `content/taittiriya_v1.json` | 1–12 | Shikshavalli — phonetics, peace, self-knowledge | ❌ PENDING |
| `content/taittiriya_v2.json` | 1–9 | Brahmanandavalli — five sheaths, Brahman as bliss | ❌ PENDING |
| `content/taittiriya_v3.json` | 1–10 | Bhriguvalli — Bhrigu's inquiry, food is Brahman | ❌ PENDING |

### Chandogya (ids 1–154)
| File | Mantras | Content | Status |
|---|---|---|---|
| `content/chandogya_p1-2.json` | 1–30 | Prapathakas 1–2 — OM, Udgitha, breath | ❌ PENDING |
| `content/chandogya_p3.json` | 1–20 | Prapathaka 3 — Honey doctrine, Gayatri | ❌ PENDING |
| `content/chandogya_p4.json` | 1–17 | Prapathaka 4 — Satyakama, Raikva | ❌ PENDING |
| `content/chandogya_p5.json` | 1–24 | Prapathaka 5 — Prana, five fires | ❌ PENDING |
| `content/chandogya_p6.json` | 1–16 | Prapathaka 6 — Tat Tvam Asi (Uddalaka) | ❌ PENDING |
| `content/chandogya_p7.json` | 1–26 | Prapathaka 7 — Narada and Sanatkumara | ❌ PENDING |
| `content/chandogya_p8.json` | 1–15 | Prapathaka 8 — City of Brahman | ❌ PENDING |

### Brihadaranyaka (ids 1–190)
| File | Mantras | Content | Status |
|---|---|---|---|
| `content/brihad_1.json` | 1–28 | Adhyaya 1 — Horse sacrifice, creation | ❌ PENDING |
| `content/brihad_2.json` | 1–25 | Adhyaya 2 — Ajatashatru dialogue, neti neti begins | ❌ PENDING |
| `content/brihad_3.json` | 1–35 | Adhyaya 3 — Yajnavalkya's debates (Janaka's court) | ❌ PENDING |
| `content/brihad_4.json` | 1–30 | Adhyaya 4 — Maitreyi & Yajnavalkya; neti neti | ❌ PENDING |
| `content/brihad_5.json` | 1–30 | Adhyaya 5 — Meditation on heart, OM | ❌ PENDING |
| `content/brihad_6.json` | 1–25 | Adhyaya 6 — Panchaagni, progeny, guru lineage | ❌ PENDING |

## Schema (each mantra in the JSON array)
```json
{
  "id": 5,
  "sk": "Sanskrit devanagari text",
  "ro": "romanized · transliteration · with · middle-dots",
  "hi": "Hindi translation (2-3 sentences, sacred register)",
  "en": "English translation (faithful, not over-poetic)",
  "ws": [
    {"s": "पदम्", "h": "हिंदी अर्थ", "e": "english meaning — grammar note"}
  ],
  "gr": "<strong>Key word</strong> — grammatical analysis. <strong>Another</strong> — ...",
  "mt": "REVIEW_NEEDED: ... · Upanishad reference",
  "cm": {
    "advaita":   {"a": "शंकराचार्य · Adi Shankaracharya", "h": "...", "en": "...", "ins": "..."},
    "vishisht":  {"a": "रामानुजाचार्य · Ramanujacharya",  "h": "...", "en": "...", "ins": "..."},
    "aurobindo": {"a": "श्री अरविंद · Sri Aurobindo",     "h": "...", "en": "...", "ins": "..."}
  },
  "dp": [
    {"q": "🔍 Topic heading", "a": "Deep dive explanation with <strong>key terms</strong>."},
    {"q": "...", "a": "..."}
  ]
}
```
