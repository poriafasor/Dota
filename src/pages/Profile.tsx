import { Link } from 'react-router-dom';
import { useTranslation } from '@/hooks/useTranslation';
import { useStore } from '@/store/useStore';
import { getHero } from '@/data/dota';
import { getItem } from '@/data/items';
import { cn } from '@/lib/utils';
import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer, BarChart, Bar, ReferenceLine, CartesianGrid } from 'recharts';
import { Star, Trash2, User, TrendingUp, Save } from 'lucide-react';

export default function Profile() {
  const { t, lang } = useTranslation();
  const { savedBuilds, removeBuild, favorites, toggleFavorite } = useStore();

  // Demo performance data (the user wants comparative charts)
  const perfData = Array.from({ length: 10 }, (_, i) => {
    const gpm = 400 + Math.round(Math.sin(i * 0.7) * 120) + i * 12 + Math.round(Math.random() * 60);
    const xpm = 450 + Math.round(Math.cos(i * 0.5) * 130) + i * 10 + Math.round(Math.random() * 50);
    const kda = +(2 + Math.sin(i * 0.9) * 1.5 + Math.random()).toFixed(2);
    const win = Math.random() > 0.45 ? 1 : 0;
    return { match: `M${i + 1}`, gpm, xpm, kda, win };
  });
  const wins = perfData.filter(p => p.win).length;
  const avgGpm = Math.round(perfData.reduce((s, p) => s + p.gpm, 0) / perfData.length);
  const avgXpm = Math.round(perfData.reduce((s, p) => s + p.xpm, 0) / perfData.length);
  const avgKda = +(perfData.reduce((s, p) => s + p.kda, 0) / perfData.length).toFixed(2);

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-3xl font-extrabold text-white flex items-center gap-2">
          <User className="w-7 h-7 text-blue-400" /> {t('profileTitle')}
        </h1>
        <p className="text-slate-400 mt-1">{t('profileSub')}</p>
      </div>

      {/* Performance stats */}
      <section className="rounded-2xl border border-white/10 bg-[#0d1117] p-5">
        <h2 className="text-xl font-bold text-white mb-4 flex items-center gap-2">
          <TrendingUp className="w-5 h-5 text-emerald-400" /> {t('performance')}
        </h2>

        <div className="grid grid-cols-2 md:grid-cols-4 gap-3 mb-5">
          <StatCard label={t('winRate')} value={`${Math.round((wins / perfData.length) * 100)}%`} sub={`${wins}/${perfData.length} ${t('matches')}`} color="text-emerald-400" />
          <StatCard label={t('gpm')} value={`${avgGpm}`} sub="avg" color="text-amber-400" />
          <StatCard label={t('xpm')} value={`${avgXpm}`} sub="avg" color="text-blue-400" />
          <StatCard label={t('kda')} value={`${avgKda}`} sub="avg" color="text-red-400" />
        </div>

        <div className="grid md:grid-cols-2 gap-5">
          <div className="rounded-xl bg-white/5 border border-white/10 p-4">
            <p className="text-sm font-bold text-amber-300 mb-3">{t('gpm')} & {t('xpm')}</p>
            <ResponsiveContainer width="100%" height={220}>
              <LineChart data={perfData}>
                <CartesianGrid strokeDasharray="3 3" stroke="#1e293b" />
                <XAxis dataKey="match" tick={{ fill: '#64748b', fontSize: 11 }} />
                <YAxis tick={{ fill: '#64748b', fontSize: 11 }} />
                <Tooltip contentStyle={{ background: '#0d1117', border: '1px solid #334155', borderRadius: 8, fontSize: 12 }} />
                <Line type="monotone" dataKey="gpm" stroke="#f59e0b" strokeWidth={2} dot={{ r: 3 }} name="GPM" />
                <Line type="monotone" dataKey="xpm" stroke="#3b82f6" strokeWidth={2} dot={{ r: 3 }} name="XPM" />
              </LineChart>
            </ResponsiveContainer>
          </div>
          <div className="rounded-xl bg-white/5 border border-white/10 p-4">
            <p className="text-sm font-bold text-red-300 mb-3">{t('kda')} per match</p>
            <ResponsiveContainer width="100%" height={220}>
              <BarChart data={perfData}>
                <CartesianGrid strokeDasharray="3 3" stroke="#1e293b" />
                <XAxis dataKey="match" tick={{ fill: '#64748b', fontSize: 11 }} />
                <YAxis tick={{ fill: '#64748b', fontSize: 11 }} />
                <Tooltip contentStyle={{ background: '#0d1117', border: '1px solid #334155', borderRadius: 8, fontSize: 12 }} />
                <ReferenceLine y={3} stroke="#10b981" strokeDasharray="3 3" label={{ value: 'good', fill: '#10b981', fontSize: 10 }} />
                <Bar dataKey="kda" fill="#ef4444" radius={[4, 4, 0, 0]} name="KDA" />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>
      </section>

      {/* Saved builds */}
      <section className="rounded-2xl border border-white/10 bg-[#0d1117] p-5">
        <h2 className="text-xl font-bold text-white mb-4 flex items-center gap-2">
          <Save className="w-5 h-5 text-amber-400" /> {t('mySavedBuilds')} ({savedBuilds.length})
        </h2>
        {savedBuilds.length === 0 ? (
          <div className="py-10 text-center text-slate-500">
            <Save className="w-10 h-10 mx-auto mb-3 opacity-30" />
            {t('noSavedBuilds')}
          </div>
        ) : (
          <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-3">
            {savedBuilds.slice().reverse().map(b => {
              const hero = getHero(b.heroId);
              return (
                <div key={b.id} className="rounded-xl bg-white/5 border border-white/10 p-3">
                  <div className="flex items-center gap-3 mb-2">
                    {hero && <img src={hero.img} alt="" className="w-12 h-14 rounded-lg object-cover" />}
                    <div className="flex-1 min-w-0">
                      <p className="font-bold text-white truncate">{b.name}</p>
                      <p className="text-xs text-slate-400">{hero?.name[lang]}</p>
                      <span className={cn("inline-block text-[10px] font-bold px-2 py-0.5 rounded mt-1",
                        b.role === 'core' ? "bg-red-500/15 text-red-300" : "bg-emerald-500/15 text-emerald-300")}>
                        {b.role === 'core' ? t('coreRole') : t('supportRole')}
                      </span>
                    </div>
                    <button onClick={() => removeBuild(b.id)} className="text-slate-400 hover:text-red-400 self-start">
                      <Trash2 className="w-4 h-4" />
                    </button>
                  </div>
                  {b.notes && <p className="text-xs text-slate-400 italic mb-2 line-clamp-2">{b.notes}</p>}
                  <div className="flex gap-1 flex-wrap">
                    {[...b.earlyGame, ...b.midGame, ...b.lateGame].slice(0, 6).map((id, i) => {
                      const item = getItem(id);
                      return item ? <img key={i} src={item.img} alt="" loading="lazy" className="w-8 h-8 rounded object-cover bg-slate-800 border border-white/10" /> : null;
                    })}
                  </div>
                  {hero && (
                    <Link to={`/hero/${hero.id}`} className="block mt-2 text-xs font-bold text-red-400 hover:underline">
                      {t('viewDetails')} →
                    </Link>
                  )}
                </div>
              );
            })}
          </div>
        )}
      </section>

      {/* Favorites */}
      <section className="rounded-2xl border border-white/10 bg-[#0d1117] p-5">
        <h2 className="text-xl font-bold text-white mb-4 flex items-center gap-2">
          <Star className="w-5 h-5 text-amber-400" /> {t('myFavorites')} ({favorites.length})
        </h2>
        {favorites.length === 0 ? (
          <div className="py-10 text-center text-slate-500">
            <Star className="w-10 h-10 mx-auto mb-3 opacity-30" />
            {t('noFavorites')}
          </div>
        ) : (
          <div className="grid grid-cols-3 sm:grid-cols-4 md:grid-cols-6 lg:grid-cols-8 gap-3">
            {favorites.map(fid => {
              const h = getHero(fid);
              if (!h) return null;
              return (
                <div key={fid} className="group relative rounded-xl overflow-hidden bg-white/5 border border-white/10">
                  <Link to={`/hero/${h.id}`}>
                    <img src={h.img} alt="" loading="lazy" className="w-full aspect-[3/4] object-cover" />
                    <p className="text-xs font-bold text-white truncate px-1.5 py-1">{h.name[lang]}</p>
                  </Link>
                  <button onClick={() => toggleFavorite(h.id)}
                    className="absolute top-1.5 right-1.5 p-1 rounded-full bg-amber-500/90 text-white">
                    <Star className="w-3 h-3" fill="currentColor" />
                  </button>
                </div>
              );
            })}
          </div>
        )}
      </section>
    </div>
  );
}

function StatCard({ label, value, sub, color }: { label: string; value: string; sub?: string; color: string }) {
  return (
    <div className="rounded-xl bg-white/5 border border-white/10 p-4">
      <p className="text-xs text-slate-400 font-bold uppercase tracking-wide">{label}</p>
      <p className={cn("text-2xl font-extrabold mt-1", color)}>{value}</p>
      {sub && <p className="text-[10px] text-slate-500 mt-0.5">{sub}</p>}
    </div>
  );
}
