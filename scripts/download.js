// Download all hero & item images locally for offline use.
import fs from 'fs';
import https from 'https';
import path from 'path';
import { heroes } from '../src/data/heroes.ts';
import { items } from '../src/data/items.ts';

const CDN = 'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react';
const heroDir = path.join(process.cwd(), 'public/assets/heroes');
const itemDir = path.join(process.cwd(), 'public/assets/items');
fs.mkdirSync(heroDir, { recursive: true });
fs.mkdirSync(itemDir, { recursive: true });

const download = (url, dest) => new Promise((resolve) => {
  if (fs.existsSync(dest) && fs.statSync(dest).size > 1000) return resolve('cached');
  const file = fs.createWriteStream(dest);
  https.get(url, (res) => {
    if (res.statusCode === 200) { res.pipe(file); file.on('finish', () => { file.close(); resolve('ok'); }); }
    else { file.close(); fs.unlink(dest, () => resolve(`skip:${res.statusCode}`)); }
  }).on('error', () => { fs.unlink(dest, () => resolve('err')); });
});

async function run() {
  console.log(`Downloading ${heroes.length} heroes + ${items.length} items...`);
  let hOk = 0, iOk = 0;
  for (const h of heroes) {
    const r = await download(`${CDN}/heroes/${h.id}.png`, path.join(heroDir, `${h.id}.png`));
    if (r === 'ok' || r === 'cached') hOk++;
  }
  for (const i of items) {
    const r = await download(`${CDN}/items/${i.id}.png`, path.join(itemDir, `${i.id}.png`));
    if (r === 'ok' || r === 'cached') iOk++;
  }
  console.log(`Done: ${hOk}/${heroes.length} heroes, ${iOk}/${items.length} items.`);
}
run();
