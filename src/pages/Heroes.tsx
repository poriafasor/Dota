import { useState, useMemo } from 'react';
import { Link } from 'react-router-dom';
import { motion, AnimatePresence } from 'framer-motion';
import { heroes } from '@/data/dota';
import { useTranslation } from '@/hooks/useTranslation';
import { useStore } from '@/store/useStore';
import { Search, Star } from 'lucide-react';
import { cn } from '@/lib/utils';

const ATTR_INFO: Record<string, { labelEn: string; labelFa: string; color: string; ring: string }> = {
  str: { labelEn: 'Strength', labelFa: 'قدرتی', color: 'text-red-400', ring: 'hover:border-red-500/70' },
  agi: { labelEn: 'Agility', labelFa: 'سرعتی', color: 'text-emerald-400', ring: 'hover:border-emerald-500/70' },
  int: { labelEn: 'Intelligence', labelFa: 'هوشی', color: 'text-blue-400', ring: 'hover:border-blue-500/70' },
  all: { labelEn: 'Universal', labelFa: 'یونیورسال', color: 'text-amber-400', ring: 'hover:border-amber-500/70' },
};

export default function Heroes() {
  const { t, dir, lang } = useTranslation();
  const { favorites, toggleFavorite, addHistory } = useStore();
  const [query, setQuery] = useState('');
  const [attr, setAttr] = useState<string>('all');
  const [role, setRole] = useState<string>('all');
  const [favOnly, setFavOnly] = useState(false);

  const roles = ['all', 'Carry', 'Support', 'Initiator', 'Disabler', 'Durable', 'Nuker', 'Escape', 'Pusher', 'Jungler'];

  const filtered = useMemo(() => {
    const q = query.toLowerCase().trim();
    return heroes.filter(h => {
      const matchQ = !q || h.name.en.toLowerCase().includes(q) || h.name.fa.includes(query) || h.id.includes(q);
      const matchAttr = attr === 'all' || h.primaryAttr === attr;
      const matchRole = role === 'all' || h.roles.includes(role);
      const matchFav = !favOnly || favorites.includes(h.id);
      return matchQ && matchAttr && matchRole && matchFav;
    });
  }, [query, attr, role, favOnly, favorites]);

  const cats = [{ id: 'all', label: t('allHeroes') },
    ...Object.entries(ATTR_INFO).map(([id, v]) => ({ id, label: lang === 'fa' ? v.labelFa : v.labelEn }))];

  return (
    <div className="space-y-6">
      <div className="flex flex-col gap-4">
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
          <div>
            <h1 className="text-3xl font-extrabold text-white flex items-center gap-2">
              <span className="text-red-500">⚔️</span> {t('heroes')}
              <span className="text-sm font-bold text-slate-500">({heroes.length})</span>
            </h1>
          </div>
          <div className="relative w-full md:w-96">
            <Search className={cn("absolute top-1/2 -translate-y-1/2 w-5 h-5 text-slate-400", dir === 'rtl' ? 'right-4' : 'left-4')} />
            <input value={query} onChange={e => setQuery(e.target.value)} placeholder={t('searchHeroes')}
              className={cn("w-full bg-[#161b22] border-2 border-white/10 focus:border-red-500 rounded-xl py-3 text-base font-bold text-white placeholder:font-medium placeholder:text-slate-500 focus:outline-none focus:ring-4 focus:ring-red-500/20 transition-all",
                dir === 'rtl' ? 'pr-12 pl-4' : 'pl-12 pr-4')} />
          </div>
        </div>

        <div className="flex flex-wrap gap-2">
          {cats.map(c => (
            <button key={c.id} onClick={() => setAttr(c.id)}
              className={cn("px-3.5 py-1.5 rounded-lg text-sm font-bold border transition-all",
                attr === c.id ? "bg-white/10 border-white/30 text-white" : "bg-transparent border-white/10 text-slate-400 hover:bg-white/5")}>
              {c.id !== 'all' && <span className={ATTR_INFO[c.id].color}>● </span>}
              {c.label}
            </button>
          ))}
        </div>

        <div className="flex flex-wrap gap-2">
          {roles.map(r => (
            <button key={r} onClick={() => setRole(r)}
              className={cn("px-3 py-1 rounded-full text-xs font-semibold border transition-all",
                role === r ? "bg-emerald-500/15 border-emerald-500/40 text-emerald-300" : "bg-transparent border-white/10 text-slate-400 hover:bg-white/5")}>
              {r === 'all' ? (lang === 'fa' ? 'همه نقش‌ها' : 'All Roles') : r}
            </button>
          ))}
          <button onClick={() => setFavOnly(f => !f)}
            className={cn("px-3 py-1 rounded-full text-xs font-bold border transition-all flex items-center gap-1",
              favOnly ? "bg-amber-500/20 border-amber-500/50 text-amber-300" : "bg-transparent border-white/10 text-slate-400 hover:bg-white/5")}>
            <Star className="w-3.5 h-3.5" /> {t('favorites')} ({favorites.length})
          </button>
        </div>
      </div>

      <p className="text-sm text-slate-400">{filtered.length} / {heroes.length}</p>

      <motion.div layout className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 xl:grid-cols-6 gap-3 md:gap-4">
        <AnimatePresence>
          {filtered.map(h => {
            const info = ATTR_INFO[h.primaryAttr];
            const isFav = favorites.includes(h.id);
            return (
              <motion.div key={h.id} layout initial={{ opacity: 0, scale: 0.95 }} animate={{ opacity: 1, scale: 1 }} exit={{ opacity: 0 }}>
                <Link to={`/hero/${h.id}`} onClick={() => addHistory({ type: 'hero', refId: h.id, name: h.name[lang] })}
                  className={cn("group relative block rounded-2xl overflow-hidden bg-[#0d1117] border border-white/10 transition-all", info.ring, "hover:shadow-lg hover:shadow-red-900/20")}>
                  <div className="aspect-[3/4] bg-slate-800 overflow-hidden">
                    <img src={h.img} alt={h.name[lang]} loading="lazy"
                      className="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500" />
                  </div>
                  <div className="absolute inset-0 bg-gradient-to-t from-[#0a0d12] via-[#0a0d12]/40 to-transparent" />
                  <button onClick={(e) => { e.preventDefault(); toggleFavorite(h.id); }}
                    className={cn("absolute top-2 z-10 p-1.5 rounded-full backdrop-blur transition-all",
                      dir === 'rtl' ? 'left-2' : 'right-2',
                      isFav ? "bg-amber-500/90 text-white" : "bg-black/50 text-slate-300 hover:bg-amber-500/80 hover:text-white")}>
                    <Star className="w-3.5 h-3.5" fill={isFav ? 'currentColor' : 'none'} />
                  </button>
                  <div className="absolute bottom-0 w-full p-2.5">
                    <p className="text-sm font-extrabold text-white truncate drop-shadow">{h.name[lang]}</p>
                    <div className="flex items-center gap-1 mt-0.5">
                      <span className={cn("text-[10px] font-bold", info.color)}>{lang === 'fa' ? info.labelFa : info.labelEn}</span>
                      <span className="text-slate-600">·</span>
                      <span className="text-[10px] text-slate-400 truncate">{h.roles.slice(0, 2).join(', ')}</span>
                    </div>
                  </div>
                </Link>
              </motion.div>
            );
          })}
        </AnimatePresence>
      </motion.div>

      {filtered.length === 0 && (
        <div className="py-16 text-center text-slate-500">
          <Search className="w-12 h-12 mx-auto mb-3 opacity-30" />
          {t('noResults')}
        </div>
      )}
    </div>
  );
}
