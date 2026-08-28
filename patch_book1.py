with open('book1-golden-feather.html', 'r') as f:
    html = f.read()

fixes = [
    # DAY 11 affirmation
    ('"I never gave up!"', '"I am grateful!"'),
    # DAY 12 affirmation
    ('"I keep going!"', '"I belong here!"'),
    # DAY 13 affirmation
    ('"I am almost there!"', '"I am ready!"'),

    # DAY 02 page 1
    (
        'y="248">Kev woke up and stretched</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#1A237E" x="500" y="296">his wings — as wide</text>\n  <text font-family="Patrick Hand, cursive" font-s',
        'y="248">Kev woke before the sun.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#1A237E" x="500" y="296">His wings felt heavy.</text>\n  <text font-family="Patrick Hand, cursive" font-s'
    ),
    # DAY 02 page 2
    (
        'y="270">He felt the cool morning air</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#1A237E" x="500" y="318">fill him right up.',
        'y="270">Showing up, he thought,</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#1A237E" x="500" y="318">is its own kind of strength.'
    ),
    # DAY 03 page 1
    (
        'y="242">Every morning, Kev would laugh</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#3E2000" x="500" y="290">his big kookaburra laugh —',
        'y="242">Every morning in the bush,</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#3E2000" x="500" y="290">someone had to go first.'
    ),
    # DAY 03 page 2
    (
        'y="252">His laugh woke the whole bush up.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#33691E" x="500" y="312">Even the gum trees</text>\n  <text font-family="Pa',
        'y="252">HA HA HA! His laugh rang out</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#33691E" x="500" y="312">across Billabong Creek!</text>\n  <text font-family="Pa'
    ),
    # DAY 04 page 1
    (
        'y="238">One morning, it rained</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#263238" x="500" y="284">and rained.',
        'y="238">The sky was heavy.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#263238" x="500" y="284">A hot wind blew from the north.'
    ),
    # DAY 05 page 1
    (
        'y="242">But he took a breath</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#263238" x="500" y="290">and got up anyway.',
        'y="242">It rained. And rained.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#263238" x="500" y="290">And rained some more.'
    ),
    # DAY 06 page 1
    (
        'y="192">A tiny blue bird</text>\n  <text font-family="Patrick Hand, cursive" font-size="30" fill="#1A237E" x="580" y="236">landed beside Kev.',
        'y="192">A tiny flash of blue</text>\n  <text font-family="Patrick Hand, cursive" font-size="30" fill="#1A237E" x="580" y="236">landed on the branch beside Kev.'
    ),
    # DAY 07 page 1
    (
        'y="196">Seven days!</text>\n  <text font-family="Patrick Hand, cursive" font-size="30" fill="#1A237E" x="490" y="240">Kev looked at the sky.',
        'y="196">Seven days.</text>\n  <text font-family="Patrick Hand, cursive" font-size="30" fill="#1A237E" x="490" y="240">Kev looked at the sky above the creek.'
    ),
    # DAY 07 page 2
    (
        'y="192">He spread his wings…</text>\n  <text font-family="Patrick Hand, cursive" font-size="30" fill="#1565C0" x="588" y="260">and soared above</text>\n  <text font-family="Patrick Hand, cur',
        'y="192">He spread his wings.</text>\n  <text font-family="Patrick Hand, cursive" font-size="30" fill="#1565C0" x="588" y="260">And then — he was flying.</text>\n  <text font-family="Patrick Hand, cur'
    ),
    # DAY 08 page 1
    (
        'y="190">A large shadow fell</text>\n  <text font-family="Patrick Hand, cursive" font-size="30" fill="#1A237E" x="584" y="232">across the branch.',
        'y="190">A large shadow fell</text>\n  <text font-family="Patrick Hand, cursive" font-size="30" fill="#1A237E" x="584" y="232">across the branch. It was Rudie —'
    ),
    # DAY 08 page 2
    (
        'y="180">"That took courage,"</text>\n  <text font-family="Patrick Hand, cursive" font-size="30" fill="#1A237E" x="584" y="222">"I saw you fly," said Rudie.',
        'y="180">"I saw you fly," said Rudie.</text>\n  <text font-family="Patrick Hand, cursive" font-size="30" fill="#1A237E" x="584" y="222">"There is no just," he said.'
    ),
    # DAY 09 page 1
    (
        'text-anchor="middle">A flash of colour danced below Kev.</text>\n  <text font-family="Patrick Hand, cursive" font-size="36" fill="#0097A7" x="480" y="170" text-anchor="middle">"Move your body!" cheered ',
        'text-anchor="middle">A flash of colour — it was Coco!</text>\n  <text font-family="Patrick Hand, cursive" font-size="36" fill="#0097A7" x="480" y="170" text-anchor="middle">The Lyrebird danced through the gum trees.'
    ),
    # DAY 09 page 2
    (
        'text-anchor="middle">Kev laughed and stretched his wings.</text>\n  <text font-family="Patrick Hand, cursive" font-size="36" fill="#0097A7" x="480" y="170" text-anchor="middle">Moving felt good. Really ',
        'text-anchor="middle">"MOVE YOUR BODY, KEV!" she sang.</text>\n  <text font-family="Patrick Hand, cursive" font-size="36" fill="#0097A7" x="480" y="170" text-anchor="middle">Kev laughed and stretched wide.'
    ),
    # DAY 10 page 1
    (
        'text-anchor="middle">A wise owl landed beside Kev.</text>\n  <text font-family="Patrick Hand, cursive" font-size="35" fill="#8B6914" x="480" y="168" text-anchor="middle">"What did you learn today?" aske',
        'text-anchor="middle">A wise owl landed softly beside Kev.</text>\n  <text font-family="Patrick Hand, cursive" font-size="35" fill="#8B6914" x="480" y="168" text-anchor="middle">"What did you learn today?" aske'
    ),
    # DAY 10 page 2
    (
        'text-anchor="middle">"I learned I can keep going," said Kev.</text>\n  <text font-family="Patrick Hand, cursive" font-size="35" fill="#8B6914" x="480" y="168" text-anchor="middle">"That," said Fifi, "is ',
        'text-anchor="middle">"I learned I am enough," said Kev.</text>\n  <text font-family="Patrick Hand, cursive" font-size="35" fill="#8B6914" x="480" y="168" text-anchor="middle">"Learning never stops," said Fifi.'
    ),
    # DAY 11 page 1
    (
        'text-anchor="middle">That evening, Kev sat quietly</text>\n  <text font-family="Patrick Hand, cursive" font-size="35" fill="white" x="480" y="162" text-anchor="middle">and watched the sun go down.',
        'text-anchor="middle">That evening, Kev sat quietly</text>\n  <text font-family="Patrick Hand, cursive" font-size="35" fill="white" x="480" y="162" text-anchor="middle">and watched the sun go down over the creek.'
    ),
    # DAY 11 page 2
    (
        'text-anchor="middle">"Eleven days," he whispered.</text>\n  <text font-family="Patrick Hand, cursive" font-size="35" fill="#FFF176" x="480" y="162" text-anchor="middle">"I didn\'t give up. Not once."',
        'text-anchor="middle">He thought of Ollie, Rudie, Coco, Fifi.</text>\n  <text font-family="Patrick Hand, cursive" font-size="35" fill="#FFF176" x="480" y="162" text-anchor="middle">All of it is something to be grateful for.'
    ),
    # DAY 12 page 1
    (
        'text-anchor="middle">The morning was cold and grey.</text>\n  <text font-family="Patrick Hand, cursive" font-size="35" fill="#B0BEC5" x="480" y="168" text-anchor="middle">Kev didn\'t feel like it at all.',
        'text-anchor="middle">The morning was cold and grey.</text>\n  <text font-family="Patrick Hand, cursive" font-size="35" fill="#B0BEC5" x="480" y="168" text-anchor="middle">Do I belong here? he wondered.'
    ),
    # DAY 12 page 2 — find Day 12 "But he took a breath" specifically
    (
        'fill="#546E7A" x="480" y="152" text-anchor="middle">But he took a breath.',
        'fill="#546E7A" x="480" y="152" text-anchor="middle">He listened to the creek. The gum trees.'
    ),
    # DAY 13 page 1
    (
        'text-anchor="middle">Then the clouds parted.</text>\n  <text font-family="Patrick Hand, cursive" font-size="35" fill="#0097A7" x="480" y="152" text-anchor="middle">And all his friends were waiting.',
        'text-anchor="middle">Kev felt something different in the air.</text>\n  <text font-family="Patrick Hand, cursive" font-size="35" fill="#0097A7" x="480" y="152" text-anchor="middle">Then the clouds parted — and his friends were waiting.'
    ),
    # DAY 13 page 2
    (
        'text-anchor="middle">"You made it this far!" they cheered.</text>\n  <text font-family="Patrick Hand, cursive" font-size="35" fill="#0097A7" x="480" y="152" text-anchor="middle">"One more day, Kev. One m',
        'text-anchor="middle">"You made it this far!" cheered Ollie.</text>\n  <text font-family="Patrick Hand, cursive" font-size="35" fill="#0097A7" x="480" y="152" text-anchor="middle">"One more day," said Rudie. Fifi smiled.'
    ),
    # DAY 14
    (
        'text-anchor="middle">14 days. Every single one.</text>\n  <text font-family="Patrick Hand, cursive" font-size="30" fill="#90CAF9" x="480" y="228" text-anchor="middle">Kev did it. He really did it.',
        'text-anchor="middle">Fourteen mornings. Every single one.</text>\n  <text font-family="Patrick Hand, cursive" font-size="30" fill="#90CAF9" x="480" y="228" text-anchor="middle">The rain ones. The hard ones. He showed up for all of them.'
    ),
]

count_ok = 0
count_miss = 0
for old, new in fixes:
    if old in html:
        html = html.replace(old, new, 1)
        print(f'✅ {old[:55]}...')
        count_ok += 1
    else:
        print(f'⚠️  NOT FOUND: {old[:55]}...')
        count_miss += 1

with open('book1-golden-feather.html', 'w') as f:
    f.write(html)

print(f'\n========================================')
print(f'✅ {count_ok} fixes applied')
print(f'⚠️  {count_miss} not found')
print(f'File: book1-golden-feather.html')
print(f'Size: {len(html):,} bytes')
print(f'========================================')
