// For now, we'll use localhost for all environments since we're running the backend locally
export const API_BASE_URL = 'http://localhost:8000';

const API_URL = import.meta.env.VITE_API_URL;

export const generateProblemUrl = (problemType, difficulty) =>
  `${API_BASE_URL}/problems/generate?problem_type=${problemType}&difficulty=${difficulty}`;

export const getPracticeProblemsUrl = () =>
  `${API_BASE_URL}/problems/practice`;

export const getMentalMathUrl = () =>
  `${API_BASE_URL}/problems/mental-math`; 