with open('book1-golden-feather.html', 'r') as f:
    html = f.read()

fixes = []

# ============================================================
# FIX 1 — Cover — remove certificate text
# ============================================================
fixes.append((
    'with Kev the Kookaburra. You showed up. You believed.',
    'with Kev the Kookaburra'
))

# ============================================================
# FIX 2 — Day 01 Page 1 — let question breathe alone
# remove "It matters that I start" from P1
# ============================================================
fixes.append((
    'fill="#FDD835" x="500" y="350">What if nothing happened?</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="410">It matters that I start.',
    'fill="#FDD835" x="500" y="350">What if nothing happened?'
))

# ============================================================
# FIX 3 — Day 01 Page 2 — add "It matters that I start" here
# ============================================================
fixes.append((
    'fill="#3E1F00" x="500" y="316">He stretched his wings wide.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#3E1F00" x="500" y="374">The cool morning air filled him right up.',
    'fill="#3E1F00" x="500" y="290">He stretched his wings wide.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#3E1F00" x="500" y="348">The cool morning air filled him right up.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#3E1F00" x="500" y="406">It matters that I start.'
))

# ============================================================
# FIX 4 — Day 02 Page 1 — add connective tissue
# ============================================================
fixes.append((
    'fill="#1B5E20" x="508" y="168">DAY 02</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#1A237E" x="500" y="248">Kev woke before the sun.',
    'fill="#1B5E20" x="508" y="168">DAY 02</text>\n  <text font-family="Patrick Hand, cursive" font-size="22" fill="#4CAF82" x="500" y="210" text-anchor="middle">The warmth in his wing was still there.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#1A237E" x="500" y="268">Kev woke before the sun.'
))

# ============================================================
# FIX 5 — Day 03 Page 1 — add connective tissue
# ============================================================
fixes.append((
    'fill="#FF8F00" x="508" y="168">DAY 03</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#3E2000" x="500" y="242">Every morning in the bush,',
    'fill="#FF8F00" x="508" y="168">DAY 03</text>\n  <text font-family="Patrick Hand, cursive" font-size="22" fill="#FF8F00" x="500" y="210" text-anchor="middle">Two mornings. Two words. The bush was listening.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#3E2000" x="500" y="262">Every morning in the bush,'
))

# ============================================================
# FIX 6 — Day 04 Page 1 — add connective tissue + fix palette
# ============================================================
fixes.append((
    'fill="#388E3C" x="508" y="152">DAY 04</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#1A237E" x="500" y="234">The sky was heavy.',
    'fill="#388E3C" x="508" y="152">DAY 04</text>\n  <text font-family="Patrick Hand, cursive" font-size="22" fill="#FF8F00" x="500" y="196" text-anchor="middle">His voice had woken the whole bush. But today felt different.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#5D4037" x="500" y="254">The sky was heavy.'
))

# ============================================================
# FIX 7 — Day 04 background palette — spring green to hot dry
# ============================================================
fixes.append((
    '<rect width="960" height="540" fill="#E8F5E9"/>',
    '<rect width="960" height="540" fill="#FFF8E1"/>'
))
fixes.append((
    '<rect width="960" height="540" fill="#F1F8E9"/>',
    '<rect width="960" height="540" fill="#FFF3E0"/>'
))

# ============================================================
# FIX 8 — Day 05 Page 1 — add connective tissue
# ============================================================
fixes.append((
    'fill="#90A4AE" x="508" y="158">DAY 05</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#263238" x="500" y="238">It rained. And rained.',
    'fill="#90A4AE" x="508" y="158">DAY 05</text>\n  <text font-family="Patrick Hand, cursive" font-size="22" fill="#90A4AE" x="500" y="200" text-anchor="middle">Even on the hard day, Kev had shown up.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#263238" x="500" y="252">It rained. And rained.'
))

# ============================================================
# FIX 9 — Day 06 Page 1 — add connective tissue
# ============================================================
fixes.append((
    'fill="#1565C0" x="588" y="124">DAY 06</text>\n  <text font-family="Patrick Hand, cursive" font-size="30" fill="#1A237E" x="580" y="192">A tiny flash of blue',
    'fill="#1565C0" x="588" y="124">DAY 06</text>\n  <text font-family="Patrick Hand, cursive" font-size="22" fill="#1565C0" x="580" y="160">He had shown up in the rain. He had shown up on the hard days.</text>\n  <text font-family="Patrick Hand, cursive" font-size="30" fill="#1A237E" x="580" y="210">A tiny flash of blue'
))

# ============================================================
# FIX 10 — Day 06 Page 2 — replace preachy Ollie line
# ============================================================
fixes.append((
    'fill="#1A237E" x="580" y="192">Ollie was small but</text>\n  <text font-family="Patrick Hand, cursive" font-size="30" fill="#1A237E" x="580" y="236">full of sparkle.</text>\n  <text font-family="Patrick Hand, cursive" font-size="30" fill="#1565C0" x="580" y="300">"Kindness starts</text>\n  <text font-family="Patrick Hand, cursive" font-size="30" fill="#1565C0" x="580" y="344">with hello," she said.',
    'fill="#1A237E" x="580" y="192">"I\'ve been watching you," said Ollie.</text>\n  <text font-family="Patrick Hand, cursive" font-size="30" fill="#1A237E" x="580" y="236">"Every morning. You always say something good."</text>\n  <text font-family="Patrick Hand, cursive" font-size="30" fill="#1565C0" x="580" y="300">"Does it help?" she asked.</text>\n  <text font-family="Patrick Hand, cursive" font-size="30" fill="#1A237E" x="580" y="344">Kev thought about it. "I think it does."'
))

# ============================================================
# FIX 11 — Day 07 Page 1 — add connective tissue + rewrite
# ============================================================
fixes.append((
    'fill="#1565C0" x="498" y="124">DAY 07</text>\n  <text font-family="Patrick Hand, cursive" font-size="30" fill="#1A237E" x="490" y="196">Seven days.</text>\n  <text font-family="Patrick Hand, cursive" font-size="30" fill="#1A237E" x="490" y="240">Kev looked at the sky above the creek.</text>\n  <text font-family="Patrick Hand, cursive" font-size="30" fill="#1565C0" x="490" y="308">Maybe that means doing the thing that scares you.',
    'fill="#1565C0" x="498" y="124">DAY 07</text>\n  <text font-family="Patrick Hand, cursive" font-size="22" fill="#1565C0" x="490" y="164">Ollie\'s hello was still warm in his chest.</text>\n  <text font-family="Patrick Hand, cursive" font-size="30" fill="#1A237E" x="490" y="210">Seven mornings. Seven words said out loud.</text>\n  <text font-family="Patrick Hand, cursive" font-size="30" fill="#1A237E" x="490" y="258">Kev looked at the water.</text>\n  <text font-family="Patrick Hand, cursive" font-size="30" fill="#1A237E" x="490" y="306">It was a long way down.</text>\n  <text font-family="Patrick Hand, cursive" font-size="30" fill="#1565C0" x="490" y="362">Maybe finding your voice means using it</text>\n  <text font-family="Patrick Hand, cursive" font-size="30" fill="#1565C0" x="490" y="406">somewhere that scares you.'
))

# ============================================================
# FIX 12 — Day 08 Page 1 — add connective tissue
# ============================================================
fixes.append((
    'fill="#FF8F00" x="590" y="124">DAY 08</text>\n  <text font-family="Patrick Hand, cursive" font-size="30" fill="#1A237E" x="584" y="190">A large shadow fell',
    'fill="#FF8F00" x="590" y="124">DAY 08</text>\n  <text font-family="Patrick Hand, cursive" font-size="22" fill="#FF8F00" x="584" y="160">He had flown. He had actually flown.</text>\n  <text font-family="Patrick Hand, cursive" font-size="30" fill="#1A237E" x="584" y="206">A large shadow fell'
))

# ============================================================
# FIX 13 — Day 09 Page 1 — add connective tissue
# ============================================================
fixes.append((
    'fill="#0097A7" x="480" y="50">DAY 09</text>\n  <text font-family="Patrick Hand, cursive" font-size="36" fill="#1A237E" x="480" y="114">A flash of colour — it was Coco!',
    'fill="#0097A7" x="480" y="50">DAY 09</text>\n  <text font-family="Patrick Hand, cursive" font-size="22" fill="#0097A7" x="480" y="86" text-anchor="middle">Rudie had said: there is no just.</text>\n  <text font-family="Patrick Hand, cursive" font-size="36" fill="#1A237E" x="480" y="128">A flash of colour — it was Coco!'
))

# ============================================================
# FIX 14 — Day 09 Page 2 — add more physical movement text
# ============================================================
fixes.append((
    'fill="#0097A7" x="480" y="114">"MOVE YOUR BODY, KEV!" she sang.</text>\n  <text font-family="Patrick Hand, cursive" font-size="36" fill="#0097A7" x="480" y="170">Kev laughed and stretched wide.',
    'fill="#0097A7" x="480" y="100">"MOVE YOUR BODY, KEV!" she sang.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#1A237E" x="480" y="154" text-anchor="middle">He stretched left. He stretched right.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#1A237E" x="480" y="198" text-anchor="middle">He shook out his tail feathers.</text>\n  <text font-family="Patrick Hand, cursive" font-size="32" fill="#0097A7" x="480" y="242" text-anchor="middle">Moving felt good. Really, really good.'
))

# ============================================================
# FIX 15 — Day 10 Page 1 — add connective tissue
# ============================================================
fixes.append((
    'fill="#8B6914" x="480" y="50">DAY 10</text>\n  <text font-family="Patrick Hand, cursive" font-size="35" fill="#1A237E" x="480" y="112">A wise owl landed softly beside Kev.',
    'fill="#8B6914" x="480" y="50">DAY 10</text>\n  <text font-family="Patrick Hand, cursive" font-size="22" fill="#8B6914" x="480" y="84" text-anchor="middle">Coco\'s laugh was still somewhere in his feathers.</text>\n  <text font-family="Patrick Hand, cursive" font-size="35" fill="#1A237E" x="480" y="128">A wise owl landed softly beside Kev.'
))

# ============================================================
# FIX 16 — Day 10 Page 2 — change what Kev learned
# ============================================================
fixes.append((
    'fill="#1A237E" x="480" y="112" text-anchor="middle">"I learned I am enough," said Kev.</text>\n  <text font-family="Patrick Hand, cursive" font-size="35" fill="#8B6914" x="480" y="168" text-anchor="middle">"Learning never stops," said Fifi.',
    'fill="#1A237E" x="480" y="100" text-anchor="middle">"I learned that showing up is enough,"</text>\n  <text font-family="Patrick Hand, cursive" font-size="35" fill="#1A237E" x="480" y="148" text-anchor="middle">said Kev. "That I don\'t have to be ready.</text>\n  <text font-family="Patrick Hand, cursive" font-size="35" fill="#1A237E" x="480" y="196" text-anchor="middle">I just have to begin."</text>\n  <text font-family="Patrick Hand, cursive" font-size="35" fill="#8B6914" x="480" y="250" text-anchor="middle">Fifi smiled. "Now that," she said, "is everything."'
))

# ============================================================
# FIX 17 — Day 11 Page 1 — add connective tissue + image detail
# ============================================================
fixes.append((
    'fill="#FFF176" x="480" y="50">DAY 11</text>\n  <text font-family="Patrick Hand, cursive" font-size="35" fill="white" x="480" y="112">That evening, Kev sat quietly</text>\n  <text font-family="Patrick Hand, cursive" font-size="35" fill="white" x="480" y="162">and watched the sun go down over the creek.',
    'fill="#FFF176" x="480" y="50">DAY 11</text>\n  <text font-family="Patrick Hand, cursive" font-size="22" fill="#FFF176" x="480" y="84" text-anchor="middle">Fifi had asked: what did you learn?</text>\n  <text font-family="Patrick Hand, cursive" font-size="35" fill="white" x="480" y="128">That evening, Kev sat quietly.</text>\n  <text font-family="Patrick Hand, cursive" font-size="30" fill="white" x="480" y="174" text-anchor="middle">The creek turned orange. Then pink.</text>\n  <text font-family="Patrick Hand, cursive" font-size="30" fill="#FFF176" x="480" y="218" text-anchor="middle">Then deep, deep blue.</text>\n  <text font-family="Patrick Hand, cursive" font-size="30" fill="white" x="480" y="262" text-anchor="middle">And Kev didn\'t move. He just watched.'
))

# ============================================================
# FIX 18 — Day 12 Page 1 — add connective tissue + extra beat
# ============================================================
fixes.append((
    'fill="#B0BEC5" x="480" y="50">DAY 12</text>\n  <text font-family="Patrick Hand, cursive" font-size="35" fill="white" x="480" y="112">The morning was cold and grey.</text>\n  <text font-family="Patrick Hand, cursive" font-size="35" fill="#B0BEC5" x="480" y="168">Do I belong here? he wondered.',
    'fill="#B0BEC5" x="480" y="50">DAY 12</text>\n  <text font-family="Patrick Hand, cursive" font-size="22" fill="#B0BEC5" x="480" y="84" text-anchor="middle">He had watched the sun go down and felt grateful.</text>\n  <text font-family="Patrick Hand, cursive" font-size="35" fill="white" x="480" y="128">The morning was cold and grey.</text>\n  <text font-family="Patrick Hand, cursive" font-size="30" fill="white" x="480" y="178" text-anchor="middle">No warmth. No colour. Just Kev</text>\n  <text font-family="Patrick Hand, cursive" font-size="30" fill="white" x="480" y="222" text-anchor="middle">and the quiet bush.</text>\n  <text font-family="Patrick Hand, cursive" font-size="35" fill="#B0BEC5" x="480" y="278">Do I belong here? he wondered.'
))

# ============================================================
# FIX 19 — Day 13 Page 1 — add connective tissue
# ============================================================
fixes.append((
    'fill="#0097A7" x="480" y="46">DAY 13</text>\n  <text font-family="Patrick Hand, cursive" font-size="35" fill="#1A237E" x="480" y="100">Kev felt something different in the air.',
    'fill="#0097A7" x="480" y="46">DAY 13</text>\n  <text font-family="Patrick Hand, cursive" font-size="22" fill="#0097A7" x="480" y="76" text-anchor="middle">He belonged here. He knew it now.</text>\n  <text font-family="Patrick Hand, cursive" font-size="35" fill="#1A237E" x="480" y="118">Kev felt something different in the air.'
))

# ============================================================
# FIX 20 — Day 13 Page 1+2 — increase character scale
# ============================================================
fixes.append((
    'translate(20, 260) scale(0.53)',
    'translate(0, 230) scale(0.68)'
))

# ============================================================
# FIX 21 — Day 14 Page 1 — replace with lizards/wombats echo
# ============================================================
fixes.append((
    'fill="#4CAF82" x="480" y="54" text-anchor="middle">DAY 14</text>\n  <text font-family="Fredoka One, cursive" font-size="38" fill="#FDD835" x="480" y="128" text-anchor="middle">Fourteen mornings. Every single one.</text>\n  <text font-family="Patrick Hand, cursive" font-size="30" fill="#90CAF9" x="480" y="200" text-anchor="middle">The rain ones. The hard ones. He showed up for all of them.',
    'fill="#4CAF82" x="480" y="54" text-anchor="middle">DAY 14</text>\n  <text font-family="Patrick Hand, cursive" font-size="34" fill="white" x="480" y="120" text-anchor="middle">He woke before the lizards.</text>\n  <text font-family="Patrick Hand, cursive" font-size="34" fill="white" x="480" y="170" text-anchor="middle">Before the wombats.</text>\n  <text font-family="Patrick Hand, cursive" font-size="34" fill="white" x="480" y="220" text-anchor="middle">Before anyone.</text>\n  <text font-family="Patrick Hand, cursive" font-size="30" fill="#FDD835" x="480" y="290" text-anchor="middle">But this morning, he already knew</text>\n  <text font-family="Patrick Hand, cursive" font-size="30" fill="#FDD835" x="480" y="334" text-anchor="middle">what he was going to say.'
))

# ============================================================
# FIX 22 — Wing of Words — increase Kev scale
# ============================================================
fixes.append((
    'translate(380, 180) scale(0.38)',
    'translate(350, 160) scale(0.55)'
))

# ============================================================
# FIX 23 — Certificate — increase Kev scale
# ============================================================
fixes.append((
    'translate(406, 388) scale(0.26)',
    'translate(380, 320) scale(0.48)'
))

# ============================================================
# NEW PAGE 4 — Friends overheard (insert before Day 01 Page 1)
# ============================================================
new_page_4 = '''<div class="slide" data-label="THE LEGEND · PAGE 2 — FRIENDS"><svg class="page" viewBox="0 0 960 540" xmlns="http://www.w3.org/2000/svg">
  <rect width="960" height="540" fill="#0D1B4B"/>
  <rect width="960" height="280" fill="#0A1535" opacity="0.5"/>
  <circle cx="78" cy="40" r="2.5" fill="white" opacity="0.9"/><circle cx="170" cy="26" r="1.8" fill="white" opacity="0.7"/><circle cx="268" cy="50" r="2" fill="white" opacity="0.8"/><circle cx="382" cy="32" r="1.8" fill="white" opacity="0.6"/><circle cx="494" cy="44" r="2.5" fill="white" opacity="0.7"/><circle cx="608" cy="24" r="1.8" fill="white" opacity="0.8"/><circle cx="706" cy="54" r="2" fill="white" opacity="0.6"/><circle cx="806" cy="36" r="2.5" fill="white" opacity="0.9"/><circle cx="904" cy="48" r="1.8" fill="white" opacity="0.7"/>
  <circle cx="848" cy="102" r="54" fill="#FFF9C4" opacity="0.95"/><circle cx="874" cy="86" r="46" fill="#0D1B4B"/>
  <path d="M0 372 Q114 330 228 348 Q342 314 480 334 Q618 314 744 330 Q846 314 960 328 L960 540 L0 540 Z" fill="#111D40"/>
  <rect x="678" y="242" width="14" height="178" rx="6" fill="#0A1232"/><ellipse cx="685" cy="236" rx="40" ry="54" fill="#0A1232"/>
  <rect x="26" y="256" width="13" height="168" rx="5" fill="#0A1232"/><ellipse cx="33" cy="250" rx="32" ry="44" fill="#0A1232"/>
  <path d="M0 398 Q226 380 452 390 Q678 380 960 390" stroke="#1A2860" stroke-width="22" fill="none" stroke-linecap="round"/>
  <path d="M0 398 Q226 380 452 390 Q678 380 960 390" stroke="#243070" stroke-width="14" fill="none" stroke-linecap="round"/>
  <rect x="0" y="520" width="960" height="20" fill="#090F28"/>
  <!-- Branch in mid distance -->
  <rect x="280" y="295" width="340" height="12" rx="5" fill="#2C1A0E"/>
  <!-- Four bird silhouettes on branch — unnamed, distinctive shapes -->
  <!-- Tiny round bird — Ollie (electric blue) -->
  <ellipse cx="310" cy="276" rx="14" ry="12" fill="#1565C0"/>
  <circle cx="310" cy="262" r="10" fill="#1565C0"/>
  <!-- Large spread-wing bird — Rudie (dark) -->
  <ellipse cx="380" cy="272" rx="22" ry="16" fill="#2C1A0E"/>
  <circle cx="380" cy="254" r="14" fill="#2C1A0E"/>
  <path d="M358 268 Q340 258 328 248" stroke="#2C1A0E" stroke-width="6" stroke-linecap="round" fill="none"/>
  <path d="M402 268 Q420 258 432 248" stroke="#2C1A0E" stroke-width="6" stroke-linecap="round" fill="none"/>
  <!-- Fan-tailed bird — Coco (teal) -->
  <ellipse cx="460" cy="274" rx="18" ry="14" fill="#0097A7"/>
  <circle cx="460" cy="258" r="12" fill="#0097A7"/>
  <path d="M442 282 Q430 296 422 308" stroke="#0097A7" stroke-width="5" stroke-linecap="round" fill="none"/>
  <path d="M450 284 Q444 300 440 314" stroke="#0097A7" stroke-width="4" stroke-linecap="round" fill="none"/>
  <path d="M460 285 Q460 302 460 316" stroke="#0097A7" stroke-width="4" stroke-linecap="round" fill="none"/>
  <!-- Round-headed upright bird — Fifi (amber) -->
  <ellipse cx="530" cy="278" rx="14" ry="12" fill="#8B6914"/>
  <circle cx="530" cy="260" r="16" fill="#8B6914"/>
  <!-- Speech bubbles — fragments, overlapping -->
  <rect x="290" y="220" width="180" height="32" rx="14" fill="white" opacity="0.08"/>
  <rect x="290" y="220" width="180" height="32" rx="14" fill="none" stroke="white" stroke-width="1" opacity="0.3"/>
  <text font-family="Patrick Hand, cursive" font-size="18" fill="white" opacity="0.8" x="380" y="241" text-anchor="middle">"…they say if you truly believe…"</text>
  <rect x="370" y="188" width="140" height="28" rx="12" fill="white" opacity="0.06"/>
  <rect x="370" y="188" width="140" height="28" rx="12" fill="none" stroke="#FDD835" stroke-width="1" opacity="0.25"/>
  <text font-family="Patrick Hand, cursive" font-size="17" fill="#FDD835" opacity="0.7" x="440" y="207" text-anchor="middle">"…one feather…"</text>
  <rect x="440" y="156" width="160" height="28" rx="12" fill="white" opacity="0.06"/>
  <rect x="440" y="156" width="160" height="28" rx="12" fill="none" stroke="#FDD835" stroke-width="1" opacity="0.25"/>
  <text font-family="Patrick Hand, cursive" font-size="17" fill="#FDD835" opacity="0.8" x="520" y="175" text-anchor="middle">"…turns gold…?"</text>
  <!-- Kev — higher branch, hidden behind gum leaf, listening -->
  <!-- Gum leaf obscuring Kev -->
  <ellipse cx="158" cy="198" rx="52" ry="32" fill="#0A1232" transform="rotate(-20 158 198)"/>
  <!-- Kev peeking — just head and one eye visible -->
  <circle cx="172" cy="210" r="20" fill="#FDECC8" opacity="0.9"/>
  <path d="M152 198 Q164 188 178 194 Q182 202 176 208 Q164 206 152 198Z" fill="#5C3A1E"/>
  <circle cx="176" cy="208" r="8" fill="white"/><circle cx="178" cy="208" r="5" fill="#1A1A2E"/><circle cx="180" cy="206" r="2" fill="white"/>
  <!-- Higher branch Kev is on -->
  <rect x="80" y="218" width="120" height="8" rx="3" fill="#3D2208" opacity="0.7"/>
  <!-- Kev's thought — bottom left, small, private -->
  <text font-family="Patrick Hand, cursive" font-size="24" fill="white" opacity="0.6" x="56" y="380">He had never quite believed</text>
  <text font-family="Patrick Hand, cursive" font-size="24" fill="white" opacity="0.6" x="56" y="414">it could happen to him.</text>
  <text font-family="Patrick Hand, cursive" font-size="24" fill="#FDD835" opacity="0.8" x="56" y="460">...could it?</text>
</svg></div>'''

# ============================================================
# NEW PAGE 5A — Kev examines his wing
# ============================================================
new_page_5a = '''<div class="slide" data-label="THE LEGEND · PAGE 3 — THE LOOKING"><svg class="page" viewBox="0 0 960 540" xmlns="http://www.w3.org/2000/svg">
  <rect width="960" height="540" fill="#FF8F00"/>
  <rect width="960" height="540" fill="#FFB300" opacity="0.3"/>
  <rect x="0" y="0" width="960" height="160" fill="#E65100" opacity="0.2"/>
  <circle cx="480" cy="320" r="110" fill="#FFF176" opacity="0.9"/><circle cx="480" cy="320" r="86" fill="#FFEE58"/>
  <path d="M0 402 Q114 350 228 370 Q342 336 480 356 Q618 336 756 352 Q858 336 960 348 L960 540 L0 540 Z" fill="#2E7D32"/>
  <path d="M0 432 Q128 392 256 410 Q396 380 540 398 L960 390 L960 540 L0 540 Z" fill="#388E3C"/>
  <rect x="694" y="266" width="16" height="198" rx="6" fill="#1B5E20"/><ellipse cx="702" cy="259" rx="42" ry="58" fill="#1B5E20"/>
  <rect x="68" y="276" width="20" height="234" rx="7" fill="#1B5E20"/><ellipse cx="78" cy="268" rx="48" ry="66" fill="#2E7D32"/>
  <path d="M0 398 Q226 380 452 390 Q678 380 960 390" stroke="#4E342E" stroke-width="22" fill="none" stroke-linecap="round"/>
  <path d="M0 398 Q226 380 452 390 Q678 380 960 390" stroke="#5D4037" stroke-width="14" fill="none" stroke-linecap="round"/>
  <!-- Kev examining wing — right side, looking down at extended wing -->
  <g transform="translate(500, 148) scale(0.68)">
    <path d="M228 294 Q202 322 194 360" stroke="#8B5E3C" stroke-width="7" fill="none" stroke-linecap="round"/>
    <ellipse cx="318" cy="298" rx="72" ry="62" fill="#8B5E3C"/>
    <ellipse cx="318" cy="310" rx="50" ry="42" fill="#FDECC8"/>
    <path d="M258 280 Q236 256 248 220 Q268 254 270 284 Z" fill="#5C3A1E"/>
    <circle cx="318" cy="195" r="82" fill="#FDECC8"/>
    <path d="M246 178 Q262 108 318 96 Q374 108 390 178 Q364 146 318 142 Q272 146 246 178Z" fill="#5C3A1E"/>
    <path d="M294 124 Q280 74 290 48 Q304 76 302 126Z" fill="#5C3A1E"/>
    <path d="M314 118 Q308 58 318 30 Q330 60 326 120Z" fill="#8B5E3C"/>
    <path d="M334 120 Q332 60 340 32 Q350 62 346 122Z" fill="#5C3A1E"/>
    <circle cx="360" cy="186" r="22" fill="white"/><circle cx="360" cy="194" r="14" fill="#1A1A2E"/><circle cx="366" cy="194" r="6" fill="white"/>
    <path d="M344 168 Q360 162 374 170" stroke="#5C3A1E" stroke-width="5" fill="none" stroke-linecap="round"/>
    <path d="M392 202 L452 194 L392 216 Z" fill="#E07B2A"/>
    <path d="M268 310 Q230 330 190 346 Q210 320 250 298 Q268 290 278 296 Z" fill="#8B5E3C"/>
    <line x1="296" y1="354" x2="288" y2="374" stroke="#E07B2A" stroke-width="5" stroke-linecap="round"/>
    <line x1="288" y1="374" x2="274" y2="381" stroke="#E07B2A" stroke-width="4" stroke-linecap="round"/>
    <line x1="288" y1="374" x2="284" y2="390" stroke="#E07B2A" stroke-width="4" stroke-linecap="round"/>
    <line x1="288" y1="374" x2="300" y2="381" stroke="#E07B2A" stroke-width="4" stroke-linecap="round"/>
    <line x1="340" y1="356" x2="348" y2="374" stroke="#E07B2A" stroke-width="5" stroke-linecap="round"/>
    <line x1="348" y1="374" x2="336" y2="381" stroke="#E07B2A" stroke-width="4" stroke-linecap="round"/>
    <line x1="348" y1="374" x2="344" y2="390" stroke="#E07B2A" stroke-width="4" stroke-linecap="round"/>
    <line x1="348" y1="374" x2="360" y2="381" stroke="#E07B2A" stroke-width="4" stroke-linecap="round"/>
  </g>
  <text font-family="Fredoka One, cursive" font-size="52" fill="#3E1F00" x="56" y="180">Brown and cream.</text>
  <text font-family="Fredoka One, cursive" font-size="64" fill="#3E1F00" x="56" y="270">Ordinary.</text>
  <text font-family="Patrick Hand, cursive" font-size="36" fill="#5D4037" x="56" y="360">...wasn\'t it?</text>
</svg></div>'''

# ============================================================
# NEW PAGE 5B — The Decision
# ============================================================
new_page_5b = '''<div class="slide" data-label="THE LEGEND · PAGE 4 — THE DECISION"><svg class="page" viewBox="0 0 960 540" xmlns="http://www.w3.org/2000/svg">
  <rect width="960" height="540" fill="#FF8F00"/>
  <rect width="960" height="540" fill="#FFB300" opacity="0.2"/>
  <circle cx="480" cy="290" r="130" fill="#FFF176" opacity="0.95"/><circle cx="480" cy="290" r="100" fill="#FFEE58"/>
  <path d="M0 402 Q114 350 228 370 Q342 336 480 356 Q618 336 756 352 Q858 336 960 348 L960 540 L0 540 Z" fill="#2E7D32"/>
  <path d="M0 432 Q128 392 256 410 Q396 380 540 398 L960 390 L960 540 L0 540 Z" fill="#388E3C"/>
  <path d="M0 398 Q226 380 452 390 Q678 380 960 390" stroke="#4E342E" stroke-width="22" fill="none" stroke-linecap="round"/>
  <path d="M0 398 Q226 380 452 390 Q678 380 960 390" stroke="#5D4037" stroke-width="14" fill="none" stroke-linecap="round"/>
  <!-- Kev standing tall — forward facing, wings slightly open, beak open -->
  <g transform="translate(528, 170) scale(0.62)">
    <path d="M260 292 Q210 250 178 208 Q232 244 268 282 Z" fill="#5C3A1E"/>
    <path d="M264 286 Q220 252 206 218 Q248 246 270 278 Z" fill="#8B5E3C"/>
    <path d="M376 292 Q426 250 458 208 Q404 244 368 282 Z" fill="#5C3A1E"/>
    <path d="M372 286 Q416 252 430 218 Q388 246 366 278 Z" fill="#8B5E3C"/>
    <ellipse cx="318" cy="306" rx="72" ry="58" fill="#8B5E3C"/>
    <ellipse cx="318" cy="318" rx="48" ry="38" fill="#FDECC8"/>
    <circle cx="318" cy="204" r="80" fill="#FDECC8"/>
    <path d="M246 188 Q262 120 318 108 Q374 120 390 188 Q364 156 318 152 Q272 156 246 188Z" fill="#5C3A1E"/>
    <path d="M290 134 Q276 84 286 58 Q300 86 298 136Z" fill="#5C3A1E"/>
    <path d="M310 128 Q304 66 314 38 Q326 68 322 130Z" fill="#8B5E3C"/>
    <path d="M330 130 Q328 60 336 34 Q346 64 342 132Z" fill="#5C3A1E"/>
    <circle cx="284" cy="192" r="22" fill="white"/><circle cx="286" cy="190" r="14" fill="#1A1A2E"/><circle cx="292" cy="184" r="6" fill="white"/>
    <circle cx="352" cy="190" r="22" fill="white"/><circle cx="354" cy="188" r="14" fill="#1A1A2E"/><circle cx="360" cy="182" r="6" fill="white"/>
    <path d="M318 208 L318 208 L368 220 L318 232 Z" fill="#E07B2A"/>
    <line x1="296" y1="358" x2="288" y2="375" stroke="#E07B2A" stroke-width="5" stroke-linecap="round"/>
    <line x1="340" y1="358" x2="348" y2="375" stroke="#E07B2A" stroke-width="5" stroke-linecap="round"/>
  </g>
  <text font-family="Patrick Hand, cursive" font-size="36" fill="#3E1F00" x="56" y="180">"What if,"</text>
  <text font-family="Patrick Hand, cursive" font-size="36" fill="#3E1F00" x="56" y="230">thought Kev,</text>
  <text font-family="Patrick Hand, cursive" font-size="36" fill="#3E1F00" x="56" y="290">"it could happen</text>
  <text font-family="Patrick Hand, cursive" font-size="36" fill="#3E1F00" x="56" y="340">to me?"</text>
  <text font-family="Patrick Hand, cursive" font-size="28" fill="#5D4037" x="56" y="400">Just fourteen mornings.</text>
  <text font-family="Patrick Hand, cursive" font-size="28" fill="#5D4037" x="56" y="440">Just one word.</text>
  <text font-family="Patrick Hand, cursive" font-size="28" fill="#E65100" x="56" y="490">What would happen?</text>
</svg></div>'''

# ============================================================
# NEW THRESHOLD PAGE — bridge to Day 1
# ============================================================
new_threshold = '''<div class="slide" data-label="THE LEGEND · PAGE 5 — AND SO"><svg class="page" viewBox="0 0 960 540" xmlns="http://www.w3.org/2000/svg">
  <rect width="960" height="540" fill="#0D1B4B"/>
  <rect width="960" height="280" fill="#0A1535" opacity="0.5"/>
  <circle cx="78" cy="40" r="2.5" fill="white" opacity="0.9"/><circle cx="170" cy="26" r="1.8" fill="white" opacity="0.7"/><circle cx="268" cy="50" r="2" fill="white" opacity="0.8"/><circle cx="382" cy="32" r="1.8" fill="white" opacity="0.6"/><circle cx="494" cy="44" r="2.5" fill="white" opacity="0.7"/><circle cx="608" cy="24" r="1.8" fill="white" opacity="0.8"/>
  <circle cx="848" cy="102" r="54" fill="#FFF9C4" opacity="0.95"/><circle cx="874" cy="86" r="46" fill="#0D1B4B"/>
  <rect x="0" y="310" width="960" height="60" fill="#FF8F00" opacity="0.08"/>
  <path d="M0 372 Q114 330 228 348 Q342 314 480 334 Q618 314 744 330 Q846 314 960 328 L960 540 L0 540 Z" fill="#111D40"/>
  <rect x="678" y="242" width="14" height="178" rx="6" fill="#0A1232"/><ellipse cx="685" cy="236" rx="40" ry="54" fill="#0A1232"/>
  <rect x="26" y="256" width="13" height="168" rx="5" fill="#0A1232"/><ellipse cx="33" cy="250" rx="32" ry="44" fill="#0A1232"/>
  <path d="M0 398 Q226 380 452 390 Q678 380 960 390" stroke="#1A2860" stroke-width="22" fill="none" stroke-linecap="round"/>
  <path d="M0 398 Q226 380 452 390 Q678 380 960 390" stroke="#243070" stroke-width="14" fill="none" stroke-linecap="round"/>
  <rect x="0" y="520" width="960" height="20" fill="#090F28"/>
  <!-- Small Kev on branch, looking forward, beak open — about to begin -->
  <g transform="translate(54, 198) scale(0.58)">
    <path d="M228 294 Q202 322 194 360" stroke="#8B5E3C" stroke-width="7" fill="none" stroke-linecap="round"/>
    <ellipse cx="318" cy="298" rx="72" ry="62" fill="#8B5E3C"/>
    <ellipse cx="318" cy="310" rx="50" ry="42" fill="#FDECC8"/>
    <path d="M258 280 Q236 256 248 220 Q268 254 270 284 Z" fill="#5C3A1E"/>
    <circle cx="318" cy="195" r="82" fill="#FDECC8"/>
    <path d="M246 178 Q262 108 318 96 Q374 108 390 178 Q364 146 318 142 Q272 146 246 178Z" fill="#5C3A1E"/>
    <path d="M294 124 Q280 74 290 48 Q304 76 302 126Z" fill="#5C3A1E"/>
    <path d="M314 118 Q308 58 318 30 Q330 60 326 120Z" fill="#8B5E3C"/>
    <path d="M334 120 Q332 60 340 32 Q350 62 346 122Z" fill="#5C3A1E"/>
    <circle cx="360" cy="186" r="22" fill="white"/><circle cx="362" cy="182" r="14" fill="#1A1A2E"/><circle cx="368" cy="176" r="6" fill="white"/>
    <path d="M392 202 L452 194 L392 216 Z" fill="#E07B2A"/>
    <line x1="296" y1="354" x2="288" y2="374" stroke="#E07B2A" stroke-width="5" stroke-linecap="round"/>
    <line x1="288" y1="374" x2="274" y2="381" stroke="#E07B2A" stroke-width="4" stroke-linecap="round"/>
    <line x1="340" y1="356" x2="348" y2="374" stroke="#E07B2A" stroke-width="5" stroke-linecap="round"/>
    <line x1="348" y1="374" x2="360" y2="381" stroke="#E07B2A" stroke-width="4" stroke-linecap="round"/>
  </g>
  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="180">And so, the very next morning —</text>
  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="240">before the lizards,</text>
  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="300">before the wombats,</text>
  <text font-family="Patrick Hand, cursive" font-size="32" fill="#FDD835" x="500" y="360">before anyone —</text>
  <text font-family="Fredoka One, cursive" font-size="42" fill="#FDD835" x="500" y="440">Kev opened his beak.</text>
</svg></div>'''

# ============================================================
# ADD UMBRELLA to Day 18 and 19 (rain pages)
# ============================================================
# Add umbrella SVG group after the Kev character group on Day 05 pages
umbrella = '''
  <!-- Umbrella -->
  <g transform="translate(142, 248)">
    <line x1="0" y1="0" x2="0" y2="60" stroke="#C62828" stroke-width="4" stroke-linecap="round"/>
    <line x1="0" y1="60" x2="10" y2="72" stroke="#C62828" stroke-width="3" stroke-linecap="round"/>
    <path d="M-38 0 Q-20 -30 0 -32 Q20 -30 38 0 Z" fill="#E53935"/>
    <path d="M-38 0 Q-20 -30 0 -32 Q20 -30 38 0" fill="none" stroke="#C62828" stroke-width="2"/>
    <line x1="-26" y1="-2" x2="-20" y2="-24" stroke="#C62828" stroke-width="1.5" opacity="0.5"/>
    <line x1="0" y1="-2" x2="0" y2="-32" stroke="#C62828" stroke-width="1.5" opacity="0.5"/>
    <line x1="26" y1="-2" x2="20" y2="-24" stroke="#C62828" stroke-width="1.5" opacity="0.5"/>
  </g>
  <!-- Rain drops around Kev -->
  <line x1="200" y1="300" x2="196" y2="320" stroke="#90CAF9" stroke-width="1.5" opacity="0.6" stroke-linecap="round"/>
  <line x1="240" y1="280" x2="236" y2="300" stroke="#90CAF9" stroke-width="1.5" opacity="0.5" stroke-linecap="round"/>
  <line x1="170" y1="320" x2="166" y2="340" stroke="#90CAF9" stroke-width="1.5" opacity="0.4" stroke-linecap="round"/>'''

# Find Day 05 Page 1 Kev group end and insert umbrella
day05_p1_kev_end = 'translate(54, 220) scale(0.76)'
idx_d5 = html.find('data-label="DAY 05 · PAGE 1"')
if idx_d5 > -1:
    kev_end = html.find('</g>', html.find(day05_p1_kev_end, idx_d5))
    if kev_end > -1:
        html = html[:kev_end+4] + umbrella + html[kev_end+4:]
        print('✅ Umbrella added to Day 05 Page 1')

# ============================================================
# INJECT NEW PAGES before DAY 01 · PAGE 1
# ============================================================
inject_marker = '<!-- PAGE: THE LEGEND · PAGE 1 -->'
new_pages_block = f'''<!-- PAGE: FRIENDS OVERHEARD -->
        {new_page_4}

        <!-- PAGE: THE LOOKING -->
        {new_page_5a}

        <!-- PAGE: THE DECISION -->
        {new_page_5b}

        <!-- PAGE: THRESHOLD -->
        {new_threshold}

        {inject_marker}'''

if inject_marker in html:
    html = html.replace(inject_marker, new_pages_block, 1)
    print('✅ 4 new opening pages injected')
else:
    print('⚠️ Inject marker not found')

# ============================================================
# UPDATE TOTAL — add 4 new pages
# ============================================================
import re
current_total = re.search(r'TOTAL = (\d+)', html)
if current_total:
    old_total = int(current_total.group(1))
    new_total = old_total + 4
    html = html.replace(f'TOTAL = {old_total}', f'TOTAL = {new_total}')
    print(f'✅ TOTAL updated from {old_total} to {new_total}')

# ============================================================
# APPLY ALL TEXT FIXES
# ============================================================
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

# ============================================================
# WRITE OUTPUT
# ============================================================
with open('book1-golden-feather.html', 'w') as f:
    f.write(html)

print(f'\n========================================')
print(f'✅ {count_ok} text fixes applied')
print(f'⚠️  {count_miss} not found')
print(f'✅ New pages injected')
print(f'Size: {len(html):,} bytes')
print(f'========================================')
