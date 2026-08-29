with open('book1-golden-feather.html', 'r') as f:
    html = f.read()

# ============================================================
# THE 3 NEW OPENING PAGES — SVG content
# ============================================================

opening_page1 = '''<div class="slide" data-label="THE LEGEND · PAGE 1"><svg class="page" viewBox="0 0 960 540" xmlns="http://www.w3.org/2000/svg">
  <rect width="960" height="540" fill="#0D1B4B"/>
  <rect width="960" height="280" fill="#0A1535" opacity="0.5"/>
  <circle cx="78" cy="40" r="2.5" fill="white" opacity="0.9"/><circle cx="170" cy="26" r="1.8" fill="white" opacity="0.7"/><circle cx="268" cy="50" r="2" fill="white" opacity="0.8"/><circle cx="382" cy="32" r="1.8" fill="white" opacity="0.6"/><circle cx="494" cy="44" r="2.5" fill="white" opacity="0.7"/><circle cx="608" cy="24" r="1.8" fill="white" opacity="0.8"/><circle cx="706" cy="54" r="2" fill="white" opacity="0.6"/><circle cx="806" cy="36" r="2.5" fill="white" opacity="0.9"/><circle cx="904" cy="48" r="1.8" fill="white" opacity="0.7"/><circle cx="114" cy="76" r="1.4" fill="white" opacity="0.5"/><circle cx="220" cy="86" r="1.2" fill="white" opacity="0.6"/><circle cx="330" cy="68" r="1.4" fill="white" opacity="0.7"/><circle cx="430" cy="20" r="1.2" fill="white" opacity="0.8"/>
  <circle cx="848" cy="102" r="54" fill="#FFF9C4" opacity="0.95"/><circle cx="874" cy="86" r="46" fill="#0D1B4B"/>
  <path d="M0 372 Q114 330 228 348 Q342 314 480 334 Q618 314 744 330 Q846 314 960 328 L960 540 L0 540 Z" fill="#111D40"/>
  <rect x="678" y="242" width="14" height="178" rx="6" fill="#0A1232"/><ellipse cx="685" cy="236" rx="40" ry="54" fill="#0A1232"/><ellipse cx="662" cy="252" rx="26" ry="38" fill="#0A1232"/>
  <rect x="876" y="232" width="14" height="192" rx="6" fill="#0A1232"/><ellipse cx="883" cy="226" rx="42" ry="56" fill="#0A1232"/>
  <rect x="26" y="256" width="13" height="168" rx="5" fill="#0A1232"/><ellipse cx="33" cy="250" rx="32" ry="44" fill="#0A1232"/>
  <path d="M0 398 Q226 380 452 390 Q678 380 960 390" stroke="#1A2860" stroke-width="22" fill="none" stroke-linecap="round"/>
  <path d="M0 398 Q226 380 452 390 Q678 380 960 390" stroke="#243070" stroke-width="14" fill="none" stroke-linecap="round"/>
  <rect x="0" y="520" width="960" height="20" fill="#090F28"/>
  <text font-family="Fredoka One, cursive" font-size="14" fill="#4CAF82" letter-spacing="3" x="508" y="60">BILLABONG CREEK</text>
  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="140">Deep in the Australian bush,</text>
  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="188">at a place called Billabong Creek,</text>
  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="252">there lived a kookaburra</text>
  <text font-family="Patrick Hand, cursive" font-size="32" fill="#FDD835" x="500" y="300">named Kev.</text>
  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="364">Every morning, Kev would wake at dawn —</text>
  <text font-family="Patrick Hand, cursive" font-size="32" fill="white" x="500" y="412">before the lizards,</text>
  <text font-family="Patrick Hand, cursive" font-size="32" fill="#FDD835" x="500" y="460">before anyone.</text>
  <g transform="translate(54, 198) scale(0.79)">
    <ellipse cx="118" cy="182" rx="76" ry="58" fill="#8B5E3C"/><ellipse cx="130" cy="196" rx="52" ry="40" fill="#FDECC8"/>
    <path d="M72 172 Q56 150 70 128 Q86 150 84 176 Z" fill="#5C3A1E"/>
    <circle cx="118" cy="108" r="78" fill="#FDECC8"/>
    <path d="M50 92 Q64 28 118 16 Q172 28 186 92 Q162 62 118 58 Q74 62 50 92Z" fill="#5C3A1E"/>
    <path d="M90 34 Q84 -10 90 -32 Q102 -8 98 36Z" fill="#5C3A1E"/><path d="M110 28 Q106 -18 114 -42 Q126 -16 120 30Z" fill="#8B5E3C"/><path d="M130 30 Q128 -16 138 -40 Q148 -14 140 32Z" fill="#5C3A1E"/>
    <circle cx="154" cy="100" r="22" fill="white"/><circle cx="156" cy="98" r="14" fill="#1A1A2E"/><circle cx="162" cy="92" r="6" fill="white"/>
    <path d="M178 108 L228 103 L180 120 Z" fill="#E07B2A"/>
    <line x1="98" y1="236" x2="90" y2="254" stroke="#E07B2A" stroke-width="5" stroke-linecap="round"/><line x1="90" y1="254" x2="76" y2="262" stroke="#E07B2A" stroke-width="4" stroke-linecap="round"/><line x1="90" y1="254" x2="86" y2="270" stroke="#E07B2A" stroke-width="4" stroke-linecap="round"/><line x1="90" y1="254" x2="102" y2="262" stroke="#E07B2A" stroke-width="4" stroke-linecap="round"/>
    <line x1="138" y1="238" x2="146" y2="254" stroke="#E07B2A" stroke-width="5" stroke-linecap="round"/><line x1="146" y1="254" x2="134" y2="262" stroke="#E07B2A" stroke-width="4" stroke-linecap="round"/><line x1="146" y1="254" x2="144" y2="270" stroke="#E07B2A" stroke-width="4" stroke-linecap="round"/><line x1="146" y1="254" x2="158" y2="262" stroke="#E07B2A" stroke-width="4" stroke-linecap="round"/>
  </g>
</svg></div>'''

opening_page2 = '''<div class="slide" data-label="THE LEGEND · PAGE 2"><svg class="page" viewBox="0 0 960 540" xmlns="http://www.w3.org/2000/svg">
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
  <rect x="460" y="100" width="460" height="300" rx="20" fill="white" opacity="0.04"/>
  <rect x="460" y="100" width="460" height="300" rx="20" fill="none" stroke="#FDD835" stroke-width="1.5" opacity="0.3"/>
  <text font-family="Fredoka One, cursive" font-size="16" fill="#FDD835" letter-spacing="2" x="690" y="140" text-anchor="middle">THE LEGEND</text>
  <text font-family="Patrick Hand, cursive" font-size="26" fill="white" x="690" y="188" text-anchor="middle">The elders of the bush whispered:</text>
  <text font-family="Patrick Hand, cursive" font-size="28" fill="#FDD835" x="690" y="234" text-anchor="middle">"If a kookaburra truly</text>
  <text font-family="Patrick Hand, cursive" font-size="28" fill="#FDD835" x="690" y="272" text-anchor="middle">finds their voice —</text>
  <text font-family="Patrick Hand, cursive" font-size="28" fill="white" x="690" y="310" text-anchor="middle">really believes in it —</text>
  <text font-family="Patrick Hand, cursive" font-size="28" fill="#FDD835" x="690" y="356" text-anchor="middle">one of their feathers</text>
  <text font-family="Fredoka One, cursive" font-size="36" fill="#FDD835" x="690" y="400" text-anchor="middle">turns gold."</text>
  <text font-family="Patrick Hand, cursive" font-size="26" fill="white" opacity="0.7" x="56" y="200">Kev had heard</text>
  <text font-family="Patrick Hand, cursive" font-size="26" fill="white" opacity="0.7" x="56" y="240">the legend</text>
  <text font-family="Patrick Hand, cursive" font-size="26" fill="white" opacity="0.7" x="56" y="280">his whole life.</text>
  <text font-family="Patrick Hand, cursive" font-size="26" fill="white" opacity="0.7" x="56" y="340">He had never quite</text>
  <text font-family="Patrick Hand, cursive" font-size="26" fill="white" opacity="0.7" x="56" y="380">believed it could</text>
  <text font-family="Patrick Hand, cursive" font-size="26" fill="#FDD835" x="56" y="420">happen to him.</text>
  <line x1="32" y1="128" x2="32" y2="440" stroke="#FDD835" stroke-width="2" opacity="0.15" stroke-linecap="round"/>
  <circle cx="32" cy="128" r="5" fill="#FDD835" opacity="0.4"/>
  <circle cx="32" cy="440" r="5" fill="#FDD835" opacity="0.4"/>
</svg></div>'''

opening_page3 = '''<div class="slide" data-label="THE LEGEND · PAGE 3"><svg class="page" viewBox="0 0 960 540" xmlns="http://www.w3.org/2000/svg">
  <rect width="960" height="540" fill="#FF8F00"/>
  <rect width="960" height="540" fill="#FFB300" opacity="0.4"/>
  <rect x="0" y="0" width="960" height="170" fill="#E65100" opacity="0.25"/>
  <circle cx="480" cy="340" r="110" fill="#FFF176" opacity="0.95"/><circle cx="480" cy="340" r="86" fill="#FFEE58"/>
  <path d="M0 402 Q114 350 228 370 Q342 336 480 356 Q618 336 756 352 Q858 336 960 348 L960 540 L0 540 Z" fill="#2E7D32"/>
  <path d="M0 432 Q128 392 256 410 Q396 380 540 398 L960 390 L960 540 L0 540 Z" fill="#388E3C"/>
  <path d="M0 468 Q170 448 340 458 Q510 442 680 452 L960 450 L960 540 L0 540 Z" fill="#43A047"/>
  <rect x="694" y="266" width="16" height="198" rx="6" fill="#1B5E20"/><ellipse cx="702" cy="259" rx="42" ry="58" fill="#1B5E20"/>
  <rect x="890" y="258" width="14" height="204" rx="5" fill="#1B5E20"/><ellipse cx="897" cy="252" rx="38" ry="52" fill="#1B5E20"/>
  <rect x="68" y="276" width="20" height="234" rx="7" fill="#1B5E20"/><ellipse cx="78" cy="268" rx="48" ry="66" fill="#2E7D32"/>
  <path d="M0 398 Q226 380 452 390 Q678 380 960 390" stroke="#4E342E" stroke-width="22" fill="none" stroke-linecap="round"/>
  <path d="M0 398 Q226 380 452 390 Q678 380 960 390" stroke="#5D4037" stroke-width="14" fill="none" stroke-linecap="round"/>
  <text font-family="Patrick Hand, cursive" font-size="32" fill="#3E1F00" x="56" y="120">One morning, Kev looked</text>
  <text font-family="Patrick Hand, cursive" font-size="32" fill="#3E1F00" x="56" y="164">at his wings.</text>
  <text font-family="Patrick Hand, cursive" font-size="32" fill="#3E1F00" x="56" y="228">Brown and cream.</text>
  <text font-family="Fredoka One, cursive" font-size="36" fill="#3E1F00" x="56" y="280">Ordinary.</text>
  <text font-family="Patrick Hand, cursive" font-size="32" fill="#3E1F00" x="56" y="344">"What if I tried?"</text>
  <text font-family="Fredoka One, cursive" font-size="30" fill="#E65100" x="56" y="392">"Today is Day One.</text>
  <text font-family="Fredoka One, cursive" font-size="30" fill="#E65100" x="56" y="434">And I have something</text>
  <text font-family="Fredoka One, cursive" font-size="30" fill="#E65100" x="56" y="476">to say."</text>
  <g transform="translate(500, 158) scale(0.62)">
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
</svg></div>'''

# ============================================================
# CLOSING PAGES
# ============================================================

closing_kev_speaks = '''<div class="slide" data-label="CLOSING · KEV SPEAKS"><svg class="page" viewBox="0 0 960 540" xmlns="http://www.w3.org/2000/svg">
  <rect width="960" height="540" fill="#1A237E"/>
  <circle cx="480" cy="282" r="396" fill="none" stroke="#1565C0" stroke-width="2" opacity="0.5"/>
  <circle cx="480" cy="282" r="310" fill="none" stroke="#1565C0" stroke-width="2" opacity="0.5"/>
  <circle cx="480" cy="282" r="226" fill="none" stroke="#1565C0" stroke-width="2" opacity="0.4"/>
  <circle cx="480" cy="282" r="142" fill="none" stroke="#1565C0" stroke-width="2" opacity="0.4"/>
  <path d="M0 0 L98 0 L0 98 Z" fill="#FDD835" opacity="0.1"/><path d="M960 0 L862 0 L960 98 Z" fill="#FDD835" opacity="0.1"/>
  <path d="M0 540 L98 540 L0 442 Z" fill="#4CAF82" opacity="0.1"/><path d="M960 540 L862 540 L960 442 Z" fill="#4CAF82" opacity="0.1"/>
  <path d="M84 84 L88 70 L92 84 L106 88 L92 92 L88 106 L84 92 L70 88 Z" fill="#FDD835" opacity="0.8"/>
  <circle cx="170" cy="226" r="7" fill="#F06292" opacity="0.6"/><circle cx="790" cy="212" r="6" fill="#4CAF82" opacity="0.6"/>
  <g transform="translate(528, 210) scale(0.60)">
    <path d="M260 292 Q192 224 154 164 Q222 214 268 282 Z" fill="#5C3A1E"/>
    <path d="M264 286 Q212 232 192 188 Q248 226 270 278 Z" fill="#8B5E3C"/>
    <path d="M376 292 Q444 224 482 164 Q414 214 368 282 Z" fill="#5C3A1E"/>
    <path d="M372 286 Q424 232 444 188 Q388 226 366 278 Z" fill="#8B5E3C"/>
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
  <text font-family="Patrick Hand, cursive" font-size="28" fill="white" x="56" y="160">"You have been on this journey</text>
  <text font-family="Patrick Hand, cursive" font-size="28" fill="white" x="56" y="200">with me," said Kev.</text>
  <text font-family="Patrick Hand, cursive" font-size="28" fill="white" x="56" y="256">"Every morning.</text>
  <text font-family="Patrick Hand, cursive" font-size="28" fill="white" x="56" y="296">Every word."</text>
  <text font-family="Patrick Hand, cursive" font-size="28" fill="white" x="56" y="352">"Here is what I know now:"</text>
  <text font-family="Fredoka One, cursive" font-size="32" fill="#FDD835" x="56" y="410">Words have wings.</text>
  <text font-family="Fredoka One, cursive" font-size="32" fill="#4CAF82" x="56" y="454">And so do you.</text>
  <text font-family="Fredoka One, cursive" font-size="26" fill="white" x="56" y="504">What is YOUR word today?</text>
</svg></div>'''

closing_wing_of_words = '''<div class="slide" data-label="CLOSING · WING OF WORDS"><svg class="page" viewBox="0 0 960 540" xmlns="http://www.w3.org/2000/svg">
  <rect width="960" height="540" fill="#1A237E"/>
  <circle cx="480" cy="320" r="420" fill="none" stroke="#1565C0" stroke-width="2" opacity="0.4"/>
  <circle cx="480" cy="320" r="300" fill="none" stroke="#1565C0" stroke-width="2" opacity="0.35"/>
  <path d="M0 0 L98 0 L0 98 Z" fill="#FDD835" opacity="0.1"/><path d="M960 0 L862 0 L960 98 Z" fill="#FDD835" opacity="0.1"/>
  <path d="M0 540 L98 540 L0 442 Z" fill="#4CAF82" opacity="0.1"/><path d="M960 540 L862 540 L960 442 Z" fill="#4CAF82" opacity="0.1"/>
  <path d="M84 84 L88 70 L92 84 L106 88 L92 92 L88 106 L84 92 L70 88 Z" fill="#FDD835" opacity="0.8"/>
  <text font-family="Fredoka One, cursive" font-size="22" fill="#4CAF82" letter-spacing="3" x="480" y="54" text-anchor="middle">KEV\'S WING OF WORDS</text>
  <g transform="translate(380, 180) scale(0.38)">
    <path d="M260 292 Q192 224 154 164 Q222 214 268 282 Z" fill="#5C3A1E"/>
    <path d="M264 286 Q212 232 192 188 Q248 226 270 278 Z" fill="#8B5E3C"/>
    <path d="M376 292 Q444 224 482 164 Q414 214 368 282 Z" fill="#5C3A1E"/>
    <path d="M372 286 Q424 232 444 188 Q388 226 366 278 Z" fill="#8B5E3C"/>
    <ellipse cx="318" cy="306" rx="72" ry="58" fill="#8B5E3C"/>
    <ellipse cx="318" cy="318" rx="48" ry="38" fill="#FDECC8"/>
    <circle cx="318" cy="204" r="80" fill="#FDECC8"/>
    <path d="M246 188 Q262 120 318 108 Q374 120 390 188 Q364 156 318 152 Q272 156 246 188Z" fill="#5C3A1E"/>
    <path d="M310 128 Q304 66 314 38 Q326 68 322 130Z" fill="#8B5E3C"/>
    <circle cx="284" cy="192" r="22" fill="white"/><circle cx="286" cy="190" r="14" fill="#1A1A2E"/><circle cx="292" cy="184" r="6" fill="white"/>
    <circle cx="352" cy="190" r="22" fill="white"/><circle cx="354" cy="188" r="14" fill="#1A1A2E"/><circle cx="360" cy="182" r="6" fill="white"/>
    <path d="M318 208 L318 208 L368 220 L318 232 Z" fill="#E07B2A"/>
    <circle cx="200" cy="230" r="12" fill="#FDD835" opacity="0.9"/><circle cx="200" cy="230" r="7" fill="#F9A825"/>
  </g>
  <rect x="42" y="168" width="198" height="30" rx="14" fill="#FDD835" opacity="0.15"/><rect x="42" y="168" width="198" height="30" rx="14" fill="none" stroke="#FDD835" stroke-width="1.2" opacity="0.6"/>
  <text font-family="Patrick Hand, cursive" font-size="17" fill="#FDD835" x="141" y="189" text-anchor="middle">Day 1 — I believe in me!</text>
  <rect x="28" y="210" width="192" height="30" rx="14" fill="#FDD835" opacity="0.12"/><rect x="28" y="210" width="192" height="30" rx="14" fill="none" stroke="#FDD835" stroke-width="1.2" opacity="0.5"/>
  <text font-family="Patrick Hand, cursive" font-size="17" fill="#FDD835" x="124" y="231" text-anchor="middle">Day 2 — I am strong!</text>
  <rect x="22" y="252" width="216" height="30" rx="14" fill="#4CAF82" opacity="0.12"/><rect x="22" y="252" width="216" height="30" rx="14" fill="none" stroke="#4CAF82" stroke-width="1.2" opacity="0.5"/>
  <text font-family="Patrick Hand, cursive" font-size="17" fill="#4CAF82" x="130" y="273" text-anchor="middle">Day 3 — My voice matters!</text>
  <rect x="22" y="294" width="232" height="30" rx="14" fill="#4CAF82" opacity="0.12"/><rect x="22" y="294" width="232" height="30" rx="14" fill="none" stroke="#4CAF82" stroke-width="1.2" opacity="0.5"/>
  <text font-family="Patrick Hand, cursive" font-size="17" fill="#4CAF82" x="138" y="315" text-anchor="middle">Day 4 — I can do hard things!</text>
  <rect x="28" y="336" width="238" height="30" rx="14" fill="#F06292" opacity="0.12"/><rect x="28" y="336" width="238" height="30" rx="14" fill="none" stroke="#F06292" stroke-width="1.2" opacity="0.5"/>
  <text font-family="Patrick Hand, cursive" font-size="17" fill="#F06292" x="147" y="357" text-anchor="middle">Day 5 — I show up every day!</text>
  <rect x="40" y="378" width="196" height="30" rx="14" fill="#F06292" opacity="0.12"/><rect x="40" y="378" width="196" height="30" rx="14" fill="none" stroke="#F06292" stroke-width="1.2" opacity="0.5"/>
  <text font-family="Patrick Hand, cursive" font-size="17" fill="#F06292" x="138" y="399" text-anchor="middle">Day 6 — I am kind!</text>
  <rect x="58" y="420" width="196" height="30" rx="14" fill="#FF5C00" opacity="0.12"/><rect x="58" y="420" width="196" height="30" rx="14" fill="none" stroke="#FF5C00" stroke-width="1.2" opacity="0.5"/>
  <text font-family="Patrick Hand, cursive" font-size="17" fill="#FF5C00" x="156" y="441" text-anchor="middle">Day 7 — I am brave!</text>
  <rect x="720" y="168" width="198" height="30" rx="14" fill="#FDD835" opacity="0.15"/><rect x="720" y="168" width="198" height="30" rx="14" fill="none" stroke="#FDD835" stroke-width="1.2" opacity="0.6"/>
  <text font-family="Patrick Hand, cursive" font-size="17" fill="#FDD835" x="819" y="189" text-anchor="middle">Day 8 — I am enough!</text>
  <rect x="740" y="210" width="196" height="30" rx="14" fill="#FDD835" opacity="0.12"/><rect x="740" y="210" width="196" height="30" rx="14" fill="none" stroke="#FDD835" stroke-width="1.2" opacity="0.5"/>
  <text font-family="Patrick Hand, cursive" font-size="17" fill="#FDD835" x="838" y="231" text-anchor="middle">Day 9 — I take care of me!</text>
  <rect x="722" y="252" width="216" height="30" rx="14" fill="#4CAF82" opacity="0.12"/><rect x="722" y="252" width="216" height="30" rx="14" fill="none" stroke="#4CAF82" stroke-width="1.2" opacity="0.5"/>
  <text font-family="Patrick Hand, cursive" font-size="17" fill="#4CAF82" x="830" y="273" text-anchor="middle">Day 10 — I love to learn!</text>
  <rect x="710" y="294" width="228" height="30" rx="14" fill="#4CAF82" opacity="0.12"/><rect x="710" y="294" width="228" height="30" rx="14" fill="none" stroke="#4CAF82" stroke-width="1.2" opacity="0.5"/>
  <text font-family="Patrick Hand, cursive" font-size="17" fill="#4CAF82" x="824" y="315" text-anchor="middle">Day 11 — I am grateful!</text>
  <rect x="694" y="336" width="238" height="30" rx="14" fill="#F06292" opacity="0.12"/><rect x="694" y="336" width="238" height="30" rx="14" fill="none" stroke="#F06292" stroke-width="1.2" opacity="0.5"/>
  <text font-family="Patrick Hand, cursive" font-size="17" fill="#F06292" x="813" y="357" text-anchor="middle">Day 12 — I belong here!</text>
  <rect x="706" y="378" width="212" height="30" rx="14" fill="#F06292" opacity="0.12"/><rect x="706" y="378" width="212" height="30" rx="14" fill="none" stroke="#F06292" stroke-width="1.2" opacity="0.5"/>
  <text font-family="Patrick Hand, cursive" font-size="17" fill="#F06292" x="812" y="399" text-anchor="middle">Day 13 — I am ready!</text>
  <rect x="282" y="464" width="396" height="36" rx="18" fill="#FDD835" opacity="0.18"/><rect x="282" y="464" width="396" height="36" rx="18" fill="none" stroke="#FDD835" stroke-width="2" opacity="0.9"/>
  <text font-family="Fredoka One, cursive" font-size="18" fill="#FDD835" x="480" y="488" text-anchor="middle">Day 14 — Words have wings — and so do I!</text>
  <text font-family="Fredoka One, cursive" font-size="14" fill="white" opacity="0.25" x="480" y="528" text-anchor="middle">Small habits. Big wings.</text>
</svg></div>'''

closing_golden_feather = '''<div class="slide" data-label="CLOSING · GOLDEN FEATHER"><svg class="page" viewBox="0 0 960 540" xmlns="http://www.w3.org/2000/svg">
  <rect width="960" height="540" fill="#1A237E"/>
  <circle cx="480" cy="282" r="396" fill="none" stroke="#1565C0" stroke-width="2" opacity="0.5"/>
  <circle cx="480" cy="282" r="310" fill="none" stroke="#1565C0" stroke-width="2" opacity="0.5"/>
  <circle cx="480" cy="282" r="226" fill="none" stroke="#1565C0" stroke-width="2" opacity="0.4"/>
  <circle cx="480" cy="282" r="142" fill="none" stroke="#1565C0" stroke-width="2" opacity="0.4"/>
  <path d="M0 0 L98 0 L0 98 Z" fill="#FDD835" opacity="0.1"/><path d="M960 0 L862 0 L960 98 Z" fill="#FDD835" opacity="0.1"/>
  <path d="M0 540 L98 540 L0 442 Z" fill="#4CAF82" opacity="0.1"/><path d="M960 540 L862 540 L960 442 Z" fill="#4CAF82" opacity="0.1"/>
  <path d="M84 84 L88 70 L92 84 L106 88 L92 92 L88 106 L84 92 L70 88 Z" fill="#FDD835" opacity="0.8"/>
  <circle cx="170" cy="226" r="7" fill="#F06292" opacity="0.6"/><circle cx="790" cy="212" r="6" fill="#4CAF82" opacity="0.6"/>
  <circle cx="340" cy="506" r="5" fill="#FDD835" opacity="0.5"/><circle cx="396" cy="506" r="5" fill="#4CAF82" opacity="0.5"/><circle cx="452" cy="506" r="5" fill="#FF5C00" opacity="0.5"/><circle cx="508" cy="506" r="5" fill="#FDD835" opacity="0.5"/><circle cx="564" cy="506" r="5" fill="#4CAF82" opacity="0.5"/><circle cx="620" cy="506" r="5" fill="#FF5C00" opacity="0.5"/>
  <g transform="translate(498, 180) scale(0.68)">
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
    <path d="M264 286 Q230 310 200 340 Q220 306 252 290 Z" fill="#8B5E3C"/>
  </g>
  <g transform="translate(310, 290) rotate(-35)">
    <line x1="0" y1="120" x2="0" y2="-80" stroke="#8B6914" stroke-width="4" stroke-linecap="round"/>
    <path d="M0 -60 Q-22 -50 -32 -38 Q-16 -46 0 -44Z" fill="#FDD835"/>
    <path d="M0 -38 Q-28 -26 -40 -12 Q-22 -22 0 -20Z" fill="#FDD835"/>
    <path d="M0 -16 Q-30 -2 -42 14 Q-24 2 0 4Z" fill="#FDD835"/>
    <path d="M0 8 Q-30 24 -40 42 Q-22 28 0 28Z" fill="#FDD835"/>
    <path d="M0 32 Q-28 50 -36 68 Q-20 54 0 52Z" fill="#FDD835" opacity="0.9"/>
    <path d="M0 56 Q-24 72 -28 88 Q-14 76 0 76Z" fill="#FDD835" opacity="0.75"/>
    <path d="M0 -60 Q22 -50 32 -38 Q16 -46 0 -44Z" fill="#F9A825"/>
    <path d="M0 -38 Q28 -26 40 -12 Q22 -22 0 -20Z" fill="#F9A825"/>
    <path d="M0 -16 Q30 -2 42 14 Q24 2 0 4Z" fill="#F9A825"/>
    <path d="M0 8 Q30 24 40 42 Q22 28 0 28Z" fill="#F9A825"/>
    <path d="M0 32 Q28 50 36 68 Q20 54 0 52Z" fill="#F9A825" opacity="0.9"/>
    <path d="M0 56 Q24 72 28 88 Q14 76 0 76Z" fill="#F9A825" opacity="0.75"/>
    <ellipse cx="0" cy="20" rx="30" ry="80" fill="#FDD835" opacity="0.12"/>
    <circle cx="-48" cy="10" r="3" fill="#FDD835" opacity="0.7"/>
    <circle cx="50" cy="-20" r="2.5" fill="#FDD835" opacity="0.6"/>
  </g>
  <text font-family="Patrick Hand, cursive" font-size="30" fill="white" x="56" y="200">"This golden feather</text>
  <text font-family="Patrick Hand, cursive" font-size="30" fill="white" x="56" y="244">is yours now."</text>
  <text font-family="Fredoka One, cursive" font-size="44" fill="#FDD835" x="56" y="320">"You earned it."</text>
  <text font-family="Patrick Hand, cursive" font-size="26" fill="white" opacity="0.8" x="56" y="390">said Kev,</text>
  <text font-family="Patrick Hand, cursive" font-size="26" fill="white" opacity="0.8" x="56" y="428">right to you.</text>
  <text font-family="Fredoka One, cursive" font-size="14" fill="white" opacity="0.25" x="480" y="528" text-anchor="middle">2026 Hatch a Habit - VERO PTY LTD</text>
</svg></div>'''

# ============================================================
# FEATHER GLOW — append to each affirmation page
# ============================================================
feather_note = '''
  <text font-family="Patrick Hand, cursive" font-size="22" fill="white" opacity="0.7" x="480" y="460" text-anchor="middle">And somewhere in his wing…</text>
  <text font-family="Fredoka One, cursive" font-size="24" fill="#FDD835" x="480" y="494" text-anchor="middle">he felt something warm. ✦</text>'''

# Find all affirmation pages and add feather note before closing </svg></div>
# Affirmation pages have "KEV'S AFFIRMATION" text
aff_marker = 'KEV\'S AFFIRMATION'
count = 0
pos = 0
while True:
    idx = html.find(aff_marker, pos)
    if idx == -1:
        break
    # Find the closing </svg></div> after this affirmation
    close_idx = html.find('</svg></div>', idx)
    if close_idx == -1:
        break
    # Check feather note not already there
    if 'something warm' not in html[idx:close_idx]:
        html = html[:close_idx] + feather_note + '\n' + html[close_idx:]
        count += 1
    pos = close_idx + 100

print(f'✅ Feather glow added to {count} affirmation pages')

# ============================================================
# INJECT OPENING PAGES — before DAY 01 PAGE 1
# ============================================================
inject_point = '<!-- PAGE: DAY 01 · PAGE 1 -->'
opening_block = f'''<!-- PAGE: THE LEGEND · PAGE 1 -->
        {opening_page1}

        <!-- PAGE: THE LEGEND · PAGE 2 -->
        {opening_page2}

        <!-- PAGE: THE LEGEND · PAGE 3 -->
        {opening_page3}

        {inject_point}'''

if inject_point in html:
    html = html.replace(inject_point, opening_block, 1)
    print('✅ 3 opening pages injected')
else:
    print('⚠️ Opening inject point not found')

# ============================================================
# INJECT CLOSING PAGES — before the existing closing/certificate
# ============================================================
# Find the existing affirmations recap or certificate slide
close_point = '<!-- PAGE: CLOSING'
if close_point not in html:
    # Try to find the last slide before certificate
    close_point = '<!-- PAGE: DAY 14'
    idx = html.rfind(close_point)
    # Find the end of day 14 slide block
    end_idx = html.find('</svg></div>', idx)
    end_idx = html.find('\n', end_idx) + 1
    closing_block = f'''
        <!-- PAGE: CLOSING · KEV SPEAKS -->
        {closing_kev_speaks}

        <!-- PAGE: CLOSING · WING OF WORDS -->
        {closing_wing_of_words}

        <!-- PAGE: CLOSING · GOLDEN FEATHER -->
        {closing_golden_feather}

        '''
    html = html[:end_idx] + closing_block + html[end_idx:]
    print('✅ 3 closing pages injected after Day 14')
else:
    print('⚠️ Closing inject point — check manually')

# ============================================================
# WRITE OUTPUT
# ============================================================
with open('book1-golden-feather.html', 'w') as f:
    f.write(html)

print(f'\n========================================')
print(f'✅ book1-golden-feather.html complete')
print(f'   Size: {len(html):,} bytes')
print(f'========================================')
