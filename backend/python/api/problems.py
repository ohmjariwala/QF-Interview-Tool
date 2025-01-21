from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse
import json
from src.services.problem_generator import ProblemGenerator

# Initialize problem generator
problem_generator = ProblemGenerator()

def parse_query_params(url):
    """Parse query parameters from URL."""
    parsed = urlparse(url)
    params = parse_qs(parsed.query)
    return {k: v[0] for k, v in params.items()}

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        """Handle GET requests."""
        try:
            # Parse the path and query parameters
            parsed_path = urlparse(self.path)
            path = parsed_path.path
            params = parse_query_params(self.path)

            # Set CORS headers
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type')
            self.end_headers()

            # Route the request
            if path == '/api/problems/generate':
                problem = problem_generator.generate_problem(
                    params.get('problem_type'),
                    params.get('difficulty')
                )
                response = {"status": "success", "problem": problem}
            
            elif path == '/api/problems/types':
                response = {
                    "status": "success",
                    "types": problem_generator.problem_types,
                    "difficulties": problem_generator.difficulty_levels
                }
            
            elif path == '/api/problems/practice':
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
                response = {"status": "success", "problems": problems}
            
            else:
                response = {"status": "error", "message": "Invalid endpoint"}

            self.wfile.write(json.dumps(response).encode())
        
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            error_response = {"status": "error", "message": str(e)}
            self.wfile.write(json.dumps(error_response).encode())

    def do_OPTIONS(self):
        """Handle OPTIONS requests for CORS."""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers() 