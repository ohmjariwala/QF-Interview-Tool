from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse
import json
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.services.problem_generator import ProblemGenerator

# Initialize problem generator
problem_generator = ProblemGenerator()

def handle_generate(params):
    """Handle generate problem request."""
    problem = problem_generator.generate_problem(
        params.get('problem_type', [None])[0],
        params.get('difficulty', [None])[0]
    )
    return {"status": "success", "problem": problem}

def handle_types():
    """Handle get problem types request."""
    return {
        "status": "success",
        "types": problem_generator.problem_types,
        "difficulties": problem_generator.difficulty_levels
    }

def handle_practice():
    """Handle get practice problems request."""
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

async def handler(request):
    """Main handler function for Vercel serverless deployment."""
    # Set default headers
    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type'
    }

    try:
        # Get the HTTP method
        method = request.get('method', '')

        # Handle OPTIONS request for CORS
        if method == 'OPTIONS':
            return {
                'statusCode': 200,
                'headers': headers,
                'body': ''
            }

        # Parse URL from request
        url = request.get('url', '')
        parsed_url = urlparse(url)
        path = parsed_url.path
        query_params = parse_qs(parsed_url.query)

        # Route the request
        if path == '/api/problems/generate':
            response_data = handle_generate(query_params)
        elif path == '/api/problems/types':
            response_data = handle_types()
        elif path == '/api/problems/practice':
            response_data = handle_practice()
        else:
            response_data = {"status": "error", "message": f"Invalid endpoint: {path}"}
            return {
                'statusCode': 404,
                'headers': headers,
                'body': json.dumps(response_data)
            }

        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps(response_data)
        }

    except Exception as e:
        error_response = {
            "status": "error", 
            "message": str(e),
            "path": path if 'path' in locals() else 'unknown',
            "method": method if 'method' in locals() else 'unknown'
        }
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps(error_response)
        } 