const API_URL = import.meta.env.VITE_API_URL;

console.log('API URL:', API_URL); // Debug log

const fetchWithTimeout = async (url, options = {}) => {
  const timeout = 5000; // 5 seconds timeout
  const controller = new AbortController();
  const id = setTimeout(() => controller.abort(), timeout);

  const defaultOptions = {
    mode: 'cors',
    credentials: 'omit',
    headers: {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
    },
  };

  try {
    console.log('Fetching from URL:', url); // Debug log
    const response = await fetch(url, {
      ...defaultOptions,
      ...options,
      signal: controller.signal,
    });
    clearTimeout(id);

    if (!response.ok) {
      console.error('Response not OK:', response.status, response.statusText); // Debug log
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    return response;
  } catch (error) {
    console.error('Fetch error:', error.message, '\nURL:', url); // Debug log
    if (error.name === 'AbortError') {
      throw new Error('Request timed out');
    }
    throw error;
  }
};

export const generateProblemUrl = (problemType, difficulty) =>
  `${API_URL}/problems/generate?problem_type=${problemType}&difficulty=${difficulty}`;

export const getPracticeProblemsUrl = () =>
  `${API_URL}/problems/practice`;

export const fetchApi = async (url) => {
  try {
    console.log('Making API request to:', url); // Debug log
    const response = await fetchWithTimeout(url);
    const data = await response.json();
    console.log('API response:', data); // Debug log
    return data;
  } catch (error) {
    console.error('API Error:', error.message, '\nStack:', error.stack); // Debug log
    throw new Error(
      'Failed to connect to the server. Please try again later or contact support if the issue persists.'
    );
  }
}; 