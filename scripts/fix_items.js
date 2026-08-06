import fs from 'fs';

async function run() {
  const itemsRes = await fetch('https://api.opendota.com/api/constants/items');
  const itemsData = await itemsRes.json();
  
  const validItems = Object.entries(itemsData).filter(([key, i]) => {
    if (!i.dname) return false;
    if (key.includes('recipe')) return false;
    return true;
  });

  let dotaTs = fs.readFileSync('src/data/dota.ts', 'utf-8');
  dotaTs = dotaTs.split('export const items: Item[] =')[0];
  
  dotaTs += `export const items: Item[] = [\n`;
  for (const [key, i] of validItems) {
    const nameStr = i.dname.replace(/'/g, "\\'");
    let idName = key.replace('item_', '');
    const cost = i.cost || 0;
    const imgUrl = "https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/items/" + idName + ".png";

    const descEn = (i.hint && i.hint.length ? i.hint[0] : '').replace(/'/g, "\\'").replace(/\n/g, " ").replace(/\r/g, "");
    
    let cat = 'neutral';
    if (cost > 4000) cat = 'late';
    else if (cost > 2000) cat = 'mid';
    else if (cost > 0) cat = 'early';

    dotaTs += `  { id: '${idName}', name: { en: '${nameStr}', fa: '${nameStr}' }, img: '${imgUrl}', cost: ${cost}, category: '${cat}', description: { en: '${descEn}', fa: '${descEn}' }, goodFor: { en: 'Situational', fa: 'بسته به شرایط' } },\n`;
  }
  dotaTs += `];\n`;
  
  fs.writeFileSync('src/data/dota.ts', dotaTs);
  console.log("Fixed items array properly!");
}
run();
