import fs from 'fs';
import https from 'https';
import path from 'path';

async function download(url, dest) {
  return new Promise((resolve, reject) => {
    const file = fs.createWriteStream(dest);
    https.get(url, (response) => {
      if (response.statusCode === 200) {
        response.pipe(file);
        file.on('finish', () => { file.close(); resolve(true); });
      } else {
        file.close();
        fs.unlink(dest, () => resolve(false));
      }
    }).on('error', (err) => { fs.unlink(dest, () => {}); resolve(false); });
  });
}

async function run() {
  console.log("Fetching heroes from OpenDota...");
  const heroesRes = await fetch('https://api.opendota.com/api/heroes');
  const heroesData = await heroesRes.json();
  
  console.log("Fetching items from OpenDota...");
  const itemsRes = await fetch('https://api.opendota.com/api/constants/items');
  const itemsData = await itemsRes.json();

  fs.mkdirSync('public/assets/heroes', { recursive: true });
  fs.mkdirSync('public/assets/items', { recursive: true });

  let dotaTs = `export interface LocalizedString {
  en: string;
  fa: string;
}

export interface Hero {
  id: string;
  name: LocalizedString;
  img: string;
  roles: string[];
  primaryAttr: string;
  stats: { str: string; agi: string; int: string; };
}

export interface Item {
  id: string;
  name: LocalizedString;
  img: string;
  cost: number;
  category: string;
  description: LocalizedString;
  goodFor: LocalizedString;
}

export const heroes: Hero[] = [\n`;

  console.log("Processing heroes...");
  for (const h of heroesData) {
    const nameStr = h.localized_name.replace(/'/g, "\\'");
    const idName = h.name.replace('npc_dota_hero_', '');
    const imgUrl = "https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/" + idName + ".png";
    const localImg = "/assets/heroes/" + idName + ".png";
    
    // Start download in background
    download(imgUrl, "public" + localImg);
    
    dotaTs += `  { id: '${idName}', name: { en: '${nameStr}', fa: '${nameStr}' }, img: '${localImg}', roles: ${JSON.stringify(h.roles)}, primaryAttr: '${h.primary_attr}', stats: { str: '-', agi: '-', int: '-' } },\n`;
  }
  
  dotaTs += `];\n\nexport const items: Item[] = [\n`;
  
  const validItems = Object.values(itemsData).filter(i => i.name && !i.name.includes("recipe"));
  
  console.log("Processing items...");
  for (const i of validItems) {
    if (!i.dname) continue;
    const nameStr = i.dname.replace(/'/g, "\\'");
    const idName = i.name.replace('item_', '');
    const cost = i.cost;
    const imgUrl = "https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/items/" + idName + ".png";
    const localImg = "/assets/items/" + idName + ".png";
    
    download(imgUrl, "public" + localImg);

    const descEn = (i.hint ? i.hint[0] : '').replace(/'/g, "\\'").replace(/\n/g, " ").replace(/\r/g, "");
    
    let cat = 'early';
    if (cost > 4000) cat = 'late';
    else if (cost > 2000) cat = 'mid';
    else if (cost < 500) cat = 'consumable';

    dotaTs += `  { id: '${idName}', name: { en: '${nameStr}', fa: '${nameStr}' }, img: '${localImg}', cost: ${cost}, category: '${cat}', description: { en: '${descEn}', fa: '${descEn}' }, goodFor: { en: 'Situational', fa: 'بسته به شرایط' } },\n`;
  }
  
  dotaTs += `];\n`;
  
  fs.writeFileSync('src/data/dota.ts', dotaTs);
  console.log("Data generated and downloads started!");
}

run();
