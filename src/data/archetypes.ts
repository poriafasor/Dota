// Archetype build templates: 6-slot role-based builds (patch 7.39+ meta)
// Each archetype defines starting items, early/mid/late 6-slot builds, and situational items.

export interface ArchetypeBuild {
  starting: string[];
  early: string[];
  mid: string[];
  late: string[];
  situational: string[];
}

export const ARCHETYPES: Record<string, ArchetypeBuild> = {
  // AGI carries - mobility + right-click (Anti-Mage, Slark, Medusa, Spectre, Drow, Sniper, Luna, Troll, PA, PL, Naga, Riki, Weaver, Clinkz, Meepo, Lone Druid, TB, Arc Warden, Ember, MK, Kez, Gyro, Ursa, Hoodwink)
  agi_carry: {
    starting: ['tango', 'flask', 'branches', 'branches', 'wraith_band', 'boots'],
    early: ['power_treads', 'wraith_band', 'magic_wand', 'boots', 'ring_of_wraith_band', 'orb_of_corrosion'],
    mid: ['power_treads', 'manta', 'bkb', 'wraith_band', 'blink', 'diffusal_blade'],
    late: ['power_treads', 'manta', 'bkb', 'butterfly', 'skadi', 'abyssal_blade'],
    situational: ['satanic', 'daedalus', 'monkey_king_bar', 'linkens_sphere', 'heart', 'assault'],
  },

  // AGI farming carries - Battle Fury core (PA, Jugg, Sven, Faceless, Alchemist, Lifestealer, Lycan, CK, Tiny)
  agi_carry_farming: {
    starting: ['tango', 'flask', 'branches', 'branches', 'wraith_band', 'stout_shield'],
    early: ['power_treads', 'wraith_band', 'magic_wand', 'battle_fury', 'boots', 'bracer'],
    mid: ['power_treads', 'battle_fury', 'bkb', 'blink', 'desolator', 'echo_sabre'],
    late: ['power_treads', 'battle_fury', 'bkb', 'abyssal_blade', 'satanic', 'assault'],
    situational: ['daedalus', 'butterfly', 'heart', 'monkey_king_bar', 'silver_edge', 'greater_crit'],
  },

  // INT mid casters - nukers/control (SF, Invoker, Storm, QoP, Tinker, Zeus, Lina, Leshrac, OD, Puck, Pugna, Necro, DP, Silencer, Muerta, Void Spirit, TA)
  int_mid_caster: {
    starting: ['tango', 'flask', 'branches', 'branches', 'null_talisman', 'boots'],
    early: ['power_treads', 'null_talisman', 'magic_wand', 'witch_blade', 'boots', 'bottle'],
    mid: ['power_treads', 'kaya_and_sange', 'bkb', 'witch_blade', 'aghs_scepter', 'blink'],
    late: ['power_treads', 'octarine_core', 'bkb', 'aghs_scepter', 'scythe_of_vyse', 'shivas_guard'],
    situational: ['bloodthorn', 'ethereal_blade', 'refresh_refresher', 'linkens_sphere', 'aghanims_shard', 'rod_of_atos'],
  },

  // STR offlane tanks/initiators (Axe, Centaur, Tide, Bristle, Slardar, Doom, Timber, Magnus, NS, SB, Kunkka, DK, Huskar, Tusk, LC, Primal Beast, Mars, Dawnbreaker, ET, Underlord, Largo, Brewmaster, Beastmaster, Clockwerk)
  str_offlane_tank: {
    starting: ['tango', 'flask', 'branches', 'branches', 'gauntlets', 'stout_shield'],
    early: ['phase_boots', 'bracer', 'vanguard', 'magic_wand', 'helm_of_iron_will', 'ring_of_basilius'],
    mid: ['phase_boots', 'vanguard', 'blink', 'bkb', 'bracer', 'crimson_guard'],
    late: ['phase_boots', 'blink', 'bkb', 'assault', 'heart', 'shivas_guard'],
    situational: ['crimson_guard', 'blade_mail', 'spirit_vessel', 'lotus_orb', 'heavens_halberd', 'pipe'],
  },

  // INT pos 5 supports (CM, Lion, SS, Rubick, Dazzle, Oracle, AA, Lich, WD, Warlock, SD, Disruptor, KotL, Visage, Jakiro, Enchantress, Chen, Enigma, Winter Wyvern, Bane, Earth Spirit, Ogre, Treant, Undying, Snapfire, Phoenix, ES, SK, Venomancer, Techies, Io, Grimstroke, Ringmaster, Dark Willow)
  int_support_5: {
    starting: ['tango', 'flask', 'branches', 'wind_lace', 'ring_of_basilius', 'observer_ward'],
    early: ['arcane_boots', 'magic_wand', 'urn_of_shadows', 'ring_of_basilius', 'tranquil_boots', 'glimmer_cape'],
    mid: ['arcane_boots', 'force_staff', 'urn_of_shadows', 'glimmer_cape', 'mekansm', 'solar_crest'],
    late: ['guardian_greaves', 'force_staff', 'spirit_vessel', 'scythe_of_vyse', 'solar_crest', 'pipe'],
    situational: ['aghs_scepter', 'refresh_refresher', 'lotus_orb', 'rod_of_atos', 'pavise', 'aghs_shard'],
  },

  // Universal utility / flex (Mirana, Windranger, Pudge, Venge, Razor, Viper, Morph, Bloodseeker, Furion, Pangolier, Marci, Nyx, Bounty, Batrider)
  universal_utility: {
    starting: ['tango', 'flask', 'branches', 'branches', 'bracer', 'boots'],
    early: ['phase_boots', 'bracer', 'magic_wand', 'null_talisman', 'boots', 'falcon_blade'],
    mid: ['phase_boots', 'bracer', 'bkb', 'force_staff', 'solar_crest', 'pipe'],
    late: ['phase_boots', 'bkb', 'scythe_of_vyse', 'solar_crest', 'pipe', 'heavens_halberd'],
    situational: ['aghs_scepter', 'refresh_refresher', 'lotus_orb', 'rod_of_atos', 'orchid', 'aghs_shard'],
  },
};

export const getArchetype = (name: string): ArchetypeBuild =>
  ARCHETYPES[name] || ARCHETYPES.universal_utility;
