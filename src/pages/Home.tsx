import { useState } from 'react';
import { Link } from 'react-router-dom';
import { motion, AnimatePresence } from 'framer-motion';
import { heroes, items } from '@/data/dota';
import { useTranslation } from '@/hooks/useTranslation';
import { useStore } from '@/store/useStore';
import { Search, ChevronDown } from 'lucide-react';
import { cn } from '@/lib/utils';

export default function Home() {
  const { t, dir } = useTranslation();
  const language = useStore((state) => state.language);
  const [heroSearch, setHeroSearch] = useState('');
  const [itemSearch, setItemSearch] = useState('');
  const [activeHeroCat, setActiveHeroCat] = useState('all');
  const [activeItemCat, setActiveItemCat] = useState('all');

  const heroCategories = [
    { id: 'all', label: { en: 'All Heroes', fa: 'همه هیروها' }, color: 'text-zinc-200' },
    { id: 'str', label: { en: 'Strength', fa: 'قدرتی' }, color: 'text-red-500' },
    { id: 'agi', label: { en: 'Agility', fa: 'سرعتی' }, color: 'text-emerald-500' },
    { id: 'int', label: { en: 'Intelligence', fa: 'هوشی' }, color: 'text-blue-500' },
    { id: 'all_attr', label: { en: 'Universal', fa: 'یونیورسال' }, color: 'text-purple-500' }
  ];

  const itemCategories = [
    { id: 'all', label: { en: 'All Items', fa: 'همه آیتم‌ها' } },
    { id: 'consumable', label: { en: 'Consumables', fa: 'مصرفی' } },
    { id: 'early', label: { en: 'Early Game', fa: 'اوایل بازی' } },
    { id: 'mid', label: { en: 'Mid Game', fa: 'اواسط بازی' } },
    { id: 'late', label: { en: 'Late Game', fa: 'اواخر بازی' } },
  ];

  // Bilingual search filter
  const filteredHeroes = heroes.filter(h => {
    const matchesSearch = h.name.en.toLowerCase().includes(heroSearch.toLowerCase()) || 
                          h.name.fa.includes(heroSearch);
    const matchesCat = activeHeroCat === 'all' || 
                      (activeHeroCat === 'all_attr' ? h.primaryAttr === 'all' : h.primaryAttr === activeHeroCat);
    return matchesSearch && matchesCat;
  });

  const filteredItems = items.filter(i => {
    const matchesSearch = i.name.en.toLowerCase().includes(itemSearch.toLowerCase()) || 
                          i.name.fa.includes(itemSearch) ||
                          i.goodFor.en.toLowerCase().includes(itemSearch.toLowerCase()) ||
                          i.goodFor.fa.includes(itemSearch);
    const matchesCat = activeItemCat === 'all' || i.category === activeItemCat;
    return matchesSearch && matchesCat;
  });

  return (
    <div className="space-y-16 pb-24 md:pb-8">
      
      {/* Heroes Section */}
      <section className="space-y-8">
        <div className="flex flex-col gap-6">
          <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
            <h2 className="text-3xl font-bold tracking-tight text-white">{t('heroes')}</h2>
            
            {/* Bold, prominent search */}
            <div className="relative w-full md:w-96 shadow-lg shadow-black/20">
              <Search className={`absolute ${dir === 'rtl' ? 'right-4' : 'left-4'} top-1/2 -tranzinc-y-1/2 w-5 h-5 text-zinc-400`} />
              <input 
                type="text" 
                placeholder={t('searchHeroes')}
                className={`w-full ${dir === 'rtl' ? 'pr-12 pl-4' : 'pl-12 pr-4'} py-3.5 bg-zinc-900 border-2 border-zinc-700 rounded-xl text-lg font-bold text-white focus:outline-none focus:border-red-500 focus:ring-4 focus:ring-red-500/20 transition-all placeholder:font-medium placeholder:text-zinc-500`}
                value={heroSearch}
                onChange={(e) => setHeroSearch(e.target.value)}
              />
            </div>
          </div>

          {/* Categories */}
          <div className="flex flex-wrap gap-2">
            {heroCategories.map(cat => (
              <button
                key={cat.id}
                onClick={() => setActiveHeroCat(cat.id)}
                className={cn(
                  "px-4 py-2 rounded-lg text-sm font-semibold transition-all border",
                  activeHeroCat === cat.id 
                    ? "bg-zinc-800 border-zinc-600 text-white shadow-md" 
                    : "bg-zinc-950 border-zinc-800 text-zinc-400 hover:bg-zinc-900 hover:border-zinc-700"
                )}
              >
                <span className={cat.color}>{cat.label[language as 'en' | 'fa']}</span>
              </button>
            ))}
          </div>
        </div>

        <motion.div layout className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 xl:grid-cols-6 gap-6 lg:gap-8">
          <AnimatePresence>
            {filteredHeroes.map((hero, idx) => (
              <Link key={hero.id} to={`/hero/${hero.id}`}>
                <motion.div
                  layout
                  initial={{ opacity: 0, scale: 0.9 }}
                  animate={{ opacity: 1, scale: 1 }}
                  exit={{ opacity: 0, scale: 0.9 }}
                  transition={{ duration: 0.2 }}
                  className="group relative rounded-xl overflow-hidden aspect-[4/3] bg-zinc-900 border border-zinc-800 hover:border-red-500/80 hover:shadow-lg hover:shadow-red-500/20 transition-all cursor-pointer"
                >
                  <img 
                    src={hero.img} 
                    alt={hero.name[language as 'en' | 'fa']} 
                    className="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-500"
                    loading="lazy"
                  />
                  <div className="absolute inset-0 bg-gradient-to-t from-zinc-950 via-zinc-950/40 to-transparent opacity-90 group-hover:opacity-100 transition-opacity" />
                  <div className="absolute bottom-0 w-full p-2">
                    <p className="text-sm font-bold text-center text-white truncate drop-shadow-md">
                      {hero.name[language as 'en' | 'fa']}
                    </p>
                  </div>
                </motion.div>
              </Link>
            ))}
            {filteredHeroes.length === 0 && (
              <div className="col-span-full py-12 text-center text-zinc-500 font-medium bg-zinc-900/50 rounded-2xl border border-zinc-800 border-dashed">
                هیچ هیرویی یافت نشد / No heroes found
              </div>
            )}
          </AnimatePresence>
        </motion.div>
      </section>

      {/* Items Section */}
      <section className="space-y-8 pt-10 border-t border-zinc-800/80">
        <div className="flex flex-col gap-6">
          <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
            <h2 className="text-3xl font-bold tracking-tight text-white">{t('items')}</h2>
            
            <div className="relative w-full md:w-96 shadow-lg shadow-black/20">
              <Search className={`absolute ${dir === 'rtl' ? 'right-4' : 'left-4'} top-1/2 -tranzinc-y-1/2 w-5 h-5 text-zinc-400`} />
              <input 
                type="text" 
                placeholder={t('searchItems')}
                className={`w-full ${dir === 'rtl' ? 'pr-12 pl-4' : 'pl-12 pr-4'} py-3.5 bg-zinc-900 border-2 border-zinc-700 rounded-xl text-lg font-bold text-white focus:outline-none focus:border-blue-500 focus:ring-4 focus:ring-blue-500/20 transition-all placeholder:font-medium placeholder:text-zinc-500`}
                value={itemSearch}
                onChange={(e) => setItemSearch(e.target.value)}
              />
            </div>
          </div>

          <div className="flex flex-wrap gap-2">
            {itemCategories.map(cat => (
              <button
                key={cat.id}
                onClick={() => setActiveItemCat(cat.id)}
                className={cn(
                  "px-4 py-2 rounded-lg text-sm font-semibold transition-all border",
                  activeItemCat === cat.id 
                    ? "bg-zinc-800 border-zinc-600 text-white shadow-md" 
                    : "bg-zinc-950 border-zinc-800 text-zinc-400 hover:bg-zinc-900 hover:border-zinc-700"
                )}
              >
                {cat.label[language as 'en' | 'fa']}
              </button>
            ))}
          </div>
        </div>

        <motion.div layout className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4">
          <AnimatePresence>
            {filteredItems.map((item) => (
              <motion.div
                layout
                initial={{ opacity: 0, scale: 0.95 }}
                animate={{ opacity: 1, scale: 1 }}
                exit={{ opacity: 0, scale: 0.95 }}
                transition={{ duration: 0.2 }}
                key={item.id}
              >
                <Link to={`/item/${item.id}`} className="block p-5 bg-zinc-900 border border-zinc-800 rounded-2xl hover:border-zinc-500 hover:bg-zinc-800/80 transition-all flex gap-4 shadow-lg shadow-black/10 group h-full">
                  <img src={item.img} alt={item.name[language as 'en' | 'fa']} className="w-16 h-12 rounded-lg shadow-md shrink-0 border border-zinc-700" loading="lazy" />
                  <div className="flex-1 space-y-2">
                    <div className="flex items-start justify-between">
                      <h3 className="text-base font-bold text-white group-hover:text-blue-400 transition-colors">{item.name[language as 'en' | 'fa']}</h3>
                      <span className="text-sm text-yellow-500 font-mono font-bold bg-yellow-500/10 px-2 py-0.5 rounded">{item.cost}</span>
                    </div>
                    <p className="text-xs text-zinc-300 leading-relaxed font-medium line-clamp-2">
                      {item.description[language as 'en' | 'fa']}
                    </p>
                    <div className="pt-3 border-t border-zinc-800/80">
                      <p className="text-[11px] text-emerald-400/90 font-semibold flex flex-wrap gap-1">
                        <span className="text-zinc-500">{t('goodFor')}:</span> {item.goodFor[language as 'en' | 'fa']}
                      </p>
                    </div>
                  </div>
                </Link>
              </motion.div>
            ))}
            {filteredItems.length === 0 && (
              <div className="col-span-full py-12 text-center text-zinc-500 font-medium bg-zinc-900/50 rounded-2xl border border-zinc-800 border-dashed">
                هیچ آیتمی یافت نشد / No items found
              </div>
            )}
          </AnimatePresence>
        </motion.div>
      </section>
    </div>
  );
}
