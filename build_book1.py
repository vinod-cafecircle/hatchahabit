import re

with open('book1.html', 'r') as f:
    html = f.read()

# ============================================================
# HELPER — read new SVG assets
# ============================================================
def read_svg(path):
    with open(path, 'r') as f:
        return f.read().strip()

opening_svg = read_svg('assets/characters/kev-nervous-hopeful-opening.svg')
feather_svg = read_svg('assets/characters/feather-glow-day-end.svg')
holding_svg = read_svg('assets/characters/kev-holding-golden-feather.svg')
wings_svg   = read_svg('assets/characters/kev-wing-of-words.svg')

# ============================================================
# STEP 1 — Update all 14 affirmation texts
# ============================================================
affirmations = {
    'DAY 04': ('"I am kind!"',        '"I can do hard things!"'),
    'DAY 07': ('"I can do hard things!"', '"I am brave!"'),
    'DAY 08': ('"I am brave!"',       '"I am enough!"'),
    'DAY 11': ('"I never gave up!"',  '"I am grateful!"'),
    'DAY 12': ('"I keep going!"',     '"I belong here!"'),
    'DAY 13': ('"I am almost there!"','"I am ready!"'),
}

for day, (old_aff, new_aff) in affirmations.items():
    old = f'font-size="58" fill="#FDD835" x="480" y="314" text-anchor="middle">{old_aff}'
    new = f'font-size="58" fill="#FDD835" x="480" y="314" text-anchor="middle">{new_aff}'
    if old in html:
        html = html.replace(old, new, 1)
        print(f'✅ {day} affirmation updated to {new_aff}')
    else:
        print(f'⚠️  {day} affirmation NOT found — check manually')

# ============================================================
# STEP 2 — Update story text per day
# ============================================================
story_updates = [
    # DAY 01 page 1 — night scene
    (
        'Deep in the Australian bush,</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#FDD835" x="500" y="286">when the stars were still out…</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="350">Kev was fast asleep.',
        'The bush was still dark</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="286">when Kev opened one eye.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#FDD835" x="500" y="350">What if nothing happened?'
    ),
    # DAY 01 page 2 — sunrise
    (
        'Then the sun began to rise…</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#3E1F00" x="500" y="316">and Kev opened one eye.',
        'Kev took a breath.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#3E1F00" x="500" y="316">He stretched his wings wide.'
    ),
    # DAY 01 affirmation lead-in
    (
        'Kev took a big breath and said…',
        'It matters that I start, he thought.'
    ),
    # DAY 02 page 1
    (
        'Kev woke up and stretched</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="302">his wings — as wide</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="350">as they could go!',
        'Kev woke before the sun.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="302">His wings felt heavy.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#FDD835" x="500" y="350">Then he remembered yesterday.'
    ),
    # DAY 02 page 2
    (
        'He felt the cool morning air</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="310">fill him right up.',
        'Showing up, he thought,</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="310">is its own kind of strength.'
    ),
    # DAY 02 affirmation lead-in
    (
        'Kev spread his wings and declared…',
        'Kev stretched wide and declared…'
    ),
    # DAY 03 page 1
    (
        'Every morning, Kev would laugh</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="290">his big kookaburra laugh —</text>\n  <text font-family="Fredoka One, cursive" font-size="22" fill="#FDD835" letter-spacing="1" x="500" y="338">HA HA HA!',
        'Every morning in the bush,</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="290">someone had to go first.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#FDD835" x="500" y="338">Kev had always waited.'
    ),
    # DAY 03 page 2
    (
        'His laugh woke the whole bush up.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="310">Even the gum trees</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="358">seemed to smile.',
        'HA HA HA!</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="310">His laugh rang out across</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#FDD835" x="500" y="358">Billabong Creek!'
    ),
    # DAY 03 affirmation lead-in
    (
        'Kev laughed and laughed, then said…',
        'Even the gum trees smiled. Then Kev said…'
    ),
    # DAY 04 page 1 — Coco scene, update text only
    (
        'One morning, Kev heard</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="290">a small sound coming</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="338">from the gum tree.',
        'The sky was heavy.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="290">A hot wind blew in from the north.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#FDD835" x="500" y="338">Some mornings are just hard.'
    ),
    # DAY 04 page 2
    (
        '"Good morning, Kev,"</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="290">sang Coco.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#FDD835" x="500" y="338">"Friends make mornings</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#FDD835" x="500" y="386">better."',
        'Kev sat very still.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="290">Hard mornings are part of it,</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#FDD835" x="500" y="338">he decided. He stood up slowly.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="386">And he spoke anyway.'
    ),
    # DAY 04 affirmation lead-in
    (
        'Kev smiled his biggest smile and said…',
        'His voice came out quiet. But he meant it.'
    ),
    # DAY 05 page 1 — rainy day (keep existing art, update text)
    (
        'One morning, it rained</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="290">and rained.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="338">Kev didn\'t feel like</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="386">getting up.',
        'It rained. And rained.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="290">And rained some more.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#FDD835" x="500" y="338">Kev did not want to leave</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#FDD835" x="500" y="386">his branch.'
    ),
    # DAY 05 page 2
    (
        'But he took a breath</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="310">and got up anyway.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#FDD835" x="500" y="358">That\'s what</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#FDD835" x="500" y="406">habits do.',
        'He thought of the golden feather.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="310">It doesn\'t count on easy days only.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#FDD835" x="500" y="358">He shook off the rain</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#FDD835" x="500" y="406">and stepped forward.'
    ),
    # DAY 05 affirmation lead-in
    (
        'Even on rainy days, Kev declared…',
        'Standing in the rain, Kev declared…'
    ),
    # DAY 06 page 1 — Ollie arrives (keep art)
    (
        'A tiny blue bird</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="290">landed beside Kev.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#FDD835" x="500" y="338">"Good morning!"</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="386">chirped Ollie.',
        'A tiny flash of blue</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="290">landed on the branch beside Kev.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#FDD835" x="500" y="338">It was Ollie —</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="386">the smallest fairy wren.'
    ),
    # DAY 06 page 2
    (
        'Ollie was small but</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="310">full of sparkle.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#FDD835" x="500" y="358">"Kindness starts</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#FDD835" x="500" y="406">with hello," she said.',
        '"I\'ve been watching you,"</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="310">said Ollie, "every morning."</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#FDD835" x="500" y="358">"Kindness starts</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#FDD835" x="500" y="406">with just saying hello."'
    ),
    # DAY 06 affirmation lead-in
    (
        'Kev smiled and said…',
        'Two birds in the morning light. Kev said…'
    ),
    # DAY 07 page 1
    (
        'Seven days!</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="290">Kev looked at the sky.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="338">Could he do it?',
        'Seven days.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="290">Kev looked at the sky above the creek.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#FDD835" x="500" y="338">Wide. Open. Enormous.'
    ),
    # DAY 07 page 2
    (
        'He spread his wings…</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="310">and soared above</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#FDD835" x="500" y="358">Billabong Creek!',
        'He spread his wings.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="310">And then — he was flying.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#FDD835" x="500" y="358">It was terrifying. It was magnificent.'
    ),
    # DAY 07 affirmation lead-in
    (
        'Flying high, Kev called out…',
        'Flying high above the creek, Kev called out…'
    ),
    # DAY 08 page 1 — Rudie scene
    (
        'A large shadow fell</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="290">across the branch.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="338">It was Rudie —</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#FDD835" x="500" y="386">the Eagle!',
        'A large shadow fell</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="290">across the branch.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="338">It was Rudie —</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#FDD835" x="500" y="386">the biggest bird at Billabong Creek.'
    ),
    # DAY 08 page 2
    (
        '"That took courage,"</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="290">"I saw you fly," said Rudie.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="338">Kev stood tall.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="386">He had done it.',
        '"I saw you fly," said Rudie.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="290">"I\'m just a kookaburra," said Kev.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#FDD835" x="500" y="338">Rudie shook his great head.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#FDD835" x="500" y="386">"There is no just. You are enough."'
    ),
    # DAY 08 affirmation lead-in
    (
        'Kev puffed up his chest and said…',
        'Kev stood taller than before and said…'
    ),
    # DAY 09 page 1 — Coco dance
    (
        'A flash of colour danced below Kev.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="290">"Move your body!" cheered Coco.',
        'A flash of colour danced</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="290">through the gum trees.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#FDD835" x="500" y="338">It was Coco — the Lyrebird!'
    ),
    # DAY 09 page 2
    (
        'Kev laughed and stretched his wings.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="310">Moving felt good. Really good.',
        '"MOVE YOUR BODY, KEV!" she sang.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="310">Kev laughed and stretched wide.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#FDD835" x="500" y="358">Moving felt good. Really good.'
    ),
    # DAY 09 affirmation lead-in
    (
        'Kev stretched wide and said…',
        'I have to look after this body, he thought.'
    ),
    # DAY 10 page 1 — Fifi
    (
        'A wise owl landed beside Kev.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="290">"What did you learn today?" asked Fifi.',
        'A wise owl landed softly beside Kev.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="290">"What did you learn today?"</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#FDD835" x="500" y="338">asked Fifi, blinking her great round eyes.'
    ),
    # DAY 10 page 2
    (
        '"I learned I can keep going," said Kev.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="310">"That," said Fifi, "is everything."',
        '"I learned I am enough," said Kev.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="310">"Learning never stops,"</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#FDD835" x="500" y="358">said Fifi. "That\'s the best news."'
    ),
    # DAY 10 affirmation lead-in
    (
        'Kev nodded wisely and said…',
        'Kev looked up at the whole wide sky and said…'
    ),
    # DAY 11 page 1 — sunset
    (
        'That evening, Kev sat quietly</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="290">and watched the sun go down.',
        'That evening, Kev sat quietly</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="290">and watched the sun go down</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#FDD835" x="500" y="338">over Billabong Creek.'
    ),
    # DAY 11 page 2
    (
        '"Eleven days," he whispered.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="310">"I didn\'t give up. Not once."',
        'He thought of Ollie, Rudie, Coco, Fifi.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="310">The creek. The rain. The hard days.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#FDD835" x="500" y="358">All of it is something to be grateful for.'
    ),
    # DAY 11 affirmation lead-in
    (
        'Kev watched the stars appear and said…',
        'Watching the first star appear, Kev said…'
    ),
    # DAY 12 page 1
    (
        'The morning was cold and grey.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="290">Kev didn\'t feel like it at all.',
        'The morning was cold and grey.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="290">Do I belong here? he wondered.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#FDD835" x="500" y="338">Am I really part of this place?'
    ),
    # DAY 12 page 2
    (
        'But he took a breath.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="310">And he showed up anyway.',
        'He listened to the creek.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="310">The gum trees. The lizards.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#FDD835" x="500" y="358">This place knows me. I belong here.'
    ),
    # DAY 12 affirmation lead-in
    (
        'Kev stood up straight and said…',
        'At the edge of the creek, Kev said…'
    ),
    # DAY 13 page 1 — all friends
    (
        'Then the clouds parted.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="290">And all his friends were waiting.',
        'Kev felt something different in the air.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="290">Then the clouds parted.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#FDD835" x="500" y="338">And all his friends were waiting.'
    ),
    # DAY 13 page 2
    (
        '"You made it this far!" they cheered.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="310">"One more day, Kev. One more day."',
        '"You made it this far!" cheered Ollie.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="310">"One more day," said Rudie, steady.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#FDD835" x="500" y="358">"ONE MORE DAY!" sang Coco. Fifi smiled.'
    ),
    # DAY 13 affirmation lead-in
    (
        'Kev spread his wings wide and said…',
        'With all his friends watching, Kev said…'
    ),
    # DAY 14 graduation text
    (
        '14 days. Every single one.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="310">Kev did it. He really did it.',
        'Fourteen mornings. Every single one.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="310">The rain ones. The hard ones.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#FDD835" x="500" y="358">Kev showed up for all of them.'
    ),
]

for old_text, new_text in story_updates:
    if old_text in html:
        html = html.replace(old_text, new_text, 1)
        print(f'✅ Story text updated: {old_text[:50]}...')
    else:
        print(f'⚠️  NOT FOUND: {old_text[:50]}...')

# ============================================================
# STEP 3 — Update affirmations recap list (closing page)
# ============================================================
old_list = '''Day 1 — "I believe in me!"</text>
  <text font-family="Patrick Hand, cursive" font-size="22" fill="white" x="170" y="358">Day 2 — "I am strong!"</text>
  <text font-family="Patrick Hand, cursive" font-size="22" fill="white" x="170" y="390">Day 3 — "My voice matters!"</text>
  <text font-family="Patrick Hand, cursive" font-size="22" fill="white" x="170" y="422">Day 4 — "I can do hard things!"</text>
  <text font-family="Patrick Hand, cursive" font-size="22" fill="white" x="170" y="454">Day 5 — "I show up every day!"</text>
  <text font-family="Patrick Hand, cursive" font-size="22" fill="white" x="170" y="486">Day 6 — "I am kind!"</text>
  <text font-family="Patrick Hand, cursive" font-size="22" fill="white" x="510" y="326">Day 7 — "I can do hard things!"</text>
  <text font-family="Patrick Hand, cursive" font-size="22" fill="white" x="510" y="358">Day 8 — "I am brave!"</text>
  <text font-family="Patrick Hand, cursive" font-size="22" fill="white" x="510" y="390">Day 9 — "I take care of myself!"</text>
  <text font-family="Patrick Hand, cursive" font-size="22" fill="white" x="510" y="422">Day 10 — "I love to learn!"</text>
  <text font-family="Patrick Hand, cursive" font-size="22" fill="white" x="510" y="454">Day 11 — "I never gave up!"</text>
  <text font-family="Patrick Hand, cursive" font-size="22" fill="white" x="510" y="486">Day 12 — "I keep going!"'''

new_list = '''Day 1 — "I believe in me!"</text>
  <text font-family="Patrick Hand, cursive" font-size="22" fill="white" x="170" y="358">Day 2 — "I am strong!"</text>
  <text font-family="Patrick Hand, cursive" font-size="22" fill="white" x="170" y="390">Day 3 — "My voice matters!"</text>
  <text font-family="Patrick Hand, cursive" font-size="22" fill="white" x="170" y="422">Day 4 — "I can do hard things!"</text>
  <text font-family="Patrick Hand, cursive" font-size="22" fill="white" x="170" y="454">Day 5 — "I show up every day!"</text>
  <text font-family="Patrick Hand, cursive" font-size="22" fill="white" x="170" y="486">Day 6 — "I am kind!"</text>
  <text font-family="Patrick Hand, cursive" font-size="22" fill="white" x="510" y="326">Day 7 — "I am brave!"</text>
  <text font-family="Patrick Hand, cursive" font-size="22" fill="white" x="510" y="358">Day 8 — "I am enough!"</text>
  <text font-family="Patrick Hand, cursive" font-size="22" fill="white" x="510" y="390">Day 9 — "I take care of myself!"</text>
  <text font-family="Patrick Hand, cursive" font-size="22" fill="white" x="510" y="422">Day 10 — "I love to learn!"</text>
  <text font-family="Patrick Hand, cursive" font-size="22" fill="white" x="510" y="454">Day 11 — "I am grateful!"</text>
  <text font-family="Patrick Hand, cursive" font-size="22" fill="white" x="510" y="486">Day 12 — "I belong here!"'''

if old_list in html:
    html = html.replace(old_list, new_list, 1)
    print('✅ Affirmations recap list updated')
else:
    print('⚠️  Affirmations recap list NOT found — check manually')

# ============================================================
# STEP 4 — Update Day 13 affirmation in recap (last item)
# ============================================================
html = html.replace(
    'Day 13 — &quot;I am almost there!&quot;',
    'Day 13 — &quot;I am ready!&quot;'
)
html = html.replace(
    'Day 13 — "I am almost there!"',
    'Day 13 — "I am ready!"'
)
print('✅ Day 13 recap updated')

# ============================================================
# STEP 5 — Update certificate text
# ============================================================
html = html.replace(
    'has completed 14 days of morning habits',
    'has completed 14 mornings at Billabong Creek'
)
html = html.replace(
    'with Kev the Kookaburra',
    'with Kev the Kookaburra. You showed up. You believed.'
)
print('✅ Certificate text updated')

# ============================================================
# STEP 6 — Update Day 14 final affirmation text in recap
# ============================================================
html = html.replace(
    'Day 14 — &quot;Words have wings — and so do I!&quot;',
    'Day 14 — &quot;Words have wings — and so do I!&quot;'
)
print('✅ Day 14 recap confirmed')

# ============================================================
# WRITE OUTPUT
# ============================================================
with open('book1-golden-feather.html', 'w') as f:
    f.write(html)

print('\n========================================')
print('✅ book1-golden-feather.html written')
print(f'   Size: {len(html):,} bytes')
print('========================================')
