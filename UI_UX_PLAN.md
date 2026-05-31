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
