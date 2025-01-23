import { useState, useEffect } from 'react';
import { Box, Typography, TextField, Button, Paper, CircularProgress } from '@mui/material';
import { useTheme } from '@mui/material/styles';
import axios from 'axios';
import { getMentalMathUrl } from '../config/api';

function MentalMath() {
    const theme = useTheme();
    const [timeLeft, setTimeLeft] = useState(120);
    const [isActive, setIsActive] = useState(false);
    const [score, setScore] = useState(0);
    const [currentProblem, setCurrentProblem] = useState(null);
    const [userAnswer, setUserAnswer] = useState('');
    const [loading, setLoading] = useState(false);

    const fetchNewProblem = async () => {
        try {
            setLoading(true);
            const response = await axios.get(getMentalMathUrl());
            if (response.data.status === 'success') {
                setCurrentProblem(response.data.problem);
            }
        } catch (error) {
            console.error('Error fetching problem:', error);
        } finally {
            setLoading(false);
        }
    };

    const startGame = async () => {
        setIsActive(true);
        setScore(0);
        setTimeLeft(120);
        await fetchNewProblem();
    };

    const checkAnswer = async () => {
        if (!currentProblem) return;

        const userNum = parseInt(userAnswer);
        if (userNum === currentProblem.answer) {
            setScore(prev => prev + 1);
        }
        setUserAnswer('');
        await fetchNewProblem();
    };

    useEffect(() => {
        let interval = null;
        if (isActive && timeLeft > 0) {
            interval = setInterval(() => {
                setTimeLeft(time => time - 1);
            }, 1000);
        } else if (timeLeft === 0) {
            setIsActive(false);
            setCurrentProblem(null);
        }
        return () => clearInterval(interval);
    }, [isActive, timeLeft]);

    const handleKeyPress = (event) => {
        if (event.key === 'Enter' && userAnswer) {
            checkAnswer();
        }
    };

    return (
        <Box sx={{ p: 3, maxWidth: 600, mx: 'auto' }}>
            <Paper elevation={3} sx={{ p: 3, textAlign: 'center' }}>
                <Typography variant="h4" gutterBottom>
                    Mental Math Challenge
                </Typography>
                
                {!isActive ? (
                    <Button 
                        variant="contained" 
                        color="primary" 
                        onClick={startGame}
                        sx={{ mt: 2 }}
                    >
                        Start Game
                    </Button>
                ) : (
                    <>
                        <Typography variant="h5" sx={{ mb: 2, color: theme.palette.primary.main }}>
                            Time Left: {timeLeft}s
                        </Typography>
                        <Typography variant="h6" sx={{ mb: 2 }}>
                            Score: {score}
                        </Typography>
                        
                        {loading ? (
                            <CircularProgress />
                        ) : currentProblem && (
                            <>
                                <Typography variant="h5" sx={{ mb: 2 }}>
                                    {currentProblem.question}
                                </Typography>
                                <TextField
                                    fullWidth
                                    variant="outlined"
                                    label="Your Answer"
                                    value={userAnswer}
                                    onChange={(e) => setUserAnswer(e.target.value)}
                                    onKeyPress={handleKeyPress}
                                    type="number"
                                    autoFocus
                                    sx={{ mb: 2 }}
                                />
                                <Button 
                                    variant="contained" 
                                    color="primary"
                                    onClick={checkAnswer}
                                    disabled={!userAnswer}
                                >
                                    Submit
                                </Button>
                            </>
                        )}
                    </>
                )}
            </Paper>
        </Box>
    );
}

export default MentalMath; 