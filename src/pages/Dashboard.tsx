import { Link } from 'react-router-dom';
import { useTranslation } from '@/hooks/useTranslation';
import { useStore } from '@/store/useStore';
import { heroes, items } from '@/data/dota';
import { Swords, Package, Activity, User, Star, Clock, Trash2, TrendingUp, Zap } from 'lucide-react';
import { cn } from '@/lib/utils';

export default function Dashboard() {
  const { t, lang } = useTranslation();
  const { history, clearHistory, savedBuilds, favorites } = useStore();

  const stats = [
    { label: t('totalHeroes'), value: heroes.length, icon: Swords, color: 'from-red-600 to-orange-600', path: '/heroes' },
    { label: t('totalItems'), value: items.length, icon: Package, color: 'from-emerald-600 to-green-600', path: '/items' },
    { label: t('savedBuilds'), value: savedBuilds.length, icon: TrendingUp, color: 'from-blue-600 to-cyan-600', path: '/profile' },
    { label: t('favorites'), value: favorites.length, icon: Star, color: 'from-amber-600 to-yellow-600', path: '/profile' },
  ];

  const quickAccess = [
    { name: t('heroes'), desc: lang === 'fa' ? 'همه ۱۲۷ هیرو با بیلد' : 'All 127 heroes with builds', icon: Swords, path: '/heroes', color: 'red' },
    { name: t('items'), desc: lang === 'fa' ? 'تمام آیتم‌ها با پیش‌نیازها' : 'All items with prerequisites', icon: Package, path: '/items', color: 'emerald' },
    { name: t('liveAnalysis'), desc: lang === 'fa' ? 'کانتر پیک و تحلیل' : 'Counter picks & analysis', icon: Activity, path: '/live', color: 'orange' },
    { name: t('profile'), desc: lang === 'fa' ? 'بیلدها و محبوب‌ها' : 'Builds & favorites', icon: User, path: '/profile', color: 'blue' },
  ];

  const colorMap: Record<string, string> = {
    red: 'from-red-600/20 to-red-900/10 border-red-500/30 text-red-400 hover:bg-red-500/10',
    emerald: 'from-emerald-600/20 to-emerald-900/10 border-emerald-500/30 text-emerald-400 hover:bg-emerald-500/10',
    orange: 'from-orange-600/20 to-orange-900/10 border-orange-500/30 text-orange-400 hover:bg-orange-500/10',
    blue: 'from-blue-600/20 to-blue-900/10 border-blue-500/30 text-blue-400 hover:bg-blue-500/10',
  };

  return (
    <div className="space-y-8">
      {/* Hero banner */}
      <section className="relative overflow-hidden rounded-3xl border border-red-900/40 bg-gradient-to-br from-[#150505] via-[#0a0d12] to-[#051510] p-6 md:p-10">
        <div className="absolute inset-0 opacity-20 shimmer" />
        <div className="relative">
          <div className="flex items-center gap-3 mb-3">
            <span className="text-4xl">⚔️</span>
            <h1 className="text-3xl md:text-4xl font-extrabold bg-gradient-to-r from-red-500 via-orange-400 to-emerald-400 bg-clip-text text-transparent">
              {t('welcomeBack')}
            </h1>
          </div>
          <p className="text-slate-400 text-base md:text-lg mb-6">{t('dashboardSub')}</p>
          <div className="grid grid-cols-2 md:grid-cols-4 gap-3">
            {stats.map(s => (
              <Link key={s.label} to={s.path}
                className={cn("group relative overflow-hidden rounded-2xl p-4 border bg-gradient-to-br transition-all hover:scale-[1.02]",
                  s.color, "border-white/10")}>
                <s.icon className="w-6 h-6 mb-2 opacity-80" />
                <p className="text-3xl font-extrabold text-white">{s.value}</p>
                <p className="text-xs text-slate-300 font-semibold mt-1">{s.label}</p>
              </Link>
            ))}
          </div>
        </div>
      </section>

      {/* Quick access */}
      <section>
        <h2 className="text-xl font-bold text-white mb-4 flex items-center gap-2">
          <Zap className="w-5 h-5 text-amber-400" />
          {t('quickAccess')}
        </h2>
        <div className="grid grid-cols-2 lg:grid-cols-4 gap-3">
          {quickAccess.map(q => (
            <Link key={q.path} to={q.path}
              className={cn("group rounded-2xl p-5 border bg-gradient-to-br transition-all hover:scale-[1.02]", colorMap[q.color])}>
              <q.icon className="w-8 h-8 mb-3" />
              <p className="text-lg font-bold text-white">{q.name}</p>
              <p className="text-xs text-slate-400 mt-1">{q.desc}</p>
            </Link>
          ))}
        </div>
      </section>

      {/* History (CRM) */}
      <section className="rounded-2xl border border-white/10 bg-[#0d1117] p-5">
        <div className="flex items-center justify-between mb-4">
          <h2 className="text-xl font-bold text-white flex items-center gap-2">
            <Clock className="w-5 h-5 text-emerald-400" />
            {t('lastViewed')}
          </h2>
          {history.length > 0 && (
            <button onClick={clearHistory}
              className="flex items-center gap-1.5 text-xs font-semibold text-slate-400 hover:text-red-400 transition-colors">
              <Trash2 className="w-4 h-4" />
              {t('clearHistory')}
            </button>
          )}
        </div>
        {history.length === 0 ? (
          <div className="py-10 text-center text-slate-500 text-sm">
            <Clock className="w-10 h-10 mx-auto mb-3 opacity-30" />
            {t('noHistory')}
          </div>
        ) : (
          <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-6 gap-3">
            {history.map(h => {
              const hero = h.type === 'hero' ? heroes.find(x => x.id === h.refId) : null;
              const item = h.type === 'item' ? items.find(x => x.id === h.refId) : null;
              const img = hero?.img || item?.img;
              const path = h.type === 'hero' ? `/hero/${h.refId}` : `/item/${h.refId}`;
              return (
                <Link key={h.id} to={path}
                  className="group rounded-xl overflow-hidden bg-white/5 border border-white/5 hover:border-red-500/40 transition-all">
                  <div className="aspect-[4/3] bg-slate-800 overflow-hidden">
                    {img && <img src={img} alt={h.name} loading="lazy" className="w-full h-full object-cover group-hover:scale-110 transition-transform" />}
                  </div>
                  <div className="p-2">
                    <p className="text-xs font-bold text-white truncate">{h.name}</p>
                    <p className={cn("text-[10px] font-semibold", h.type === 'hero' ? 'text-emerald-400' : 'text-orange-400')}>
                      {h.type === 'hero' ? t('heroes') : t('items')}
                    </p>
                  </div>
                </Link>
              );
            })}
          </div>
        )}
      </section>

      {/* Patch banner */}
      <section className="rounded-2xl border border-emerald-900/40 bg-gradient-to-r from-emerald-950/40 to-transparent p-5">
        <div className="flex items-center gap-3">
          <span className="text-2xl">🟢</span>
          <div>
            <p className="font-bold text-emerald-300">Patch 7.39+ Meta</p>
            <p className="text-xs text-slate-400 mt-0.5">
              {lang === 'fa' ? 'داده‌ها بر اساس جدیدترین پچ نوت — ۱۲۷ هیرو و آیتم‌های کامل با پیش‌نیازها' : 'Data based on latest patch notes — 127 heroes & full items with prerequisites'}
            </p>
          </div>
        </div>
      </section>
    </div>
  );
}
