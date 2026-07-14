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

### Phase 1 — Smaller 8 (complete these first, build into app)

| # | Upanishad | Veda | Total Mantras | Structure | Status |
|---|---|---|---|---|---|
| 1 | Isha | Shukla Yajurveda | 18 | 1 section | ✅ In app (complete) |
| 2 | Kena | Samaveda | 34 | 4 Khandas | ✅ All JSON done |
| 3 | Katha | Krishna Yajurveda | 119 | 2 Adhyayas × 3 Vallis | ✅ All JSON done |
| 4 | Prashna | Atharvaveda | 67 | 6 Questions | ✅ All JSON done |
| 5 | Mundaka | Atharvaveda | 64 | 3 Mundakas × 2 Khandas | ⏳ In progress |
| 6 | Mandukya | Atharvaveda | 12 | 1 section | ✅ In app (complete) |
| 7 | Taittiriya | Krishna Yajurveda | 52 | 3 Vallis | ❌ Not started |
| 8 | Aitareya | Rigveda | 33 | 3 Adhyayas | ✅ In app (complete) |

**Phase 1 total: ~399 mantras | In app: 63 | JSON done: 153 | Remaining: ~183**

### Phase 2 — The two giants (after Phase 1 is merged into app)

| # | Upanishad | Veda | Total Mantras | Structure | Status |
|---|---|---|---|---|---|
| 9 | Chandogya | Samaveda | 628 | 8 Prapathakas | ❌ Not started |
| 10 | Brihadaranyaka | Shukla Yajurveda | 435 | 6 Adhyayas | ❌ Not started |

**Phase 2 total: ~1,063 mantras (file splits TBD when we get there)**

---

## Phase 1 — File List & Status

### Kena (ids 1–34, app already has 1–4)
| File | Mantras | Content | Status |
|---|---|---|---|
| `content/kena_p1b.json` | 5–8 | Verse section Part 1 remainder (paradox of knowing, immortality) | ✅ DONE |
| `content/kena_p2.json` | 9–16 | Prose Part 2 — Brahman's victory; Yaksha tests Agni & Vayu | ✅ DONE |
| `content/kena_p3.json` | 17–28 | Prose Part 3 — Indra approaches; Uma Haimavati teaches | ✅ DONE |
| `content/kena_p4.json` | 29–34 | Prose Part 4 — conclusion, lightning metaphor, teaching | ✅ DONE |

### Katha (ids 1–119)
| File | Mantras | Content | Status |
|---|---|---|---|
| `content/katha_1_1.json` | 1–29 | Adhyaya 1 Valli 1 — Nachiketa's three boons | ✅ DONE |
| `content/katha_1_2.json` | 1–25 | Adhyaya 1 Valli 2 — What is beyond the senses | ✅ DONE |
| `content/katha_1_3.json` | 1–17 | Adhyaya 1 Valli 3 — Chariot metaphor, self-knowledge | ✅ DONE |
| `content/katha_2_1.json` | 1–15 | Adhyaya 2 Valli 1 — The city of eleven gates | ✅ DONE |
| `content/katha_2_2.json` | 1–15 | Adhyaya 2 Valli 2 — The Cosmic Person | ✅ DONE |
| `content/katha_2_3.json` | 1–17 | Adhyaya 2 Valli 3 — The Yoga of the Self | ✅ DONE |

### Prashna (ids 1–67)
| File | Mantras | Content | Status |
|---|---|---|---|
| `content/prashna_q1.json` | 1–16 | Question 1 — Who sustains the world? | ✅ DONE |
| `content/prashna_q2.json` | 1–13 | Question 2 — How many gods support a creature? | ✅ DONE |
| `content/prashna_q3.json` | 1–12 | Question 3 — Whence is Prana born? | ✅ DONE |
| `content/prashna_q4.json` | 1–11 | Question 4 — What sleeps and what is awake? | ✅ DONE |
| `content/prashna_q5.json` | 1–7 | Question 5 — OM meditation | ✅ DONE |
| `content/prashna_q6.json` | 1–8 | Question 6 — The sixteen-part Person | ✅ DONE |

### Mundaka (ids 1–64)
| File | Mantras | Content | Status |
|---|---|---|---|
| `content/mundaka_1_1.json` | 1–9 | Mundaka 1 Khanda 1 — Two kinds of knowledge | ✅ DONE |
| `content/mundaka_1_2.json` | 1–13 | Mundaka 1 Khanda 2 — Raft of sacrifice | ✅ DONE |
| `content/mundaka_2_1.json` | 1–10 | Mundaka 2 Khanda 1 — The cosmic Person | ✅ DONE |
| `content/mundaka_2_2.json` | 1–11 | Mundaka 2 Khanda 2 — The knower of Brahman | ✅ DONE |
| `content/mundaka_3_1.json` | 1–10 | Mundaka 3 Khanda 1 — Two birds on one tree | ✅ DONE |
| `content/mundaka_3_2.json` | 1–11 | Mundaka 3 Khanda 2 — Satyameva Jayate | ⏳ NEXT |

### Taittiriya (ids 1–52)
| File | Mantras | Content | Status |
|---|---|---|---|
| `content/taittiriya_1a.json` | 1–6 | Shikshavalli Part 1 — invocation, phonetics, saṁhitā meditation | ❌ PENDING |
| `content/taittiriya_1b.json` | 7–12 | Shikshavalli Part 2 — vyāhṛtis, meditation on OM, convocation address | ❌ PENDING |
| `content/taittiriya_2a.json` | 1–5 | Brahmanandavalli Part 1 — five sheaths (anna to vijñāna) | ❌ PENDING |
| `content/taittiriya_2b.json` | 6–9 | Brahmanandavalli Part 2 — ānandamaya, Brahman as bliss, fear | ❌ PENDING |
| `content/taittiriya_3.json` | 1–10 | Bhriguvalli — Bhrigu's inquiry, food is Brahman | ❌ PENDING |

---

## Phase 2 — File List (TBD)

### Chandogya (628 mantras)
Detailed file splits will be planned when Phase 1 is complete.

### Brihadaranyaka (435 mantras)
Detailed file splits will be planned when Phase 1 is complete.

---

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
