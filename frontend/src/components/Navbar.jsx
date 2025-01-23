import { AppBar, Toolbar, Typography, Button } from '@mui/material';
import { useNavigate } from 'react-router-dom';

function Navbar() {
  const navigate = useNavigate();

  return (
    <AppBar position="static">
      <Toolbar>
        <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
          QF Interview Tool
        </Typography>
        <Button color="inherit" onClick={() => navigate('/')}>
          Home
        </Button>
        <Button color="inherit" onClick={() => navigate('/generate')}>
          Generate Problem
        </Button>
        <Button color="inherit" onClick={() => navigate('/practice')}>
          Practice
        </Button>
        <Button color="inherit" onClick={() => navigate('/mental-math')}>
          Mental Math
        </Button>
      </Toolbar>
    </AppBar>
  );
}

export default Navbar; 