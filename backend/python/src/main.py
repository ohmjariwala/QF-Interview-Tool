from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
import uvicorn
from dotenv import load_dotenv
import os

from services.problem_generator import ProblemGenerator

# Load environment variables
load_dotenv()

# Create FastAPI instance
app = FastAPI(
    title="QF Interview Tool - Python Backend",
    description="Python backend for quantitative finance calculations and problem generation",
    version="1.0.0"
)

# Configure CORS
origins = [
    "http://localhost:5173",
    "http://localhost:3000",
    "https://ohmjariwala.github.io"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize problem generator
problem_generator = ProblemGenerator()

@app.get("/")
async def root():
    return {"message": "QF Interview Tool Python Backend API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/problems/generate")
async def generate_problem(
    problem_type: Optional[str] = Query(None, description="Type of problem to generate"),
    difficulty: Optional[str] = Query(None, description="Difficulty level of the problem")
):
    """Generate a random quantitative finance problem."""
    try:
        problem = problem_generator.generate_problem(problem_type, difficulty)
        return {"status": "success", "problem": problem}
    except ValueError as e:
        return {"status": "error", "message": str(e)}

@app.get("/problems/types")
async def get_problem_types():
    """Get available problem types."""
    return {
        "status": "success",
        "types": problem_generator.problem_types,
        "difficulties": problem_generator.difficulty_levels
    }

@app.get("/problems/practice")
async def get_practice_problems():
    """Get a list of practice problems."""
    try:
        problems = [
            {
                "id": 1,
                "title": "Black-Scholes Option Pricing",
                "type": "option_pricing",
                "difficulty": "medium",
                "description": "Calculate the price of a European call option using the Black-Scholes formula.",
                "question": "Given a stock price of $100, strike price of $95, risk-free rate of 5%, volatility of 20%, and time to expiration of 1 year, calculate the price of a European call option.",
                "parameters": {
                    "S": 100,
                    "K": 95,
                    "r": 0.05,
                    "sigma": 0.2,
                    "T": 1
                }
            },
            {
                "id": 2,
                "title": "Portfolio Optimization",
                "type": "portfolio_optimization",
                "difficulty": "hard",
                "description": "Optimize a portfolio using Modern Portfolio Theory.",
                "question": "Given three assets with expected returns [0.1, 0.15, 0.12] and a covariance matrix, find the optimal portfolio weights that maximize the Sharpe ratio.",
                "parameters": {
                    "returns": [0.1, 0.15, 0.12],
                    "risk_free_rate": 0.02
                }
            }
        ]
        return {"status": "success", "problems": problems}
    except Exception as e:
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port) 