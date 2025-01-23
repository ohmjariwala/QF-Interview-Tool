const isDevelopment = window.location.hostname === 'localhost';

export const API_BASE_URL = isDevelopment 
  ? 'http://localhost:8000'
  : 'https://api.qf-interview-tool.com';  // You'll need to update this with your actual API URL

const API_URL = import.meta.env.VITE_API_URL;

export const generateProblemUrl = (problemType, difficulty) =>
  `${API_BASE_URL}/problems/generate?problem_type=${problemType}&difficulty=${difficulty}`;

export const getPracticeProblemsUrl = () =>
  `${API_BASE_URL}/problems/practice`;

export const getMentalMathUrl = () =>
  `${API_BASE_URL}/problems/mental-math`; 