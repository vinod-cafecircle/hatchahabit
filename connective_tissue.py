with open('book1-golden-feather.html', 'r') as f:
    html = f.read()

import re

def add_connective(html, day_label, first_story_text, connective_line, connective_colour):
    idx = html.find(f'data-label="{day_label}"')
    if idx == -1:
        print(f'⚠️  Slide not found: {day_label}')
        return html
    end = html.find('</svg></div>', idx)
    chunk = html[idx:end]
    # Find the first story text element
    story_idx = chunk.find(f'>{first_story_text}<')
    if story_idx == -1:
        print(f'⚠️  Story text not found in {day_label}: {first_story_text[:40]}')
        return html
    # Find the opening < of that text element
    el_start = chunk.rfind('<text', 0, story_idx)
    # Get the y position of this element to place connective above it
    y_match = re.search(r'y="(\d+)"', chunk[el_start:el_start+100])
    if not y_match:
        print(f'⚠️  Could not find y position in {day_label}')
        return html
    y_pos = int(y_match.group(1))
    # Get x position
    x_match = re.search(r'x="(\d+)"', chunk[el_start:el_start+100])
    x_pos = x_match.group(1) if x_match else '480'
    anchor_match = re.search(r'text-anchor="([^"]+)"', chunk[el_start:el_start+100])
    anchor = anchor_match.group(1) if anchor_match else 'start'
    # Insert connective line before this element
    connective_el = f'<text font-family="Patrick Hand, cursive" font-size="22" fill="{connective_colour}" x="{x_pos}" y="{y_pos - 44}" text-anchor="{anchor}" font-style="italic">{connective_line}</text>\n  '
    insert_pos = idx + el_start
    html = html[:insert_pos] + connective_el + html[insert_pos:]
    print(f'✅ {day_label}: added "{connective_line[:50]}"')
    return html

# Day 02
html = add_connective(html,
    'DAY 02 · PAGE 1',
    'Kev woke before the sun.',
    'The warmth in his wing was still there.',
    '#4CAF82')

# Day 03
html = add_connective(html,
    'DAY 03 · PAGE 1',
    'Every morning in the bush,',
    'Two mornings. Two words. The bush was listening.',
    '#FF8F00')

# Day 04
html = add_connective(html,
    'DAY 04 · PAGE 1',
    'The sky was heavy.',
    'His voice had woken the whole bush. But today felt different.',
    '#8D6E63')

# Day 05
html = add_connective(html,
    'DAY 05 · PAGE 1',
    'It rained. And rained.',
    'Even on the hard day, Kev had shown up.',
    '#90A4AE')

# Day 06
html = add_connective(html,
    'DAY 06 · PAGE 1',
    'A tiny flash of blue',
    'He had shown up in the rain. He had shown up on the hard days.',
    '#1565C0')

# Day 07
html = add_connective(html,
    'DAY 07 · PAGE 1',
    'Seven days.',
    "Ollie's hello was still warm in his chest.",
    '#1565C0')

# Day 07 — also rewrite the page text
html = html.replace(
    '>Seven days.</text>',
    '>Seven mornings. Seven words said out loud.</text>'
)
html = html.replace(
    '>Kev looked at the sky above the creek.</text>',
    '>Kev looked at the water below.</text>'
)
html = html.replace(
    '>Maybe that means doing the thing that scares you.',
    '>It was a long way down.</text>\n  <text font-family="Patrick Hand, cursive" font-size="30" fill="#1565C0" x="490" y="400">Maybe finding your voice means</text>\n  <text font-family="Patrick Hand, cursive" font-size="30" fill="#1565C0" x="490" y="444">using it somewhere that scares you.'
)
print('✅ Day 07 page text rewritten')

# Day 08
html = add_connective(html,
    'DAY 08 · PAGE 1',
    'A large shadow fell',
    'He had flown. He had actually flown.',
    '#FF8F00')

# Day 09
html = add_connective(html,
    'DAY 09 · PAGE 1',
    'A flash of colour — it was Coco!',
    'Rudie had said: there is no just.',
    '#0097A7')

# Day 09 Page 2 — add movement text
html = html.replace(
    'fill="#0097A7" x="480" y="170" text-anchor="middle">Kev laughed and stretched wide.<',
    'fill="#0097A7" x="480" y="150" text-anchor="middle">He stretched left. He stretched right.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#1A237E" x="480" y="198" text-anchor="middle">He shook out his tail feathers.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#0097A7" x="480" y="246" text-anchor="middle">Moving felt good. Really, really good.<'
)
print('✅ Day 09 page 2 movement text added')

# Day 10
html = add_connective(html,
    'DAY 10 · PAGE 1',
    'A wise owl landed softly beside Kev.',
    "Coco's laugh was still somewhere in his feathers.",
    '#8B6914')

# Day 11
html = add_connective(html,
    'DAY 11 · PAGE 1',
    'That evening, Kev sat quietly',
    'Fifi had asked: what did you learn?',
    '#FFF176')

# Day 11 page 1 — add image detail
html = html.replace(
    '>and watched the sun go down over the creek.<',
    '>and watched the sun go down.</text>\n  <text font-family="Patrick Hand, cursive" font-size="30" fill="white" x="480" y="212" text-anchor="middle">The creek turned orange. Then pink.</text>\n  <text font-family="Patrick Hand, cursive" font-size="30" fill="#FFF176" x="480" y="256" text-anchor="middle">Then deep, deep blue.</text>\n  <text font-family="Patrick Hand, cursive" font-size="30" fill="white" x="480" y="300" text-anchor="middle">And Kev didn\'t move. He just watched.<'
)
print('✅ Day 11 image detail added')

# Day 12
html = add_connective(html,
    'DAY 12 · PAGE 1',
    'The morning was cold and grey.',
    'He had watched the sun go down and felt grateful.',
    '#B0BEC5')

# Day 12 — add beat between question and answer
html = html.replace(
    '>Do I belong here? he wondered.<',
    '>Do I belong here? he wondered.</text>\n  <text font-family="Patrick Hand, cursive" font-size="30" fill="white" x="480" y="222" text-anchor="middle">No warmth. No colour.</text>\n  <text font-family="Patrick Hand, cursive" font-size="30" fill="white" x="480" y="266" text-anchor="middle">Just Kev and the quiet bush.<'
)
print('✅ Day 12 extra beat added')

# Day 13
html = add_connective(html,
    'DAY 13 · PAGE 1',
    'Kev felt something different in the air.',
    'He belonged here. He knew it now.',
    '#0097A7')

# Day 14 — replace with lizards/wombats echo
html = html.replace(
    '>Fourteen mornings. Every single one.<',
    '>He woke before the lizards.<'
)
html = html.replace(
    '>The rain ones. The hard ones. He showed up for all of them.<',
    '>Before the wombats. Before anyone.</text>\n  <text font-family="Patrick Hand, cursive" font-size="34" fill="white" x="480" y="220" text-anchor="middle">But this morning —</text>\n  <text font-family="Patrick Hand, cursive" font-size="30" fill="#FDD835" x="480" y="280" text-anchor="middle">he already knew what he was going to say.<'
)
html = html.replace(
    '>He looked at his wings.<',
    ''
)
print('✅ Day 14 opening rewritten')

with open('book1-golden-feather.html', 'w') as f:
    f.write(html)

import re
total = re.search(r'TOTAL = (\d+)', html)
print(f'\n========================================')
print(f'✅ Done. TOTAL = {total.group(1)}')
print(f'Size: {len(html):,} bytes')
print(f'========================================')
