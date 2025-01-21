import { AppBar, Toolbar, Typography, Button, Box } from '@mui/material';
import { Link as RouterLink } from 'react-router-dom';

function Navbar() {
  return (
    <AppBar position="static">
      <Toolbar>
        <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
          QF Interview Tool
        </Typography>
        <Box>
          <Button color="inherit" component={RouterLink} to="/">
            Home
          </Button>
          <Button color="inherit" component={RouterLink} to="/generate">
            Generate Problem
          </Button>
          <Button color="inherit" component={RouterLink} to="/practice">
            Practice
          </Button>
        </Box>
      </Toolbar>
    </AppBar>
  );
}

export default Navbar; 