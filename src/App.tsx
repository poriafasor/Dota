import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { Navigation } from '@/components/Navigation';
import Dashboard from '@/pages/Dashboard';
import Heroes from '@/pages/Heroes';
import HeroDetail from '@/pages/HeroDetail';
import Items from '@/pages/Items';
import ItemDetail from '@/pages/ItemDetail';
import LiveAnalysis from '@/pages/LiveAnalysis';
import Profile from '@/pages/Profile';

export default function App() {
  return (
    <Router>
      <Navigation>
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/heroes" element={<Heroes />} />
          <Route path="/hero/:id" element={<HeroDetail />} />
          <Route path="/items" element={<Items />} />
          <Route path="/item/:id" element={<ItemDetail />} />
          <Route path="/live" element={<LiveAnalysis />} />
          <Route path="/profile" element={<Profile />} />
        </Routes>
      </Navigation>
    </Router>
  );
}
