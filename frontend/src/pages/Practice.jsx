import { useState, useEffect } from 'react';
import {
  Typography,
  Box,
  Paper,
  Grid,
  Card,
  CardContent,
  CardActions,
  Button,
  Chip,
  CircularProgress,
  Alert,
} from '@mui/material';
import { getPracticeProblemsUrl } from '../config/api';

function Practice() {
  const [problems, setProblems] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [selectedProblem, setSelectedProblem] = useState(null);

  useEffect(() => {
    fetchProblems();
  }, []);

  const fetchProblems = async () => {
    setLoading(true);
    setError(null);
    try {
      const response = await fetch(getPracticeProblemsUrl());
      const data = await response.json();
      if (data.status === 'success') {
        setProblems(data.problems);
      } else {
        setError(data.message || 'Failed to fetch problems');
      }
    } catch (err) {
      setError('Failed to connect to the server. Make sure the backend is running on http://localhost:8000');
    }
    setLoading(false);
  };

  if (loading) {
    return (
      <Box sx={{ display: 'flex', justifyContent: 'center', mt: 4 }}>
        <CircularProgress />
      </Box>
    );
  }

  if (error) {
    return (
      <Alert severity="error" sx={{ mt: 2 }}>
        {error}
      </Alert>
    );
  }

  return (
    <Box>
      <Typography variant="h4" gutterBottom>
        Practice Problems
      </Typography>

      {selectedProblem ? (
        <Box>
          <Button 
            variant="outlined" 
            onClick={() => setSelectedProblem(null)}
            sx={{ mb: 2 }}
          >
            Back to Problems
          </Button>
          <Paper sx={{ p: 3 }}>
            <Typography variant="h5" gutterBottom>
              {selectedProblem.title}
            </Typography>
            <Box sx={{ mb: 2 }}>
              <Chip 
                label={selectedProblem.type.replace('_', ' ').toUpperCase()} 
                sx={{ mr: 1 }}
              />
              <Chip 
                label={selectedProblem.difficulty.toUpperCase()}
                color={
                  selectedProblem.difficulty === 'easy' 
                    ? 'success' 
                    : selectedProblem.difficulty === 'medium' 
                    ? 'warning' 
                    : 'error'
                }
              />
            </Box>
            <Typography variant="body1" sx={{ whiteSpace: 'pre-line', mb: 2 }}>
              {selectedProblem.question}
            </Typography>
            {selectedProblem.parameters && (
              <Box sx={{ mt: 2 }}>
                <Typography variant="subtitle2" gutterBottom>
                  Parameters:
                </Typography>
                <pre>{JSON.stringify(selectedProblem.parameters, null, 2)}</pre>
              </Box>
            )}
          </Paper>
        </Box>
      ) : (
        <Grid container spacing={3}>
          {problems.map((problem) => (
            <Grid item xs={12} sm={6} md={4} key={problem.id}>
              <Card>
                <CardContent>
                  <Typography variant="h6" gutterBottom>
                    {problem.title}
                  </Typography>
                  <Box sx={{ mb: 2 }}>
                    <Chip 
                      label={problem.type.replace('_', ' ').toUpperCase()} 
                      size="small" 
                      sx={{ mr: 1 }}
                    />
                    <Chip 
                      label={problem.difficulty.toUpperCase()}
                      size="small"
                      color={
                        problem.difficulty === 'easy' 
                          ? 'success' 
                          : problem.difficulty === 'medium' 
                          ? 'warning' 
                          : 'error'
                      }
                    />
                  </Box>
                  <Typography variant="body2" color="text.secondary">
                    {problem.description}
                  </Typography>
                </CardContent>
                <CardActions>
                  <Button 
                    size="small" 
                    onClick={() => setSelectedProblem(problem)}
                  >
                    View Problem
                  </Button>
                </CardActions>
              </Card>
            </Grid>
          ))}
        </Grid>
      )}
    </Box>
  );
}

export default Practice; 