import { useParams, Link, useNavigate } from 'react-router-dom';
import { items, getItem } from '@/data/dota';
import { useTranslation } from '@/hooks/useTranslation';
import { useStore } from '@/store/useStore';
import { cn } from '@/lib/utils';
import { ArrowLeft, Package, Coins, Zap, Layers, Link2 } from 'lucide-react';

export default function ItemDetail() {
  const { id } = useParams<{ id: string }>();
  const { t, dir, lang } = useTranslation();
  const navigate = useNavigate();
  const { addHistory } = useStore();

  const item = getItem(id || '');

  if (!item) {
    return (
      <div className="py-20 text-center">
        <p className="text-slate-400 mb-4">{t('noResults')}</p>
        <Link to="/items" className="text-emerald-400 hover:underline font-bold">{t('back')}</Link>
      </div>
    );
  }

  const components = (item.components || []).map(getItem).filter(Boolean) as typeof items;
  // Find items that use this item as a component
  const usedIn = items.filter(i => (i.components || []).includes(item.id));

  const catColor: Record<string, string> = {
    consumable: 'bg-amber-500/15 text-amber-300 border-amber-500/30',
    early: 'bg-emerald-500/15 text-emerald-300 border-emerald-500/30',
    mid: 'bg-blue-500/15 text-blue-300 border-blue-500/30',
    late: 'bg-red-500/15 text-red-300 border-red-500/30',
    neutral: 'bg-purple-500/15 text-purple-300 border-purple-500/30',
  };
  const tierColor: Record<string, string> = {
    basic: 'bg-slate-500/15 text-slate-300 border-slate-500/30',
    upgrade: 'bg-blue-500/15 text-blue-300 border-blue-500/30',
    artifact: 'bg-purple-500/15 text-purple-300 border-purple-500/30',
    neutral: 'bg-amber-500/15 text-amber-300 border-amber-500/30',
  };

  return (
    <div className="space-y-6">
      <button onClick={() => navigate(-1)} className="flex items-center gap-2 text-sm font-bold text-slate-400 hover:text-white transition-colors">
        <ArrowLeft className={cn("w-4 h-4", dir === 'rtl' && 'flip')} /> {t('back')}
      </button>

      {/* Header */}
      <section className="relative overflow-hidden rounded-3xl border border-white/10 bg-[#0d1117] p-5 md:p-8">
        <div className="flex flex-col md:flex-row gap-5">
          <div className="shrink-0">
            <img src={item.img} alt={item.name[lang]} className="w-28 h-28 md:w-36 md:h-36 rounded-2xl object-cover border-2 border-white/10 shadow-2xl" />
          </div>
          <div className="flex-1">
            <h1 className="text-3xl font-extrabold text-white">{item.name[lang]}</h1>
            <p className="text-sm text-slate-400 mt-1">{item.name.en}</p>

            <div className="flex flex-wrap gap-2 mt-3">
              <span className={cn("inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-bold border", catColor[item.category])}>
                <Package className="w-3.5 h-3.5" />
                {item.category === 'consumable' ? t('consumable') : item.category === 'early' ? t('earlyGameCat') : item.category === 'mid' ? t('midGameCat') : item.category === 'late' ? t('lateGameCat') : t('neutral')}
              </span>
              <span className={cn("px-3 py-1 rounded-full text-xs font-bold border", tierColor[item.tier] || tierColor.basic)}>
                {item.tier === 'basic' ? t('basic') : item.tier === 'upgrade' ? t('upgrade') : item.tier === 'artifact' ? t('artifact') : t('neutral')}
              </span>
              <span className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-bold border bg-amber-500/15 text-amber-300 border-amber-500/30">
                <Coins className="w-3.5 h-3.5" /> {item.cost} {t('gold')}
              </span>
            </div>

            {(item.tags || []).length > 0 && (
              <div className="flex flex-wrap gap-1.5 mt-3">
                {item.tags.map(tg => (
                  <span key={tg} className="px-2 py-0.5 rounded text-[10px] font-bold bg-white/5 text-slate-400 border border-white/10">#{tg}</span>
                ))}
              </div>
            )}
          </div>
        </div>
      </section>

      {/* Description */}
      <section className="rounded-2xl border border-emerald-500/30 bg-gradient-to-br from-emerald-950/30 to-[#0d1117] p-5">
        <h3 className="font-bold text-emerald-300 mb-2 flex items-center gap-2">
          <Package className="w-4 h-4" /> {t('itemDetails')}
        </h3>
        <p className="text-sm text-slate-200 leading-relaxed">{item.description[lang]}</p>
      </section>

      {/* Effects & abilities */}
      {item.abilities && item.abilities[lang] && (
        <section className="rounded-2xl border border-blue-500/30 bg-gradient-to-br from-blue-950/30 to-[#0d1117] p-5">
          <h3 className="font-bold text-blue-300 mb-2 flex items-center gap-2">
            <Zap className="w-4 h-4" /> {t('effects')}
          </h3>
          <p className="text-sm text-slate-200 leading-relaxed">{item.abilities[lang]}</p>
        </section>
      )}

      {/* Good for */}
      <section className="rounded-2xl border border-amber-500/30 bg-gradient-to-br from-amber-950/30 to-[#0d1117] p-5">
        <h3 className="font-bold text-amber-300 mb-2 flex items-center gap-2">
          <Layers className="w-4 h-4" /> {t('goodFor')}
        </h3>
        <p className="text-sm text-slate-200 leading-relaxed">{item.goodFor[lang]}</p>
      </section>

      {/* Components (prerequisites) */}
      <section className="rounded-2xl border border-white/10 bg-[#0d1117] p-5">
        <h3 className="font-bold text-white mb-4 flex items-center gap-2">
          <Link2 className="w-4 h-4 text-red-400" /> {t('components')}
        </h3>
        {components.length === 0 ? (
          <p className="text-sm text-slate-500">{t('noComponents')}</p>
        ) : (
          <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-3">
            {components.map(comp => (
              <Link key={comp.id} to={`/item/${comp.id}`} onClick={() => addHistory({ type: 'item', refId: comp.id, name: comp.name[lang] })}
                className="group flex items-center gap-2.5 p-2.5 rounded-xl bg-white/5 border border-white/10 hover:border-emerald-500/50 transition-all">
                <img src={comp.img} alt="" loading="lazy" className="w-12 h-12 rounded-lg object-cover bg-slate-800 border border-white/10" />
                <div className="min-w-0">
                  <p className="text-xs font-bold text-white truncate group-hover:text-emerald-300 transition-colors">{comp.name[lang]}</p>
                  <p className="text-[10px] text-amber-400 font-mono font-bold">{comp.cost}g</p>
                </div>
              </Link>
            ))}
          </div>
        )}
      </section>

      {/* Used in */}
      {usedIn.length > 0 && (
        <section className="rounded-2xl border border-white/10 bg-[#0d1117] p-5">
          <h3 className="font-bold text-white mb-4 flex items-center gap-2">
            <Layers className="w-4 h-4 text-purple-400" />
            {lang === 'fa' ? 'استفاده شده در ساخت:' : 'Used to build:'} ({usedIn.length})
          </h3>
          <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-3">
            {usedIn.map(parent => (
              <Link key={parent.id} to={`/item/${parent.id}`} onClick={() => addHistory({ type: 'item', refId: parent.id, name: parent.name[lang] })}
                className="group flex items-center gap-2.5 p-2.5 rounded-xl bg-white/5 border border-white/10 hover:border-purple-500/50 transition-all">
                <img src={parent.img} alt="" loading="lazy" className="w-12 h-12 rounded-lg object-cover bg-slate-800 border border-white/10" />
                <div className="min-w-0">
                  <p className="text-xs font-bold text-white truncate group-hover:text-purple-300 transition-colors">{parent.name[lang]}</p>
                  <p className="text-[10px] text-amber-400 font-mono font-bold">{parent.cost}g</p>
                </div>
              </Link>
            ))}
          </div>
        </section>
      )}
    </div>
  );
}
