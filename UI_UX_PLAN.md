# Upanishad App UI/UX Improvement Plan

## Current Status
- App is working.
- index.html contains the full app.
- Broken app.js has been removed.
- Service worker is temporarily disabled.
- PWA will be restored later only after UI is stable.

## Design Direction
A calm, modern spiritual reading app:
- Deep charcoal background
- Muted gold accents
- Ivory readable text
- Mobile-first layout
- Simple navigation
- Better reading experience

## Phase 1
Improve home screen:
- Better hero section
- Clear start/explore buttons
- Better spacing
- Better mobile readability

## Phase 2
Fix screen navigation:
- Only one screen visible at a time
- Home, list, and reading screens should switch cleanly

## Phase 3
Improve reading screen:
- Better Sanskrit/Hindi/English readability
- Font size controls
- Sticky reading header
- Better previous/next controls

## Phase 4
Add useful features:
- Search
- Bookmark
- Continue reading
- Local progress saving

## Phase 5
Restore PWA later:
- Clean manifest
- Icons
- Safe service worker
- Then Play Store/TWA path

## Rule
Change one thing at a time, test, commit, then continue.

## Updated Navigation Architecture Plan

### Problem Observed
The Upanishad overview screen should not behave like a raw mantra dump. For larger Upanishads, showing all mantras on the same screen creates too much scrolling and weak navigation.

### Target Flow
Home
↓
Upanishad Overview
↓
Section Screen
↓
Mantra Reading Screen

Optional:
Upanishad Overview
↓
All Mantras Screen
↓
Grouped section-wise mantra list

### Upanishad Overview Screen
Purpose: orientation and resume.

Should show:
- Upanishad title
- Resume card
- Sections / अध्याय
- View All Mantras button
- Search entry point

Should not show:
- Full raw mantra list

### Section Screen
When user taps a section, open a dedicated section screen.

It should show:
- Upanishad name
- Section name
- Mantra range
- Section description
- Mantras only from that section

### All Mantras Screen
A separate full-index screen.

It should show:
- All mantras grouped by section
- Section headers
- Mantra number and short preview

### Search
Search should work across:
- Sanskrit
- Hindi meaning
- English meaning
- Word meanings
- Mantra number
- Section title

### Reading Screen Improvements
Reading screen must show:
- Upanishad name
- Section name
- Mantra number
- Section range

Example:
ईशावास्य उपनिषद्
कर्म, त्याग और आत्मा · Mantra 4/18

### Section Transition UX
Next button should not silently cross section boundaries.

When current section ends and next starts, show a transition notice:
- Section completed
- Next section name
- Continue button or clear notification

Example:
Section Complete
कर्म, त्याग और आत्मा · Mantras 2–8

Next:
विद्या और अविद्या · Mantras 9–14

### Resume Memory
Resume should become section-aware:
- lastUpanishad
- lastSection
- lastMantra
- lastReadAt

Resume card should show:
Continue
Section 2: कर्म, त्याग और आत्मा
Mantra 6

### Implementation Order
1. Add section awareness to reading screen header.
2. Add section transition notice when Next crosses section boundary.
3. Create dedicated Section Screen.
4. Make section cards open Section Screen instead of directly opening first mantra.
5. Create All Mantras grouped screen.
6. Add search.
7. Improve resume memory to include section.

## Reading Screen UX Redesign Plan

### Problem Observed
The mantra reading screen is functional, but it still feels too heavy and control-driven. The user sees many UI elements around the scripture: header, progress, chanting player, tabs, word table, commentary cards, and bottom navigation. This makes the screen feel like a dashboard rather than a scripture-first reading experience.

### Target Experience
The reading screen should follow this natural study journey:

Read → Understand → Decode → Reflect

The mantra should remain the center. Navigation, chanting, explanation, and reflection should support it quietly.

### New Top-Level Reading Tabs
Replace the current tabs:

अर्थ | शब्द | व्याख्या | गहराई

with:

पाठ | अर्थ | शब्द | चिंतन

### Tab 1: पाठ
Purpose: read and chant.

Should include:
- Sanskrit mantra
- Roman transliteration
- Compact chanting strip

The chanting player should live here and should not interrupt other reading modes.

### Tab 2: अर्थ
Purpose: quick understanding.

Should include:
- Hindi meaning
- English meaning
- Meter / note if available

Hindi and English should be stacked, clear, and readable. English should not be too faint or overly italic.

### Tab 3: शब्द
Purpose: word-by-word learning.

Current issue:
- It behaves like a 3-column table, which is cramped on mobile.

Target format:
Each word should be a stacked card:

उकारः
उ-कार
the U-sound

This is better for mobile learning.

### Tab 4: चिंतन
Purpose: commentary and deeper reflection.

Merge current:
व्याख्या + गहराई

Inside चिंतन, use smaller chips:
- शंकर
- रामानुज
- अरविंद
- प्रश्न / चिंतन

This reduces top-level clutter.

### Header Improvement
Current header is too dominant.

Target:
← सूची      माण्डूक्य · मंत्र 9/12      🔖
खंड 3 · अ, उ, म और मौन

Keep the progress line thin and calm.

### Bottom Navigation Improvement
Current bottom navigation is too heavy.

Target:
‹      मंत्र 9/12      ›

Keep previous/next accessible, but reduce height and visual weight.

### Chanting Player Improvement
Current chanting card is too large.

Target compact form:
▶ Chant     Slow · Medium · Normal

Later it can expand on tap.

### Visual Direction
- Less boxiness
- More scripture-first spacing
- Less repeated metadata
- Stronger text hierarchy
- Manuscript-like section dividers
- Fewer competing gold elements

### Patch Order
1. Relabel reading tabs to पाठ | अर्थ | शब्द | चिंतन.
2. Make पाठ the default tab when opening a mantra.
3. Move chanting player into पाठ.
4. Convert शब्द view from 3-column rows to stacked word cards.
5. Merge व्याख्या and गहराई into चिंतन.
6. Slim reading header.
7. Slim bottom navigation.
8. Retest all reading flows on mobile.
