with open('book1-golden-feather.html', 'r') as f:
    html = f.read()

fixes = []

# ============================================================
# FIX 1 — Page 27 — remove "the Eagle!" fragment
# ============================================================
fixes.append((
    'fill="#FF8F00" x="584" y="326">the Eagle!</text>',
    'fill="#FF8F00" x="584" y="326"></text>'
))

# ============================================================
# FIX 2 — Page 13 — remove "seemed to smile." fragment
# ============================================================
fixes.append((
    'fill="#33691E" x="500" y="360">seemed to smile.',
    'fill="#33691E" x="500" y="360">Even the gum trees seemed to smile.'
))

# ============================================================
# FIX 3 — Page 6 (Day 01 Page 1) — add one more line
# ============================================================
fixes.append((
    'fill="#FDD835" x="500" y="350">What if nothing happened?</text>\n  <text font-family="Fredoka One, cursive" font-size="14" fill="white" opacity="0.25" x="480" y="528"',
    'fill="#FDD835" x="500" y="350">What if nothing happened?</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="410">It matters that I start.</text>\n  <text font-family="Fredoka One, cursive" font-size="14" fill="white" opacity="0.25" x="480" y="528"'
))

# ============================================================
# FIX 4 — Page 7 (Day 01 Page 2) — add one more line
# ============================================================
fixes.append((
    'fill="#3E1F00" x="500" y="316">He stretched his wings wide.</text>\n  <text font-family="Fredoka One, cursive" font-size="14" fill="#3E1F00" opacity="0.25" x="480" y="528"',
    'fill="#3E1F00" x="500" y="316">He stretched his wings wide.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#3E1F00" x="500" y="374">The cool morning air filled him right up.</text>\n  <text font-family="Fredoka One, cursive" font-size="14" fill="#3E1F00" opacity="0.25" x="480" y="528"'
))

# ============================================================
# FIX 5 — Page 19 (Day 05 Page 2) — fix tense
# ============================================================
fixes.append((
    "It doesn't count on easy days only.",
    "It didn't count on easy days only."
))

# ============================================================
# FIX 6 — Page 28 (Day 08 Page 2) — add Kev's line before Rudie
# ============================================================
fixes.append((
    'fill="#1A237E" x="584" y="180">"I saw you fly," said Rudie.</text>\n  <text font-family="Patrick Hand, cursive" font-size="30" fill="#1A237E" x="584" y="222">"There is no just," he said.',
    'fill="#1A237E" x="584" y="180">"I saw you fly," said Rudie.</text>\n  <text font-family="Patrick Hand, cursive" font-size="30" fill="#FF8F00" x="584" y="222">"I\'m just a kookaburra," said Kev.</text>\n  <text font-family="Patrick Hand, cursive" font-size="30" fill="#1A237E" x="584" y="264">"There is no just," said Rudie.</text>\n  <text font-family="Patrick Hand, cursive" font-size="30" fill="#FF8F00" x="584" y="306">"You are exactly enough."'
))

# ============================================================
# FIX 7 — Page 45 (Day 14 Page 1) — add golden feather reveal
# ============================================================
fixes.append((
    'fill="#90CAF9" x="480" y="228" text-anchor="middle">The rain ones. The hard ones. He showed up for all of them.',
    'fill="#90CAF9" x="480" y="200" text-anchor="middle">The rain ones. The hard ones. He showed up for all of them.</text>\n  <text font-family="Patrick Hand, cursive" font-size="30" fill="white" x="480" y="270" text-anchor="middle">He looked at his wings.</text>\n  <text font-family="Fredoka One, cursive" font-size="38" fill="#FDD835" x="480" y="330" text-anchor="middle">There — shining gold —</text>\n  <text font-family="Fredoka One, cursive" font-size="38" fill="#FDD835" x="480" y="378" text-anchor="middle">was the feather.'
))

# ============================================================
# FIX 8 — Page 15 (Day 04 Page 1) — Kev too small, reposition
# ============================================================
fixes.append((
    'translate(10, 48) scale(0.44)',
    'translate(60, 140) scale(0.68)'
))

# ============================================================
# FIX 9 — Page 25 (Day 07 Page 2) — Kev too large
# ============================================================
fixes.append((
    'translate(86, 114) scale(1.02)',
    'translate(60, 114) scale(0.76)'
))

# ============================================================
# FIX 10 — Pages 42 and 43 (Day 13) — fix negative x
# ============================================================
fixes.append((
    'translate(-22, 210) scale(0.53)',
    'translate(20, 210) scale(0.53)'
))

# ============================================================
# FIX 11 — Standardise all affirmation font sizes to 58px
# ============================================================
# "I am brave!" — currently 46px
fixes.append((
    'font-size="46" fill="#FDD835" x="480" y="314" text-anchor="middle">"I am brave!"',
    'font-size="58" fill="#FDD835" x="480" y="314" text-anchor="middle">"I am brave!"'
))
# "I take care of myself!" — currently 46px
fixes.append((
    'font-size="46" fill="#FDD835" x="480" y="314" text-anchor="middle">"I take care of myself!"',
    'font-size="52" fill="#FDD835" x="480" y="314" text-anchor="middle">"I take care of myself!"'
))
# "I show up every day!" — currently 52px — ok, leave
# "I love to learn!" — currently 52px — bump to 58px
fixes.append((
    'font-size="52" fill="#FDD835" x="480" y="314" text-anchor="middle">"I love to learn!"',
    'font-size="58" fill="#FDD835" x="480" y="314" text-anchor="middle">"I love to learn!"'
))
# "I am grateful!" — currently 52px
fixes.append((
    'font-size="52" fill="#FDD835" x="480" y="314" text-anchor="middle">"I am grateful!"',
    'font-size="58" fill="#FDD835" x="480" y="314" text-anchor="middle">"I am grateful!"'
))
# "I belong here!" — currently 52px
fixes.append((
    'font-size="52" fill="#FDD835" x="480" y="314" text-anchor="middle">"I belong here!"',
    'font-size="58" fill="#FDD835" x="480" y="314" text-anchor="middle">"I belong here!"'
))
# "I am ready!" — currently 44px
fixes.append((
    'font-size="44" fill="#FDD835" x="480" y="314" text-anchor="middle">"I am ready!"',
    'font-size="58" fill="#FDD835" x="480" y="314" text-anchor="middle">"I am ready!"'
))
# "I show up every day!" — 52px to 58px
fixes.append((
    'font-size="52" fill="#FDD835" x="480" y="314" text-anchor="middle">"I show up every day!"',
    'font-size="58" fill="#FDD835" x="480" y="314" text-anchor="middle">"I show up every day!"'
))

# ============================================================
# Apply all fixes
# ============================================================
count_ok = 0
count_miss = 0

for old, new in fixes:
    if old in html:
        html = html.replace(old, new, 1)
        print(f'✅ {old[:60]}...')
        count_ok += 1
    else:
        print(f'⚠️  NOT FOUND: {old[:60]}...')
        count_miss += 1

with open('book1-golden-feather.html', 'w') as f:
    f.write(html)

print(f'\n========================================')
print(f'✅ {count_ok} fixes applied')
print(f'⚠️  {count_miss} not found')
print(f'Size: {len(html):,} bytes')
print(f'========================================')
