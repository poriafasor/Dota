import { create } from 'zustand';
import { persist } from 'zustand/middleware';

export type Language = 'en' | 'fa';

export interface SavedBuild {
  id: string;
  heroId: string;
  name: string;
  role: 'core' | 'support';
  earlyGame: string[];
  midGame: string[];
  lateGame: string[];
  notes: string;
  date: string;
}

export interface HistoryEntry {
  id: string;
  type: 'hero' | 'item';
  refId: string;
  name: string;
  date: string;
}

interface AppState {
  language: Language;
  setLanguage: (lang: Language) => void;
  savedBuilds: SavedBuild[];
  saveBuild: (build: SavedBuild) => void;
  removeBuild: (id: string) => void;
  history: HistoryEntry[];
  addHistory: (entry: Omit<HistoryEntry, 'id' | 'date'>) => void;
  clearHistory: () => void;
  favorites: string[]; // hero ids
  toggleFavorite: (heroId: string) => void;
}

export const useStore = create<AppState>()(
  persist(
    (set) => ({
      language: 'fa',
      setLanguage: (lang) => set({ language: lang }),
      savedBuilds: [],
      saveBuild: (build) => set((state) => ({
        savedBuilds: [...state.savedBuilds.filter(b => b.id !== build.id), build],
      })),
      removeBuild: (id) => set((state) => ({ savedBuilds: state.savedBuilds.filter(b => b.id !== id) })),
      history: [],
      addHistory: (entry) => set((state) => ({
        history: [{ ...entry, id: crypto.randomUUID?.() || String(Date.now()), date: new Date().toISOString() }, ...state.history].slice(0, 24),
      })),
      clearHistory: () => set({ history: [] }),
      favorites: [],
      toggleFavorite: (heroId) => set((state) => ({
        favorites: state.favorites.includes(heroId)
          ? state.favorites.filter(f => f !== heroId)
          : [...state.favorites, heroId],
      })),
    }),
    { name: 'prf-dota-2-storage' }
  )
);
