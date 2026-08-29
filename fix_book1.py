with open('book1-golden-feather.html', 'r') as f:
    html = f.read()

fixes = []

# ============================================================
# FIX 1 — Day 02 Page 1 — remove orphaned "as they could go!"
# ============================================================
fixes.append((
    'fill="#1A237E" x="500" y="344">as they could go!',
    'fill="#1A237E" x="500" y="344">Then he remembered yesterday.'
))

# ============================================================
# FIX 2 — Day 03 Page 1 — remove double HA HA HA
# Replace the HA HA HA on page 1 with setup text
# ============================================================
fixes.append((
    'font-size="48" fill="#FF8F00" x="500" y="356">HA HA HA!',
    'font-size="32" fill="#FF8F00" x="500" y="356">Kev had always waited.'
))

# ============================================================
# FIX 3 — Day 04 Page 1 — replace old Coco story with hard day
# ============================================================
fixes.append((
    'fill="#1A237E" x="500" y="234">One morning, Kev heard</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#1A237E" x="500" y="280">a small sound coming</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#1A237E" x="500" y="326">from the gum tree.',
    'fill="#1A237E" x="500" y="234">The sky was heavy.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#1A237E" x="500" y="280">A hot wind blew from the north.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#1A237E" x="500" y="326">Some mornings are just hard.'
))

# ============================================================
# FIX 4 — Day 04 Page 2 — replace old Coco dialogue with hard day resolve
# ============================================================
fixes.append((
    'fill="#1A237E" x="500" y="234">"Good morning, Kev,"</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#1A237E" x="500" y="280">sang Coco.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#2E7D32" x="500" y="325">"Friends make mornings</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#2E7D32" x="500" y="362">better."',
    'fill="#1A237E" x="500" y="234">Kev sat very still.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#1A237E" x="500" y="280">Hard mornings are part of it,</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#1A237E" x="500" y="325">he decided. He stood up</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#1A237E" x="500" y="362">and spoke anyway.'
))

# ============================================================
# FIX 5 — Day 05 Page 1 — swap hot wind text for rain text
# ============================================================
fixes.append((
    'fill="#263238" x="500" y="238">The sky was heavy.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#263238" x="500" y="284">A hot wind blew from the north.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#37474F" x="500" y="348">Kev didn\'t feel like</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#37474F" x="500" y="394">getting up.',
    'fill="#263238" x="500" y="238">It rained. And rained.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#263238" x="500" y="284">And rained some more.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#37474F" x="500" y="348">Kev did not want to leave</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#37474F" x="500" y="394">his branch.'
))

# ============================================================
# FIX 6 — Day 05 Page 2 — swap rain text for resolve text
# ============================================================
fixes.append((
    'fill="#263238" x="500" y="242">It rained. And rained.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#263238" x="500" y="290">And rained some more.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#1A237E" x="500" y="358">That\'s what</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#1A237E" x="500" y="404">habits do.',
    'fill="#263238" x="500" y="242">He thought of the golden feather.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#263238" x="500" y="290">It doesn\'t count on easy days only.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#1A237E" x="500" y="358">He shook off the rain</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#1A237E" x="500" y="404">and stepped forward.'
))

# ============================================================
# FIX 7 — Day 07 Page 1 — remove "Could he do it?"
# ============================================================
fixes.append((
    'fill="#1565C0" x="490" y="308">Could he do it?',
    'fill="#1565C0" x="490" y="308">Maybe that means doing the thing that scares you.'
))

# ============================================================
# FIX 8 — Day 08 Page 1 — remove duplicate "It was Rudie —"
# ============================================================
fixes.append((
    'fill="#1A237E" x="584" y="232">across the branch. It was Rudie —</text>\n  <text font-family="Patrick Hand, cursive" font-size="30" fill="#FF8F00" x="584" y="284">It was Rudie —</text>\n  <text font-family="Patrick Hand, cursive" font-size="30"',
    'fill="#1A237E" x="584" y="232">across the branch.</text>\n  <text font-family="Patrick Hand, cursive" font-size="30" fill="#FF8F00" x="584" y="284">It was Rudie — the Eagle.</text>\n  <text font-family="Patrick Hand, cursive" font-size="30"'
))

# ============================================================
# FIX 9 — Day 09 Page 1 — remove ".Coco." fragment
# ============================================================
fixes.append((
    '>The Lyrebird danced through the gum trees.Coco.<',
    '>The Lyrebird — dancing through the gum trees!<'
))

# ============================================================
# FIX 10 — Day 09 Page 2 — remove ".good." fragment
# ============================================================
fixes.append((
    '>Kev laughed and stretched wide.good.<',
    '>Kev laughed and stretched wide.<'
))

# ============================================================
# FIX 11 — Day 10 Page 2 — remove ".everything." fragment
# ============================================================
fixes.append((
    '>"Learning never stops," said Fifi.everything."<',
    '>"Learning never stops," said Fifi.<'
))

# ============================================================
# FIX 12 — Day 13 Page 2 — remove ".ore day." fragment
# ============================================================
fixes.append((
    '>"One more day," said Rudie. Fifi smiled.ore day."<',
    '>"One more day," said Rudie. Fifi just smiled.<'
))

# ============================================================
# FIX 13 — Day 14 — remove "Graduation Day!" heading
# ============================================================
fixes.append((
    'font-size="48" fill="#FDD835" x="480" y="128" text-anchor="middle">Graduation Day!</text>\n  <text font-family="Patrick Hand, cursive" font-size="30" fill="white" x="480" y="184" text-anchor="middle">Fourteen mornings.',
    'font-size="38" fill="#FDD835" x="480" y="128" text-anchor="middle">Fourteen mornings.'
))

# ============================================================
# FIX 14 — Closing Page — fix "said Kev, right to you"
# ============================================================
fixes.append((
    'fill="white" opacity="0.8" x="56" y="390">said Kev,</text>\n  <text font-family="Patrick Hand, cursive" font-size="26" fill="white" opacity="0.8" x="56" y="428">right to you.',
    'fill="white" opacity="0.8" x="56" y="390">Kev held it out —</text>\n  <text font-family="Patrick Hand, cursive" font-size="26" fill="white" opacity="0.8" x="56" y="428">just for you.'
))

# ============================================================
# FIX 15 — Affirmations recap page — fix Days 7, 11, 12
# ============================================================
fixes.append((
    'Day 11 — "I never gave up!"',
    'Day 11 — "I am grateful!"'
))
fixes.append((
    'Day 12 — "I keep going!"',
    'Day 12 — "I belong here!"'
))
fixes.append((
    'fill="#90CAF9" x="530" y="192">Day 11 — "I never gave up!"',
    'fill="#90CAF9" x="530" y="192">Day 11 — "I am grateful!"'
))
fixes.append((
    'fill="#90CAF9" x="530" y="224">Day 12 — "I keep going!"',
    'fill="#90CAF9" x="530" y="224">Day 12 — "I belong here!"'
))

# ============================================================
# FIX 16 — Affirmation lead-ins — standardise to third person
# ============================================================
fixes.append((
    '>His voice came out quiet. But he meant it.<',
    '>Quietly but clearly, Kev said…<'
))
fixes.append((
    '>I have to look after this body, he thought.<',
    '>Stretching wide, Kev said…<'
))
fixes.append((
    '>It matters that I start, he thought.<',
    '>Taking a breath, Kev said…<'
))

# ============================================================
# Now find and fix Day 04 and Day 07 affirmations
# They are in wrong positions — need to find by context
# ============================================================
# Day 04 affirmation should be "I can do hard things!" not "I am enough!"
# Find it by the DAY 04 affirmation page marker
import re

# Find all affirmation pages with their day labels and affirmation text
aff_pages = list(re.finditer(r'(DAY 0[0-9] · PAGE 3)', html))
for m in aff_pages:
    day_label = m.group(1)
    snippet = html[m.start():m.start()+600]
    aff_match = re.search(r'"(I [^"]+)"</text>\n  \n  <text font-family="Patrick Hand.*?something warm', snippet, re.DOTALL)
    if aff_match:
        print(f"{day_label}: {aff_match.group(1)}")

# ============================================================
# Apply all fixes
# ============================================================
count_ok = 0
count_miss = 0
for old, new in fixes:
    if old in html:
        html = html.replace(old, new, 1)
        print(f'✅ Fixed: {old[:55]}...')
        count_ok += 1
    else:
        print(f'⚠️  NOT FOUND: {old[:55]}...')
        count_miss += 1

with open('book1-golden-feather.html', 'w') as f:
    f.write(html)

print(f'\n========================================')
print(f'✅ {count_ok} fixes applied')
print(f'⚠️  {count_miss} not found')
print(f'Size: {len(html):,} bytes')
print(f'========================================')
