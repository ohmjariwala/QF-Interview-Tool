const API_URL = import.meta.env.VITE_API_URL;

export const generateProblemUrl = (problemType, difficulty) =>
  `${API_URL}/problems/generate?problem_type=${problemType}&difficulty=${difficulty}`;

export const getPracticeProblemsUrl = () =>
  `${API_URL}/problems/practice`; 