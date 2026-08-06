import fs from 'fs';

const p = {
  a: 'ا', b: 'ب', c: 'ک', d: 'د', e: 'ا', f: 'ف', g: 'گ', h: 'ه', i: 'ای', j: 'ج', k: 'ک',
  l: 'ل', m: 'م', n: 'ن', o: 'و', p: 'پ', q: 'ک', r: 'ر', s: 'س', t: 'ت', u: 'و', v: 'و',
  w: 'و', x: 'کس', y: 'ی', z: 'ز', ' ': ' ', '-': '-', "'": "'"
};

const map = {
  'Anti-Mage': 'آنتی-میج',
  'Axe': 'اکس',
  'Bane': 'بین',
  'Bloodseeker': 'بلادسیکر',
  'Crystal Maiden': 'کریستال میدن',
  'Drow Ranger': 'دراو رنجر',
  'Earthshaker': 'ارث شیکر',
  'Juggernaut': 'جاگرنات',
  'Mirana': 'میرانا',
  'Morphling': 'مورفلینگ',
  'Shadow Fiend': 'شدو فایند',
  'Phantom Lancer': 'فانتوم لنسر',
  'Puck': 'پاک',
  'Pudge': 'پاج',
  'Razor': 'ریزر',
  'Sand King': 'سند کینگ',
  'Storm Spirit': 'استورم اسپریت',
  'Sven': 'سون',
  'Tiny': 'تاینی',
  'Vengeful Spirit': 'ونجفول اسپریت',
  'Windranger': 'ویندرنجر',
  'Zeus': 'زئوس',
  'Kunkka': 'کانکا',
  'Lina': 'لینا',
  'Lion': 'لاین',
  'Shadow Shaman': 'شدو شامان',
  'Slardar': 'اسلادار',
  'Tidehunter': 'تایدهانتر',
  'Witch Doctor': 'ویچ دکتر',
  'Lich': 'لیچ',
  'Riki': 'ریکی',
  'Enigma': 'انیگما',
  'Tinker': 'تینکر',
  'Sniper': 'اسنایپر',
  'Necrophos': 'نکروفوس',
  'Warlock': 'وارلوک',
  'Beastmaster': 'بیست مستر',
  'Queen of Pain': 'کویین آف پین',
  'Venomancer': 'ونومانسر',
  'Faceless Void': 'فیسلس وید',
  'Wraith King': 'ریث کینگ',
  'Death Prophet': 'دث پرافیت',
  'Phantom Assassin': 'فانتوم اسسین',
  'Pugna': 'پوگنا',
  'Templar Assassin': 'تمپلار اسسین',
  'Viper': 'وایپر',
  'Luna': 'لونا',
  'Dragon Knight': 'دراگون نایت',
  'Dazzle': 'دازل',
  'Clockwerk': 'کلاک ورک',
  'Leshrac': 'لشراک',
  "Nature's Prophet": 'نیچرز پرافیت',
  'Lifestealer': 'لایف استیلر',
  'Dark Seer': 'دارک سیر',
  'Clinkz': 'کلینکز',
  'Omniknight': 'آمنینایت',
  'Enchantress': 'انچانترس',
  'Huskar': 'هاسکار',
  'Night Stalker': 'نایت استاکر',
  'Broodmother': 'برودمادر',
  'Bounty Hunter': 'باونتی هانتر',
  'Weaver': 'ویور',
  'Jakiro': 'جاکیرو',
  'Batrider': 'بترایدر',
  'Chen': 'چن',
  'Spectre': 'اسپکتر',
  'Ancient Apparition': 'انشنت آپاریشن',
  'Doom': 'دوم',
  'Ursa': 'اورسا',
  'Spirit Breaker': 'اسپریت بریکر',
  'Gyrocopter': 'جایروکاپتر',
  'Alchemist': 'الکمیست',
  'Invoker': 'اینووکر',
  'Silencer': 'سایلنسر',
  'Outworld Destroyer': 'اوت ورلد دسترویر',
  'Lycan': 'لایکن',
  'Brewmaster': 'برومستر',
  'Shadow Demon': 'شدو دیمون',
  'Lone Druid': 'لون درویید',
  'Chaos Knight': 'کائوس نایت',
  'Meepo': 'میپو',
  'Treant Protector': 'ترینت پروتکتور',
  'Ogre Magi': 'اوگر مجای',
  'Undying': 'آندایینگ',
  'Rubick': 'روبیک',
  'Disruptor': 'دیسراپتور',
  'Nyx Assassin': 'نیکس اسسین',
  'Naga Siren': 'ناگا سایِرِن',
  'Keeper of the Light': 'کیپر آو د لایت',
  'Io': 'ایو',
  'Visage': 'ویزاژ',
  'Slark': 'اسلارک',
  'Medusa': 'مدوسا',
  'Troll Warlord': 'ترول وارلورد',
  'Centaur Warrunner': 'سنتور واررانر',
  'Magnus': 'مگنوس',
  'Timbersaw': 'تیمبرساو',
  'Bristleback': 'بریستل بک',
  'Tusk': 'تاسک',
  'Skywrath Mage': 'اسکای راث میج',
  'Abaddon': 'آبادون',
  'Elder Titan': 'الدر تایتان',
  'Legion Commander': 'لژیون کماندر',
  'Techies': 'تکیز',
  'Ember Spirit': 'امبر اسپریت',
  'Earth Spirit': 'ارث اسپریت',
  'Underlord': 'آندر لورد',
  'Terrorblade': 'ترور بلید',
  'Phoenix': 'فینیکس',
  'Oracle': 'اوراکل',
  'Winter Wyvern': 'وینتر وایورن',
  'Arc Warden': 'ارک واردن',
  'Monkey King': 'مانکی کینگ',
  'Dark Willow': 'دارک ویلو',
  'Pangolier': 'پانگولیر',
  'Grimstroke': 'گریم استروک',
  'Hoodwink': 'هودوینک',
  'Void Spirit': 'وید اسپریت',
  'Snapfire': 'اسنپ فایر',
  'Mars': 'مارس',
  'Dawnbreaker': 'دان بریکر',
  'Marci': 'مارسی',
  'Primal Beast': 'پرایمال بیست',
  'Muerta': 'مورتا'
};

function translit(en) {
  if (map[en]) return map[en];
  let res = '';
  const lower = en.toLowerCase();
  for (let i=0; i<lower.length; i++) {
    res += p[lower[i]] || lower[i];
  }
  return res;
}

let dota = fs.readFileSync('src/data/dota.ts', 'utf-8');

// Replace hero persian names
dota = dota.replace(/fa:\ '([^']+)'/g, (match, enName) => {
  // If it's a known english name, transliterate it
  // Wait, the regex might catch descriptions. But descriptions have fa: 'something long'.
  // Actually, let's just do it cleanly for names: name: { en: 'Axe', fa: 'Axe' }
  return match; // fallback
});

// Better replacement for heroes and items name:
dota = dota.replace(/name:\ {\ en:\ '([^']+)',\ fa:\ '([^']+)'\ }/g, (match, en, fa) => {
  return `name: { en: '${en}', fa: '${translit(en)}' }`;
});

fs.writeFileSync('src/data/dota.ts', dota);
console.log("Transliteration applied.");
