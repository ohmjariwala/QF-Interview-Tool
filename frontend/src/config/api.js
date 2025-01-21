const API_URL = import.meta.env.VITE_API_URL;

export const generateProblemUrl = (problemType, difficulty) =>
  `${API_URL}/problems/generate?problem_type=${problemType}&difficulty=${difficulty}`;

export const getPracticeProblemsUrl = () =>
  `${API_URL}/problems/practice`;

export const getInterviewQuestionsUrl = (count = 10, source = null) => {
  let url = `${API_URL}/problems/interview?count=${count}`;
  if (source) {
    url += `&source=${source}`;
  }
  return url;
}; 