#!/usr/bin/env python3
"""Generate src/data/enrichments.ts: hero-specific professional builds for all 127 heroes.
Each entry overrides: support build (differentiated), combos, playstyle, skillBuild,
counters, goodAgainst, difficulty, patchTier. Core builds stay from builds.ts.
"""
import json

# Hero id -> (en, fa, attr)
heroes = json.loads('''[["antimage","Anti-Mage","آنتی-میج","agi"],["axe","Axe","اکس","str"],["bane","Bane","بین","all"],["bloodseeker","Bloodseeker","بلادسیکر","agi"],["crystal_maiden","Crystal Maiden","کریستال میدن","int"],["drow_ranger","Drow Ranger","دراو رنجر","agi"],["earthshaker","Earthshaker","ارث‌شیکر","str"],["juggernaut","Juggernaut","جاگرنات","agi"],["mirana","Mirana","میرانا","agi"],["morphling","Morphling","مورفلینگ","agi"],["nevermore","Shadow Fiend","شدو فایند","agi"],["phantom_lancer","Phantom Lancer","فانتوم لنسر","agi"],["puck","Puck","پاک","int"],["pudge","Pudge","پاج","str"],["razor","Razor","ریزر","agi"],["sand_king","Sand King","سند کینگ","all"],["storm_spirit","Storm Spirit","استورم اسپریت","int"],["sven","Sven","سون","str"],["tiny","Tiny","تاینی","str"],["vengefulspirit","Vengeful Spirit","ونجفول اسپریت","agi"],["windrunner","Windranger","ویندرنجر","int"],["zuus","Zeus","زئوس","int"],["kunkka","Kunkka","کانکا","str"],["lina","Lina","لینا","int"],["lion","Lion","لاین","int"],["shadow_shaman","Shadow Shaman","شدو شامان","int"],["slardar","Slardar","اسلادار","str"],["tidehunter","Tidehunter","تایدهانتر","str"],["witch_doctor","Witch Doctor","ویچ دکتر","int"],["lich","Lich","لیچ","int"],["riki","Riki","ریکی","agi"],["enigma","Enigma","انیگما","all"],["tinker","Tinker","تینکر","int"],["sniper","Sniper","اسنایپر","agi"],["necrolyte","Necrophos","نکروفوس","int"],["warlock","Warlock","وارلوک","int"],["beastmaster","Beastmaster","بیست‌مستر","str"],["queenofpain","Queen of Pain","کویین آو پین","int"],["venomancer","Venomancer","ونومانسر","all"],["faceless_void","Faceless Void","فیسلس وید","agi"],["skeleton_king","Wraith King","ریث کینگ","str"],["death_prophet","Death Prophet","دث پرافیت","int"],["phantom_assassin","Phantom Assassin","فانتوم اسسین","agi"],["pugna","Pugna","پوگنا","int"],["templar_assassin","Templar Assassin","تمپلار اسسین","agi"],["viper","Viper","وایپر","agi"],["luna","Luna","لونا","agi"],["dragon_knight","Dragon Knight","دراگون نایت","str"],["dazzle","Dazzle","دازل","int"],["rattletrap","Clockwerk","کلاک‌ورک","str"],["leshrac","Leshrac","لشراک","int"],["furion","Nature's Prophet","نیچرز پروفت","int"],["life_stealer","Lifestealer","لایف‌استیلر","str"],["dark_seer","Dark Seer","دارک سیر","int"],["clinkz","Clinkz","کلینکز","agi"],["omniknight","Omniknight","آمنینایت","str"],["enchantress","Enchantress","انچانترس","int"],["huskar","Huskar","هاسکار","str"],["night_stalker","Night Stalker","نایت استاکر","str"],["broodmother","Broodmother","برودمادر","agi"],["bounty_hunter","Bounty Hunter","باونتی هانتر","agi"],["weaver","Weaver","ویور","agi"],["jakiro","Jakiro","جاکیرو","int"],["batrider","Batrider","بترایدر","all"],["chen","Chen","چن","int"],["spectre","Spectre","اسپکتر","agi"],["ancient_apparition","Ancient Apparition","انشنت آپاریشن","int"],["doom_bringer","Doom","دوم","str"],["ursa","Ursa","اورسا","agi"],["spirit_breaker","Spirit Breaker","اسپریت بریکر","str"],["gyrocopter","Gyrocopter","جایروکاپتر","agi"],["alchemist","Alchemist","الکمیست","str"],["invoker","Invoker","اینووکر","int"],["silencer","Silencer","سایلنسر","int"],["obsidian_destroyer","Outworld Destroyer","اوت‌ورلد دسترویر","int"],["lycan","Lycan","لایکن","str"],["brewmaster","Brewmaster","برومستر","str"],["shadow_demon","Shadow Demon","شدو دیمون","int"],["lone_druid","Lone Druid","لون درویید","agi"],["chaos_knight","Chaos Knight","کائوس نایت","str"],["meepo","Meepo","میپو","agi"],["treant","Treant Protector","ترینت پروتکتور","str"],["ogre_magi","Ogre Magi","اوگر مجای","str"],["undying","Undying","آندایینگ","str"],["rubick","Rubick","روبیک","int"],["disruptor","Disruptor","دیسراپتور","int"],["nyx_assassin","Nyx Assassin","نیکس اسسین","agi"],["naga_siren","Naga Siren","ناگا سایرِن","agi"],["keeper_of_the_light","Keeper of the Light","کیپر آو د لایت","int"],["wisp","Io","ایو","all"],["visage","Visage","ویزاژ","all"],["slark","Slark","اسلارک","agi"],["medusa","Medusa","مدوسا","agi"],["troll_warlord","Troll Warlord","ترول وارلورد","agi"],["centaur","Centaur Warrunner","سنتور واررانر","str"],["magnataur","Magnus","مگنوس","str"],["shredder","Timbersaw","تیمبرسا","str"],["bristleback","Bristleback","بریستل‌بک","str"],["tusk","Tusk","تاسک","str"],["skywrath_mage","Skywrath Mage","اسکای‌راث میج","int"],["abaddon","Abaddon","آبادون","all"],["elder_titan","Elder Titan","الدر تایتان","str"],["legion_commander","Legion Commander","لیجن کماندر","str"],["techies","Techies","تکیز","int"],["ember_spirit","Ember Spirit","امبر اسپریت","agi"],["earth_spirit","Earth Spirit","ارث اسپریت","str"],["abyssal_underlord","Underlord","آندرلورد","str"],["terrorblade","Terrorblade","تروربلید","agi"],["phoenix","Phoenix","فونیکس","str"],["oracle","Oracle","اوراکل","int"],["winter_wyvern","Winter Wyvern","وینتر وایورن","int"],["arc_warden","Arc Warden","آرک وارن","agi"],["monkey_king","Monkey King","مانکی کینگ","agi"],["dark_willow","Dark Willow","دارک ویلو","int"],["pangolier","Pangolier","پانگولیر","all"],["grimstroke","Grimstroke","گریم‌استروک","int"],["mars","Mars","مارس","str"],["snapfire","Snapfire","سناپ‌فایر","str"],["void_spirit","Void Spirit","وید اسپریت","int"],["hoodwink","Hoodwink","هودوینک","agi"],["dawnbreaker","Dawnbreaker","دان‌بریکر","str"],["marci","Marci","مارسی","str"],["primal_beast","Primal Beast","پرایمال بیست","str"],["muerta","Muerta","موئرتا","int"],["ringmaster","Ringmaster","رینگ‌مستر","int"],["kez","Kez","کز","agi"],["largo","Largo","لارگو","str"]]''')

HERO = {h[0]: {'en': h[1], 'fa': h[2], 'attr': h[3]} for h in heroes}
HERO_IDS = [h[0] for h in heroes]

# ---- Support build templates (differentiated, professional pos-4/5) ----
SUP_INT_RANGE = {  # ranged INT supports - glimmer/force/greaves core
    'starting': ["tango","flask","branches","wind_lace","ring_of_basilius","observer_ward"],
    'early': ["arcane_boots","magic_wand","urn_of_shadows","glimmer_cape","wind_lace","sentry_ward"],
    'mid': ["arcane_boots","glimmer_cape","force_staff","urn_of_shadows","solar_crest","aghs_shard"],
    'late': ["guardian_greaves","glimmer_cape","force_staff","sheepstick","solar_crest","pipe"],
    'situational': ["aghanims_scepter","refresher","lotus_orb","rod_of_atos","pavise","mekansm"],
}
SUP_INT_AGGRO = {  # aggressive disable supports (Lion, SS, Rubick) - blink/force
    'starting': ["tango","flask","branches","wind_lace","ring_of_basilius","observer_ward"],
    'early': ["arcane_boots","magic_wand","urn_of_shadows","blink","wind_lace","tranquil_boots"],
    'mid': ["arcane_boots","blink","force_staff","glimmer_cape","aghs_shard","urn_of_shadows"],
    'late': ["guardian_greaves","blink","sheepstick","aghanims_scepter","glimmer_cape","refresher"],
    'situational': ["lotus_orb","rod_of_atos","pavise","solar_crest","pipe","aghs_shard"],
}
SUP_STR_MELEE = {  # STR melee supports/initiators (ES, Treant, Undying, Ogre, Tusk)
    'starting': ["tango","flask","branches","gauntlets","stout_shield","observer_ward"],
    'early': ["arcane_boots","magic_wand","urn_of_shadows","bracer","wind_lace","glimmer_cape"],
    'mid': ["arcane_boots","urn_of_shadows","force_staff","glimmer_cape","bracer","aghs_shard"],
    'late': ["guardian_greaves","force_staff","spirit_vessel","pipe","solar_crest","lotus_orb"],
    'situational': ["aghanims_scepter","refresher","sheepstick","crimson_guard","blade_mail","pavise"],
}
SUP_JUNGLER = {  # Chen/Enchantress - dominated creeps
    'starting': ["tango","flask","branches","wind_lace","ring_of_basilius","observer_ward"],
    'early': ["arcane_boots","magic_wand","urn_of_shadows","glimmer_cape","wind_lace","aghs_shard"],
    'mid': ["arcane_boots","glimmer_cape","force_staff","mekansm","aghs_shard","solar_crest"],
    'late': ["guardian_greaves","force_staff","glimmer_cape","aghanims_scepter","mekansm","solar_crest"],
    'situational': ["refresher","lotus_orb","rod_of_atos","pavise","pipe","aghs_shard"],
}
SUP_SAVE = {  # save supports (Dazzle, Oracle, Wyvern, Abaddon) - glimmer/force/eul
    'starting': ["tango","flask","branches","wind_lace","ring_of_basilius","observer_ward"],
    'early': ["arcane_boots","magic_wand","urn_of_shadows","glimmer_cape","solar_crest","sentry_ward"],
    'mid': ["arcane_boots","glimmer_cape","force_staff","solar_crest","aghs_shard","urn_of_shadows"],
    'late': ["guardian_greaves","glimmer_cape","force_staff","solar_crest","aghanims_scepter","lotus_orb"],
    'situational': ["refresher","sheepstick","pipe","pavise","rod_of_atos","mekansm"],
}

# ---- Per-hero professional data ----
# Each entry: support_template, combos(en,fa), playstyle(en,fa), skillBuild(en,fa),
#   counters[], goodAgainst[], difficulty(1-3), patchTier(1-5)
# Counters/goodAgainst use REAL hero ids.

DATA = {}

# ===================== AGI CARRIES =====================
DATA["antimage"] = (None,
  ("Blink on top of target, Mana Break attacks to burn mana, Counterspell to block spells, BKB if needed, Mana Void on low-mana cluster for AoE kill.",
   "بلینک روی هدف، حمله Mana Break برای سوختن مانا، Counterspell برای مسدود طلسم، BKB در صورت نیاز، Mana Void روی دشمنان کم‌مانا."),
  ("Hard carry: farm aggressively with Battle Fury, split-push lanes, only fight with BKB off cooldown. Target supports first. Join fights late game with Abyssal+BKB.",
   "کری هارد: با Battle Fury سریع فارم کن، لین‌پوش کن، فقط با BKB آماده بجنگ. اول ساپورت‌ها را بزن. لیت گیم با Abyssal+BKB وارد درگیری شو."),
  ("Max Q (Mana Break) first, then E (Counterspell), 1 point W (Blink) early, ulti at 6/12/18.",
   "ابتدا Q (Mana Break) ماکس، بعد E (Counterspell)، یک پوینت W (Blink) زود، اولتی ۶/۱۲/۱۸."),
  ["axe","legion_commander","bloodseeker","slark"], ["medusa","morphling","storm_spirit","tinker"], 2, 2)

DATA["axe"] = (SUP_STR_MELEE,
  ("Blink onto 3+ enemies, Berserker's Call to lock all, pop Blade Mail, Culling Blade the low-HP target to reset and intimidate.",
   "بلینک روی ۳+ دشمن، Berserker's Call برای لاک همه، Blade Mail بزن، Culling Blade روی هدف کم‌خون برای ریست و ترس."),
  ("Offlane/initiator: get Blink by 12-15 min, Berserker's Call multiple heroes, soak damage with Blade Mail. Counter right-click carries.",
   "آفلین/اینیشیتور: تا ۱۲-۱۵ دقیقه Blink بگیر، چند هیرو را Berserker's Call کن، با Blade Mail آسیب جذب کن. کانتر کری‌های راست‌کلیک."),
  ("Max Q (Berserker's Call) or W (Battle Hunger) first, then the other, ulti when available.",
   "ابتدا Q (Berserker's Call) یا W (Battle Hunger) ماکس، بعد دیگری، اولتی آماده."),
  ["viper","drow_ranger","sniper","lina"], ["phantom_assassin","juggernaut","troll_warlord","life_stealer"], 1, 2)

DATA["bloodseeker"] = (None,
  ("Cast Blood Rite to silence, Thirst to track low-HP enemies, Rupture the mobile carry, right-click with BKB to finish.",
   "Blood Rite برای سایلنس، Thirst برای ردیابی کم‌خون‌ها، Rupture روی کری متحرک، راست‌کلیک با BKB برای کشتن."),
  ("Carry/ganker: farm jungle efficiently, use Thirst to find low-HP targets, Rupture escaping heroes. Build right-click + BKB.",
   "کری/گنکر: جنگل را خوب فارم کن، با Thirst کم‌خون‌ها را پیدا کن، Rupture روی فراری‌ها. راست‌کلیک + BKB بخر."),
  ("Max Q (Blood Rite) and W (Thirst) together, ulti when available.",
   "Q (Blood Rite) و W (Thirst) با هم ماکس، اولتی آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["antimage","storm_spirit","weaver","clinkz"], 1, 3)

DATA["drow_ranger"] = (SUP_INT_RANGE,
  ("Position in back, Frost Arrow slow, Silence the caster, pop BKB + Multishot (Gust) for AoE, Marksmanship pierce when stacked.",
   "پوزیشن عقب، Frost Arrow کند، Silence روی کستر، BKB + Multishot برای AOE، Marksmanship وقتی استک شد."),
  ("Hard ranged carry: max Frost Arrows, build AGI items (Manta, Butterfly, Silver Edge), build BKB early, position safe in back.",
   "کری رنج هارد: Frost Arrows ماکس، آیتم AGI (Manta, Butterfly, Silver Edge)، BKB زود، پوزیشن عقب امن."),
  ("Max Q (Frost Arrows) then W (Gust), ulti (Marksmanship) when available.",
   "ابتدا Q (Frost Arrows) بعد W (Gust)، اولتی (Marksmanship) آماده."),
  ["axe","slark","phantom_assassin","night_stalker"], ["templar_assassin","sniper","medusa","luna"], 1, 2)

DATA["juggernaut"] = (None,
  ("Blade Fury for magic immunity, Omnislash on clustered enemies, right-click with Healing Ward nearby, Swiftslash late to finish.",
   "Blade Fury برای ایمونی، Omnislash روی دشمنان تجمعی، راست‌کلیک با Healing Ward کنار، Swiftslash لیت برای کشتن."),
  ("Hard carry: farm with Battle Fury, Blade Fury to avoid disables, Omnislash in teamfights for burst, Healing Ward for sustain.",
   "کری هارد: با Battle Fury فارم کن، Blade Fury برای فرار دیزیبل، Omnislash در درگیری برای برست، Healing Ward برای پایداری."),
  ("Max Q (Blade Fury) first, then E (Blade Dance), 1 point Healing Ward early, ulti when available.",
   "ابتدا Q (Blade Fury) ماکس، بعد E (Blade Dance)، یک پوینت Healing Ward زود، اولتی آماده."),
  ["axe","legion_commander","doom_bringer","faceless_void"], ["templar_assassin","medusa","phantom_lancer","sniper"], 2, 1)

DATA["mirana"] = (SUP_INT_AGGRO,
  ("Sacred Arrow into Arrow-into-Moonlight Shadow, Leap to engage, Starstorm for burst, Sacred Arrow follow-up.",
   "Sacred Arrow سپس Moonlight Shadow، Leap برای ورود، Starstorm برای برست، Sacred Arrow دنباله."),
  ("Flex carry/support: Arrow setup for ganks, Moonlight Shadow for team invis initiation, Leap to escape. Build AGI/BKB.",
   "فلکس کری/ساپورت: Arrow برای گنک، Moonlight Shadow برای اینیشیت تیمی، Leap برای فرار. AGI/BKB بخر."),
  ("Max Q (Starstorm) or W (Sacred Arrow) first, then the other, ulti (Moonlight Shadow) when available.",
   "ابتدا Q (Starstorm) یا W (Sacred Arrow) ماکس، بعد دیگری، اولتی (Moonlight Shadow) آماده."),
  ["doom_bringer","legion_commander","axe","slark"], ["templar_assassin","sniper","medusa","luna"], 3, 3)

DATA["morphling"] = (None,
  ("Shift to AGI for damage, Adaptive Strike (AGI) for burst, Waveform to reposition, Replicate to escape, Shotgun (Ethereal+Adaptive) combo.",
   "شیفت به AGI برای آسیب، Adaptive Strike (AGI) برای برست، Waveform برای پوزیشن، Replicate برای فرار، کمبو Shotgun."),
  ("Hard carry: Waveform to farm/initiate, shotgun build (Ethereal+Adaptive Strike) for burst, Replicate for safety. Build AGI/BKB.",
   "کری هارد: Waveform برای فارم/اینیشیت، کمبو Shotgun (Ethereal+Adaptive)، Replicate برای امن. AGI/BKB بخر."),
  ("Max Q (Waveform) or W (Adaptive Strike), 1 point E (Morph), ulti (Replicate) when available.",
   "ابتدا Q (Waveform) یا W (Adaptive Strike)، یک پوینت E (Morph)، اولتی (Replicate) آماده."),
  ["axe","doom_bringer","legion_commander","faceless_void"], ["templar_assassin","sniper","medusa","luna"], 3, 2)

DATA["nevermore"] = (None,
  ("Raze to nuke, stack souls for damage, Requiem of Souls in the middle of cluster with BKB, right-click with deso.",
   "Raze برای نیوک، استک روح برای آسیب، Requiem of Souls وسط دشمنان با BKB، راست‌کلیک با Deso."),
  ("Mid carry: last-hit with Raze, stack souls, BKB before Requiem. Build right-click + BKB + Blink for initiation.",
   "مید کری: لست‌هیت با Raze، استک روح، BKB قبل از Requiem. راست‌کلیک + BKB + Blink بخر."),
  ("Max Q/W/E (Raze) together, ulti (Requiem of Souls) when available.",
   "Q/W/E (Raze) با هم ماکس، اولتی (Requiem of Souls) آماده."),
  ["axe","legion_commander","doom_bringer","storm_spirit"], ["templar_assassin","medusa","phantom_lancer","sniper"], 3, 2)

DATA["phantom_lancer"] = (None,
  ("Spirit Lance to slow + spawn illusion, Doppelwalk to confuse, Phantom Rush, right-click with diffusal to burn mana.",
   "Spirit Lance برای کند + ایلوژن، Doppelwalk برای گیج، Phantom Rush، راست‌کلیک با Diffusal برای سوختن مانا."),
  ("Hard carry: spam Spirit Lance, Doppelwalk to dodge, illusions + Diffusal to overwhelm. Build Manta + Diffusal + BKB.",
   "کری هارد: Spirit Lance اسپم، Doppelwalk برای داج، ایلوژن + Diffusal برای غلبه. Manta + Diffusal + BKB بخر."),
  ("Max Q (Spirit Lance) then W (Doppelwalk), ulti (Juxtapose) when available.",
   "ابتدا Q (Spirit Lance) بعد W (Doppelwalk)، اولتی (Juxtapose) آماده."),
  ["axe","legion_commander","doom_bringer","earthshaker"], ["medusa","templar_assassin","sniper","troll_warlord"], 2, 2)

DATA["razor"] = (SUP_INT_RANGE,
  ("Static Link to steal damage, Eye of the Storm for sustained DPS, Plasma Field for slow, right-click with stolen damage.",
   "Static Link برای دزدی آسیب، Eye of the Storm برای DPS، Plasma Field برای کند، راست‌کلیک با آسیب دزدیده."),
  ("Carry/anti-carry: Static Link the enemy carry to steal damage, Eye of the Storm in fights. Build tanky-AGI + BKB.",
   "کری/آنتی‌کری: Static Link روی کری دشمن برای دزدی آسیب، Eye of the Storm در درگیری. تانک-AGI + BKB بخر."),
  ("Max Q (Plasma Field) and W (Static Link), ulti (Eye of the Storm) when available.",
   "ابتدا Q (Plasma Field) و W (Static Link)، اولتی (Eye of the Storm) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["phantom_assassin","troll_warlord","medusa","luna"], 2, 3)

DATA["slark"] = (None,
  ("Pounce to leash, Dark Pact to purge debuffs, Essence Shift on hits, Shadow Dance to escape/stealth-heal.",
   "Pounce برای بند، Dark Pact برای پورج، Essence Shift روی ضربات، Shadow Dance برای فرار/هیل استلت."),
  ("Carry/assassin: Pounce to lock, Essence Shift stacks for damage, Dark Pact to purge disables. Build Silver Edge + BKB + Skadi.",
   "کری/اسسین: Pounce برای لاک، Essence Shift استک برای آسیب، Dark Pact برای پورج دیزیبل. Silver Edge + BKB + Skadi بخر."),
  ("Max Q (Dark Pact) and W (Pounce), ulti (Shadow Dance) when available.",
   "ابتدا Q (Dark Pact) و W (Pounce)، اولتی (Shadow Dance) آماده."),
  ["axe","legion_commander","doom_bringer","bloodseeker"], ["medusa","templar_assassin","phantom_lancer","sniper"], 2, 2)

DATA["medusa"] = (None,
  ("Stone Gaze to petrify + slow, Mystic Snake to nuke/steal mana, Split Shot for AoE, right-click with BKB.",
   "Stone Gaze برای پتریفای + کند، Mystic Snake برای نیوک/دزدی مانا، Split Shot برای AOE، راست‌کلیک با BKB."),
  ("Hard ranged carry: farm safely, Split Shot for waves, Mystic Snake for mana, Stone Gaze in teamfights. Build Skadi + Butterfly + BKB.",
   "کری رنج هارد: امن فارم کن، Split Shot برای ویو، Mystic Snake برای مانا، Stone Gaze در درگیری. Skadi + Butterfly + BKB بخر."),
  ("Max Q (Split Shot) or W (Mystic Snake), ulti (Stone Gaze) when available.",
   "ابتدا Q (Split Shot) یا W (Mystic Snake)، اولتی (Stone Gaze) آماده."),
  ["axe","slark","phantom_assassin","antimage"], ["templar_assassin","phantom_lancer","troll_warlord","luna"], 2, 2)

DATA["faceless_void"] = (None,
  ("Chronosphere to trap enemies (avoid catching allies), Time Walk to rewind damage, right-click with Time Lock, Time Dilation.",
   "Chronosphere برای لاک دشمن (مراقب الی)، Time Walk برای ریویند آسیب، راست‌کلیک با Time Lock، Time Dilation."),
  ("Hard carry/initiator: farm with Maelstrom, Time Walk to survive, Chronosphere to win teamfights. Build Maelstrom + Mjollnir + BKB.",
   "کری هارد/اینیشیتور: با Maelstrom فارم کن، Time Walk برای زنده ماندن، Chronosphere برای برد درگیری. Maelstrom + Mjollnir + BKB بخر."),
  ("Max Q (Time Walk) then W (Time Dilation), 1 point E (Time Lock) early, ulti (Chronosphere) when available.",
   "ابتدا Q (Time Walk) بعد W (Time Dilation)، یک پوینت E (Time Lock) زود، اولتی (Chronosphere) آماده."),
  ["doom_bringer","legion_commander","axe","slark"], ["templar_assassin","medusa","phantom_lancer","sniper"], 3, 1)

DATA["phantom_assassin"] = (None,
  ("Stifling Dagger to slow/initiate, Blink Strike to close, Phantom Strike + Blur for crits, right-click with BKB.",
   "Stifling Dagger برای کند/اینیشیت، Blink Strike برای نزدیک، Phantom Strike + Blur برای کرت، راست‌کلیک با BKB."),
  ("Hard carry: farm with Stifling Dagger, Blur to dodge, crit burst with BKB. Build Battle Fury + BKB + Desolator + Satanic.",
   "کری هارد: با Stifling Dagger فارم، Blur برای داج، کرت برست با BKB. Battle Fury + BKB + Desolator + Satanic بخر."),
  ("Max Q (Stifling Dagger) then E (Blur), ulti (Coup de Grace) when available.",
   "ابتدا Q (Stifling Dagger) بعد E (Blur)، اولتی (Coup de Grace) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["templar_assassin","medusa","sniper","drow_ranger"], 2, 2)

DATA["spectre"] = (None,
  ("Haunt to join fights globally, Reality to jump, Desolate for isolation bonus, right-click with Radiance + Manta.",
   "Haunt برای ورود جهانی، Reality برای جامپ، Desolate برای بونوس ایزوله، راست‌کلیک با Radiance + Manta."),
  ("Hard carry: farm with Radiance, Haunt to join every teamfight globally, build tanky + Manta. Build Radiance + Manta + Heart + BKB.",
   "کری هارد: با Radiance فارم، Haunt برای ورود به هر درگیری جهانی، تانک + Manta. Radiance + Manta + Heart + BKB بخر."),
  ("Max Q (Spectral Dagger) then E (Desolate), ulti (Haunt) when available.",
   "ابتدا Q (Spectral Dagger) بعد E (Desolate)، اولتی (Haunt) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["templar_assassin","medusa","sniper","drow_ranger"], 2, 2)

DATA["ember_spirit"] = (None,
  ("Sleight of Fist to AoE right-click, Searing Chains to root, Flame Guard for magic shield, Fire Remnant to escape/chase.",
   "Sleight of Fist برای AOE راست‌کلیک، Searing Chains برای روت، Flame Guard برای شیلد جادویی، Fire Remnant برای فرار/تعقیب."),
  ("Mid carry: Sleight of Fist to AoE, Fire Remnant for mobility/escape, BKB before fights. Build Maelstrom + Battle Fury + BKB.",
   "مید کری: Sleight of Fist برای AOE، Fire Remnant برای موبیلیتی/فرار، BKB قبل از درگیری. Maelstrom + Battle Fury + BKB بخر."),
  ("Max Q (Searing Chains) or E (Sleight of Fist), W (Flame Guard) mid, ulti (Fire Remnant) when available.",
   "ابتدا Q (Searing Chains) یا E (Sleight of Fist)، W (Flame Guard) مید، اولتی (Fire Remnant) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["templar_assassin","medusa","phantom_lancer","sniper"], 3, 2)

DATA["monkey_king"] = (None,
  ("Tree Dance to position, Primal Spring to engage, Jingu Mastery stacks for bonus, Wukong's Command for teamfight.",
   "Tree Dance برای پوزیشن، Primal Spring برای ورود، Jingu Mastery استک برای بونوس، Wukong's Command برای درگیری."),
  ("Carry/initiator: Tree Dance for vision/escape, Jingu Mastery stacks for burst, Wukong's Command in fights. Build Battle Fury + BKB + MKB.",
   "کری/اینیشیتور: Tree Dance برای ویژن/فرار، Jingu Mastery استک برای برست، Wukong's Command در درگیری. Battle Fury + BKB + MKB بخر."),
  ("Max Q (Boundless Strike) or W (Primal Spring), ulti (Wukong's Command) when available.",
   "ابتدا Q (Boundless Strike) یا W (Primal Spring)، اولتی (Wukong's Command) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["templar_assassin","medusa","sniper","drow_ranger"], 3, 2)

DATA["templar_assassin"] = (None,
  ("Refraction to absorb damage, Meld to hide+burst, Psi Blades for splash, Trap to slow, right-click with Desolator.",
   "Refraction برای جذب آسیب، Meld برای پنهان+برست، Psi Blades برای اسپلش، Trap برای کند، راست‌کلیک با Desolator."),
  ("Mid carry: Refraction for protection, Meld for burst/trap, Psi Blades for splash. Build Desolator + Blink + BKB.",
   "مید کری: Refraction برای محافظت، Meld برای برست/تله، Psi Blades برای اسپلش. Desolator + Blink + BKB بخر."),
  ("Max Q (Refraction) then E (Psi Blades), ulti (Psionic Trap) when available.",
   "ابتدا Q (Refraction) بعد E (Psi Blades)، اولتی (Psionic Trap) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["medusa","phantom_lancer","troll_warlord","luna"], 3, 1)

DATA["luna"] = (None,
  ("Lucent Beam to nuke, Moon Glaive for AoE, Eclipse for burst in fights, right-click with BKB + Manta.",
   "Lucent Beam برای نیوک، Moon Glaive برای AOE، Eclipse برای برست در درگیری، راست‌کلیک با BKB + Manta."),
  ("Hard ranged carry: Moon Glaive for wave clear, Eclipse for teamfights, BKB early. Build Manta + Butterfly + BKB + Satanic.",
   "کری رنج هارد: Moon Glaive برای کلیر ویو، Eclipse برای درگیری، BKB زود. Manta + Butterfly + BKB + Satanic بخر."),
  ("Max Q (Lucent Beam) then W (Moon Glaive), ulti (Eclipse) when available.",
   "ابتدا Q (Lucent Beam) بعد W (Moon Glaive)، اولتی (Eclipse) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["templar_assassin","phantom_lancer","medusa","sniper"], 2, 2)

DATA["sniper"] = (None,
  ("Headshot procs for stun, Shrapnel for slow/vision, Assassinate for long-range nuke, position far back with BKB.",
   "Headshot برای استان، Shrapnel برای کند/ویژن، Assassinate برای نیوک دور‌برد، پوزیشن عقب با BKB."),
  ("Hard ranged carry: farm safely from max range, Shrapnel for vision, BKB early to avoid dives. Build Manta + Butterfly + BKB + Skadi.",
   "کری رنج هارد: از ماکس رنج امن فارم کن، Shrapnel برای ویژن، BKB زود برای فرار دایو. Manta + Butterfly + BKB + Skadi بخر."),
  ("Max Q (Shrapnel) then E (Headshot), ulti (Assassinate) when available.",
   "ابتدا Q (Shrapnel) بعد E (Headshot)، اولتی (Assassinate) آماده."),
  ["axe","slark","phantom_assassin","night_stalker"], ["templar_assassin","medusa","troll_warlord","luna"], 1, 2)

DATA["troll_warlord"] = (None,
  ("Berserker's Rage to switch melee/ranged, Whirling Axes for blind/slow, Fervor stacks, Battle Trance to chase.",
   "Berserker's Rage برای سوییچ میل/رنج، Whirling Axes برای بلیند/کند، Fervor استک، Battle Trance برای تعقیب."),
  ("Carry: Berserker's Rage melee for fights, Whirling Axes to blind enemy carries, Battle Trance to chase. Build BKB + Satanic + MKB.",
   "کری: Berserker's Rage میل برای درگیری، Whirling Axes برای بلیند کری دشمن، Battle Trance برای تعقیب. BKB + Satanic + MKB بخر."),
  ("Max Q (Whirling Axes) then E (Fervor), ulti (Battle Trance) when available.",
   "ابتدا Q (Whirling Axes) بعد E (Fervor)، اولتی (Battle Trance) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["templar_assassin","medusa","phantom_lancer","sniper"], 2, 3)

DATA["weaver"] = (None,
  ("The Swarm for vision/armor reduction, Shukuchi to invis/escape, Geminate Attack for double-hit, Time Lapse to rewind.",
   "The Swarm برای ویژن/کاهش زره، Shukuchi برای اینویس/فرار، Geminate Attack برای دوضرب، Time Lapse برای ریویند."),
  ("Carry/escape: Shukuchi to dodge, The Swarm for armor reduction, Time Lapse to heal. Build Desolator + BKB + Butterfly.",
   "کری/فرار: Shukuchi برای داج، The Swarm برای کاهش زره، Time Lapse برای هیل. Desolator + BKB + Butterfly بخر."),
  ("Max Q (The Swarm) then W (Shikuchi), ulti (Time Lapse) when available.",
   "ابتدا Q (The Swarm) بعد W (Shukuchi)، اولتی (Time Lapse) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["templar_assassin","medusa","phantom_lancer","sniper"], 2, 3)

DATA["clinkz"] = (None,
  ("Strafe for attack speed, Searing Arrows for burn, Skeleton Walk to invis/position, Death Pact for sustain, right-click burst.",
   "Strafe برای سرعت حمله، Searing Arrows برای برن، Skeleton Walk برای اینویس/پوزیشن، Death Pact برای پایداری، برست راست‌کلیک."),
  ("Carry/ganker: Skeleton Walk to roam, Strafe + Searing Arrows for burst, Death Pact for sustain. Build Desolator + BKB + Butterfly.",
   "کری/گنکر: Skeleton Walk برای روم، Strafe + Searing Arrows برای برست، Death Pact برای پایداری. Desolator + BKB + Butterfly بخر."),
  ("Max Q (Strafe) and W (Searing Arrows), ulti (Death Pact) when available.",
   "ابتدا Q (Strafe) و W (Searing Arrows)، اولتی (Death Pact) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["templar_assassin","medusa","phantom_lancer","sniper"], 2, 2)

DATA["riki"] = (None,
  ("Smoke Screen to silence/miss, Blink Strike to close, Tricks of the Trade to invuln+attack, right-click with Diffusal.",
   "Smoke Screen برای سایلنس/میس، Blink Strike برای نزدیک، Tricks of the Trade برای ایون+حمله، راست‌کلیک با Diffusal."),
  ("Carry/initiator: Smoke Screen to disable, Tricks of the Trade for invuln burst, Permanent Invisibility to roam. Build Diffusal + BKB + Butterfly.",
   "کری/اینیشیتور: Smoke Screen برای دیزیبل، Tricks of the Trade برای برست ایون، Permanent Invisibility برای روم. Diffusal + BKB + Butterfly بخر."),
  ("Max Q (Smoke Screen) then W (Blink Strike), ulti (Tricks of the Trade) when available.",
   "ابتدا Q (Smoke Screen) بعد W (Blink Strike)، اولتی (Tricks of the Trade) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["templar_assassin","medusa","phantom_lancer","sniper"], 2, 3)

DATA["ursa"] = (None,
  ("Earthshock to slow, Fury Swipes stacks for damage, Enrage for damage reduction, right-click with BKB + Skadi.",
   "Earthshock برای کند، Fury Swipes استک برای آسیب، Enrage برای کاهش آسیب، راست‌کلیک با BKB + Skadi."),
  ("Carry/jungler: stack Fury Swipes, Enrage to tank, BKB to avoid disables. Build Blink + BKB + Skadi + Satanic.",
   "کری/جنگلر: Fury Swipes استک، Enrage برای تانک، BKB برای فرار دیزیبل. Blink + BKB + Skadi + Satanic بخر."),
  ("Max W (Fury Swipes) then Q (Earthshock), ulti (Enrage) when available.",
   "ابتدا W (Fury Swipes) بعد Q (Earthshock)، اولتی (Enrage) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["templar_assassin","medusa","phantom_lancer","sniper"], 2, 3)

DATA["gyrocopter"] = (None,
  ("Rocket Barrage for AoE, Homing Missile for stun, Flak Cannon for AoE right-click, Call Down for teamfight.",
   "Rocket Barrage برای AOE، Homing Missile برای استان، Flak Cannon برای AOE راست‌کلیک، Call Down برای درگیری."),
  ("Ranged carry: Flak Cannon for AoE wave clear, Call Down for teamfights, BKB early. Build Manta + Butterfly + BKB + Satanic.",
   "کری رنج: Flak Cannon برای کلیر ویو AOE، Call Down برای درگیری، BKB زود. Manta + Butterfly + BKB + Satanic بخر."),
  ("Max Q (Rocket Barrage) then W (Homing Missile), ulti (Call Down) when available.",
   "ابتدا Q (Rocket Barrage) بعد W (Homing Missile)، اولتی (Call Down) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["templar_assassin","medusa","phantom_lancer","sniper"], 2, 3)

DATA["naga_siren"] = (SUP_INT_RANGE,
  ("Mirror Image to confuse, Ensnare to root, Rip Tide for AoE, Song of the Siren to initiate/disable/escape.",
   "Mirror Image برای گیج، Ensnare برای روت، Rip Tide برای AOE، Song of the Siren برای اینیشیت/دیزیبل/فرار."),
  ("Carry/support: Mirror Image to push/farm, Ensnare to lock, Song to set up fights. Build Diffusal + Manta + BKB.",
   "کری/ساپورت: Mirror Image برای پوش/فارم، Ensnare برای لاک، Song برای درگیری. Diffusal + Manta + BKB بخر."),
  ("Max Q (Mirror Image) then E (Rip Tide), ulti (Song of the Siren) when available.",
   "ابتدا Q (Mirror Image) بعد E (Rip Tide)، اولتی (Song of the Siren) آماده."),
  ["axe","legion_commander","doom_bringer","earthshaker"], ["templar_assassin","medusa","sniper","drow_ranger"], 3, 3)

DATA["arc_warden"] = (None,
  ("Flux to slow, Magnetic Field for evasion/atk speed, Spark Wraith for damage, Tempest Double to double items.",
   "Flux برای کند، Magnetic Field برای ایویژن/سرعت، Spark Wraith برای آسیب، Tempest Double برای دابل آیتم."),
  ("Hard carry: Tempest Double to double items/effects, Magnetic Field for fights. Build Mjollnir + Butterfly + BKB + Scythe.",
   "کری هارد: Tempest Double برای دابل آیتم، Magnetic Field برای درگیری. Mjollnir + Butterfly + BKB + Scythe بخر."),
  ("Max Q (Flux) then W (Magnetic Field), ulti (Tempest Double) when available.",
   "ابتدا Q (Flux) بعد W (Magnetic Field)، اولتی (Tempest Double) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["templar_assassin","medusa","phantom_lancer","sniper"], 3, 3)

DATA["terrorblade"] = (None,
  ("Reflection to slow, Metamorphosis for ranged + damage, Conjure Image for push, Sunder to swap HP.",
   "Reflection برای کند، Metamorphosis برای رنج+آسیب، Conjure Image برای پوش، Sunder برای جابجایی HP."),
  ("Hard carry: Metamorphosis for ranged burst, Conjure Image to push, Sunder to survive. Build Manta + Butterfly + BKB + Skadi.",
   "کری هارد: Metamorphosis برای برست رنج، Conjure Image برای پوش، Sunder برای زنده ماندن. Manta + Butterfly + BKB + Skadi بخر."),
  ("Max Q (Reflection) or E (Conjure Image), ulti (Sunder) when available.",
   "ابتدا Q (Reflection) یا E (Conjure Image)، اولتی (Sunder) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["templar_assassin","medusa","phantom_lancer","sniper"], 3, 2)

DATA["lone_druid"] = (None,
  ("Summon Spirit Bear to tank/push, Rabid for attack speed, Entangling Claws on bear, Savage Roar, True Form for tank.",
   "Summon Spirit Bear برای تانک/پوش، Rabid برای سرعت حمله، Entangling Claws روی خرس، Savage Roar، True Form برای تانک."),
  ("Carry/pusher: Spirit Bear to tank/push, True Form for fights. Build items on both hero + bear (Radiance on bear).",
   "کری/پوشر: Spirit Bear برای تانک/پوش، True Form برای درگیری. آیتم روی هیرو + خرس (Radiance روی خرس)."),
  ("Max Q (Summon Spirit Bear) then W (Rabid), ulti (True Form) when available.",
   "ابتدا Q (Summon Spirit Bear) بعد W (Rabid)، اولتی (True Form) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["templar_assassin","medusa","phantom_lancer","sniper"], 3, 3)

DATA["meepo"] = (None,
  ("Earthbind to root, Poof to teleport+between Meepos, Geostrike slow, Divided We Stand for multiple Meepos.",
   "Earthbind برای روت، Poof برای تلپورت+بین میپوها، Geostrike کند، Divided We Stand برای چند میپو."),
  ("Hard carry (micro): poof all Meepos to one for burst, Earthbind chain, build AGI on all. Build Power Treads + Blink + BKB.",
   "کری هارد (میکرو): همه میپوها را Poof کن برای برست، Earthbind زنجیر، AGI روی همه. Power Treads + Blink + BKB بخر."),
  ("Max E (Poof) then Q (Earthbind), ulti (Divided We Stand) when available.",
   "ابتدا E (Poof) بعد Q (Earthbind)، اولتی (Divided We Stand) آماده."),
  ["axe","legion_commander","doom_bringer","earthshaker"], ["templar_assassin","medusa","sniper","drow_ranger"], 3, 4)

DATA["broodmother"] = (None,
  ("Spawn Spiderlings to push, Spin Web for invis/regen, Incapacitating Bite slow, Insatiable Hunger for lifesteal.",
   "Spawn Spiderlings برای پوش، Spin Web برای اینویس/رهجن، Incapacitating Bite کند، Insatiable Hunger برای لایف‌استیل."),
  ("Carry/pusher: Spin Web for territory, Spiderlings to push, Insatiable Hunger for fights. Build BKB + Butterfly + Skadi.",
   "کری/پوشر: Spin Web برای قلمرو، Spiderlings برای پوش، Insatiable Hunger برای درگیری. BKB + Butterfly + Skadi بخر."),
  ("Max Q (Spawn Spiderlings) then W (Spin Web), ulti (Insatiable Hunger) when available.",
   "ابتدا Q (Spawn Spiderlings) بعد W (Spin Web)، اولتی (Insatiable Hunger) آماده."),
  ["axe","legion_commander","doom_bringer","earthshaker"], ["templar_assassin","medusa","sniper","drow_ranger"], 3, 3)

DATA["viper"] = (SUP_INT_RANGE,
  ("Poison Attack to slow, Nethertoxin for AoE, Corrosive Skin for resistance, Viper Strike for slow burst.",
   "Poison Attack برای کند، Nethertoxin برای AOE، Corrosive Skin برای مقاومت، Viper Strike برای کند برست."),
  ("Carry/anti-carry: Poison Attack to slow, Nethertoxin to break passives, Viper Strike the carry. Build BKB + Butterfly + Skadi.",
   "کری/آنتی‌کری: Poison Attack برای کند، Nethertoxin برای بریک پسو، Viper Strike روی کری. BKB + Butterfly + Skadi بخر."),
  ("Max Q (Poison Attack) then W (Nethertoxin), ulti (Viper Strike) when available.",
   "ابتدا Q (Poison Attack) بعد W (Nethertoxin)، اولتی (Viper Strike) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["templar_assassin","troll_warlord","medusa","luna"], 1, 3)

DATA["kez"] = (None,
  ("Switch stances (Ravager/Reckoning), use abilities per stance, Ember Swift for mobility, right-click with BKB.",
   "سوییچ استنس (Ravager/Reckoning)، ابیلیتی هر استنس، Ember Swift برای موبیلیتی، راست‌کلیک با BKB."),
  ("Carry: master stance switching for combos, BKB for fights. Build Manta + BKB + Butterfly + Skadi.",
   "کری: سوییچ استنس برای کمبو، BKB برای درگیری. Manta + BKB + Butterfly + Skadi بخر."),
  ("Max Q/W/E balanced per stance, ulti when available.",
   "Q/W/E متوازن هر استنس، اولتی آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["templar_assassin","medusa","sniper","drow_ranger"], 3, 3)

DATA["hoodwink"] = (SUP_INT_RANGE,
  ("Acorn Shot for nuke/slow, Bushwhack for stun+armor, Scurry for evasion, Sharpshooter for piercing nuke.",
   "Acorn Shot برای نیوک/کند، Bushwhack برای استان+زره، Scurry برای ایویژن، Sharpshooter برای نیوک پیرس."),
  ("Support/flex: Acorn Shot to poke, Bushwhack to stun, Sharpshooter to pierce. Build Gleipnir + BKB + Scythe.",
   "ساپورت/فلکس: Acorn Shot برای پوک، Bushwhack برای استان، Sharpshooter برای پیرس. Gleipnir + BKB + Scythe بخر."),
  ("Max Q (Acorn Shot) then W (Bushwhack), ulti (Sharpshooter) when available.",
   "ابتدا Q (Acorn Shot) بعد W (Bushwhack)، اولتی (Sharpshooter) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["templar_assassin","medusa","sniper","drow_ranger"], 3, 3)

# ===================== INT MID CASTERS =====================
DATA["storm_spirit"] = (None,
  ("Static Remnant for nuke, Electric Vortex to pull, Overload for bonus, Ball Lightning to zip in/out, burst with mana.",
   "Static Remnant برای نیوک، Electric Vortex برای کشیدن، Overload برای بونوس، Ball Lightning برای جامپ، برست با مانا."),
  ("Mid carry/ganker: Ball Lightning to initiate/pick off, mana pool core, BKB. Build Orchid + Bloodthorn + BKB + Scythe.",
   "مید کری/گنکر: Ball Lightning برای اینیشیت/پیک، پول مانا هسته، BKB. Orchid + Bloodthorn + BKB + Scythe بخر."),
  ("Max Q (Static Remnant) or E (Overload), ulti (Ball Lightning) when available.",
   "ابتدا Q (Static Remnant) یا E (Overload)، اولتی (Ball Lightning) آماده."),
  ["axe","legion_commander","doom_bringer","antimage"], ["templar_assassin","medusa","sniper","drow_ranger"], 3, 2)

DATA["puck"] = (None,
  ("Illusory Orb to nuke/escape, Waning Rift to silence, Phase Shift to dodge, Dream Coil to lock team.",
   "Illusory Orb برای نیوک/فرار، Waning Rift برای سایلنس، Phase Shift برای داج، Dream Coil برای لاک تیم."),
  ("Mid initiator: Illusory Orb for mobility, Phase Shift to dodge, Dream Coil to initiate. Build Blink + BKB + Scythe.",
   "مید اینیشیتور: Illusory Orb برای موبیلیتی، Phase Shift برای داج، Dream Coil برای اینیشیت. Blink + BKB + Scythe بخر."),
  ("Max Q (Illusory Orb) then W (Waning Rift), ulti (Dream Coil) when available.",
   "ابتدا Q (Illusory Orb) بعد W (Waning Rift)، اولتی (Dream Coil) آماده."),
  ["axe","legion_commander","doom_bringer","silencer"], ["templar_assassin","medusa","sniper","drow_ranger"], 3, 2)

DATA["zuus"] = (None,
  ("Arc Lightning to spam, Lightning Bolt to nuke+stun, Static Field for %HP damage, Thundergod's Wrath global nuke.",
   "Arc Lightning برای اسپم، Lightning Bolt برای نیوک+ستان، Static Field برای %HP آسیب، Thundergod's Wrath نیوک جهانی."),
  ("Mid nuker: spam Arc Lightning, Lightning Bolt for burst, Thundergod's Wrath to finish low-HP globally. Build Aghanim's + Refresher + Ethereal.",
   "مید نیوکر: Arc Lightning اسپم، Lightning Bolt برای برست، Thundergod's Wrath جهانی برای کشتن کم‌خون. Aghanim's + Refresher + Ethereal بخر."),
  ("Max Q (Arc Lightning) then W (Lightning Bolt), ulti (Thundergod's Wrath) when available.",
   "ابتدا Q (Arc Lightning) بعد W (Lightning Bolt)، اولتی (Thundergod's Wrath) آماده."),
  ["axe","legion_commander","doom_bringer","antimage"], ["templar_assassin","medusa","sniper","drow_ranger"], 1, 2)

DATA["lina"] = (SUP_INT_RANGE,
  ("Dragon Slave to nuke waves, Light Strike Array to stun, Fiery Soul for attack speed, Laguna Blade for burst.",
   "Dragon Slave برای کلیر ویو، Light Strike Array برای استان، Fiery Soul برای سرعت حمله، Laguna Blade برای برست."),
  ("Mid/support: Light Strike Array to setup, Laguna Blade to burst, Fiery Soul for right-click. Build BKB + Aghanim's + Scythe.",
   "مید/ساپورت: Light Strike Array برای ستاپ، Laguna Blade برای برست، Fiery Soul برای راست‌کلیک. BKB + Aghanim's + Scythe بخر."),
  ("Max Q (Dragon Slave) and W (Light Strike Array), ulti (Laguna Blade) when available.",
   "ابتدا Q (Dragon Slave) و W (Light Strike Array)، اولتی (Laguna Blade) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["templar_assassin","medusa","sniper","drow_ranger"], 3, 2)

DATA["tinker"] = (None,
  ("Laser to blind+nuke, Heat-Seeking Missile for AoE, March of the Machines for push, Rearm to reset all cooldowns.",
   "Laser برای بلیند+نیوک، Heat-Seeking Missile برای AOE، March of the Machines برای پوش، Rearm برای ریست همه CD."),
  ("Mid carry/pusher: Rearm to spam abilities, split-push with March, pick off with Laser+Missile. Build Blink + Aghanim's + Ethereal + BKB.",
   "مید کری/پوشر: Rearm برای اسپم ابیلیتی، پوش با March، پیک با Laser+Missile. Blink + Aghanim's + Ethereal + BKB بخر."),
  ("Max Q (Laser) and W (Heat-Seeking Missile), ulti (Rearm) ASAP at 6.",
   "ابتدا Q (Laser) و W (Heat-Seeking Missile)، اولتی (Rearm) سریع در ۶."),
  ["axe","legion_commander","doom_bringer","slark"], ["templar_assassin","medusa","sniper","drow_ranger"], 3, 3)

DATA["invoker"] = (None,
  ("Cold Snap + Sun Strike combo, Tornado + EMP for mana burn, Chaos Meteor for AoE, Deafening Blast to disarm.",
   "کمبو Cold Snap + Sun Strike، Tornado + EMP برای سوختن مانا، Chaos Meteor برای AOE، Deafening Blast برای دیسرم."),
  ("Mid carry: master Invoke combos, Sun Strike for global kills, BKB for fights. Build Aghanim's + Octarine + BKB + Scythe.",
   "مید کری: کمبو Invoke را یاد بگیر، Sun Strike برای کشتن جهانی، BKB برای درگیری. Aghanim's + Octarine + BKB + Scythe بخر."),
  ("Max Quas/Wex/Exort per build, Invoke whenever available.",
   "Quas/Wex/Exort هر بیلد، Invoke همیشه آماده."),
  ["axe","legion_commander","doom_bringer","silencer"], ["templar_assassin","medusa","sniper","drow_ranger"], 3, 1)

DATA["queenofpain"] = (None,
  ("Shadow Strike to slow+DoT, Blink to engage/escape, Scream of Pain for AoE, Sonic Wave for teamfight nuke.",
   "Shadow Strike برای کند+DoT، Blink برای ورود/فرار، Scream of Pain برای AOE، Sonic Wave برای نیوک درگیری."),
  ("Mid carry: Blink for mobility, Scream for AoE, Sonic Wave for teamfights. Build BKB + Orchid + Scythe.",
   "مید کری: Blink برای موبیلیتی، Scream برای AOE، Sonic Wave برای درگیری. BKB + Orchid + Scythe بخر."),
  ("Max Q (Shadow Strike) then W (Blink), ulti (Sonic Wave) when available.",
   "ابتدا Q (Shadow Strike) بعد W (Blink)، اولتی (Sonic Wave) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["templar_assassin","medusa","sniper","drow_ranger"], 2, 3)

DATA["obsidian_destroyer"] = (None,
  ("Astral Imprisonment to banish+steal INT, Arcane Orb for %mana damage, Sanity's Eclipse for INT-based nuke.",
   "Astral Imprisonment برای بنیش+دزدی INT، Arcane Orb برای %مانا آسیب، Sanity's Eclipse برای نیوک بر اساس INT."),
  ("Mid carry: Arcane Orb for scaling damage, Astral to save/burst, Sanity's Eclipse for AoE. Build BKB + Octarine + Scythe.",
   "مید کری: Arcane Orb برای آسیب اسکیل، Astral برای سیو/برست، Sanity's Eclipse برای AOE. BKB + Octarine + Scythe بخر."),
  ("Max W (Astral Imprisonment) then Q (Arcane Orb), ulti (Sanity's Eclipse) when available.",
   "ابتدا W (Astral Imprisonment) بعد Q (Arcane Orb)، اولتی (Sanity's Eclipse) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["templar_assassin","medusa","sniper","drow_ranger"], 3, 2)

DATA["pugna"] = (SUP_INT_RANGE,
  ("Nether Blast to nuke towers/units, Decrepify to amplify magic, Nether Ward to punish casters, Life Drain for sustain.",
   "Nether Blast برای نیوک تاور/یونیت، Decrepify برای تقویت جادو، Nether Ward برای تنبیه کستر، Life Drain برای پایداری."),
  ("Mid/pusher: Nether Blast to push, Life Drain to sustain, Nether Ward vs casters. Build Aghanim's + BKB + Octarine.",
   "مید/پوشر: Nether Blast برای پوش، Life Drain برای پایداری، Nether Ward علیه کستر. Aghanim's + BKB + Octarine بخر."),
  ("Max Q (Nether Blast) then W (Decrepify), ulti (Life Drain) when available.",
   "ابتدا Q (Nether Blast) بعد W (Decrepify)، اولتی (Life Drain) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["templar_assassin","medusa","sniper","drow_ranger"], 2, 3)

DATA["leshrac"] = (SUP_INT_RANGE,
  ("Split Earth to stun, Diabolic Edict for tower damage, Lightning Storm to slow, Pulse Nova for sustained AoE.",
   "Split Earth برای استان، Diabolic Edict برای آسیب تاور، Lightning Storm برای کند، Pulse Nova برای AOE پایدار."),
  ("Mid/carry: Diabolic Edict to push, Pulse Nova for fights, BKB to channel. Build BKB + Octarine + Bloodthorn.",
   "مید/کری: Diabolic Edict برای پوش، Pulse Nova برای درگیری، BKB برای چنل. BKB + Octarine + Bloodthorn بخر."),
  ("Max Q (Split Earth) then W (Diabolic Edict), ulti (Pulse Nova) when available.",
   "ابتدا Q (Split Earth) بعد W (Diabolic Edict)، اولتی (Pulse Nova) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["templar_assassin","medusa","sniper","drow_ranger"], 2, 3)

DATA["necrolyte"] = (None,
  ("Death Pulse to nuke+heal, Heartstopper Aura for %HP drain, Ghost Shroud for amplify, Reaper's Scythe to execute.",
   "Death Pulse برای نیوک+هیل، Heartstopper Aura برای %HP درین، Ghost Shroud برای تقویت، Reaper's Scythe برای اگزکیوت."),
  ("Carry/nuker: Death Pulse for sustain, Reaper's Scythe to execute, BKB for fights. Build Radiance + BKB + Octarine.",
   "کری/نیوکر: Death Pulse برای پایداری، Reaper's Scythe برای اگزکیوت، BKB برای درگیری. Radiance + BKB + Octarine بخر."),
  ("Max Q (Death Pulse) then W (Heartstopper Aura), ulti (Reaper's Scythe) when available.",
   "ابتدا Q (Death Pulse) بعد W (Heartstopper Aura)، اولتی (Reaper's Scythe) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["templar_assassin","medusa","phantom_lancer","troll_warlord"], 2, 2)

DATA["death_prophet"] = (None,
  ("Crypt Swarm to nuke, Silence to disable, Spirit Siphon for drain, Exorcism for teamfight + tower push.",
   "Crypt Swarm برای نیوک، Silence برای دیزیبل، Spirit Siphon برای درین، Exorcism برای درگیری + پوش تاور."),
  ("Mid/carry: Crypt Swarm to nuke, Exorcism for fights+push, BKB to channel. Build BKB + Octarine + Shiva's.",
   "مید/کری: Crypt Swarm برای نیوک، Exorcism برای درگیری+پوش، BKB برای چنل. BKB + Octarine + Shiva's بخر."),
  ("Max Q (Crypt Swarm) then W (Silence), ulti (Exorcism) when available.",
   "ابتدا Q (Crypt Swarm) بعد W (Silence)، اولتی (Exorcism) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["templar_assassin","medusa","phantom_lancer","troll_warlord"], 2, 3)

DATA["silencer"] = (SUP_SAVE,
  ("Arcane Curse to slow+DoT, Glaives of Wisdom for INT damage, Last Word to silence, Global Silence to shut all casters.",
   "Arcane Curse برای کند+DoT، Glaives of Wisdom برای آسیب INT، Last Word برای سایلنس، Global Silence برای خاموش همه کسترها."),
  ("Carry/support: Glaives for INT-scaling damage, Global Silence to win teamfights, steal INT on kills. Build BKB + Octarine + Scythe.",
   "کری/ساپورت: Glaives برای آسیب INT، Global Silence برای برد درگیری، دزدی INT. BKB + Octarine + Scythe بخر."),
  ("Max Q (Arcane Curse) then W (Glaives of Wisdom), ulti (Global Silence) when available.",
   "ابتدا Q (Arcane Curse) بعد W (Glaives of Wisdom)، اولتی (Global Silence) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["templar_assassin","medusa","storm_spirit","tinker"], 2, 3)

DATA["void_spirit"] = (None,
  ("Aether Remnant to stun, Dissimilate to dodge+nuke, Resonant Pulse for shield, Astral Step for burst+mobility.",
   "Aether Remnant برای استان، Dissimilate برای داج+نیوک، Resonant Pulse برای شیلد، Astral Step برای برست+موبیلیتی."),
  ("Mid carry: Astral Step for mobility/burst, Resonant Pulse for shield, BKB for fights. Build BKB + Maelstrom + Bloodthorn.",
   "مید کری: Astral Step برای موبیلیتی/برست، Resonant Pulse برای شیلد، BKB برای درگیری. BKB + Maelstrom + Bloodthorn بخر."),
  ("Max Q (Aether Remnant) then E (Resonant Pulse), ulti (Astral Step) when available.",
   "ابتدا Q (Aether Remnant) بعد E (Resonant Pulse)، اولتی (Astral Step) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["templar_assassin","medusa","sniper","drow_ranger"], 3, 2)

# ===================== STR OFFLANE TANKS =====================
DATA["sven"] = (None,
  ("Storm Hammer to stun, Warcry for armor+speed, Great Cleave for farm, God's Strength for massive right-click.",
   "Storm Hammer برای استان، Warcry برای زره+سرعت، Great Cleave برای فارم، God's Strength برای راست‌کلیک بزرگ."),
  ("Carry/initiator: farm with Great Cleave, Storm Hammer to initiate, God's Strength + BKB for burst. Build Blink + BKB + Satanic + Daedalus.",
   "کری/اینیشیتور: با Great Cleave فارم، Storm Hammer برای اینیشیت، God's Strength + BKB برای برست. Blink + BKB + Satanic + Daedalus بخر."),
  ("Max Q (Storm Hammer) then W (Warcry), ulti (God's Strength) when available.",
   "ابتدا Q (Storm Hammer) بعد W (Warcry)، اولتی (God's Strength) آماده."),
  ["viper","drow_ranger","sniper","lina"], ["phantom_assassin","juggernaut","troll_warlord","life_stealer"], 2, 2)

DATA["tiny"] = (None,
  ("Avalanche to stun, Toss to throw enemy/ally, Craggy Exterior for counter-stun, Grow for damage, Tree Grab for splash.",
   "Avalanche برای استان، Toss برای پرت کردن دشمن/الی، Cragy Exterior برای کانتر-ستان، Grow برای آسیب، Tree Grab برای اسپلش."),
  ("Carry/initiator: Avalanche+Toss combo for burst, Blink to initiate, Grow for damage. Build Blink + BKB + Assault + Daedalus.",
   "کری/اینیشیتور: کمبو Avalanche+Toss برای برست، Blink برای اینیشیت، Grow برای آسیب. Blink + BKB + Assault + Daedalus بخر."),
  ("Max Q (Avalanche) and W (Toss), ulti (Grow) when available.",
   "ابتدا Q (Avalanche) و W (Toss)، اولتی (Grow) آماده."),
  ["viper","drow_ranger","sniper","lina"], ["phantom_assassin","juggernaut","troll_warlord","life_stealer"], 2, 2)

DATA["kunkka"] = (SUP_INT_AGGRO,
  ("Torrent to knock up, Tidebringer for cleave, X Marks the Spot to return, Ghostship for stun+rum buff.",
   "Torrent برای ناک‌آپ، Tidebringer برای کلیو، X Marks the Spot برای برگردان، Ghostship برای استان+باف رام."),
  ("Carry/initiator: Tidebringer for cleave burst, X+Torrent combo, Ghostship for fights. Build Daedalus + BKB + Assault.",
   "کری/اینیشیتور: Tidebringer برای کلیو برست، کمبو X+Torrent، Ghostship برای درگیری. Daedalus + BKB + Assault بخر."),
  ("Max W (Tidebringer) then Q (Torrent), ulti (Ghostship) when available.",
   "ابتدا W (Tidebringer) بعد Q (Torrent)، اولتی (Ghostship) آماده."),
  ["viper","drow_ranger","sniper","lina"], ["phantom_assassin","juggernaut","troll_warlord","life_stealer"], 3, 3)

DATA["slardar"] = (None,
  ("Slithereen Crush to stun+slow, Corrosive Haze for armor reduction, Guardian Sprint for chase, right-click with BKB.",
   "Slithereen Crush برای استان+کند، Corrosive Haze برای کاهش زره، Guardian Sprint برای تعقیب، راست‌کلیک با BKB."),
  ("Offlane/initiator: Corrosive Haze to shred armor, Slithereen Crush to stun, Blink to initiate. Build Blink + BKB + Assault + Vanguard.",
   "آفلین/اینیشیتور: Corrosive Haze برای کاهش زره، Slithereen Crush برای استان، Blink برای اینیشیت. Blink + BKB + Assault + Vanguard بخر."),
  ("Max Q (Slithereen Crush) then W (Corrosive Haze), ulti (Guardian Sprint) when available.",
   "ابتدا Q (Slithereen Crush) بعد W (Corrosive Haze)، اولتی (Guardian Sprint) آماده."),
  ["viper","drow_ranger","sniper","lina"], ["templar_assassin","medusa","phantom_lancer","troll_warlord"], 2, 3)

DATA["tidehunter"] = (None,
  ("Gush to slow+armor reduction, Kraken Shell to purge, Anchor Smash for AoE, Ravage for teamfight stun.",
   "Gush برای کند+کاهش زره، Kraken Shell برای پورج، Anchor Smash برای AOE، Ravage برای استان تیمی."),
  ("Offlane/initiator: Ravage to win teamfights, Kraken Shell to tank, Blink to initiate. Build Blink + BKB + Refresher + Shiva's.",
   "آفلین/اینیشیتور: Ravage برای برد درگیری، Kraken Shell برای تانک، Blink برای اینیشیت. Blink + BKB + Refresher + Shiva's بخر."),
  ("Max Q (Gush) then E (Anchor Smash), ulti (Ravage) when available.",
   "ابتدا Q (Gush) بعد E (Anchor Smash)، اولتی (Ravage) آماده."),
  ["viper","drow_ranger","sniper","lina"], ["phantom_assassin","juggernaut","troll_warlord","life_stealer"], 1, 2)

DATA["beastmaster"] = (None,
  ("Wild Axes to nuke+armor reduction, Call of the Wild boar (slow) + hawk (vision), Primal Roar for single-target stun.",
   "Wild Axes برای نیوک+کاهش زره، Call of the Wild بور (کند) + هاک (ویژن)، Primal Roar برای استان تک‌هدف."),
  ("Offlane/initiator: Primal Roar to lock carry, pets for vision/slow, BKB for fights. Build Blink + BKB + Assault + Necronomicon.",
   "آفلین/اینیشیتور: Primal Roar برای لاک کری، پت برای ویژن/کند، BKB برای درگیری. Blink + BKB + Assault + Necronomicon بخر."),
  ("Max Q (Wild Axes) then W (Call of the Wild), ulti (Primal Roar) when available.",
   "ابتدا Q (Wild Axes) بعد W (Call of the Wild)، اولتی (Primal Roar) آماده."),
  ["viper","drow_ranger","sniper","lina"], ["phantom_assassin","juggernaut","troll_warlord","life_stealer"], 2, 3)

DATA["doom_bringer"] = (None,
  ("Devour to farm, Scorched Earth for chase+heal, Infernal Blade for %HP burn, Doom to silence+mute one hero.",
   "Devour برای فارم، Scorched Earth برای تعقیب+هیل، Infernal Blade برای %HP برن، Doom برای سایلنس+میوت یک هیرو."),
  ("Offlane/carry: Devour to farm fast, Doom to shut enemy carry, BKB for fights. Build Blink + BKB + Shiva's + Assault.",
   "آفلین/کری: Devour برای فارم سریع، Doom برای خاموش کری دشمن، BKB برای درگیری. Blink + BKB + Shiva's + Assault بخر."),
  ("Max Q (Devour) then W (Scorched Earth), ulti (Doom) when available.",
   "ابتدا Q (Devour) بعد W (Scorched Earth)، اولتی (Doom) آماده."),
  ["viper","drow_ranger","sniper","lina"], ["antimage","storm_spirit","tinker","invoker"], 1, 2)

DATA["life_stealer"] = (None,
  ("Feast for lifesteal+%HP, Open Wounds to slow, Rage for magic immunity, Infest to hide in creep/ally.",
   "Feast برای لایف‌استیل+%HP، Open Wounds برای کند، Rage برای ایمونی جادویی، Infest برای پنهان در کریپ/الی."),
  ("Carry: Feast for sustain vs tanks, Rage for BKB, Infest to engage. Build Desolator + BKB + Assault + Satanic.",
   "کری: Feast برای پایداری علیه تانک، Rage برای BKB، Infest برای ورود. Desolator + BKB + Assault + Satanic بخر."),
  ("Max Q (Feast) then W (Open Wounds), ulti (Infest) when available.",
   "ابتدا Q (Feast) بعد W (Open Wounds)، اولتی (Infest) آماده."),
  ["viper","drow_ranger","sniper","lina"], ["axe","bristleback","centaur","tidehunter"], 2, 2)

DATA["dragon_knight"] = (None,
  ("Breathe Fire to nuke+reduce damage, Dragon Tail to stun, Dragon Blood for regen+armor, Elder Dragon Form for ranged AoE.",
   "Breathe Fire برای نیوک+کاهش آسیب، Dragon Tail برای استان، Dragon Blood برای رجن+زره، Elder Dragon Form برای رنج AOE."),
  ("Carry/pusher: Dragon Blood for lane sustain, Elder Dragon Form to push/fight, BKB for fights. Build BKB + Maelstrom + Assault + Heart.",
   "کری/پوشر: Dragon Blood برای پایداری لین، Elder Dragon Form برای پوش/درگیری، BKB برای درگیری. BKB + Maelstrom + Assault + Heart بخر."),
  ("Max Q (Breathe Fire) then E (Dragon Blood), ulti (Elder Dragon Form) when available.",
   "ابتدا Q (Breathe Fire) بعد E (Dragon Blood)، اولتی (Elder Dragon Form) آماده."),
  ["viper","drow_ranger","sniper","lina"], ["templar_assassin","medusa","phantom_lancer","troll_warlord"], 1, 3)

DATA["huskar"] = (None,
  ("Inner Vitality to heal, Burning Spear for DoT, Berserker's Blood for attack speed at low HP, Life Break to engage+slow.",
   "Inner Vitality برای هیل، Burning Spear برای DoT، Berserker's Blood برای سرعت در HP کم، Life Break برای ورود+کند."),
  ("Carry/initiator: Life Break to engage, Berserker's Blood for damage at low HP, Armlet for sustain. Build Armlet + BKB + Satanic + Halberd.",
   "کری/اینیشیتور: Life Break برای ورود، Berserker's Blood برای آسیب در HP کم، Armlet برای پایداری. Armlet + BKB + Satanic + Halberd بخر."),
  ("Max Q (Inner Vitality) or W (Burning Spears), ulti (Life Break) when available.",
   "ابتدا Q (Inner Vitality) یا W (Burning Spears)، اولتی (Life Break) آماده."),
  ["ancient_apparition","lina","zuus","slark"], ["axe","bristleback","centaur","tidehunter"], 2, 3)

DATA["night_stalker"] = (None,
  ("Void to slow+stun, Crippling Fear to silence, Hunter in the Night for night bonuses, Dark Ascension for flying+damage.",
   "Void برای کند+ستان، Crippling Fear برای سایلنس، Hunter in the Night برای بونوس شب، Dark Ascension برای پرواز+آسیب."),
  ("Carry/initiator: dominate at night, Void to slow, Dark Ascension for fights. Build BKB + Assault + Halberd + Heart.",
   "کری/اینیشیتور: در شب مسلط شو، Void برای کند، Dark Ascension برای درگیری. BKB + Assault + Halberd + Heart بخر."),
  ("Max Q (Void) then W (Crippling Fear), ulti (Dark Ascension) when available.",
   "ابتدا Q (Void) بعد W (Crippling Fear)، اولتی (Dark Ascension) آماده."),
  ["viper","drow_ranger","sniper","lina"], ["templar_assassin","medusa","phantom_lancer","troll_warlord"], 2, 3)

DATA["spirit_breaker"] = (None,
  ("Charge of Darkness to globally gank, Bulldoze for magic resist+speed, Greater Bash on hits, Nether Strike for big knockback.",
   "Charge of Darkness برای گنک جهانی، Bulldoze برای مقاومت جادویی+سرعت، Greater Bash روی ضربات، Nether Strike برای ناک‌بک بزرگ."),
  ("Offlane/ganker: Charge to pick off, Bulldoze to tank, Nether Strike to lock. Build BKB + Assault + Heart + Halberd.",
   "آفلین/گنکر: Charge برای پیک، Bulldoze برای تانک، Nether Strike برای لاک. BKB + Assault + Heart + Halberd بخر."),
  ("Max W (Bulldoze) then E (Greater Bash), ulti (Nether Strike) when available.",
   "ابتدا W (Bulldoze) بعد E (Greater Bash)، اولتی (Nether Strike) آماده."),
  ["viper","drow_ranger","sniper","lina"], ["antimage","storm_spirit","tinker","weaver"], 1, 3)

DATA["centaur"] = (None,
  ("Hoof Stomp to stun, Double Edge for nuke, Retaliate for counter-damage, Stampede for team-wide speed+escape.",
   "Hoof Stomp برای استان، Double Edge برای نیوک، Retaliate برای کانتر-آسیب، Stampede برای سرعت تیمی+فرار."),
  ("Offlane/initiator: Hoof Stomp to stun, Retaliate to tank damage, Stampede to save team. Build Blink + BKB + Heart + Assault.",
   "آفلین/اینیشیتور: Hoof Stomp برای استان، Retaliate برای تانک آسیب، Stampede برای سیو تیم. Blink + BKB + Heart + Assault بخر."),
  ("Max Q (Hoof Stomp) then E (Retaliate), ulti (Stampede) when available.",
   "ابتدا Q (Hoof Stomp) بعد E (Retaliate)، اولتی (Stampede) آماده."),
  ["viper","drow_ranger","sniper","lina"], ["phantom_assassin","juggernaut","troll_warlord","life_stealer"], 1, 2)

DATA["magnataur"] = (None,
  ("Shockwave to nuke, Empower for cleave, Skewer to reposition enemies, Reverse Polarity to group+stun team.",
   "Shockwave برای نیوک، Empower برای کلیو، Skewer برای جابجایی دشمن، Reverse Polarity برای گروه+استان تیم."),
  ("Offlane/initiator: Reverse Polarity to set up teamfights, Skewer to reposition, BKB. Build Blink + BKB + Assault + Refresher.",
   "آفلین/اینیشیتور: Reverse Polarity برای ستاپ درگیری، Skewer برای جابجایی، BKB. Blink + BKB + Assault + Refresher بخر."),
  ("Max Q (Shockwave) then E (Empower), ulti (Reverse Polarity) when available.",
   "ابتدا Q (Shockwave) بعد E (Empower)، اولتی (Reverse Polarity) آماده."),
  ["viper","drow_ranger","sniper","lina"], ["phantom_assassin","juggernaut","troll_warlord","life_stealer"], 3, 2)

DATA["shredder"] = (None,
  ("Whirling Death to nuke+stat reduction, Timber Chain to mobility+damage, Reactive Armor for stacks, Chakram for AoE slow.",
   "Whirling Death برای نیوک+کاهش استت، Timber Chain برای موبیلیتی+آسیب، Reactive Armor برای استک، Chakram برای AOE کند."),
  ("Offlane/initiator: Timber Chain for mobility, Reactive Armor to tank, Chakram for fights. Build Bloodstone + BKB + Shiva's.",
   "آفلین/اینیشیتور: Timber Chain برای موبیلیتی، Reactive Armor برای تانک، Chakram برای درگیری. Bloodstone + BKB + Shiva's بخر."),
  ("Max W (Timber Chain) then Q (Whirling Death), ulti (Chakram) when available.",
   "ابتدا W (Timber Chain) بعد Q (Whirling Death)، اولتی (Chakram) آماده."),
  ["viper","drow_ranger","sniper","lina"], ["phantom_assassin","juggernaut","troll_warlord","life_stealer"], 2, 3)

DATA["bristleback"] = (None,
  ("Quill Spray to stack damage, Viscous Nasal Goo for slow+armor reduction, Bristleback for rear damage reduction, Warpath stacks.",
   "Quill Spray برای استک آسیب، Viscous Nasal Goo برای کند+کاهش زره، Bristleback برای کاهش آسیب پشت، Warpath استک."),
  ("Carry/offlane: tank from behind, Quill Spray to stack, Warpath for damage. Build Vanguard + Radiance + BKB + Assault + Heart.",
   "کری/آفلین: از پشت تانک کن، Quill Spray برای استک، Warpath برای آسیب. Vanguard + Radiance + BKB + Assault + Heart بخر."),
  ("Max Q (Quill Spray) then W (Viscous Nasal Goo), ulti (Warpath) when available.",
   "ابتدا Q (Quill Spray) بعد W (Viscous Nasal Goo)، اولتی (Warpath) آماده."),
  ["ancient_apparition","lina","zuus","slark"], ["axe","tidehunter","centaur","life_stealer"], 1, 2)

DATA["rattletrap"] = (None,
  ("Battery Assault for AoE ministun, Power Cogs for trap+mana burn, Rocket Flare for nuke+vision, Hookshot to initiate.",
   "Battery Assault برای AOE مینی‌استان، Power Cogs برای تله+سوزن مانا، Rocket Flare برای نیوک+ویژن، Hookshot برای اینیشیت."),
  ("Offlane/initiator: Hookshot to initiate, Battery Assault to lock, Cogs to trap. Build Blink + BKB + Blademail + Assault.",
   "آفلین/اینیشیتور: Hookshot برای اینیشیت، Battery Assault برای لاک، Cogs برای تله. Blink + BKB + Blademail + Assault بخر."),
  ("Max Q (Battery Assault) then W (Power Cogs), ulti (Hookshot) when available.",
   "ابتدا Q (Battery Assault) بعد W (Power Cogs)، اولتی (Hookshot) آماده."),
  ["viper","drow_ranger","sniper","lina"], ["phantom_assassin","juggernaut","troll_warlord","life_stealer"], 2, 3)

DATA["legion_commander"] = (None,
  ("Overwhelming Odds for AoE, Press the Attack for heal+attack speed, Moment of Courage for counter-lifesteal, Duel to win damage.",
   "Overwhelming Odds برای AOE، Press the Attack برای هیل+سرعت، Moment of Courage برای کانتر-لایف‌استیل، Duel برای برد آسیب."),
  ("Offlane/carry: Blink+Duel to win damage, Press the Attack to sustain, BKB to avoid interrupts. Build Blink + BKB + Assault + Blademail.",
   "آفلین/کری: Blink+Duel برای برد آسیب، Press the Attack برای پایداری، BKB برای فرار وقفه. Blink + BKB + Assault + Blademail بخر."),
  ("Max W (Press the Attack) then E (Moment of Courage), ulti (Duel) when available.",
   "ابتدا W (Press the Attack) بعد E (Moment of Courage)، اولتی (Duel) آماده."),
  ["viper","drow_ranger","sniper","lina"], ["antimage","storm_spirit","tinker","weaver"], 2, 3)

DATA["elder_titan"] = (None,
  ("Echo Stomp to sleep, Astral Spirit for nuke+buff, Natural Order for armor/magic reduction, Earth Splitter for AoE.",
   "Echo Stomp برای خواب، Astral Spirit برای نیوک+باف، Natural Order برای کاهش زره/جادو، Earth Splitter برای AOE."),
  ("Offlane/initiator: Echo Stomp to setup, Natural Order to shred, Earth Splitter for fights. Build Blink + BKB + Refresher + Shiva's.",
   "آفلین/اینیشیتور: Echo Stomp برای ستاپ، Natural Order برای کاهش، Earth Splitter برای درگیری. Blink + BKB + Refresher + Shiva's بخر."),
  ("Max Q (Echo Stomp) then W (Astral Spirit), ulti (Earth Splitter) when available.",
   "ابتدا Q (Echo Stomp) بعد W (Astral Spirit)، اولتی (Earth Splitter) آماده."),
  ["viper","drow_ranger","sniper","lina"], ["templar_assassin","medusa","phantom_lancer","troll_warlord"], 3, 3)

DATA["abyssal_underlord"] = (None,
  ("Firestorm for AoE, Pit of Malice to root, Atrophy Aura for enemy damage reduction, Fiend's Gate for teleport.",
   "Firestorm برای AOE، Pit of Malice برای روت، Atrophy Aura برای کاهش آسیب دشمن، Fiend's Gate برای تلپورت."),
  ("Offlane/tank: Firestorm to push, Pit of Malice to root, Fiend's Gate for mobility. Build Vanguard + BKB + Shiva's + Heart + Assault.",
   "آفلین/تانک: Firestorm برای پوش، Pit of Malice برای روت، Fiend's Gate برای موبیلیتی. Vanguard + BKB + Shiva's + Heart + Assault بخر."),
  ("Max Q (Firestorm) then W (Pit of Malice), ulti (Fiend's Gate) when available.",
   "ابتدا Q (Firestorm) بعد W (Pit of Malice)، اولتی (Fiend's Gate) آماده."),
  ["viper","drow_ranger","sniper","lina"], ["templar_assassin","medusa","phantom_lancer","troll_warlord"], 2, 3)

DATA["tusk"] = (SUP_STR_MELEE,
  ("Ice Shards to trap, Snowball to engage+invuln, Tag Team for ally buff, Walrus PUNCH! for big crit knockback.",
   "Ice Shards برای تله، Snowball برای ورود+ایون، Tag Team برای باف الی، Walrus PUNCH! برای کرت بزرگ ناک‌بک."),
  ("Offlane/initiator: Snowball to engage, Walrus PUNCH! to launch, BKB for fights. Build Blink + BKB + Assault + Heart.",
   "آفلین/اینیشیتور: Snowball برای ورود، Walrus PUNCH! برای پرتاب، BKB برای درگیری. Blink + BKB + Assault + Heart بخر."),
  ("Max Q (Ice Shards) then W (Snowball), ulti (Walrus PUNCH!) when available.",
   "ابتدا Q (Ice Shards) بعد W (Snowball)، اولتی (Walrus PUNCH!) آماده."),
  ["viper","drow_ranger","sniper","lina"], ["phantom_assassin","juggernaut","troll_warlord","life_stealer"], 2, 3)

DATA["brewmaster"] = (None,
  ("Thunder Clap for AoE slow, Cinder Brew for burn+break, Drunken Brawler for evasion, Primal Split for 3 spirits.",
   "Thunder Clap برای AOE کند، Cinder Brew برای برن+بریک، Drunken Brawler برای ایویژن، Primal Split برای ۳ روح."),
  ("Offlane/initiator: Primal Split for teamfight control, Thunder Clap to slow, BKB. Build Blink + BKB + Assault + Aghanim's.",
   "آفلین/اینیشیتور: Primal Split برای کنترل درگیری، Thunder Clap برای کند، BKB. Blink + BKB + Assault + Aghanim's بخر."),
  ("Max Q (Thunder Clap) then W (Cinder Brew), ulti (Primal Split) when available.",
   "ابتدا Q (Thunder Clap) بعد W (Cinder Brew)، اولتی (Primal Split) آماده."),
  ["viper","drow_ranger","sniper","lina"], ["phantom_assassin","juggernaut","troll_warlord","life_stealer"], 3, 3)

DATA["mars"] = (None,
  ("Spear of Mars to pin to wall, God's Rebuke for cone damage, Bulwark for frontal block, Arena of Blood for teamfight trap.",
   "Spear of Mars برای پین به دیوار، God's Rebuke برای آسیب مخروطی، Bulwark برای بلاک جلو، Arena of Blood برای تله درگیری."),
  ("Offlane/initiator: Arena of Blood to trap team, Spear to pin, Bulwark to tank. Build Blink + BKB + Assault + Black King Bar.",
   "آفلین/اینیشیتور: Arena of Blood برای تله تیم، Spear برای پین، Bulwark برای تانک. Blink + BKB + Assault + Black King Bar بخر."),
  ("Max Q (Spear of Mars) then W (God's Rebuke), ulti (Arena of Blood) when available.",
   "ابتدا Q (Spear of Mars) بعد W (God's Rebuke)، اولتی (Arena of Blood) آماده."),
  ["viper","drow_ranger","sniper","lina"], ["phantom_assassin","juggernaut","troll_warlord","life_stealer"], 2, 2)

DATA["dawnbreaker"] = (None,
  ("Starbreaker for stun+catch, Celestial Hammer for nuke+slow, Luminosity for heal, Solar Guardian for global heal+stun.",
   "Starbreaker برای استان+کچ، Celestial Hammer برای نیوک+کند، Luminosity برای هیل، Solar Guardian برای هیل جهانی+استان."),
  ("Carry/initiator: Starbreaker to engage, Luminosity to heal team, Solar Guardian to join fights globally. Build BKB + Assault + Heart + BKB.",
   "کری/اینیشیتور: Starbreaker برای ورود، Luminosity برای هیل تیم، Solar Guardian برای ورود جهانی. BKB + Assault + Heart + BKB بخر."),
  ("Max Q (Starbreaker) then W (Celestial Hammer), ulti (Solar Guardian) when available.",
   "ابتدا Q (Starbreaker) بعد W (Celestial Hammer)، اولتی (Solar Guardian) آماده."),
  ["viper","drow_ranger","sniper","lina"], ["phantom_assassin","juggernaut","troll_warlord","life_stealer"], 2, 3)

DATA["primal_beast"] = (None,
  ("Onslaught to charge, Uproar for stacks, Trample for AoE, Pulverize for single-target lock+damage.",
   "Onslaught برای شارژ، Uproar برای استک، Trample برای AOE، Pulverize برای لاک تک‌هدف+آسیب."),
  ("Offlane/initiator: Trample for AoE, Pulverize to lock carry, BKB for fights. Build Blink + BKB + Assault + Heart.",
   "آفلین/اینیشیتور: Trample برای AOE، Pulverize برای لاک کری، BKB برای درگیری. Blink + BKB + Assault + Heart بخر."),
  ("Max Q (Onslaught) then W (Uproar), ulti (Pulverize) when available.",
   "ابتدا Q (Onslaught) بعد W (Uproar)، اولتی (Pulverize) آماده."),
  ["viper","drow_ranger","sniper","lina"], ["phantom_assassin","juggernaut","troll_warlord","life_stealer"], 3, 3)

DATA["largo"] = (SUP_STR_MELEE,
  ("Initiate with Blink, lockdown enemy carry, soak damage, peel for carries. Use ulti to disrupt teamfights.",
   "با Blink اینیشیت کن، کری دشمن را لاک‌داون کن، آسیب جذب کن، برای کری‌ها پیل کن. اولتی برای اختلال درگیری."),
  ("Offlane/support: survive, get levels. Build tanky + blink. Initiate fights, soak spells, lockdown enemy carries.",
   "آفلین/ساپورت: زنده بمان، لول بگیر. تانک + بلینک بخر. درگیری را اینیشیت کن، طلسم جذب کن، کری دشمن را لاک‌داون."),
  ("Max initiate/disable skill, then durability skill, ulti when available.",
   "ابتدا اسیل اینیشیت/دیزیبل را ماکس کن، بعد دوام، اولتی آماده."),
  ["viper","drow_ranger","sniper","lina"], ["phantom_assassin","juggernaut","troll_warlord","life_stealer"], 2, 3)

# ===================== INT SUPPORTS (pos 4/5) =====================
DATA["crystal_maiden"] = (SUP_INT_RANGE,
  ("Crystal Nova to slow AoE, Frostbite to root+nuke, Arcane Aura for mana regen, Freezing Field for teamfight AoE.",
   "Crystal Nova برای کند AOE، Frostbite برای روت+نیوک، Arcane Aura برای رجن مانا، Freezing Field برای AOE درگیری."),
  ("Pos 5 support: Crystal Nova to slow, Frostbite to lock, Freezing Field in fights with BKB/Glimmer. Build Glimmer + Force + Greaves.",
   "ساپورت پوز ۵: Crystal Nova برای کند، Frostbite برای لاک، Freezing Field در درگیری با BKB/Glimmer. Glimmer + Force + Greaves بخر."),
  ("Max Q (Crystal Nova) and W (Frostbite), ulti (Freezing Field) when available.",
   "ابتدا Q (Crystal Nova) و W (Frostbite)، اولتی (Freezing Field) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["antimage","storm_spirit","tinker","weaver"], 1, 3)

DATA["lion"] = (SUP_INT_AGGRO,
  ("Earth Spike to stun, Mana Drain to sustain, Hex to disable, Finger of Death for huge burst nuke.",
   "Earth Spike برای استان، Mana Drain برای پایداری، Hex برای دیزیبل، Finger of Death برای برست نیوک بزرگ."),
  ("Pos 4/5 support: Earth Spike + Hex for chain disable, Finger of Death to burst, Blink to initiate. Build Blink + Glimmer + Force + Aghanim's.",
   "ساپورت پوز ۴/۵: Earth Spike + Hex برای چین دیزیبل، Finger of Death برای برست، Blink برای اینیشیت. Blink + Glimmer + Force + Aghanim's بخر."),
  ("Max Q (Earth Spike) then W (Hex), ulti (Finger of Death) when available.",
   "ابتدا Q (Earth Spike) بعد W (Hex)، اولتی (Finger of Death) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["antimage","storm_spirit","tinker","weaver"], 2, 2)

DATA["shadow_shaman"] = (SUP_INT_AGGRO,
  ("Ether Shock to nuke, Hex to disable, Shackles to channel-root, Mass Serpent Wards for push+lockdown.",
   "Ether Shock برای نیوک، Hex برای دیزیبل، Shackles برای چنل-روت، Mass Serpent Wards برای پوش+لاک‌داون."),
  ("Pos 4/5 support: Hex + Shackles for chain disable, Mass Serpent Wards to push/lock, Blink to initiate. Build Blink + Glimmer + Aghanim's + Refresher.",
   "ساپورت پوز ۴/۵: Hex + Shackles برای چین دیزیبل، Mass Serpent Wards برای پوش/لاک، Blink برای اینیشیت. Blink + Glimmer + Aghanim's + Refresher بخر."),
  ("Max W (Hex) then Q (Ether Shock), ulti (Mass Serpent Wards) when available.",
   "ابتدا W (Hex) بعد Q (Ether Shock)، اولتی (Mass Serpent Wards) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["antimage","storm_spirit","tinker","weaver"], 2, 2)

DATA["earthshaker"] = (SUP_STR_MELEE,
  ("Fissure to stun+wall, Enchant Totem for leap+damage, Aftershock for aftershock stuns, Echo Slam for AoE nuke.",
   "Fissure برای استان+دیوار، Enchant Totem برای لیپ+آسیب، Aftershock برای استان بعدی، Echo Slam برای AOE نیوک."),
  ("Pos 4 support/initiator: Fissure to wall, Echo Slam for teamfights vs illusions, Blink to initiate. Build Blink + BKB + Shiva's + Aghanim's.",
   "ساپورت پوز ۴/اینیشیتور: Fissure برای دیوار، Echo Slam برای درگیری علیه ایلوژن، Blink برای اینیشیت. Blink + BKB + Shiva's + Aghanim's بخر."),
  ("Max Q (Fissure) then E (Aftershock), ulti (Echo Slam) when available.",
   "ابتدا Q (Fissure) بعد E (Aftershock)، اولتی (Echo Slam) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["phantom_lancer","meepo","broodmother","naga_siren"], 2, 2)

DATA["bane"] = (SUP_SAVE,
  ("Enfeeble to reduce damage, Brain Sap to nuke+heal, Nightmare to disable, Fiend's Grip for channel disable.",
   "Enfeeble برای کاهش آسیب، Brain Sap برای نیوک+هیل، Nightmare برای دیزیبل، Fiend's Grip برای چنل دیزیبل."),
  ("Pos 5 support: Enfeeble the carry, Fiend's Grip to lock, BKB/Glimmer to channel. Build Glimmer + Force + Aghanim's + BKB.",
   "ساپورت پوز ۵: Enfeeble روی کری، Fiend's Grip برای لاک، BKB/Glimmer برای چنل. Glimmer + Force + Aghanim's + BKB بخر."),
  ("Max W (Brain Sap) then Q (Enfeeble), ulti (Fiend's Grip) when available.",
   "ابتدا W (Brain Sap) بعد Q (Enfeeble)، اولتی (Fiend's Grip) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["antimage","storm_spirit","tinker","weaver"], 3, 3)

DATA["lich"] = (SUP_INT_RANGE,
  ("Frost Blast for AoE nuke, Frost Shield for ally protection, Sinister Gaze for disable, Chain Frost for bouncing nuke.",
   "Frost Blast برای AOE نیوک، Frost Shield برای محافظت الی، Sinister Gaze برای دیزیبل، Chain Frost برای نیوک پرشی."),
  ("Pos 5 support: Frost Shield to save carry, Chain Frost in fights, Frost Blast to nuke. Build Glimmer + Force + Greaves + Aghanim's.",
   "ساپورت پوز ۵: Frost Shield برای سیو کری، Chain Frost در درگیری، Frost Blast برای نیوک. Glimmer + Force + Greaves + Aghanim's بخر."),
  ("Max Q (Frost Blast) then W (Frost Shield), ulti (Chain Frost) when available.",
   "ابتدا Q (Frost Blast) بعد W (Frost Shield)، اولتی (Chain Frost) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["phantom_lancer","meepo","broodmother","naga_siren"], 1, 2)

DATA["witch_doctor"] = (SUP_INT_RANGE,
  ("Paralyzing Cask to bounce stun, Voodoo Restoration for heal, Maledict for DoT, Death Ward for channel burst.",
   "Paralyzing Cask برای استان پرشی، Voodoo Restoration برای هیل، Maledict برای DoT، Death Ward برای چنل برست."),
  ("Pos 4/5 support: Paralyzing Cask for chain stun, Death Ward with BKB/Glimmer, Maledict to finish. Build Glimmer + BKB + Aghanim's.",
   "ساپورت پوز ۴/۵: Paralyzing Cask برای چین استان، Death Ward با BKB/Glimmer، Maledict برای کشتن. Glimmer + BKB + Aghanim's بخر."),
  ("Max Q (Paralyzing Cask) then W (Voodoo Restoration), ulti (Death Ward) when available.",
   "ابتدا Q (Paralyzing Cask) بعد W (Voodoo Restoration)، اولتی (Death Ward) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["antimage","storm_spirit","tinker","weaver"], 2, 2)

DATA["warlock"] = (SUP_INT_RANGE,
  ("Fatal Bonds to link damage, Shadow Word for heal/damage, Upheaval for slow, Chaotic Offering for golem+stun.",
   "Fatal Bonds برای پیوند آسیب، Shadow Word برای هیل/آسیب، Upheaval برای کند، Chaotic Offering برای گولم+استان."),
  ("Pos 5 support: Fatal Bonds to amplify, Chaotic Offering for teamfight golem, Shadow Word to save. Build Glimmer + Refresher + Aghanim's.",
   "ساپورت پوز ۵: Fatal Bonds برای تقویت، Chaotic Offering برای گولم درگیری، Shadow Word برای سیو. Glimmer + Refresher + Aghanim's بخر."),
  ("Max W (Shadow Word) then Q (Fatal Bonds), ulti (Chaotic Offering) when available.",
   "ابتدا W (Shadow Word) بعد Q (Fatal Bonds)، اولتی (Chaotic Offering) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["phantom_lancer","meepo","broodmother","naga_siren"], 2, 2)

DATA["dazzle"] = (SUP_SAVE,
  ("Poison Touch for slow+DoT, Shallow Grave to prevent death, Shadow Wave for heal+nuke, Bad Juju for armor+cooldown.",
   "Poison Touch برای کند+DoT، Shallow Grave برای جلوگیری مرگ، Shadow Wave برای هیل+نیوک، Bad Juju برای زره+کوول‌داون."),
  ("Pos 4/5 support: Shallow Grave to save, Shadow Wave to heal, Poison Touch to slow. Build Glimmer + Force + Aghanim's + Solar Crest.",
   "ساپورت پوز ۴/۵: Shallow Grave برای سیو، Shadow Wave برای هیل، Poison Touch برای کند. Glimmer + Force + Aghanim's + Solar Crest بخر."),
  ("Max Q (Poison Touch) then W (Shadow Wave), ulti (Bad Juju) when available.",
   "ابتدا Q (Poison Touch) بعد W (Shadow Wave)، اولتی (Bad Juju) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["antimage","storm_spirit","tinker","weaver"], 2, 2)

DATA["omniknight"] = (SUP_SAVE,
  ("Purification to heal+nuke, Heavenly Grace for dispel+regen, Degeneration for slow aura, Guardian Angel for physical immunity.",
   "Purification برای هیل+نیوک، Heavenly Grace برای دیسپل+رهجن، Degeneration برای کند اورا، Guardian Angel برای ایمونی فیزیکی."),
  ("Pos 4/5 support: Purification to heal, Guardian Angel for teamfights, Heavenly Grace to dispel. Build Glimmer + Aghanim's + Greaves.",
   "ساپورت پوز ۴/۵: Purification برای هیل، Guardian Angel برای درگیری، Heavenly Grace برای دیسپل. Glimmer + Aghanim's + Greaves بخر."),
  ("Max Q (Purification) then W (Heavenly Grace), ulti (Guardian Angel) when available.",
   "ابتدا Q (Purification) بعد W (Heavenly Grace)، اولتی (Guardian Angel) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["phantom_assassin","juggernaut","troll_warlord","templar_assassin"], 2, 2)

DATA["enchantress"] = (SUP_JUNGLER,
  ("Enchant to dominate creep, Impetus for pure damage, Nature's Attendants for heal, Untouchable for attack slow.",
   "Enchant برای کنترل کریپ، Impetus برای آسیب پیور، Nature's Attendants برای هیل، Untouchable برای کند حمله."),
  ("Pos 4 jungler/support: Enchant creeps for ganks, Impetus for damage, Untouchable vs right-click. Build Glimmer + Aghanim's + Solar Crest.",
   "ساپورت جنگلر پوز ۴: Enchant کریپ برای گنک، Impetus برای آسیب، Untouchable علیه راست‌کلیک. Glimmer + Aghanim's + Solar Crest بخر."),
  ("Max Q (Untouchable) or W (Enchant), ulti (Impetus) when available.",
   "ابتدا Q (Untouchable) یا W (Enchant)، اولتی (Impetus) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["antimage","storm_spirit","tinker","weaver"], 2, 3)

DATA["jakiro"] = (SUP_INT_RANGE,
  ("Dual Breath for slow+burn, Liquid Fire for tower damage, Ice Path for stun line, Macropyre for AoE fire.",
   "Dual Breath برای کند+برن، Liquid Fire برای آسیب تاور، Ice Path برای خط استان، Macropyre برای AOE آتش."),
  ("Pos 4/5 support: Ice Path to stun, Dual Breath + Macropyre for AoE, Liquid Fire to push. Build Glimmer + Force + Aghanim's.",
   "ساپورت پوز ۴/۵: Ice Path برای استان، Dual Breath + Macropyre برای AOE، Liquid Fire برای پوش. Glimmer + Force + Aghanim's بخر."),
  ("Max Q (Dual Breath) then W (Liquid Fire), ulti (Macropyre) when available.",
   "ابتدا Q (Dual Breath) بعد W (Liquid Fire)، اولتی (Macropyre) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["phantom_lancer","meepo","broodmother","naga_siren"], 2, 2)

DATA["chen"] = (SUP_JUNGLER,
  ("Holy Persuasion to dominate creeps, Divine Favor for heal+damage, Penitence for slow+amplify, Hand of God for global heal.",
   "Holy Persuasion برای کنترل کریپ، Divine Favor برای هیل+آسیب، Penitence برای کند+تقویت، Hand of God برای هیل جهانی."),
  ("Pos 4 jungler/support: dominate creeps for push/ganks, Hand of God to save globally. Build Mekansm + Glimmer + Aghanim's + Greaves.",
   "ساپورت جنگلر پوز ۴: کنترل کریپ برای پوش/گنک، Hand of God برای سیو جهانی. Mekansm + Glimmer + Aghanim's + Greaves بخر."),
  ("Max Q (Holy Persuasion) then W (Divine Favor), ulti (Hand of God) when available.",
   "ابتدا Q (Holy Persuasion) بعد W (Divine Favor)، اولتی (Hand of God) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["antimage","storm_spirit","tinker","weaver"], 3, 4)

DATA["treant"] = (SUP_STR_MELEE,
  ("Nature's Guise for invis, Leech Seed for slow+heal, Living Armor for global save, Overgrowth for AoE root.",
   "Nature's Guise برای اینویس، Leech Seed برای کند+هیل، Living Armor برای سیو جهانی، Overgrowth برای AOE روت."),
  ("Pos 4/5 support: Living Armor to save allies globally, Overgrowth for teamfights, Leech Seed to slow. Build Glimmer + Force + Aghanim's.",
   "ساپورت پوز ۴/۵: Living Armor برای سیو جهانی، Overgrowth برای درگیری، Leech Seed برای کند. Glimmer + Force + Aghanim's بخر."),
  ("Max W (Leech Seed) then E (Living Armor), ulti (Overgrowth) when available.",
   "ابتدا W (Leech Seed) بعد E (Living Armor)، اولتی (Overgrowth) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["antimage","storm_spirit","tinker","weaver"], 2, 3)

DATA["ogre_magi"] = (SUP_STR_MELEE,
  ("Fireblast for stun, Ignite for DoT slow, Bloodlust for attack speed, Unrefined Fireblast for multicast stun.",
   "Fireblast برای استان، Ignite برای DoT کند، Bloodlust برای سرعت حمله، Unrefined Fireblast برای مولتی‌کست استان."),
  ("Pos 4/5 support: Fireblast for stun, Bloodlust to buff carry, multicast for burst. Build Blink + Glimmer + Aghanim's + Force.",
   "ساپورت پوز ۴/۵: Fireblast برای استان، Bloodlust برای باف کری، مولتی‌کست برای برست. Blink + Glimmer + Aghanim's + Force بخر."),
  ("Max Q (Fireblast) then W (Ignite), ulti (Bloodlust) when available.",
   "ابتدا Q (Fireblast) بعد W (Ignite)، اولتی (Bloodlust) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["antimage","storm_spirit","tinker","weaver"], 1, 2)

DATA["undying"] = (SUP_STR_MELEE,
  ("Decay to steal STR, Soul Rip for nuke/heal, Tombstone for zombies, Flesh Golem for amplify+slow.",
   "Decay برای دزدی STR، Soul Rip برای نیوک/هیل، Tombstone برای زامبی، Flesh Golem برای تقویت+کند."),
  ("Pos 4/5 support: Tombstone in fights, Decay to steal STR, Flesh Golem for teamfight. Build Glimmer + Force + Pipe + Greaves.",
   "ساپورت پوز ۴/۵: Tombstone در درگیری، Decay برای دزدی STR، Flesh Golem برای درگیری. Glimmer + Force + Pipe + Greaves بخر."),
  ("Max Q (Decay) then W (Soul Rip), ulti (Flesh Golem) when available.",
   "ابتدا Q (Decay) بعد W (Soul Rip)، اولتی (Flesh Golem) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["phantom_lancer","meepo","broodmother","naga_siren"], 2, 3)

DATA["rubick"] = (SUP_INT_AGGRO,
  ("Fade Bolt to nuke+bounce, Telekinesis to lift, Null Field for magic resist, Spell Steal to steal enemy spells.",
   "Fade Bolt برای نیوک+پرش، Telekinesis برای لیفت، Null Field برای مقاومت جادویی، Spell Steal برای دزدی طلسم دشمن."),
  ("Pos 4 support: Spell Steal for value, Telekinesis to setup, Fade Bolt to nuke. Build Blink + Glimmer + Aghanim's + Force.",
   "ساپورت پوز ۴: Spell Steal برای ولیو، Telekinesis برای ستاپ، Fade Bolt برای نیوک. Blink + Glimmer + Aghanim's + Force بخر."),
  ("Max Q (Fade Bolt) then W (Telekinesis), ulti (Spell Steal) when available.",
   "ابتدا Q (Fade Bolt) بعد W (Telekinesis)، اولتی (Spell Steal) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["invoker","tinker","storm_spirit","zuus"], 3, 2)

DATA["disruptor"] = (SUP_INT_AGGRO,
  ("Thunder Strike for AoE nuke, Glimpse to teleport back, Static Storm for silence area, Kinetic Field for trap.",
   "Thunder Strike برای AOE نیوک، Glimpse برای تلپورت برگردان، Static Storm برای سایلنس منطقه، Kinetic Field برای تله."),
  ("Pos 4 support: Glimpse to catch, Kinetic Field + Static Storm combo, Thunder Strike to nuke. Build Glimmer + Force + Aghanim's.",
   "ساپورت پوز ۴: Glimpse برای کچ، کمبو Kinetic Field + Static Storm، Thunder Strike برای نیوک. Glimmer + Force + Aghanim's بخر."),
  ("Max Q (Thunder Strike) then W (Glimpse), ulti (Static Storm) when available.",
   "ابتدا Q (Thunder Strike) بعد W (Glimpse)، اولتی (Static Storm) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["antimage","storm_spirit","tinker","weaver"], 3, 2)

DATA["nyx_assassin"] = (SUP_INT_AGGRO,
  ("Impale to stun, Mana Burn for nuke, Spiked Carapace for reflect+stun, Vendetta for invis burst.",
   "Impale برای استان، Mana Burn برای نیوک، Spiked Carapace برای رفلکت+استان، Vendetta برای اینویس برست."),
  ("Pos 4 support/ganker: Vendetta to roam, Impale + Mana Burn for burst, Spiked Carapace to counter. Build Blink + Glimmer + Dagon.",
   "ساپورت پوز ۴/گنکر: Vendetta برای روم، Impale + Mana Burn برای برست، Spiked Carapace برای کانتر. Blink + Glimmer + Dagon بخر."),
  ("Max Q (Impale) then E (Spiked Carapace), ulti (Vendetta) when available.",
   "ابتدا Q (Impale) بعد E (Spiked Carapace)، اولتی (Vendetta) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["zuus","tinker","storm_spirit","obsidian_destroyer"], 2, 2)

DATA["keeper_of_the_light"] = (SUP_INT_RANGE,
  ("Illuminate for nuke, Mana Leak for slow+mana drain, Chakra Magic for mana restore, Will-O-Wisp for taunt.",
   "Illuminate برای نیوک، Mana Leak برای کند+درین مانا، Chakra Magic برای بازیابی مانا، Will-O-Wisp برای تانت."),
  ("Pos 5 support: Illuminate to nuke waves, Chakra Magic to sustain allies, Will-O-Wisp for fights. Build Glimmer + Aghanim's + Force.",
   "ساپورت پوز ۵: Illuminate برای کلیر ویو، Chakra Magic برای پایداری الی، Will-O-Wisp برای درگیری. Glimmer + Aghanim's + Force بخر."),
  ("Max Q (Illuminate) then W (Mana Leak), ulti (Will-O-Wisp) when available.",
   "ابتدا Q (Illuminate) بعد W (Mana Leak)، اولتی (Will-O-Wisp) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["zuus","tinker","storm_spirit","obsidian_destroyer"], 2, 2)

DATA["wisp"] = (SUP_SAVE,
  ("Tether to link ally, Spirits for nuke, Overcharge for attack speed+damage resist, Relocate for global teleport.",
   "Tether برای پیوند الی، Spirits برای نیوک، Overcharge برای سرعت+مقاومت، Relocate برای تلپورت جهانی."),
  ("Pos 4 support: Tether carry for buffs, Relocate for global ganks, Overcharge for fights. Build Glimmer + Aghanim's + Holy Locket.",
   "ساپورت پوز ۴: Tether کری برای باف، Relocate برای گنک جهانی، Overcharge برای درگیری. Glimmer + Aghanim's + Holy Locket بخر."),
  ("Max W (Spirits) then Q (Tether), ulti (Relocate) when available.",
   "ابتدا W (Spirits) بعد Q (Tether)، اولتی (Relocate) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["antimage","storm_spirit","tinker","weaver"], 3, 4)

DATA["visage"] = (SUP_INT_AGGRO,
  ("Grave Chill for slow+steal, Soul Assumption for nuke, Gravekeeper's Cloak for armor, Summon Familiars for birds.",
   "Grave Chill برای کند+دزدی، Soul Assumption برای نیوک، Gravekeeper's Cloak برای زره، Summon Familiars برای پرندگان."),
  ("Pos 4 support: Familiars for damage/push, Soul Assumption for burst, Grave Chill to slow. Build Glimmer + Aghanim's + Medallion.",
   "ساپورت پوز ۴: Familiars برای آسیب/پوش، Soul Assumption برای برست، Grave Chill برای کند. Glimmer + Aghanim's + Medallion بخر."),
  ("Max Q (Grave Chill) then W (Soul Assumption), ulti (Summon Familiars) when available.",
   "ابتدا Q (Grave Chill) بعد W (Soul Assumption)، اولتی (Summon Familiars) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["antimage","storm_spirit","tinker","weaver"], 3, 3)

DATA["skywrath_mage"] = (SUP_INT_RANGE,
  ("Arcane Bolt for nuke, Concussive Shot for slow, Ancient Seal for silence+amp, Mystic Flare for burst.",
   "Arcane Bolt برای نیوک، Concussive Shot برای کند، Ancient Seal برای سایلنس+تقویت، Mystic Flare برای برست."),
  ("Pos 4/5 support: Ancient Seal to silence, Mystic Flare to burst, Arcane Bolt to spam. Build Glimmer + Aghanim's + Rod of Atos.",
   "ساپورت پوز ۴/۵: Ancient Seal برای سایلنس، Mystic Flare برای برست، Arcane Bolt برای اسپم. Glimmer + Aghanim's + Rod of Atos بخر."),
  ("Max Q (Arcane Bolt) then W (Concussive Shot), ulti (Mystic Flare) when available.",
   "ابتدا Q (Arcane Bolt) بعد W (Concussive Shot)، اولتی (Mystic Flare) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["antimage","storm_spirit","tinker","weaver"], 2, 2)

DATA["techies"] = (SUP_INT_RANGE,
  ("Proximity Mines for AoE, Sticky Bomb for slow+nuke, Blast Off! for suicide nuke+silence, Remote Mines for trap.",
   "Proximity Mines برای AOE، Sticky Bomb برای کند+نیوک، Blast Off! برای سوئیساید نیوک+سایلنس، Remote Mines برای تله."),
  ("Pos 4/5 support: mine map for vision/damage, Blast Off! to silence, Remote Mines for area denial. Build Aghanim's + Scythe + Force.",
   "ساپورت پوز ۴/۵: مپ را مین بگذار، Blast Off! برای سایلنس، Remote Mines برای انکار منطقه. Aghanim's + Scythe + Force بخر."),
  ("Max Q (Proximity Mines) then W (Sticky Bomb), ulti (Remote Mines) when available.",
   "ابتدا Q (Proximity Mines) بعد W (Sticky Bomb)، اولتی (Remote Mines) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["antimage","storm_spirit","tinker","weaver"], 3, 4)

DATA["earth_spirit"] = (SUP_STR_MELEE,
  ("Boulder Smash for nuke+silence, Rolling Boulder for engage+escape, Geomagnetic Grip for pull, Magnetize for AoE silence.",
   "Boulder Smash برای نیوک+سایلنس، Rolling Boulder برای ورود+فرار، Geomagnetic Grip برای کشیدن، Magnetize برای AOE سایلنس."),
  ("Pos 4 support/initiator: Rolling Boulder to engage, Magnetize for teamfight silence, stones for combos. Build Blink + BKB + Aghanim's.",
   "ساپورت پوز ۴/اینیشیتور: Rolling Boulder برای ورود، Magnetize برای سایلنس درگیری، استون برای کمبو. Blink + BKB + Aghanim's بخر."),
  ("Max Q (Boulder Smash) then E (Geomagnetic Grip), ulti (Magnetize) when available.",
   "ابتدا Q (Boulder Smash) بعد E (Geomagnetic Grip)، اولتی (Magnetize) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["antimage","storm_spirit","tinker","weaver"], 3, 4)

DATA["phoenix"] = (SUP_STR_MELEE,
  ("Icarus Dive for engage+escape, Fire Spirits for attack slow, Sun Ray for heal/damage, Supernova for stun+rebirth.",
   "Icarus Dive برای ورود+فرار، Fire Spirits برای کند حمله، Sun Ray برای هیل/آسیب، Supernova برای استان+ری‌برث."),
  ("Pos 4 support: Supernova in teamfights, Icarus Dive to engage, Fire Spirits vs right-click. Build Shiva's + BKB + Aghanim's.",
   "ساپورت پوز ۴: Supernova در درگیری، Icarus Dive برای ورود، Fire Spirits علیه راست‌کلیک. Shiva's + BKB + Aghanim's بخر."),
  ("Max W (Fire Spirits) then Q (Icarus Dive), ulti (Supernova) when available.",
   "ابتدا W (Fire Spirits) بعد Q (Icarus Dive)، اولتی (Supernova) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["phantom_assassin","juggernaut","troll_warlord","templar_assassin"], 3, 2)

DATA["oracle"] = (SUP_SAVE,
  ("Fortune's End for purge+nuke, Fate's Edict for magic immunity+heal amp, Purifying Flames for heal/damage, False Promise for save.",
   "Fortune's End برای پورج+نیوک، Fate's Edict برای ایمونی جادویی+هیل، Purifying Flames برای هیل/آسیب، False Promise برای سیو."),
  ("Pos 4/5 support: False Promise to save, Purifying Flames to heal, Fortune's End to purge. Build Glimmer + Force + Aghanim's.",
   "ساپورت پوز ۴/۵: False Promise برای سیو، Purifying Flames برای هیل، Fortune's End برای پورج. Glimmer + Force + Aghanim's بخر."),
  ("Max Q (Fortune's End) then W (Fate's Edict), ulti (False Promise) when available.",
   "ابتدا Q (Fortune's End) بعد W (Fate's Edict)، اولتی (False Promise) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["antimage","storm_spirit","tinker","weaver"], 3, 2)

DATA["winter_wyvern"] = (SUP_SAVE,
  ("Arctic Burn for slow+vision, Splinter Blast for nuke, Cold Embrace for save, Winter's Curse for enemy teamfight turn.",
   "Arctic Burn برای کند+ویژن، Splinter Blast برای نیوک، Cold Embrace برای سیو، Winter's Curse برای درگیری تیمی دشمن."),
  ("Pos 4/5 support: Winter's Curse to turn enemy fights, Cold Embrace to save, Splinter Blast to nuke. Build Glimmer + Aghanim's + Force.",
   "ساپورت پوز ۴/۵: Winter's Curse برای درگیری دشمن، Cold Embrace برای سیو، Splinter Blast برای نیوک. Glimmer + Aghanim's + Force بخر."),
  ("Max W (Splinter Blast) then Q (Arctic Burn), ulti (Winter's Curse) when available.",
   "ابتدا W (Splinter Blast) بعد Q (Arctic Burn)، اولتی (Winter's Curse) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["phantom_lancer","meepo","broodmother","naga_siren"], 3, 2)

DATA["ancient_apparition"] = (SUP_INT_RANGE,
  ("Cold Feet for stun, Ice Vortex for slow+magic amp, Chilling Touch for bonus damage, Ice Blast for global nuke+heal prevention.",
   "Cold Feet برای استان، Ice Vortex برای کند+تقویت جادو، Chilling Touch برای بونوس آسیب، Ice Blast برای نیوک جهانی+جلوگیری هیل."),
  ("Pos 5 support: Ice Blast to finish low-HP globally + counter heals, Cold Feet to stun. Build Glimmer + Aghanim's + Force.",
   "ساپورت پوز ۵: Ice Blast برای کشتن جهانی + کانتر هیل، Cold Feet برای استان. Glimmer + Aghanim's + Force بخر."),
  ("Max Q (Cold Feet) then W (Ice Vortex), ulti (Ice Blast) when available.",
   "ابتدا Q (Cold Feet) بعد W (Ice Vortex)، اولتی (Ice Blast) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["huskar","necrolyte","bristleback","alchemist"], 3, 2)

DATA["venomancer"] = (SUP_INT_RANGE,
  ("Venomous Gale for slow+poison, Poison Sting for DoT, Plague Ward for vision+push, Poison Nova for AoE DoT.",
   "Venomous Gale برای کند+سم، Poison Sting برای DoT، Plague Ward برای ویژن+پوش، Poison Nova برای AOE DoT."),
  ("Pos 4/5 support: Poison Nova for teamfights, Plague Ward to push/vision, Venomous Gale to slow. Build Glimmer + Aghanim's + Pipe.",
   "ساپورت پوز ۴/۵: Poison Nova برای درگیری، Plague Ward برای پوش/ویژن، Venomous Gale برای کند. Glimmer + Aghanim's + Pipe بخر."),
  ("Max Q (Venomous Gale) then W (Poison Sting), ulti (Poison Nova) when available.",
   "ابتدا Q (Venomous Gale) بعد W (Poison Sting)، اولتی (Poison Nova) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["huskar","bristleback","alchemist","tidehunter"], 1, 3)

DATA["shadow_demon"] = (SUP_INT_AGGRO,
  ("Disruption to banish+illusions, Soul Catcher for amp, Shadow Poison for stacking DoT, Demonic Purge for slow+purge.",
   "Disruption برای بنیش+ایلوژن، Soul Catcher برای تقویت، Shadow Poison برای استک DoT، Demonic Purge برای کند+پورج."),
  ("Pos 4/5 support: Disruption to save/setup, Soul Catcher to amplify, Shadow Poison stacks. Build Glimmer + Aghanim's + Force.",
   "ساپورت پوز ۴/۵: Disruption برای سیو/ستاپ، Soul Catcher برای تقویت، Shadow Poison استک. Glimmer + Aghanim's + Force بخر."),
  ("Max Q (Disruption) then W (Soul Catcher), ulti (Demonic Purge) when available.",
   "ابتدا Q (Disruption) بعد W (Soul Catcher)، اولتی (Demonic Purge) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["phantom_lancer","meepo","broodmother","naga_siren"], 3, 3)

DATA["enigma"] = (SUP_JUNGLER,
  ("Malefice for stun, Demonic Conversion for eidolons+push, Midnight Pulse for AoE, Black Hole for teamfight channel.",
   "Malefice برای استان، Demonic Conversion برای ایدولن+پوش، Midnight Pulse برای AOE، Black Hole برای چنل درگیری."),
  ("Pos 4 jungler/initiator: Black Hole to win teamfights, Blink to initiate, Eidolons to farm/push. Build Blink + BKB + Refresher + Aghanim's.",
   "ساپورت جنگلر پوز ۴/اینیشیتور: Black Hole برای برد درگیری، Blink برای اینیشیت، Eidolons برای فارم/پوش. Blink + BKB + Refresher + Aghanim's بخر."),
  ("Max E (Demonic Conversion) then Q (Malefice), ulti (Black Hole) when available.",
   "ابتدا E (Demonic Conversion) بعد Q (Malefice)، اولتی (Black Hole) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["phantom_lancer","meepo","broodmother","naga_siren"], 3, 2)

DATA["abaddon"] = (SUP_SAVE,
  ("Mist Coil for nuke+heal, Aphotic Shield for dispel+nuke, Curse of Avernus for slow+lock, Borrowed Time for auto-save.",
   "Mist Coil برای نیوک+هیل، Aphotic Shield برای دیسپل+نیوک، Curse of Avernus برای کند+لاک، Borrowed Time برای سیو خودکار."),
  ("Pos 4/5 support/carry: Aphotic Shield to dispel/save, Borrowed Time to tank, Curse to lock. Build Radiance + BKB + Aghanim's.",
   "ساپورت پوز ۴/۵/کری: Aphotic Shield برای دیسپل/سیو، Borrowed Time برای تانک، Curse برای لاک. Radiance + BKB + Aghanim's بخر."),
  ("Max Q (Mist Coil) then W (Aphotic Shield), ulti (Borrowed Time) when available.",
   "ابتدا Q (Mist Coil) بعد W (Aphotic Shield)، اولتی (Borrowed Time) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["antimage","storm_spirit","tinker","weaver"], 1, 2)

DATA["dark_willow"] = (SUP_INT_AGGRO,
  ("Bramble Maze for trap, Shadow Realm for invis, Cursed Crown for stun, Bedlam + Terrorize for nuke+fear.",
   "Bramble Maze برای تله، Shadow Realm برای اینویس، Cursed Crown برای استان، Bedlam + Terrorize برای نیوک+ترس."),
  ("Pos 4 support: Bramble Maze to lock, Shadow Realm to dodge, Bedlam for burst, Terrorize for fights. Build Glimmer + Aghanim's + Force.",
   "ساپورت پوز ۴: Bramble Maze برای لاک، Shadow Realm برای داج، Bedlam برای برست، Terrorize برای درگیری. Glimmer + Aghanim's + Force بخر."),
  ("Max Q (Bramble Maze) then W (Shadow Realm), ulti (Bedlam/Terrorize) when available.",
   "ابتدا Q (Bramble Maze) بعد W (Shadow Realm)، اولتی (Bedlam/Terrorize) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["antimage","storm_spirit","tinker","weaver"], 3, 3)

DATA["pangolier"] = (SUP_STR_MELEE,
  ("Swashbuckle for nuke, Shield Crash for damage reduction, Lucky Shot for disarm, Rolling Thunder for AoE knockback.",
   "Swashbuckle برای نیوک، Shield Crash برای کاهش آسیب، Lucky Shot برای دیسرم، Rolling Thunder برای AOE ناک‌بک."),
  ("Carry/initiator: Swashbuckle to nuke, Rolling Thunder for teamfights, Shield Crash to tank. Build BKB + Maelstrom + Assault + Diffusal.",
   "کری/اینیشیتور: Swashbuckle برای نیوک، Rolling Thunder برای درگیری، Shield Crash برای تانک. BKB + Maelstrom + Assault + Diffusal بخر."),
  ("Max Q (Swashbuckle) then W (Shield Crash), ulti (Rolling Thunder) when available.",
   "ابتدا Q (Swashbuckle) بعد W (Shield Crash)، اولتی (Rolling Thunder) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["templar_assassin","medusa","phantom_lancer","troll_warlord"], 3, 3)

DATA["grimstroke"] = (SUP_INT_AGGRO,
  ("Stroke of Fate for nuke+slow, Phantom's Embrace for silence, Ink Swell for stun+buff, Soulbind for link+spell amplify.",
   "Stroke of Fate برای نیوک+کند، Phantom's Embrace برای سایلنس، Ink Swell برای استان+باف، Soulbind برای پیوند+تقویت طلسم."),
  ("Pos 4/5 support: Soulbind to link enemies for double spells, Phantom's Embrace to silence, Stroke to nuke. Build Glimmer + Aghanim's + Force.",
   "ساپورت پوز ۴/۵: Soulbind برای پیوند دشمن برای دابل طلسم، Phantom's Embrace برای سایلنس، Stroke برای نیوک. Glimmer + Aghanim's + Force بخر."),
  ("Max Q (Stroke of Fate) then W (Phantom's Embrace), ulti (Soulbind) when available.",
   "ابتدا Q (Stroke of Fate) بعد W (Phantom's Embrace)، اولتی (Soulbind) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["antimage","storm_spirit","tinker","weaver"], 2, 2)

DATA["snapfire"] = (SUP_INT_RANGE,
  ("Scatterblast for nuke, Firesnap Cookie for bounce+buff, Lil' Shredder for attack, Mortimer Kisses for AoE slow+nuke.",
   "Scatterblast برای نیوک، Firesnap Cookie برای بانس+باف، Lil' Shredder برای حمله، Mortimer Kisses برای AOE کند+نیوک."),
  ("Pos 4/5 support: Firesnap Cookie to engage/save, Mortimer Kisses for teamfights, Scatterblast to nuke. Build Glimmer + Aghanim's + Force.",
   "ساپورت پوز ۴/۵: Firesnap Cookie برای ورود/سیو، Mortimer Kisses برای درگیری، Scatterblast برای نیوک. Glimmer + Aghanim's + Force بخر."),
  ("Max Q (Scatterblast) then W (Firesnap Cookie), ulti (Mortimer Kisses) when available.",
   "ابتدا Q (Scatterblast) بعد W (Firesnap Cookie)، اولتی (Mortimer Kisses) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["antimage","storm_spirit","tinker","weaver"], 2, 3)

DATA["marci"] = (SUP_STR_MELEE,
  ("Dispose to throw enemy, Rebound to jump ally/enemy, Sidekick for lifesteal buff, Primal Brawl for combo+burst.",
   "Dispose برای پرت دشمن، Rebound برای جامپ الی/دشمن، Sidekick برای باف لایف‌استیل، Primal Brawl برای کمبو+برست."),
  ("Pos 4 support/carry: Rebound to engage, Primal Brawl for burst, Sidekick to buff carry. Build BKB + Desolator + Assault.",
   "ساپورت پوز ۴/کری: Rebound برای ورود، Primal Brawl برای برست، Sidekick برای باف کری. BKB + Desolator + Assault بخر."),
  ("Max Q (Dispose) then W (Rebound), ulti (Primal Brawl) when available.",
   "ابتدا Q (Dispose) بعد W (Rebound)، اولتی (Primal Brawl) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["antimage","storm_spirit","tinker","weaver"], 2, 3)

DATA["ringmaster"] = (SUP_INT_AGGRO,
  ("Whip Replay for nuke, Escape Act for buff+escape, Improbability for random effects, Showstopper for AoE disable.",
   "Whip Replay برای نیوک، Escape Act برای باف+فرار، Improbability برای افکت تصادفی، Showstopper برای AOE دیزیبل."),
  ("Pos 4 support: Whip Replay to nuke, Showstopper for teamfights, Escape Act to save. Build Glimmer + Aghanim's + Force.",
   "ساپورت پوز ۴: Whip Replay برای نیوک، Showstopper برای درگیری، Escape Act برای سیو. Glimmer + Aghanim's + Force بخر."),
  ("Max Q (Whip Replay) then W (Escape Act), ulti (Showstopper) when available.",
   "ابتدا Q (Whip Replay) بعد W (Escape Act)، اولتی (Showstopper) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["antimage","storm_spirit","tinker","weaver"], 3, 4)

# ===================== UNIVERSAL / FLEX / SPECIAL =====================
DATA["pudge"] = (SUP_STR_MELEE,
  ("Meat Hook to grab enemy, Rot for AoE slow+damage, Flesh Heap for STR stacks, Dismember for channel disable+burst.",
   "Meat Hook برای کشیدن دشمن، Rot برای AOE کند+آسیب، Flesh Heap برای استک STR، Dismember برای چنل دیزیبل+برست."),
  ("Offlane/support: Meat Hook to pick off, Rot to slow, Dismember to lock, Flesh Heap to tank. Build Blink + BKB + Aghanim's + Force.",
   "آفلین/ساپورت: Meat Hook برای پیک، Rot برای کند، Dismember برای لاک، Flesh Heap برای تانک. Blink + BKB + Aghanim's + Force بخر."),
  ("Max Q (Meat Hook) then E (Flesh Heap), ulti (Dismember) when available.",
   "ابتدا Q (Meat Hook) بعد E (Flesh Heap)، اولتی (Dismember) آماده."),
  ["viper","drow_ranger","sniper","lina"], ["antimage","storm_spirit","tinker","weaver"], 2, 2)

DATA["sand_king"] = (SUP_STR_MELEE,
  ("Burrowstrike to stun, Sand Storm for invis+DoT, Caustic Finale for AoE, Epicenter for channel AoE nuke.",
   "Burrowstrike برای استان، Sand Storm برای اینویس+DoT، Caustic Finale برای AOE، Epicenter برای چنل AOE نیوک."),
  ("Offlane/support/initiator: Burrowstrike to stun, Epicenter for teamfights, Sand Storm to dodge. Build Blink + BKB + Shiva's + Aghanim's.",
   "آفلین/ساپورت/اینیشیتور: Burrowstrike برای استان، Epicenter برای درگیری، Sand Storm برای داج. Blink + BKB + Shiva's + Aghanim's بخر."),
  ("Max Q (Burrowstrike) then W (Sand Storm), ulti (Epicenter) when available.",
   "ابتدا Q (Burrowstrike) بعد W (Sand Storm)، اولتی (Epicenter) آماده."),
  ["viper","drow_ranger","sniper","lina"], ["phantom_lancer","meepo","broodmother","naga_siren"], 2, 3)

DATA["vengefulspirit"] = (SUP_INT_AGGRO,
  ("Magic Missile to stun, Wave of Terror for armor reduction, Vengeance Aura for damage aura, Nether Swap for position swap.",
   "Magic Missile برای استان، Wave of Terror برای کاهش زره، Vengeance Aura برای اورا آسیب، Nether Swap برای جابجایی پوزیشن."),
  ("Pos 4/5 support: Magic Missile to stun, Nether Swap to save/engage, Wave of Terror for vision. Build Glimmer + Force + Medallion.",
   "ساپورت پوز ۴/۵: Magic Missile برای استان، Nether Swap برای سیو/ورود، Wave of Terror برای ویژن. Glimmer + Force + Medallion بخر."),
  ("Max Q (Magic Missile) then W (Wave of Terror), ulti (Nether Swap) when available.",
   "ابتدا Q (Magic Missile) بعد W (Wave of Terror)، اولتی (Nether Swap) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["antimage","storm_spirit","tinker","weaver"], 1, 2)

DATA["windrunner"] = (SUP_INT_AGGRO,
  ("Shackleshot to stun (vs wall/trees), Powershot for nuke, Windrun for evasion+speed, Focus Fire for right-click burst.",
   "Shackleshot برای استان (به دیوار/درخت)، Powershot برای نیوک، Windrun برای ایویژن+سرعت، Focus Fire برای برست راست‌کلیک."),
  ("Carry/support: Shackleshot to stun, Powershot to nuke, Focus Fire for fights. Build MKB + BKB + Maelstrom + Daedalus.",
   "کری/ساپورت: Shackleshot برای استان، Powershot برای نیوک، Focus Fire برای درگیری. MKB + BKB + Maelstrom + Daedalus بخر."),
  ("Max W (Powershot) then Q (Shackleshot), ulti (Focus Fire) when available.",
   "ابتدا W (Powershot) بعد Q (Shackleshot)، اولتی (Focus Fire) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["templar_assassin","medusa","phantom_lancer","troll_warlord"], 2, 3)

DATA["batrider"] = (SUP_INT_AGGRO,
  ("Sticky Napalm for stacks, Flamebreak for nuke+knockback, Firefly for fly+DoT, Flaming Lasso to drag enemy.",
   "Sticky Napalm برای استک، Flamebreak برای نیوک+ناک‌بک، Firefly برای پرواز+DoT، Flaming Lasso برای کشیدن دشمن."),
  ("Offlane/initiator: Flaming Lasso to drag enemy carry into team, Sticky Napalm stacks, BKB. Build Blink + BKB + Force + Aghanim's.",
   "آفلین/اینیشیتور: Flaming Lasso برای کشیدن کری دشمن به تیم، Sticky Napalm استک، BKB. Blink + BKB + Force + Aghanim's بخر."),
  ("Max W (Sticky Napalm) then Q (Flamebreak), ulti (Flaming Lasso) when available.",
   "ابتدا W (Sticky Napalm) بعد Q (Flamebreak)، اولتی (Flaming Lasso) آماده."),
  ["viper","drow_ranger","sniper","lina"], ["antimage","storm_spirit","tinker","weaver"], 3, 3)

DATA["bounty_hunter"] = (SUP_INT_AGGRO,
  ("Shuriken Toss for nuke, Jinada for bonus damage, Shadow Walk for invis, Track for gold bonus+vision.",
   "Shuriken Toss برای نیوک، Jinada برای بونوس آسیب، Shadow Walk برای اینویس، Track برای بونوس گلد+ویژن."),
  ("Pos 4 support/roamer: Track for team gold, Shadow Walk to roam, Jinada for harass. Build BKB + Desolator + Aghanim's.",
   "ساپورت پوز ۴/رومر: Track برای گلد تیم، Shadow Walk برای روم، Jinada برای هاراس. BKB + Desolator + Aghanim's بخر."),
  ("Max W (Jinada) then Q (Shuriken Toss), ulti (Track) when available.",
   "ابتدا W (Jinada) بعد Q (Shuriken Toss)، اولتی (Track) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["antimage","storm_spirit","tinker","weaver"], 2, 3)

DATA["alchemist"] = (SUP_STR_MELEE,
  ("Acid Spray for armor reduction+farm, Unstable Concoction for stun, Greevil's Greed for bonus gold, Chemical Rage for regen+atk speed.",
   "Acid Spray برای کاهش زره+فارم، Unstable Concoction برای استان، Greevil's Greed برای بونوس گلد، Chemical Rage برای رجن+سرعت."),
  ("Carry/farmer: Greevil's Greed to farm fast, Chemical Rage for sustain, Acid Spray to push. Build Radiance + BKB + Assault + Aghanim's (share).",
   "کری/فارمر: Greevil's Greed برای فارم سریع، Chemical Rage برای پایداری، Acid Spray برای پوش. Radiance + BKB + Assault + Aghanim's بخر."),
  ("Max Q (Acid Spray) then E (Greevil's Greed), ulti (Chemical Rage) when available.",
   "ابتدا Q (Acid Spray) بعد E (Greevil's Greed)، اولتی (Chemical Rage) آماده."),
  ["ancient_apparition","lina","zuus","slark"], ["axe","bristleback","centaur","tidehunter"], 2, 3)

DATA["dark_seer"] = (SUP_INT_AGGRO,
  ("Vacuum to group enemies, Ion Shell for damage, Surge for speed, Wall of Replica for illusion wall.",
   "Vacuum برای گروه دشمن، Ion Shell برای آسیب، Surge برای سرعت، Wall of Replica برای دیوار ایلوژن."),
  ("Offlane/initiator: Vacuum to set up combos, Wall of Replica for teamfights, Ion Shell to push. Build Blink + BKB + Aghanim's + Shiva's.",
   "آفلین/اینیشیتور: Vacuum برای ستاپ کمبو، Wall of Replica برای درگیری، Ion Shell برای پوش. Blink + BKB + Aghanim's + Shiva's بخر."),
  ("Max Q (Vacuum) then W (Ion Shell), ulti (Wall of Replica) when available.",
   "ابتدا Q (Vacuum) بعد W (Ion Shell)، اولتی (Wall of Replica) آماده."),
  ["viper","drow_ranger","sniper","lina"], ["phantom_lancer","meepo","broodmother","naga_siren"], 2, 3)

DATA["furion"] = (SUP_INT_RANGE,
  ("Sprout for vision block, Teleport for global mobility, Nature's Call for treants+push, Wrath of Nature for global nuke.",
   "Sprout برای بلاک ویژن، Teleport برای موبیلیتی جهانی، Nature's Call برای ترینت+پوش، Wrath of Nature برای نیوک جهانی."),
  ("Carry/pusher: Teleport for split-push, Nature's Call to push towers, Wrath of Nature for global nuke. Build Desolator + BKB + Maelstrom + Necronomicon.",
   "کری/پوشر: Teleport برای اسپلیت‌پوش، Nature's Call برای پوش تاور، Wrath of Nature برای نیوک جهانی. Desolator + BKB + Maelstrom + Necronomicon بخر."),
  ("Max W (Teleport) then E (Nature's Call), ulti (Wrath of Nature) when available.",
   "ابتدا W (Teleport) بعد E (Nature's Call)، اولتی (Wrath of Nature) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["templar_assassin","medusa","sniper","drow_ranger"], 2, 3)

DATA["muerta"] = (SUP_INT_RANGE,
  ("Dead Shot for nuke+slow, The Calling for fear+damage, Gunslinger for bonus shots, Pierce the Veil for ghost form+damage.",
   "Dead Shot برای نیوک+کند، The Calling برای ترس+آسیب، Gunslinger برای ضربات بونوس، Pierce the Veil برای فرم روح+آسیب."),
  ("Carry/support: Pierce the Veil for fights, Dead Shot to nuke, The Calling to fear. Build BKB + Maelstrom + Butterfly + Aghanim's.",
   "کری/ساپورت: Pierce the Veil برای درگیری، Dead Shot برای نیوک، The Calling برای ترس. BKB + Maelstrom + Butterfly + Aghanim's بخر."),
  ("Max Q (Dead Shot) then W (The Calling), ulti (Pierce the Veil) when available.",
   "ابتدا Q (Dead Shot) بعد W (The Calling)، اولتی (Pierce the Veil) آماده."),
  ["axe","legion_commander","doom_bringer","slark"], ["templar_assassin","medusa","phantom_lancer","troll_warlord"], 3, 3)

DATA["skeleton_king"] = (SUP_STR_MELEE,
  ("Wraithfire Blast for stun+burn, Vampiric Aura for lifesteal, Skeletons for summon+push, Reincarnation for revive.",
   "Wraithfire Blast برای استان+برن، Vampiric Aura برای لایف‌استیل، Skeletons برای سامون+پوش، Reincarnation برای ریوایو."),
  ("Carry: Wraithfire Blast to stun, Vampiric Aura for sustain, Reincarnation for second life. Build Radiance + BKB + Assault + Daedalus.",
   "کری: Wraithfire Blast برای استان، Vampiric Aura برای پایداری، Reincarnation برای جان دوم. Radiance + BKB + Assault + Daedalus بخر."),
  ("Max Q (Wraithfire Blast) then E (Vampiric Aura), ulti (Reincarnation) when available.",
   "ابتدا Q (Wraithfire Blast) بعد E (Vampiric Aura)، اولتی (Reincarnation) آماده."),
  ["ancient_apparition","lina","zuus","slark"], ["axe","bristleback","centaur","tidehunter"], 1, 2)

DATA["chaos_knight"] = (None,
  ("Chaos Bolt for random stun, Reality Rift to close gap, Chaos Strike for crit, Phantasm for illusions+push.",
   "Chaos Bolt برای استان تصادفی، Reality Rift برای نزدیک، Chaos Strike برای کرت، Phantasm برای ایلوژن+پوش."),
  ("Carry: Reality Rift to engage, Phantasm for burst/push, Chaos Bolt to lock. Build Armlet + BKB + Manta + Heart.",
   "کری: Reality Rift برای ورود، Phantasm برای برست/پوش، Chaos Bolt برای لاک. Armlet + BKB + Manta + Heart بخر."),
  ("Max Q (Chaos Bolt) then E (Chaos Strike), ulti (Phantasm) when available.",
   "ابتدا Q (Chaos Bolt) بعد E (Chaos Strike)، اولتی (Phantasm) آماده."),
  ["ancient_apparition","lina","zuus","slark"], ["templar_assassin","medusa","sniper","drow_ranger"], 2, 3)

DATA["lycan"] = (None,
  ("Summon Wolves for gank+push, Howl for team buff, Feral Impulse for damage aura, Shapeshift for wolf form+speed.",
   "Summon Wolves برای گنک+پوش، Howl برای باف تیم، Feral Impulse برای اورا آسیب، Shapeshift برای فرم گرگ+سرعت."),
  ("Carry/pusher: Summon Wolves to push, Shapeshift for fights, Howl for team. Build Necronomicon + BKB + Assault + Desolator.",
   "کری/پوشر: Summon Wolves برای پوش، Shapeshift برای درگیری، Howl برای تیم. Necronomicon + BKB + Assault + Desolator بخر."),
  ("Max W (Summon Wolves) then E (Feral Impulse), ulti (Shapeshift) when available.",
   "ابتدا W (Summon Wolves) بعد E (Feral Impulse)، اولتی (Shapeshift) آماده."),
  ["viper","drow_ranger","sniper","lina"], ["templar_assassin","medusa","phantom_lancer","troll_warlord"], 2, 3)

# Validate all hero IDs in DATA are valid
missing = [hid for hid in DATA if hid not in HERO_IDS]
extra = [hid for hid in HERO_IDS if hid not in DATA]
print(f"DATA entries: {len(DATA)}")
print(f"Missing from DATA (will keep existing generic): {missing}")
print(f"Heroes without enrichment (extra): {extra}")

# Validate counters/goodAgainst hero ids
all_hero_set = set(HERO_IDS)
bad_refs = []
for hid, d in DATA.items():
    sup, combos, playstyle, skill, counters, good, diff, tier = d
    for c in counters:
        if c not in all_hero_set: bad_refs.append((hid,'counter',c))
    for g in good:
        if g not in all_hero_set: bad_refs.append((hid,'goodAgainst',g))
print(f"Bad hero refs: {bad_refs}")

# ---- Generate TypeScript ----
SUPP_TEMPLATES = {
    'SUP_INT_RANGE': SUP_INT_RANGE, 'SUP_INT_AGGRO': SUP_INT_AGGRO,
    'SUP_STR_MELEE': SUP_STR_MELEE, 'SUP_JUNGLER': SUP_JUNGLER, 'SUP_SAVE': SUP_SAVE,
}

def arr(lst):
    return '[' + ','.join(f'"{x}"' for x in lst) + ']'

def rolebuild(b):
    return ('{ starting: ' + arr(b['starting']) +
            ', early: ' + arr(b['early']) +
            ', mid: ' + arr(b['mid']) +
            ', late: ' + arr(b['late']) +
            ', situational: ' + arr(b['situational']) + ' }')

def esc(s):
    return s.replace('"','\\"').replace('\n',' ')

lines = []
lines.append('// Hero-specific professional enrichment data (patch 7.39+ meta).')
lines.append('// Merges over heroBuilds: differentiated support builds, combos, playstyle, skillBuild, counters, goodAgainst, difficulty, patchTier.')
lines.append('// Auto-generated from scripts/gen_enrichments.py — do not edit by hand.')
lines.append('import { RoleBuild } from \'./types\';')
lines.append('')
lines.append('export interface HeroEnrichment {')
lines.append('  support?: RoleBuild;')
lines.append('  combos: { en: string; fa: string };')
lines.append('  playstyle: { en: string; fa: string };')
lines.append('  skillBuild: { en: string; fa: string };')
lines.append('  counters: string[];')
lines.append('  goodAgainst: string[];')
lines.append('  difficulty: number;')
lines.append('  patchTier: number;')
lines.append('}')
lines.append('')
lines.append('export const enrichments: Record<string, HeroEnrichment> = {')

for hid in HERO_IDS:
    if hid not in DATA:
        continue
    sup, combos, playstyle, skill, counters, good, diff, tier = DATA[hid]
    lines.append(f'  "{hid}": {{')
    if sup:
        lines.append(f'    support: {rolebuild(sup)},')
    lines.append(f'    combos: {{ en: "{esc(combos[0])}", fa: "{esc(combos[1])}" }},')
    lines.append(f'    playstyle: {{ en: "{esc(playstyle[0])}", fa: "{esc(playstyle[1])}" }},')
    lines.append(f'    skillBuild: {{ en: "{esc(skill[0])}", fa: "{esc(skill[1])}" }},')
    lines.append(f'    counters: {arr(counters)},')
    lines.append(f'    goodAgainst: {arr(good)},')
    lines.append(f'    difficulty: {diff},')
    lines.append(f'    patchTier: {tier},')
    lines.append('  },')

lines.append('};')
lines.append('')
# Count
lines.append(f'export const ENRICHMENT_COUNT = {len(DATA)};')

with open('src/data/enrichments.ts','w',encoding='utf-8') as f:
    f.write('\n'.join(lines) + '\n')

print(f"\nGenerated src/data/enrichments.ts with {len(DATA)} hero enrichments.")
print(f"Heroes still using generic builds.ts data: {len(extra)}")
print("Extras:", extra)
