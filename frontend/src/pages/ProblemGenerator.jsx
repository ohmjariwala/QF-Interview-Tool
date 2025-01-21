import { useState } from 'react';
import {
  Typography,
  Box,
  Paper,
  FormControl,
  InputLabel,
  Select,
  MenuItem,
  Button,
  CircularProgress,
  Alert,
} from '@mui/material';
import { generateProblemUrl } from '../config/api';

function ProblemGenerator() {
  const [problemType, setProblemType] = useState('');
  const [difficulty, setDifficulty] = useState('');
  const [problem, setProblem] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const problemTypes = [
    'option_pricing',
    'portfolio_optimization',
    'probability',
    'statistics',
    'stochastic_processes',
    'quant_interview',
  ];

  const difficulties = ['easy', 'medium', 'hard'];

  const generateProblem = async () => {
    setLoading(true);
    setError(null);
    try {
      const response = await fetch(generateProblemUrl(problemType, difficulty));
      const data = await response.json();
      if (data.status === 'success') {
        setProblem(data.problem);
      } else {
        setError(data.message || 'Failed to generate problem');
      }
    } catch (err) {
      setError('Failed to connect to the server. Make sure the backend is running on http://localhost:8000');
    }
    setLoading(false);
  };

  return (
    <Box>
      <Typography variant="h4" gutterBottom>
        Problem Generator
      </Typography>

      <Paper sx={{ p: 3, mb: 3 }}>
        <FormControl fullWidth sx={{ mb: 2 }}>
          <InputLabel>Problem Type</InputLabel>
          <Select
            value={problemType}
            label="Problem Type"
            onChange={(e) => setProblemType(e.target.value)}
          >
            {problemTypes.map((type) => (
              <MenuItem key={type} value={type}>
                {type.replace('_', ' ').toUpperCase()}
              </MenuItem>
            ))}
          </Select>
        </FormControl>

        <FormControl fullWidth sx={{ mb: 3 }}>
          <InputLabel>Difficulty</InputLabel>
          <Select
            value={difficulty}
            label="Difficulty"
            onChange={(e) => setDifficulty(e.target.value)}
          >
            {difficulties.map((diff) => (
              <MenuItem key={diff} value={diff}>
                {diff.toUpperCase()}
              </MenuItem>
            ))}
          </Select>
        </FormControl>

        <Button
          variant="contained"
          fullWidth
          onClick={generateProblem}
          disabled={!problemType || !difficulty || loading}
        >
          {loading ? <CircularProgress size={24} /> : 'Generate Problem'}
        </Button>
      </Paper>

      {error && (
        <Alert severity="error" sx={{ mb: 3 }}>
          {error}
        </Alert>
      )}

      {problem && (
        <Paper sx={{ p: 3 }}>
          <Typography variant="h6" gutterBottom>
            Generated Problem
          </Typography>
          <Typography variant="body1" sx={{ whiteSpace: 'pre-line' }}>
            {problem.question}
          </Typography>
          {problem.parameters && (
            <Box sx={{ mt: 2 }}>
              <Typography variant="subtitle2" gutterBottom>
                Parameters:
              </Typography>
              <pre>{JSON.stringify(problem.parameters, null, 2)}</pre>
            </Box>
          )}
        </Paper>
      )}
    </Box>
  );
}

export default ProblemGenerator; 