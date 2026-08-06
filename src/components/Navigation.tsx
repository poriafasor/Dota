import { Link, useLocation, useNavigate } from 'react-router-dom';
import { useState, useMemo, type ReactNode } from 'react';
import { useTranslation } from '@/hooks/useTranslation';
import { useStore } from '@/store/useStore';
import { cn } from '@/lib/utils';
import { heroes, items } from '@/data/dota';
import { Search, Home, Activity, User, Globe, Swords, Package, X } from 'lucide-react';

export function Navigation({ children }: { children: ReactNode }) {
  const { t, dir, lang } = useTranslation();
  const location = useLocation();
  const navigate = useNavigate();
  const { language, setLanguage, addHistory } = useStore();
  const [searchOpen, setSearchOpen] = useState(false);
  const [query, setQuery] = useState('');

  const navItems = [
    { name: t('dashboard'), path: '/', icon: Home },
    { name: t('heroes'), path: '/heroes', icon: Swords },
    { name: t('items'), path: '/items', icon: Package },
    { name: t('liveAnalysis'), path: '/live', icon: Activity },
    { name: t('profile'), path: '/profile', icon: User },
  ];

  const suggestions = useMemo(() => {
    if (!query.trim()) return [];
    const q = query.toLowerCase().trim();
    const heroMatches = heroes
      .filter(h => h.name.en.toLowerCase().includes(q) || h.name.fa.includes(query) || h.id.includes(q))
      .slice(0, 6)
      .map(h => ({ kind: 'hero' as const, id: h.id, label: h.name[lang], sub: h.roles.join(', '), img: h.img, path: `/hero/${h.id}` }));
    const itemMatches = items
      .filter(i => i.name.en.toLowerCase().includes(q) || i.name.fa.includes(query) || i.id.includes(q))
      .slice(0, 6)
      .map(i => ({ kind: 'item' as const, id: i.id, label: i.name[lang], sub: `${i.cost}g · ${i.category}`, img: i.img, path: `/item/${i.id}` }));
    return [...heroMatches, ...itemMatches];
  }, [query, lang]);

  const go = (path: string, type: 'hero' | 'item', refId: string, name: string) => {
    addHistory({ type, refId, name });
    setSearchOpen(false);
    setQuery('');
    navigate(path);
  };

  return (
    <div className="min-h-screen flex flex-col bg-[#0a0d12] text-slate-100 pb-24 md:pb-0" dir={dir}>
      <header className="sticky top-0 z-40 w-full border-b border-red-900/40 bg-[#0a0d12]/90 backdrop-blur-md">
        <div className="container mx-auto px-4 h-16 flex items-center justify-between gap-4">
          <Link to="/" className="flex items-center gap-2.5 font-extrabold text-lg tracking-tight shrink-0">
            <span className="text-2xl">⚔️</span>
            <span className="bg-gradient-to-r from-red-500 via-orange-500 to-red-600 bg-clip-text text-transparent">PRF Dota 2</span>
          </Link>

          <nav className="hidden md:flex items-center gap-1">
            {navItems.map((item) => {
              const isActive = location.pathname === item.path || (item.path !== '/' && location.pathname.startsWith(item.path));
              return (
                <Link key={item.path} to={item.path}
                  className={cn(
                    "flex items-center gap-2 px-3.5 py-2 rounded-lg text-sm font-semibold transition-all",
                    isActive ? "bg-red-500/15 text-red-400 shadow-[inset_0_0_0_1px_rgba(239,68,68,0.3)]"
                             : "text-slate-400 hover:text-slate-100 hover:bg-white/5"
                  )}>
                  <item.icon className="w-4 h-4" />
                  {item.name}
                </Link>
              );
            })}
          </nav>

          <div className="flex items-center gap-2">
            <button onClick={() => setSearchOpen(s => !s)}
              className="flex items-center gap-2 px-3.5 py-2 rounded-lg bg-gradient-to-r from-red-600 to-orange-600 hover:from-red-500 hover:to-orange-500 text-white text-sm font-bold shadow-lg shadow-red-900/30 transition-all">
              <Search className="w-4 h-4" />
              <span className="hidden sm:inline">{t('search')}</span>
            </button>
            <button onClick={() => setLanguage(language === 'en' ? 'fa' : 'en')}
              className="flex items-center gap-1.5 px-3 py-2 rounded-lg bg-white/5 border border-white/10 hover:bg-white/10 text-xs font-bold text-slate-200 transition-colors">
              <Globe className="w-4 h-4 text-emerald-400" />
              {language === 'en' ? 'FA' : 'EN'}
            </button>
          </div>
        </div>

        {searchOpen && (
          <div className="border-t border-white/10 bg-[#0d1117] px-4 py-3">
            <div className="container mx-auto">
              <div className="relative">
                <Search className={cn("absolute top-1/2 -translate-y-1/2 w-5 h-5 text-slate-400", dir === 'rtl' ? 'right-4' : 'left-4')} />
                <input autoFocus type="text" value={query}
                  onChange={(e) => setQuery(e.target.value)}
                  placeholder={`${t('searchHeroes')} / ${t('searchItems')}`}
                  className={cn("w-full bg-[#161b22] border-2 border-red-900/40 focus:border-red-500 rounded-xl py-3 text-base font-bold text-white placeholder:font-medium placeholder:text-slate-500 focus:outline-none focus:ring-4 focus:ring-red-500/20 transition-all",
                    dir === 'rtl' ? 'pr-12 pl-10' : 'pl-12 pr-10')} />
                <button onClick={() => { setSearchOpen(false); setQuery(''); }}
                  className={cn("absolute top-1/2 -translate-y-1/2 text-slate-400 hover:text-white", dir === 'rtl' ? 'left-3' : 'right-3')}>
                  <X className="w-5 h-5" />
                </button>
              </div>
              {suggestions.length > 0 && (
                <div className="mt-2 grid md:grid-cols-2 gap-2 max-h-80 overflow-y-auto">
                  {suggestions.map(s => (
                    <button key={`${s.kind}-${s.id}`} onClick={() => go(s.path, s.kind, s.id, s.label)}
                      className="flex items-center gap-3 p-2.5 rounded-lg bg-white/5 hover:bg-red-500/10 border border-white/5 hover:border-red-500/30 text-start transition-all">
                      <img src={s.img} alt="" loading="lazy" className="w-10 h-10 rounded object-cover bg-slate-800 shrink-0" />
                      <div className="flex-1 min-w-0">
                        <p className="text-sm font-bold text-white truncate">{s.label}</p>
                        <p className="text-xs text-slate-400 truncate">{s.sub}</p>
                      </div>
                      <span className={cn("text-[10px] font-bold px-2 py-0.5 rounded", s.kind === 'hero' ? 'bg-emerald-500/20 text-emerald-400' : 'bg-orange-500/20 text-orange-400')}>
                        {s.kind === 'hero' ? t('heroes') : t('items')}
                      </span>
                    </button>
                  ))}
                </div>
              )}
            </div>
          </div>
        )}
      </header>

      <main className="flex-1 container mx-auto px-4 py-6 md:py-8">{children}</main>

      {/* Mobile bottom nav */}
      <nav className="md:hidden fixed bottom-0 left-0 right-0 z-40 bg-[#0a0d12]/95 backdrop-blur-xl border-t border-red-900/40 px-2 pt-2 pb-safe flex justify-around items-center h-20">
        {navItems.map((item) => {
          const isActive = location.pathname === item.path || (item.path !== '/' && location.pathname.startsWith(item.path));
          return (
            <Link key={item.path} to={item.path}
              className={cn("flex flex-col items-center gap-1 p-1.5 rounded-xl text-[11px] font-bold transition-all w-16",
                isActive ? "text-red-400 bg-red-500/10" : "text-slate-400 hover:text-slate-200")}>
              <item.icon className={cn("w-5 h-5 transition-transform", isActive && "scale-110")} />
              <span className="truncate w-full text-center">{item.name}</span>
            </Link>
          );
        })}
      </nav>
    </div>
  );
}
