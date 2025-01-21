import { Typography, Button, Box, Paper, Grid } from '@mui/material';
import { useNavigate } from 'react-router-dom';

function Home() {
  const navigate = useNavigate();

  return (
    <Box sx={{ textAlign: 'center', py: 4 }}>
      <Typography variant="h2" component="h1" gutterBottom>
        Quantitative Finance Interview Tool
      </Typography>
      <Typography variant="h5" color="text.secondary" paragraph>
        Practice quantitative finance problems and prepare for your interviews
      </Typography>
      
      <Grid container spacing={4} sx={{ mt: 4 }}>
        <Grid item xs={12} md={6}>
          <Paper sx={{ p: 3, height: '100%' }}>
            <Typography variant="h5" gutterBottom>
              Generate Problems
            </Typography>
            <Typography paragraph>
              Generate random problems in various categories including option pricing,
              portfolio optimization, probability, and more.
            </Typography>
            <Button 
              variant="contained" 
              color="primary"
              onClick={() => navigate('/generate')}
            >
              Start Generating
            </Button>
          </Paper>
        </Grid>
        
        <Grid item xs={12} md={6}>
          <Paper sx={{ p: 3, height: '100%' }}>
            <Typography variant="h5" gutterBottom>
              Practice Mode
            </Typography>
            <Typography paragraph>
              Test your skills with a collection of curated problems.
              Track your progress and get instant feedback.
            </Typography>
            <Button 
              variant="contained" 
              color="secondary"
              onClick={() => navigate('/practice')}
            >
              Start Practicing
            </Button>
          </Paper>
        </Grid>
      </Grid>
    </Box>
  );
}

export default Home; 