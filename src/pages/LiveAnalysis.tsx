import { useState, useMemo } from 'react';
import { Link } from 'react-router-dom';
import { heroes, items, heroBuilds, getHero, getItem } from '@/data/dota';
import { useTranslation } from '@/hooks/useTranslation';
import { useStore } from '@/store/useStore';
import { cn } from '@/lib/utils';
import { Activity, Plus, X, Swords, Shield, Zap, Target, Sparkles, Search } from 'lucide-react';

export default function LiveAnalysis() {
  const { t, dir, lang } = useTranslation();
  const { addHistory } = useStore();
  const [myHeroId, setMyHeroId] = useState('');
  const [enemyIds, setEnemyIds] = useState<string[]>([]);
  const [heroQuery, setHeroQuery] = useState('');
  const [enemyQuery, setEnemyQuery] = useState('');
  const [analyzed, setAnalyzed] = useState(false);

  const myHero = getHero(myHeroId);
  const myBuild = heroBuilds[myHeroId];

  // Counter picks: heroes whose goodAgainst list contains any of the enemy IDs
  const counterPicks = useMemo(() => {
    if (!enemyIds.length) return [];
    return heroes
      .filter(h => h.id !== myHeroId && !enemyIds.includes(h.id))
      .map(h => {
        const b = heroBuilds[h.id];
        const score = b?.goodAgainst.filter(g => enemyIds.includes(g)).length || 0;
        return { hero: h, score };
      })
      .filter(x => x.score > 0)
      .sort((a, b) => b.score - a.score)
      .slice(0, 6);
  }, [enemyIds, myHeroId]);

  // Items my hero should prioritize vs enemy lineup
  const recommendedItems = useMemo(() => {
    if (!myBuild || !enemyIds.length) return null;
    const enemies = enemyIds.map(getHero).filter(Boolean) as typeof heroes;
    const enemyTags: string[] = [];
    enemies.forEach(e => {
      e.roles.forEach(r => enemyTags.push(r));
      if (e.attackType === 'ranged') enemyTags.push('ranged');
      else enemyTags.push('melee');
      if (e.primaryAttr === 'int') enemyTags.push('magic-heavy');
      if (e.primaryAttr === 'agi') enemyTags.push('physical-heavy');
    });
    const hasMagic = enemyTags.includes('magic-heavy') || enemies.some(e => ['zuus','lina','skywrath_mage','leshrac','queenofpain'].includes(e.id));
    const hasPhysical = enemyTags.includes('physical-heavy') || enemies.some(e => ['phantom_assassin','juggernaut','troll_warlord','sniper','drow_ranger'].includes(e.id));
    const hasEvasion = enemies.some(e => ['phantom_assassin','windrunner','brewmaster'].includes(e.id));
    const hasHeal = enemies.some(e => ['huskar','necrolyte','alchemist','bristleback','life_stealer'].includes(e.id));
    const hasIllusions = enemies.some(e => ['phantom_lancer','naga_siren','chaos_knight','terrorblade'].includes(e.id));
    const hasInvis = enemies.some(e => ['riki','clinkz','nyx_assassin','bounty_hunter','weaver','templar_assassin'].includes(e.id));
    const hasTank = enemies.some(e => ['axe','centaur','bristleback','tidehunter','doom_bringer'].includes(e.id));

    const early: string[] = [];
    const mid: string[] = [];
    const late: string[] = [];
    const tips: string[] = [];

    if (hasMagic) { early.push('raindrop'); mid.push('pipe'); late.push('bkb'); tips.push(lang === 'fa' ? 'خطر آسیب جادویی زیاد — BKB و Pipe بگیرید.' : 'Heavy magic damage — get BKB + Pipe.'); }
    if (hasPhysical) { early.push('chain_mail'); mid.push('solar_crest'); late.push('assault'); tips.push(lang === 'fa' ? 'برست فیزیکی — زره و Crimson/Solar Cresr بگیرید.' : 'Physical burst — armor up with Crimson/Solar Crest.'); }
    if (hasEvasion) { late.push('monkey_king_bar'); tips.push(lang === 'fa' ? 'ایوژن دارند — Monkey King Bar الزامی است.' : 'They have evasion — Monkey King Bar is mandatory.'); }
    if (hasHeal) { mid.push('spirit_vessel'); tips.push(lang === 'fa' ? 'شفا زیاد دارند — Spirit Vessel برای کاهش ریجن.' : 'High heal — Spirit Vessel to cut regen.'); }
    if (hasIllusions) { mid.push('maelstrom'); late.push('mjollnir'); tips.push(lang === 'fa' ? 'ایلوژن دارند — Maelstrom/Mjollnir یا Battle Fury.' : 'Illusions — Maelstrom/Mjollnir or Battle Fury.'); }
    if (hasInvis) { early.push('dust'); mid.push('necronomicon'); late.push('gem'); tips.push(lang === 'fa' ? 'نامرئی دارند — Dust/Necronomicon/Gem بگیرید.' : 'Invis heroes — get Dust/Necronomicon/Gem.'); }
    if (hasTank) { mid.push('desolator'); late.push('greater_crit'); tips.push(lang === 'fa' ? 'تانک دارند — Desolator و Daedalus برای شکستن زره.' : 'Tanky lineup — Desolator + Daedalus to break armor.'); }

    // Skill priority
    let skill = myBuild.skillBuild[lang];
    if (enemyTags.includes('Disabler')) skill += lang === 'fa' ? ' اولویت به BKB زودرس.' : ' Prioritize early BKB.';
    if (enemyTags.includes('Initiator')) skill += lang === 'fa' ? ' پوزیشن عقب، فورس استف برای فرار.' : ' Position back, Force Staff to escape.';

    return { early: [...new Set(early)], mid: [...new Set(mid)], late: [...new Set(late)], tips, skill };
  }, [myBuild, enemyIds, lang]);

  const filteredHeroPicker = heroes.filter(h => {
    const q = heroQuery.toLowerCase().trim();
    return !q || h.name.en.toLowerCase().includes(q) || h.name.fa.includes(heroQuery) || h.id.includes(q);
  }).slice(0, 12);

  const filteredEnemyPicker = heroes.filter(h => {
    if (enemyIds.includes(h.id) || h.id === myHeroId) return false;
    const q = enemyQuery.toLowerCase().trim();
    return !q || h.name.en.toLowerCase().includes(q) || h.name.fa.includes(enemyQuery) || h.id.includes(q);
  }).slice(0, 8);

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-3xl font-extrabold text-white flex items-center gap-2">
          <Activity className="w-7 h-7 text-orange-400" /> {t('liveAnalysisTitle')}
        </h1>
      </div>

      {/* Setup */}
      <section className="grid md:grid-cols-2 gap-4">
        {/* My hero */}
        <div className="rounded-2xl border border-emerald-500/30 bg-gradient-to-br from-emerald-950/30 to-[#0d1117] p-5">
          <h3 className="font-bold text-emerald-300 mb-3 flex items-center gap-2"><Swords className="w-4 h-4" /> {t('myHero')}</h3>
          {myHero ? (
            <div className="flex items-center gap-3 p-2.5 rounded-xl bg-white/5 border border-white/10">
              <img src={myHero.img} alt="" className="w-14 h-16 rounded-lg object-cover" />
              <div className="flex-1">
                <p className="font-bold text-white">{myHero.name[lang]}</p>
                <p className="text-xs text-slate-400">{myHero.roles.slice(0,3).join(', ')}</p>
              </div>
              <button onClick={() => { setMyHeroId(''); setAnalyzed(false); }} className="text-slate-400 hover:text-red-400"><X className="w-5 h-5" /></button>
            </div>
          ) : (
            <>
              <div className="relative mb-2">
                <Search className={cn("absolute top-1/2 -translate-y-1/2 w-4 h-4 text-slate-400", dir === 'rtl' ? 'right-3' : 'left-3')} />
                <input value={heroQuery} onChange={e => setHeroQuery(e.target.value)} placeholder={t('selectYourHero')}
                  className={cn("w-full bg-[#161b22] border border-white/10 focus:border-emerald-500 rounded-lg py-2 text-sm font-medium text-white focus:outline-none",
                    dir === 'rtl' ? 'pr-9 pl-3' : 'pl-9 pr-3')} />
              </div>
              <div className="grid grid-cols-4 gap-2 max-h-60 overflow-y-auto">
                {filteredHeroPicker.map(h => (
                  <button key={h.id} onClick={() => { setMyHeroId(h.id); setHeroQuery(''); addHistory({ type: 'hero', refId: h.id, name: h.name[lang] }); }}
                    className="rounded-lg overflow-hidden bg-white/5 border border-white/10 hover:border-emerald-500/50 transition-all">
                    <img src={h.img} alt="" loading="lazy" className="w-full aspect-square object-cover" />
                    <p className="text-[9px] font-bold text-white truncate px-1 py-0.5">{h.name[lang]}</p>
                  </button>
                ))}
              </div>
            </>
          )}
        </div>

        {/* Enemy team */}
        <div className="rounded-2xl border border-red-500/30 bg-gradient-to-br from-red-950/30 to-[#0d1117] p-5">
          <h3 className="font-bold text-red-300 mb-3 flex items-center gap-2"><Shield className="w-4 h-4" /> {t('enemyTeam')} ({enemyIds.length}/5)</h3>
          {enemyIds.length > 0 && (
            <div className="flex flex-wrap gap-2 mb-3">
              {enemyIds.map(id => {
                const e = getHero(id);
                if (!e) return null;
                return (
                  <div key={id} className="flex items-center gap-1.5 bg-white/5 border border-white/10 rounded-lg p-1 pr-2">
                    <img src={e.img} alt="" className="w-8 h-10 rounded object-cover" />
                    <span className="text-xs font-bold text-white">{e.name[lang]}</span>
                    <button onClick={() => { setEnemyIds(enemyIds.filter(x => x !== id)); setAnalyzed(false); }} className="text-slate-400 hover:text-red-400 ms-1"><X className="w-4 h-4" /></button>
                  </div>
                );
              })}
            </div>
          )}
          {enemyIds.length < 5 && (
            <>
              <div className="relative mb-2">
                <Search className={cn("absolute top-1/2 -translate-y-1/2 w-4 h-4 text-slate-400", dir === 'rtl' ? 'right-3' : 'left-3')} />
                <input value={enemyQuery} onChange={e => setEnemyQuery(e.target.value)} placeholder={t('selectEnemy')}
                  className={cn("w-full bg-[#161b22] border border-white/10 focus:border-red-500 rounded-lg py-2 text-sm font-medium text-white focus:outline-none",
                    dir === 'rtl' ? 'pr-9 pl-3' : 'pl-9 pr-3')} />
              </div>
              <div className="grid grid-cols-4 gap-2 max-h-40 overflow-y-auto">
                {filteredEnemyPicker.map(h => (
                  <button key={h.id} onClick={() => { setEnemyIds([...enemyIds, h.id]); setEnemyQuery(''); setAnalyzed(false); }}
                    className="rounded-lg overflow-hidden bg-white/5 border border-white/10 hover:border-red-500/50 transition-all">
                    <img src={h.img} alt="" loading="lazy" className="w-full aspect-square object-cover" />
                    <p className="text-[9px] font-bold text-white truncate px-1 py-0.5">{h.name[lang]}</p>
                  </button>
                ))}
              </div>
            </>
          )}
        </div>
      </section>

      <div className="flex gap-3">
        <button onClick={() => setAnalyzed(true)} disabled={!myHeroId || enemyIds.length === 0}
          className="flex-1 py-3 rounded-xl bg-gradient-to-r from-orange-600 to-red-600 hover:from-orange-500 hover:to-red-500 text-white font-bold disabled:opacity-40 transition-all">
          {t('analyze')}
        </button>
        <button onClick={() => { setMyHeroId(''); setEnemyIds([]); setAnalyzed(false); }}
          className="px-5 py-3 rounded-xl bg-white/5 border border-white/10 text-slate-300 font-bold hover:bg-white/10 transition-all">
          {t('clear')}
        </button>
      </div>

      {analyzed && myHeroId && enemyIds.length > 0 ? (
        <div className="space-y-4">
          {/* Counter picks */}
          <section className="rounded-2xl border border-emerald-500/30 bg-[#0d1117] p-5">
            <h3 className="font-bold text-emerald-300 mb-3 flex items-center gap-2"><Sparkles className="w-4 h-4" /> {t('counterPicks')}</h3>
            {counterPicks.length === 0 ? (
              <p className="text-sm text-slate-500">{t('noResults')}</p>
            ) : (
              <div className="grid grid-cols-3 sm:grid-cols-4 md:grid-cols-6 gap-3">
                {counterPicks.map(({ hero, score }) => (
                  <Link key={hero.id} to={`/hero/${hero.id}`} onClick={() => addHistory({ type: 'hero', refId: hero.id, name: hero.name[lang] })}
                    className="group block rounded-xl overflow-hidden bg-white/5 border border-white/10 hover:border-emerald-500/50 transition-all">
                    <div className="aspect-[3/4] bg-slate-800 overflow-hidden">
                      <img src={hero.img} alt="" loading="lazy" className="w-full h-full object-cover group-hover:scale-110 transition-transform" />
                    </div>
                    <p className="text-xs font-bold text-white truncate px-1.5 py-1">{hero.name[lang]}</p>
                    <p className="text-[10px] text-emerald-400 font-bold px-1.5 pb-1">★ {score}</p>
                  </Link>
                ))}
              </div>
            )}
          </section>

          {/* Recommended items vs lineup */}
          {recommendedItems && (
            <section className="rounded-2xl border border-orange-500/30 bg-[#0d1117] p-5">
              <h3 className="font-bold text-orange-300 mb-4 flex items-center gap-2"><Zap className="w-4 h-4" /> {lang === 'fa' ? 'آیتم‌های پیشنهادی مقابل این ترکیب' : 'Recommended Items vs this lineup'}</h3>
              <div className="space-y-4">
                <ItemRow label={t('earlyItemVs')} ids={recommendedItems.early} lang={lang} addHistory={addHistory} color="emerald" />
                <ItemRow label={t('midItemVs')} ids={recommendedItems.mid} lang={lang} addHistory={addHistory} color="blue" />
                <ItemRow label={t('lateItemVs')} ids={recommendedItems.late} lang={lang} addHistory={addHistory} color="red" />
              </div>
            </section>
          )}

          {/* Skill priority */}
          {recommendedItems && (
            <section className="rounded-2xl border border-blue-500/30 bg-gradient-to-br from-blue-950/30 to-[#0d1117] p-5">
              <h3 className="font-bold text-blue-300 mb-2 flex items-center gap-2"><Target className="w-4 h-4" /> {t('skillPriority')}</h3>
              <p className="text-sm text-slate-200 leading-relaxed">{recommendedItems.skill}</p>
            </section>
          )}

          {/* Strategy tips */}
          {recommendedItems && recommendedItems.tips.length > 0 && (
            <section className="rounded-2xl border border-purple-500/30 bg-gradient-to-br from-purple-950/30 to-[#0d1117] p-5">
              <h3 className="font-bold text-purple-300 mb-3 flex items-center gap-2"><Sparkles className="w-4 h-4" /> {t('strategyTips')}</h3>
              <ul className="space-y-2">
                {recommendedItems.tips.map((tip, i) => (
                  <li key={i} className="text-sm text-slate-200 flex items-start gap-2">
                    <span className="text-purple-400 font-bold mt-0.5">►</span> {tip}
                  </li>
                ))}
              </ul>
            </section>
          )}
        </div>
      ) : (
        <div className="py-16 text-center text-slate-500">
          <Activity className="w-12 h-12 mx-auto mb-3 opacity-30" />
          {t('noAnalysis')}
        </div>
      )}
    </div>
  );
}

function ItemRow({ label, ids, lang, addHistory, color }: any) {
  const colorMap: Record<string, string> = { emerald: 'text-emerald-300', blue: 'text-blue-300', red: 'text-red-300' };
  if (!ids.length) return null;
  return (
    <div>
      <p className={cn("text-xs font-bold mb-2", colorMap[color])}>{label}</p>
      <div className="flex flex-wrap gap-2">
        {ids.map((id: string) => {
          const item = getItem(id);
          if (!item) return <span key={id} className="text-xs text-slate-500 bg-white/5 px-2 py-1 rounded">{id}</span>;
          return (
            <Link key={id} to={`/item/${item.id}`} onClick={() => addHistory({ type: 'item', refId: item.id, name: item.name[lang] })}
              className="group flex items-center gap-2 bg-white/5 border border-white/10 rounded-lg p-1.5 pr-3 hover:border-white/30 transition-all">
              <img src={item.img} alt="" loading="lazy" className="w-10 h-10 rounded object-cover bg-slate-800" />
              <span className="text-xs font-bold text-white group-hover:text-amber-300 transition-colors">{item.name[lang]}</span>
            </Link>
          );
        })}
      </div>
    </div>
  );
}
