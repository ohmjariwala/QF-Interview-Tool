from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
import uvicorn
from dotenv import load_dotenv
import os

from services.problem_generator import ProblemGenerator

# Load environment variables
load_dotenv()

app = FastAPI(
    title="QF Interview Tool - Python Backend",
    description="Python backend for quantitative finance calculations and problem generation",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
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
    problem_type: str = Query(None, description="Type of problem to generate"),
    difficulty: str = Query(None, description="Difficulty level of the problem")
):
    """Generate a random quantitative finance problem."""
    try:
        problem = problem_generator.generate_problem(problem_type, difficulty)
        return {"status": "success", "problem": problem}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.get("/problems/practice")
async def get_practice_problems():
    try:
        problems = problem_generator.get_practice_problems()
        return {"status": "success", "problems": problems}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.get("/problems/types")
async def get_problem_types():
    """Get available problem types."""
    return {
        "status": "success",
        "types": problem_generator.problem_types,
        "difficulties": problem_generator.difficulty_levels
    }

if __name__ == "__main__":
    port = int(os.getenv("PYTHON_PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True) 