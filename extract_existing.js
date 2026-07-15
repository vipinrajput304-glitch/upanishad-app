#!/usr/bin/env node
// Extract existing Upanishad data from index.html into JSON files
// Reads the JS data section, evaluates it, and writes standard JSON

const fs = require('fs');
const path = require('path');

const html = fs.readFileSync('index.html', 'utf8');

// Extract the script block containing data
const scriptMatch = html.match(/<script>([\s\S]*?)<\/script>/);
if (!scriptMatch) { console.error('No script block found'); process.exit(1); }

const fullScript = scriptMatch[1];

// Extract just the data portion: from "const UP=" up to "let CU="
const dataStart = fullScript.indexOf('const UP=');
const dataEnd = fullScript.indexOf('let CU=');
if (dataStart === -1 || dataEnd === -1) {
  console.error('Could not find data boundaries (UP...CU)');
  process.exit(1);
}

const dataSection = fullScript.substring(dataStart, dataEnd);

// Evaluate data section to get actual JS objects
// The data section already contains W/D/C helper declarations
const evalCode = dataSection + `
module.exports = { UP, ISHA, MANDUKYA, AITAREYA, AITAREYA_EXTRA, AITAREYA_REST, KENA, MD };
`;

// Write temp file, require it, delete temp
const tmpFile = path.join(__dirname, '_extract_tmp.js');
fs.writeFileSync(tmpFile, evalCode);

let data;
try {
  data = require(tmpFile);
} catch (e) {
  console.error('Failed to evaluate data section:', e.message);
  fs.unlinkSync(tmpFile);
  process.exit(1);
}
fs.unlinkSync(tmpFile);

const outDir = 'content';

// Normalize commentary format: ensure all cm entries have {a, h, en, ins}
// The HTML uses {a, h, en, ins} directly (not the C() helper)
function normalizeMantras(mantras) {
  return mantras.map(m => {
    const normalized = { ...m };
    // Remove adhyaya field if present (Aitareya uses it for display, not in JSON schema)
    // We'll preserve it since it might be useful
    if (normalized.cm) {
      for (const key of ['advaita', 'vishisht', 'aurobindo']) {
        const c = normalized.cm[key];
        if (c) {
          // Normalize field names: hi->h (if needed), insight->ins (if needed)
          normalized.cm[key] = {
            a: c.a || '',
            h: c.h || c.hi || '',
            en: c.en || '',
            ins: c.ins || c.insight || ''
          };
        }
      }
    }
    return normalized;
  });
}

// Extract each Upanishad
const extractions = [
  { name: 'isha', data: data.ISHA, file: 'isha.json' },
  { name: 'mandukya', data: data.MANDUKYA, file: 'mandukya.json' },
  { name: 'aitareya', data: [...data.AITAREYA, ...data.AITAREYA_EXTRA, ...data.AITAREYA_REST], file: 'aitareya.json' },
  { name: 'kena (app mantras 1-4)', data: data.KENA, file: 'kena_app.json' },
];

for (const { name, data: mantras, file } of extractions) {
  const normalized = normalizeMantras(mantras);
  const outPath = path.join(outDir, file);
  fs.writeFileSync(outPath, JSON.stringify(normalized, null, 2), 'utf8');
  console.log(`✓ ${name}: ${normalized.length} mantras → ${outPath}`);

  // Validate ids
  const ids = normalized.map(m => m.id);
  console.log(`  ids: [${ids.join(', ')}]`);
}

// Also extract UP metadata for catalog building
fs.writeFileSync(
  path.join(outDir, '_up_metadata.json'),
  JSON.stringify(data.UP, null, 2),
  'utf8'
);
console.log(`\n✓ UP metadata → ${path.join(outDir, '_up_metadata.json')}`);

// Now merge kena: app has 1-4, JSON files have 5-34
console.log('\n--- Kena merge ---');
const kenaAppPath = path.join(outDir, 'kena_app.json');
const kenaFiles = [
  path.join(outDir, 'kena_p1b.json'),  // 5-8
  path.join(outDir, 'kena_p2.json'),    // 9-16
  path.join(outDir, 'kena_p3.json'),    // 17-28
  path.join(outDir, 'kena_p4.json'),    // 29-34
];

let kenaFull = [...normalizeMantras(data.KENA)]; // 1-4 from app
for (const kf of kenaFiles) {
  if (fs.existsSync(kf)) {
    const part = JSON.parse(fs.readFileSync(kf, 'utf8'));
    kenaFull = kenaFull.concat(part);
    console.log(`  + ${path.basename(kf)}: ${part.length} mantras (ids ${part.map(m=>m.id).join(',')})`);
  } else {
    console.warn(`  ⚠ Missing: ${kf}`);
  }
}

const kenaFullPath = path.join(outDir, 'kena.json');
fs.writeFileSync(kenaFullPath, JSON.stringify(kenaFull, null, 2), 'utf8');
console.log(`✓ Kena merged: ${kenaFull.length} mantras → ${kenaFullPath}`);
console.log(`  ids: [${kenaFull.map(m=>m.id).join(', ')}]`);

console.log('\n=== Extraction complete ===');
console.log('Files created:');
console.log('  content/isha.json      - 18 mantras (full, from app)');
console.log('  content/mandukya.json  - 12 mantras (full, from app)');
console.log('  content/aitareya.json  - 33 mantras (full, from app)');
console.log('  content/kena_app.json  - 4 mantras (app-only, for reference)');
console.log('  content/kena.json      - 34 mantras (merged: app + JSON files)');
console.log('  content/_up_metadata.json - UP array metadata');
