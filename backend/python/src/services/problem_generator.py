import numpy as np
from typing import Dict, Any, Optional
import random
from datetime import datetime, timedelta

class ProblemGenerator:
    def __init__(self):
        self.difficulty_levels = ['easy', 'medium', 'hard']
        self.problem_types = [
            'option_pricing',
            'portfolio_optimization',
            'probability',
            'statistics',
            'stochastic_processes'
        ]

    def generate_option_pricing_problem(self, difficulty: str) -> Dict[str, Any]:
        """Generate an option pricing problem."""
        if difficulty == 'easy':
            S = round(random.uniform(80, 120), 2)
            K = round(S * random.uniform(0.9, 1.1), 2)
            T = round(random.uniform(0.25, 1.0), 2)
            r = round(random.uniform(0.01, 0.05), 3)
            sigma = round(random.uniform(0.15, 0.30), 2)
        else:
            # More complex scenarios for medium/hard difficulties
            S = round(random.uniform(50, 150), 2)
            K = round(S * random.uniform(0.7, 1.3), 2)
            T = round(random.uniform(0.1, 2.0), 2)
            r = round(random.uniform(0.001, 0.08), 3)
            sigma = round(random.uniform(0.10, 0.50), 2)

        problem = {
            'type': 'option_pricing',
            'difficulty': difficulty,
            'parameters': {
                'stock_price': S,
                'strike_price': K,
                'time_to_maturity': T,
                'risk_free_rate': r,
                'volatility': sigma
            },
            'question': f"""
            Calculate the Black-Scholes price for a European call option with:
            - Current stock price: ${S}
            - Strike price: ${K}
            - Time to maturity: {T} years
            - Risk-free rate: {r*100}%
            - Volatility: {sigma*100}%
            """
        }
        return problem

    def generate_portfolio_problem(self, difficulty: str) -> Dict[str, Any]:
        """Generate a portfolio optimization problem."""
        n_assets = 3 if difficulty == 'easy' else 5
        returns = [round(random.uniform(0.05, 0.15), 3) for _ in range(n_assets)]
        volatilities = [round(random.uniform(0.10, 0.30), 3) for _ in range(n_assets)]
        
        assets_info = [
            f"Asset {i+1}: Return = {returns[i]:.1%}, Volatility = {volatilities[i]:.1%}"
            for i in range(n_assets)
        ]
        
        problem = {
            'type': 'portfolio_optimization',
            'difficulty': difficulty,
            'parameters': {
                'returns': returns,
                'volatilities': volatilities,
            },
            'question': f"""
            Consider a portfolio with {n_assets} assets having the following annual returns and volatilities:
            
            {chr(10).join(assets_info)}
            
            Find the optimal portfolio weights that maximize the Sharpe ratio, assuming a risk-free rate of 2%.
            """
        }
        return problem

    def generate_probability_problem(self, difficulty: str) -> Dict[str, Any]:
        """Generate a probability/statistics problem."""
        if difficulty == 'easy':
            return {
                'type': 'probability',
                'difficulty': difficulty,
                'question': """
                A trader observes that a stock's daily returns follow a normal distribution with 
                mean 0.1% and standard deviation 1.5%. What is the probability that tomorrow's 
                return will be positive?
                """
            }
        else:
            return {
                'type': 'probability',
                'difficulty': difficulty,
                'question': """
                A trading strategy generates daily returns that are normally distributed with 
                mean 0.05% and standard deviation 1.2%. If you implement this strategy with 
                $1 million:
                1. What is the 95% Value at Risk (VaR)?
                2. What is the probability of losing more than $25,000 in a single day?
                3. What is the expected number of days in a year where losses exceed $20,000?
                """
            }

    def generate_problem(self, problem_type: Optional[str] = None, difficulty: Optional[str] = None) -> Dict[str, Any]:
        """Generate a random problem based on type and difficulty."""
        if problem_type is None:
            problem_type = random.choice(self.problem_types)
        if difficulty is None:
            difficulty = random.choice(self.difficulty_levels)

        if problem_type not in self.problem_types:
            raise ValueError(f"Invalid problem type: {problem_type}. Must be one of {self.problem_types}")
        if difficulty not in self.difficulty_levels:
            raise ValueError(f"Invalid difficulty: {difficulty}. Must be one of {self.difficulty_levels}")

        if problem_type == 'option_pricing':
            return self.generate_option_pricing_problem(difficulty)
        elif problem_type == 'portfolio_optimization':
            return self.generate_portfolio_problem(difficulty)
        elif problem_type in ['probability', 'statistics']:
            return self.generate_probability_problem(difficulty)
        else:
            raise ValueError(f"Unknown problem type: {problem_type}")

if __name__ == "__main__":
    generator = ProblemGenerator()
    print("\nGenerated Problems:\n")
    
    print("1. Random Problem:")
    print("-----------------")
    problem = generator.generate_problem()
    print(f"Type: {problem['type']}")
    print(f"Difficulty: {problem['difficulty']}")
    print("Question:")
    print(problem['question'])
    print("\n")
    
    print("2. Option Pricing Problem (Hard):")
    print("--------------------------------")
    problem = generator.generate_problem('option_pricing', 'hard')
    print(problem['question'])
    print("\n")
    
    print("3. Portfolio Problem (Easy):")
    print("---------------------------")
    problem = generator.generate_problem('portfolio_optimization', 'easy')
    print(problem['question'])
    print("\n")
    
    print("4. Probability Problem (Medium):")
    print("-------------------------------")
    problem = generator.generate_problem('probability', 'medium')
    print(problem['question']) 