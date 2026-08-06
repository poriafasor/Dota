import { useState, useMemo } from 'react';
import { Link } from 'react-router-dom';
import { motion, AnimatePresence } from 'framer-motion';
import { items } from '@/data/dota';
import { useTranslation } from '@/hooks/useTranslation';
import { useStore } from '@/store/useStore';
import { Search, Package } from 'lucide-react';
import { cn } from '@/lib/utils';

export default function Items() {
  const { t, dir, lang } = useTranslation();
  const { addHistory } = useStore();
  const [query, setQuery] = useState('');
  const [cat, setCat] = useState<string>('all');
  const [tag, setTag] = useState<string>('all');

  const categories = [
    { id: 'all', label: t('allItems') },
    { id: 'consumable', label: t('consumable') },
    { id: 'early', label: t('earlyGameCat') },
    { id: 'mid', label: t('midGameCat') },
    { id: 'late', label: t('lateGameCat') },
    { id: 'neutral', label: t('neutral') },
  ];

  const allTags = useMemo(() => {
    const s = new Set<string>();
    items.forEach(i => (i.tags || []).forEach(tg => s.add(tg)));
    return ['all', ...Array.from(s).sort()];
  }, []);

  const filtered = useMemo(() => {
    const q = query.toLowerCase().trim();
    return items.filter(i => {
      const matchQ = !q || i.name.en.toLowerCase().includes(q) || i.name.fa.includes(query) || i.id.includes(q)
        || i.goodFor.en.toLowerCase().includes(q) || i.goodFor.fa.includes(query);
      const matchCat = cat === 'all' || i.category === cat;
      const matchTag = tag === 'all' || (i.tags || []).includes(tag);
      return matchQ && matchCat && matchTag;
    });
  }, [query, cat, tag]);

  const catColor: Record<string, string> = {
    consumable: 'bg-amber-500/15 text-amber-300 border-amber-500/30',
    early: 'bg-emerald-500/15 text-emerald-300 border-emerald-500/30',
    mid: 'bg-blue-500/15 text-blue-300 border-blue-500/30',
    late: 'bg-red-500/15 text-red-300 border-red-500/30',
    neutral: 'bg-purple-500/15 text-purple-300 border-purple-500/30',
  };

  return (
    <div className="space-y-6">
      <div className="flex flex-col gap-4">
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
          <div>
            <h1 className="text-3xl font-extrabold text-white flex items-center gap-2">
              <span className="text-emerald-500">📦</span> {t('items')}
              <span className="text-sm font-bold text-slate-500">({items.length})</span>
            </h1>
          </div>
          <div className="relative w-full md:w-96">
            <Search className={cn("absolute top-1/2 -translate-y-1/2 w-5 h-5 text-slate-400", dir === 'rtl' ? 'right-4' : 'left-4')} />
            <input value={query} onChange={e => setQuery(e.target.value)} placeholder={t('searchItems')}
              className={cn("w-full bg-[#161b22] border-2 border-white/10 focus:border-emerald-500 rounded-xl py-3 text-base font-bold text-white placeholder:font-medium placeholder:text-slate-500 focus:outline-none focus:ring-4 focus:ring-emerald-500/20 transition-all",
                dir === 'rtl' ? 'pr-12 pl-4' : 'pl-12 pr-4')} />
          </div>
        </div>

        <div className="flex flex-wrap gap-2">
          {categories.map(c => (
            <button key={c.id} onClick={() => setCat(c.id)}
              className={cn("px-3.5 py-1.5 rounded-lg text-sm font-bold border transition-all",
                cat === c.id ? "bg-white/10 border-white/30 text-white" : "bg-transparent border-white/10 text-slate-400 hover:bg-white/5")}>
              {c.label}
            </button>
          ))}
        </div>

        {allTags.length > 1 && (
          <div className="flex flex-wrap gap-1.5">
            {allTags.slice(0, 24).map(tg => (
              <button key={tg} onClick={() => setTag(tg)}
                className={cn("px-2.5 py-0.5 rounded-full text-[11px] font-semibold border transition-all",
                  tag === tg ? "bg-emerald-500/20 border-emerald-500/50 text-emerald-300" : "bg-transparent border-white/10 text-slate-500 hover:text-slate-300")}>
                {tg === 'all' ? (lang === 'fa' ? 'همه تگ‌ها' : 'All tags') : tg}
              </button>
            ))}
          </div>
        )}
      </div>

      <p className="text-sm text-slate-400">{filtered.length} / {items.length}</p>

      <motion.div layout className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-3">
        <AnimatePresence>
          {filtered.map(item => (
            <motion.div key={item.id} layout initial={{ opacity: 0, scale: 0.95 }} animate={{ opacity: 1, scale: 1 }} exit={{ opacity: 0 }}>
              <Link to={`/item/${item.id}`} onClick={() => addHistory({ type: 'item', refId: item.id, name: item.name[lang] })}
                className="group block h-full p-4 bg-[#0d1117] border border-white/10 rounded-2xl hover:border-emerald-500/50 hover:bg-emerald-500/5 transition-all">
                <div className="flex gap-3">
                  <img src={item.img} alt={item.name[lang]} loading="lazy"
                    className="w-16 h-16 rounded-lg object-cover bg-slate-800 border border-white/10 shrink-0 group-hover:scale-105 transition-transform" />
                  <div className="flex-1 min-w-0">
                    <div className="flex items-start justify-between gap-2">
                      <h3 className="text-sm font-bold text-white group-hover:text-emerald-300 transition-colors truncate">{item.name[lang]}</h3>
                      <span className="text-xs font-mono font-bold text-amber-400 bg-amber-500/10 px-1.5 py-0.5 rounded shrink-0">{item.cost}</span>
                    </div>
                    <span className={cn("inline-block text-[10px] font-bold px-2 py-0.5 rounded border mt-1", catColor[item.category])}>
                      {categories.find(c => c.id === item.category)?.label || item.category}
                    </span>
                    <p className="text-[11px] text-slate-400 mt-2 line-clamp-2 leading-relaxed">{item.description[lang]}</p>
                    <p className="text-[10px] text-emerald-400/80 font-semibold mt-1.5 line-clamp-1">
                      <span className="text-slate-500">{t('goodFor')}:</span> {item.goodFor[lang]}
                    </p>
                  </div>
                </div>
              </Link>
            </motion.div>
          ))}
        </AnimatePresence>
      </motion.div>

      {filtered.length === 0 && (
        <div className="py-16 text-center text-slate-500">
          <Package className="w-12 h-12 mx-auto mb-3 opacity-30" />
          {t('noResults')}
        </div>
      )}
    </div>
  );
}
