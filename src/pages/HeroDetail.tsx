import { useParams, Link, useNavigate } from 'react-router-dom';
import { useState } from 'react';
import { heroes, items, heroBuilds, getItem, getHero } from '@/data/dota';
import { useTranslation } from '@/hooks/useTranslation';
import { useStore } from '@/store/useStore';
import { cn } from '@/lib/utils';
import { ArrowLeft, Star, Save, X, Swords, Shield, Zap, Target, Sparkles, AlertTriangle } from 'lucide-react';

export default function HeroDetail() {
  const { id } = useParams<{ id: string }>();
  const { t, dir, lang } = useTranslation();
  const navigate = useNavigate();
  const { favorites, toggleFavorite, addHistory, saveBuild } = useStore();
  const [activeRole, setActiveRole] = useState<'core' | 'support'>('core');
  const [showSave, setShowSave] = useState(false);
  const [buildName, setBuildName] = useState('');
  const [buildNotes, setBuildNotes] = useState('');

  const hero = getHero(id || '');
  const build = heroBuilds[id || ''];

  if (!hero) {
    return (
      <div className="py-20 text-center">
        <p className="text-slate-400 mb-4">{t('noResults')}</p>
        <Link to="/heroes" className="text-red-400 hover:underline font-bold">{t('back')}</Link>
      </div>
    );
  }

  const isFav = favorites.includes(hero.id);
  const roleBuild = build?.[activeRole];
  const sections: { key: 'starting' | 'early' | 'mid' | 'late' | 'situational'; label: string; icon: any; color: string }[] = [
    { key: 'starting', label: t('startingItems'), icon: Sparkles, color: 'amber' },
    { key: 'early', label: t('earlyGame'), icon: Zap, color: 'emerald' },
    { key: 'mid', label: t('midGame'), icon: Target, color: 'blue' },
    { key: 'late', label: t('lateGame'), icon: Swords, color: 'red' },
    { key: 'situational', label: t('situational'), icon: AlertTriangle, color: 'purple' },
  ];

  const attrColors: Record<string, string> = { str: 'text-red-400', agi: 'text-emerald-400', int: 'text-blue-400', all: 'text-amber-400' };
  const attrLabel: Record<string, { en: string; fa: string }> = {
    str: { en: 'Strength', fa: 'قدرت' }, agi: { en: 'Agility', fa: 'چابکی' },
    int: { en: 'Intelligence', fa: 'هوش' }, all: { en: 'Universal', fa: 'یونیورسال' },
  };

  const handleSave = () => {
    if (!buildName.trim() || !roleBuild) return;
    saveBuild({
      id: `${hero.id}-${Date.now()}`, heroId: hero.id, name: buildName.trim(),
      role: activeRole, earlyGame: roleBuild.early, midGame: roleBuild.mid,
      lateGame: roleBuild.late, notes: buildNotes.trim(), date: new Date().toISOString(),
    });
    setShowSave(false); setBuildName(''); setBuildNotes('');
  };

  return (
    <div className="space-y-6">
      <button onClick={() => navigate(-1)} className="flex items-center gap-2 text-sm font-bold text-slate-400 hover:text-white transition-colors">
        <ArrowLeft className={cn("w-4 h-4", dir === 'rtl' && 'flip')} /> {t('back')}
      </button>

      {/* Hero header */}
      <section className="relative overflow-hidden rounded-3xl border border-white/10 bg-[#0d1117]">
        <div className="absolute inset-0 opacity-30">
          <img src={hero.img} alt="" className="w-full h-full object-cover blur-2xl scale-110" />
        </div>
        <div className="relative p-5 md:p-8 flex flex-col md:flex-row gap-5">
          <div className="shrink-0">
            <img src={hero.img} alt={hero.name[lang]} className="w-40 h-56 md:w-48 md:h-64 rounded-2xl object-cover border-2 border-white/10 shadow-2xl" />
          </div>
          <div className="flex-1">
            <div className="flex items-start justify-between gap-3">
              <div>
                <h1 className="text-3xl md:text-4xl font-extrabold text-white">{hero.name[lang]}</h1>
                <p className="text-sm text-slate-400 mt-1">{hero.name.en} · ID: {hero.id}</p>
              </div>
              <div className="flex gap-2">
                <button onClick={() => toggleFavorite(hero.id)}
                  className={cn("p-2.5 rounded-xl border transition-all", isFav ? "bg-amber-500/20 border-amber-500/50 text-amber-300" : "bg-white/5 border-white/10 text-slate-400 hover:text-amber-300")}>
                  <Star className="w-5 h-5" fill={isFav ? 'currentColor' : 'none'} />
                </button>
              </div>
            </div>

            {/* Roles */}
            <div className="flex flex-wrap gap-2 mt-4">
              {hero.roles.map(r => (
                <span key={r} className="px-2.5 py-1 rounded-full text-xs font-bold bg-red-500/15 text-red-300 border border-red-500/30">{r}</span>
              ))}
            </div>

            {/* Stats grid */}
            <div className="grid grid-cols-2 md:grid-cols-4 gap-2 mt-4">
              <Stat label={t('attributes')} value={`${attrLabel[hero.primaryAttr][lang]}`} sub={`STR ${hero.stats.strBase}+${hero.stats.strGain}`} color={attrColors[hero.primaryAttr]} icon={Swords} />
              <Stat label="AGI" value={`${hero.stats.agiBase}`} sub={`+${hero.stats.agiGain}/lvl`} color="text-emerald-400" icon={Target} />
              <Stat label="INT" value={`${hero.stats.intBase}`} sub={`+${hero.stats.intGain}/lvl`} color="text-blue-400" icon={Zap} />
              <Stat label={t('moveSpeed')} value={`${hero.moveSpeed}`} sub={hero.attackType === 'melee' ? (lang === 'fa' ? 'میل' : 'Melee') : (lang === 'fa' ? 'رنج' : 'Ranged')} color="text-amber-400" icon={Shield} />
            </div>

            <p className="text-xs text-slate-400 mt-3 italic">{hero.lore[lang]}</p>
          </div>
        </div>
      </section>

      {/* Tier & difficulty */}
      {build && (
        <section className="grid grid-cols-2 gap-3">
          <div className="rounded-xl border border-white/10 bg-[#0d1117] p-4 flex items-center gap-3">
            <span className={cn("w-10 h-10 rounded-lg flex items-center justify-center font-extrabold text-sm", `tier-${['D','C','B','A','S'][build.patchTier-1] || 'tier-D'}`)}>
              {['D','C','B','A','S'][build.patchTier-1] || 'D'}
            </span>
            <div>
              <p className="text-xs text-slate-400 font-semibold">{t('patchTier')}</p>
              <p className="font-bold text-white">{t(('tier' + (['D','C','B','A','S'][build.patchTier-1] || 'D')) as any)}</p>
            </div>
          </div>
          <div className="rounded-xl border border-white/10 bg-[#0d1117] p-4 flex items-center gap-3">
            <span className="w-10 h-10 rounded-lg flex items-center justify-center bg-white/10 font-extrabold text-sm text-white">{build.difficulty}</span>
            <div>
              <p className="text-xs text-slate-400 font-semibold">{t('difficulty')}</p>
              <p className="font-bold text-white">{build.difficulty === 1 ? t('easy') : build.difficulty === 2 ? t('medium') : t('hard')}</p>
            </div>
          </div>
        </section>
      )}

      {/* Build section */}
      {build && roleBuild && (
        <section className="space-y-4">
          <div className="flex items-center justify-between flex-wrap gap-3">
            <h2 className="text-xl font-bold text-white flex items-center gap-2">
              <Swords className="w-5 h-5 text-red-400" /> {t('itemBuild')}
            </h2>
            <div className="flex gap-2">
              <button onClick={() => setActiveRole('core')}
                className={cn("px-3 py-1.5 rounded-lg text-sm font-bold transition-all", activeRole === 'core' ? "bg-red-500/20 border border-red-500/50 text-red-300" : "bg-white/5 border border-white/10 text-slate-400")}>
                {t('coreRole')}
              </button>
              <button onClick={() => setActiveRole('support')}
                className={cn("px-3 py-1.5 rounded-lg text-sm font-bold transition-all", activeRole === 'support' ? "bg-emerald-500/20 border border-emerald-500/50 text-emerald-300" : "bg-white/5 border border-white/10 text-slate-400")}>
                {t('supportRole')}
              </button>
              <button onClick={() => setShowSave(true)}
                className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-sm font-bold bg-amber-500/20 border border-amber-500/50 text-amber-300 hover:bg-amber-500/30 transition-all">
                <Save className="w-4 h-4" /> {t('saveBuild')}
              </button>
            </div>
          </div>

          {sections.map(sec => {
            const list = roleBuild[sec.key] || [];
            if (!list.length) return null;
            const colorMap: Record<string, string> = {
              amber: 'border-amber-500/30 text-amber-300', emerald: 'border-emerald-500/30 text-emerald-300',
              blue: 'border-blue-500/30 text-blue-300', red: 'border-red-500/30 text-red-300', purple: 'border-purple-500/30 text-purple-300',
            };
            return (
              <div key={sec.key} className={cn("rounded-2xl border bg-[#0d1117] p-4", colorMap[sec.color])}>
                <div className="flex items-center gap-2 mb-3">
                  <sec.icon className="w-4 h-4" />
                  <h3 className="font-bold text-sm">{sec.label}</h3>
                  <span className="text-xs text-slate-500">({list.length} {lang === 'fa' ? 'اسلات' : 'slots'})</span>
                </div>
                <div className="grid grid-cols-3 sm:grid-cols-4 md:grid-cols-6 gap-2">
                  {list.map((itemId, idx) => {
                    const item = getItem(itemId);
                    if (!item) return (
                      <div key={idx} className="aspect-square rounded-lg bg-white/5 border border-white/10 flex items-center justify-center text-xs text-slate-500 p-1 text-center">
                        {itemId}
                      </div>
                    );
                    return (
                      <Link key={idx} to={`/item/${item.id}`} onClick={() => addHistory({ type: 'item', refId: item.id, name: item.name[lang] })}
                        className="group block rounded-lg overflow-hidden bg-white/5 border border-white/10 hover:border-amber-400/60 transition-all">
                        <div className="aspect-square bg-slate-800 overflow-hidden">
                          <img src={item.img} alt={item.name[lang]} loading="lazy" className="w-full h-full object-cover group-hover:scale-110 transition-transform" />
                        </div>
                        <p className="text-[10px] font-bold text-white truncate px-1 py-1">{item.name[lang]}</p>
                      </Link>
                    );
                  })}
                </div>
              </div>
            );
          })}
        </section>
      )}

      {/* Combos & playstyle */}
      {build && (
        <section className="grid md:grid-cols-2 gap-4">
          <div className="rounded-2xl border border-red-500/30 bg-gradient-to-br from-red-950/30 to-[#0d1117] p-5">
            <h3 className="font-bold text-red-300 mb-3 flex items-center gap-2"><Zap className="w-4 h-4" /> {t('combos')}</h3>
            <p className="text-sm text-slate-200 leading-relaxed">{build.combos[lang]}</p>
          </div>
          <div className="rounded-2xl border border-emerald-500/30 bg-gradient-to-br from-emerald-950/30 to-[#0d1117] p-5">
            <h3 className="font-bold text-emerald-300 mb-3 flex items-center gap-2"><Target className="w-4 h-4" /> {t('playstyle')}</h3>
            <p className="text-sm text-slate-200 leading-relaxed">{build.playstyle[lang]}</p>
          </div>
          <div className="rounded-2xl border border-blue-500/30 bg-gradient-to-br from-blue-950/30 to-[#0d1117] p-5 md:col-span-2">
            <h3 className="font-bold text-blue-300 mb-3 flex items-center gap-2"><Sparkles className="w-4 h-4" /> {t('skillBuild')}</h3>
            <p className="text-sm text-slate-200 leading-relaxed">{build.skillBuild[lang]}</p>
          </div>
        </section>
      )}

      {/* Counters */}
      {build && (build.counters.length > 0 || build.goodAgainst.length > 0) && (
        <section className="grid md:grid-cols-2 gap-4">
          <CounterBox title={t('counters')} heroes={build.counters.map(getHero).filter(Boolean) as any} lang={lang} color="red" t={t} addHistory={addHistory} />
          <CounterBox title={t('goodAgainst')} heroes={build.goodAgainst.map(getHero).filter(Boolean) as any} lang={lang} color="emerald" t={t} addHistory={addHistory} />
        </section>
      )}

      {/* Save modal */}
      {showSave && (
        <div className="fixed inset-0 z-50 bg-black/70 backdrop-blur-sm flex items-center justify-center p-4" onClick={() => setShowSave(false)}>
          <div className="bg-[#0d1117] border border-white/10 rounded-2xl p-6 w-full max-w-md" onClick={e => e.stopPropagation()}>
            <div className="flex items-center justify-between mb-4">
              <h3 className="text-lg font-bold text-white">{t('saveAsBuild')}</h3>
              <button onClick={() => setShowSave(false)} className="text-slate-400 hover:text-white"><X className="w-5 h-5" /></button>
            </div>
            <div className="space-y-3">
              <input value={buildName} onChange={e => setBuildName(e.target.value)} placeholder={t('buildName')}
                className="w-full bg-[#161b22] border border-white/10 focus:border-red-500 rounded-lg px-3 py-2.5 text-white text-sm font-medium focus:outline-none" />
              <textarea value={buildNotes} onChange={e => setBuildNotes(e.target.value)} placeholder={t('buildNotes')} rows={3}
                className="w-full bg-[#161b22] border border-white/10 focus:border-red-500 rounded-lg px-3 py-2.5 text-white text-sm font-medium focus:outline-none resize-none" />
              <div className="flex gap-2">
                <button onClick={handleSave} disabled={!buildName.trim()}
                  className="flex-1 py-2.5 rounded-lg bg-gradient-to-r from-red-600 to-orange-600 hover:from-red-500 hover:to-orange-500 text-white font-bold text-sm disabled:opacity-40 transition-all">
                  {t('save')}
                </button>
                <button onClick={() => setShowSave(false)}
                  className="px-4 py-2.5 rounded-lg bg-white/5 border border-white/10 text-slate-300 font-bold text-sm hover:bg-white/10 transition-all">
                  {t('cancel')}
                </button>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

function Stat({ label, value, sub, color, icon: Icon }: { label: string; value: string; sub?: string; color: string; icon: any }) {
  return (
    <div className="rounded-xl bg-white/5 border border-white/10 p-3">
      <div className="flex items-center gap-1.5 mb-1">
        <Icon className={cn("w-3.5 h-3.5", color)} />
        <p className="text-[10px] text-slate-400 font-bold uppercase tracking-wide">{label}</p>
      </div>
      <p className={cn("text-xl font-extrabold", color)}>{value}</p>
      {sub && <p className="text-[10px] text-slate-500 font-medium">{sub}</p>}
    </div>
  );
}

function CounterBox({ title, heroes: heroList, lang, color, t, addHistory }: any) {
  const colorMap: Record<string, string> = {
    red: 'border-red-500/30 text-red-300', emerald: 'border-emerald-500/30 text-emerald-300',
  };
  return (
    <div className={cn("rounded-2xl border bg-[#0d1117] p-4", colorMap[color])}>
      <h3 className="font-bold text-sm mb-3">{title}</h3>
      <div className="flex flex-wrap gap-2">
        {heroList.map((h: any) => (
          <Link key={h.id} to={`/hero/${h.id}`} onClick={() => addHistory({ type: 'hero', refId: h.id, name: h.name[lang] })}
            className="flex items-center gap-2 bg-white/5 border border-white/10 rounded-lg p-1.5 pr-3 hover:border-white/30 transition-all">
            <img src={h.img} alt="" loading="lazy" className="w-8 h-10 rounded object-cover" />
            <span className="text-xs font-bold text-white">{h.name[lang]}</span>
          </Link>
        ))}
      </div>
    </div>
  );
}
