// Aggregator: re-exports all data + helpers
export { heroes, HERO_COUNT } from './heroes';
export { items, getItem, ITEM_COUNT } from './items';
export { heroBuilds, getBuild } from './builds';
export { enrichments, ENRICHMENT_COUNT, type HeroEnrichment } from './enrichments';
export { ARCHETYPES, getArchetype } from './archetypes';
export * from './types';
import { heroes } from './heroes';
import { items } from './items';

export const getHero = (id: string) => heroes.find(h => h.id === id);
export const searchAll = (q: string) => {
  const query = q.toLowerCase().trim();
  if (!query) return { heroes: [], items: [] };
  return {
    heroes: heroes.filter(h => h.name.en.toLowerCase().includes(query) || h.name.fa.includes(q) || h.id.includes(query)),
    items: items.filter(i => i.name.en.toLowerCase().includes(query) || i.name.fa.includes(q) || i.id.includes(query)),
  };
};
