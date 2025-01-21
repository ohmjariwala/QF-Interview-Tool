import { useState, useEffect } from 'react';
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
  Card,
  CardContent,
  Grid,
  Pagination,
} from '@mui/material';
import { getInterviewQuestionsUrl } from '../config/api';

function InterviewQuestions() {
  const [source, setSource] = useState('');
  const [questions, setQuestions] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [page, setPage] = useState(1);
  const questionsPerPage = 5;

  const sources = ['All', 'PDF', 'QuantNet'];

  const fetchQuestions = async () => {
    setLoading(true);
    setError(null);
    try {
      const url = getInterviewQuestionsUrl(20, source === 'All' ? null : source);
      const response = await fetch(url);
      const data = await response.json();
      if (data.status === 'success') {
        setQuestions(data.questions);
      } else {
        setError(data.message || 'Failed to fetch questions');
      }
    } catch (err) {
      setError('Failed to connect to the server');
    }
    setLoading(false);
  };

  useEffect(() => {
    fetchQuestions();
  }, [source]);

  const handlePageChange = (event, value) => {
    setPage(value);
  };

  const paginatedQuestions = questions.slice(
    (page - 1) * questionsPerPage,
    page * questionsPerPage
  );

  return (
    <Box>
      <Typography variant="h4" gutterBottom>
        Interview Questions
      </Typography>

      <Paper sx={{ p: 3, mb: 3 }}>
        <FormControl fullWidth sx={{ mb: 2 }}>
          <InputLabel>Source</InputLabel>
          <Select
            value={source}
            label="Source"
            onChange={(e) => setSource(e.target.value)}
          >
            {sources.map((src) => (
              <MenuItem key={src} value={src}>
                {src}
              </MenuItem>
            ))}
          </Select>
        </FormControl>

        <Button
          variant="contained"
          fullWidth
          onClick={fetchQuestions}
          disabled={loading}
        >
          {loading ? <CircularProgress size={24} /> : 'Refresh Questions'}
        </Button>
      </Paper>

      {error && (
        <Alert severity="error" sx={{ mb: 3 }}>
          {error}
        </Alert>
      )}

      <Grid container spacing={2}>
        {paginatedQuestions.map((question, index) => (
          <Grid item xs={12} key={index}>
            <Card>
              <CardContent>
                <Typography variant="subtitle2" color="text.secondary" gutterBottom>
                  Source: {question.source}
                </Typography>
                <Typography variant="body1">
                  {question.question}
                </Typography>
              </CardContent>
            </Card>
          </Grid>
        ))}
      </Grid>

      {questions.length > questionsPerPage && (
        <Box sx={{ mt: 3, display: 'flex', justifyContent: 'center' }}>
          <Pagination
            count={Math.ceil(questions.length / questionsPerPage)}
            page={page}
            onChange={handlePageChange}
            color="primary"
          />
        </Box>
      )}
    </Box>
  );
}

export default InterviewQuestions; 