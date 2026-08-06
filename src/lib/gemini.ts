export const analyzeDraft = async (userHero: string, enemyTeam: string[], language: string) => {
  const response = await fetch('/api/analyze-draft', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ userHero, enemyTeam, language })
  });
  
  if (!response.ok) {
    throw new Error('Failed to analyze draft');
  }
  
  const data = await response.json();
  return data.analysis;
};

export const askCoach = async (question: string, language: string) => {
  const response = await fetch('/api/ask-coach', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ question, language })
  });
  
  if (!response.ok) {
    throw new Error('Failed to ask coach');
  }
  
  const data = await response.json();
  return data.answer;
};

export const getHeroBuild = async (heroId: string, language: string) => {
  const response = await fetch(`/api/hero-build/${heroId}?lang=${language}`);
  
  if (!response.ok) {
    throw new Error('Failed to fetch hero build');
  }
  
  return await response.json();
};

