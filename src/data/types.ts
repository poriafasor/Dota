export interface LocalizedString {
  en: string;
  fa: string;
}

export type PrimaryAttr = 'str' | 'agi' | 'int' | 'all';
export type AttackType = 'melee' | 'ranged';
export type ItemCategory = 'consumable' | 'early' | 'mid' | 'late' | 'neutral';
export type ItemTier = 'basic' | 'upgrade' | 'artifact' | 'neutral';

export interface HeroStats {
  strBase: number;
  strGain: number;
  agiBase: number;
  agiGain: number;
  intBase: number;
  intGain: number;
}

export interface Hero {
  id: string;
  name: LocalizedString;
  img: string;
  roles: string[];
  primaryAttr: PrimaryAttr;
  attackType: AttackType;
  range: number;
  moveSpeed: number;
  lore: LocalizedString;
  stats: HeroStats;
  rolesFull: string[];
}

export interface Item {
  id: string;
  name: LocalizedString;
  img: string;
  cost: number;
  category: ItemCategory;
  tier: ItemTier;
  description: LocalizedString;
  goodFor: LocalizedString;
  components?: string[]; // prerequisite item ids
  abilities?: LocalizedString;
  tags?: string[];
}

export interface RoleBuild {
  early: string[];   // up to 6 item ids
  mid: string[];     // up to 6 item ids
  late: string[];    // up to 6 item ids (final 6-slot)
  starting: string[]; // starting items (consumables + basic)
  situational: string[];
}

export interface HeroBuild {
  heroId: string;
  core: RoleBuild;       // core/default role build
  support: RoleBuild;    // support variant (for supports / flex)
  combos: LocalizedString;
  playstyle: LocalizedString;
  skillBuild: LocalizedString;
  counters: string[];    // hero ids that counter this hero
  goodAgainst: string[]; // hero ids this hero is good against
  difficulty: number;    // 1-3
  patchTier: number;     // 1-5 (S-E)
}
