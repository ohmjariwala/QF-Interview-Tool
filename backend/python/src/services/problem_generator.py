import numpy as np
from typing import Dict, Any, List
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
        self.practice_problems = self._initialize_practice_problems()

    def _initialize_practice_problems(self) -> List[Dict[str, Any]]:
        """Initialize the list of practice problems with solutions."""
        return [
            {
                "id": 1,
                "title": "Tennis Game Probability",
                "type": "probability",
                "difficulty": "medium",
                "question": "For a 3 sets tennis game, would you bet on it finishing in 2 sets or 3 sets?",
                "solution": "Two sets - Let p=prob team 1 wins and q=prob team 2 wins. p^2 + q^2 = probability finish in two sets. 2*p*q = probability finish in three sets. p^2 + q^2 always >= 2*p*q, so the answer is two sets.",
                "description": "A probability problem involving game theory and tennis match outcomes"
            },
            {
                "id": 2,
                "title": "Random Dots on Square",
                "type": "probability",
                "difficulty": "medium",
                "question": "I have a square, and place three dots along the 4 edges at random. What is the probability that the dots lie on distinct edges?",
                "solution": "3/8 - Given the edge the first dot is on, the probability the other two dots are on distinct edges is (3/4)*(2/4)",
                "description": "A geometric probability problem involving random placement"
            },
            {
                "id": 3,
                "title": "Handshake Problem",
                "type": "probability",
                "difficulty": "easy",
                "question": "You have 10 people in a room. How many total handshakes if they all shake hands?",
                "solution": "45 - (10 choose 2) = 45 -- this is the total number of ways two people can shake hands.",
                "description": "A combinatorics problem involving handshakes"
            }
            # ... Add more practice problems here
        ]

    def generate_option_pricing_problem(self, difficulty: str) -> Dict[str, Any]:
        """Generate an option pricing problem."""
        if difficulty == 'easy':
            # Basic European call option
            S = round(random.uniform(80, 120), 2)
            K = round(S * random.uniform(0.9, 1.1), 2)
            T = round(random.uniform(0.25, 1.0), 2)
            r = round(random.uniform(0.01, 0.05), 3)
            sigma = round(random.uniform(0.15, 0.30), 2)
            
            return {
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
                
                Additionally, explain how changes in volatility would affect the option price.
                """
            }
        elif difficulty == 'medium':
            # American put option with dividend
            S = round(random.uniform(50, 150), 2)
            K = round(S * random.uniform(0.8, 1.2), 2)
            T = round(random.uniform(0.5, 2.0), 2)
            r = round(random.uniform(0.02, 0.06), 3)
            sigma = round(random.uniform(0.20, 0.40), 2)
            div_yield = round(random.uniform(0.01, 0.04), 3)
            
            return {
                'type': 'option_pricing',
                'difficulty': difficulty,
                'parameters': {
                    'stock_price': S,
                    'strike_price': K,
                    'time_to_maturity': T,
                    'risk_free_rate': r,
                    'volatility': sigma,
                    'dividend_yield': div_yield
                },
                'question': f"""
                Price an American put option with dividend yield:
                - Current stock price: ${S}
                - Strike price: ${K}
                - Time to maturity: {T} years
                - Risk-free rate: {r*100}%
                - Volatility: {sigma*100}%
                - Dividend yield: {div_yield*100}%
                
                1. Calculate the option price
                2. Explain early exercise considerations
                3. Compare with European put option price
                """
            }
        else:  # hard
            # Exotic option
            S = round(random.uniform(40, 160), 2)
            K = round(S * random.uniform(0.7, 1.3), 2)
            T = round(random.uniform(1.0, 3.0), 2)
            r = round(random.uniform(0.01, 0.08), 3)
            sigma = round(random.uniform(0.25, 0.50), 2)
            barrier = round(K * 1.2, 2)
            
            return {
                'type': 'option_pricing',
                'difficulty': difficulty,
                'parameters': {
                    'stock_price': S,
                    'strike_price': K,
                    'barrier_level': barrier,
                    'time_to_maturity': T,
                    'risk_free_rate': r,
                    'volatility': sigma
                },
                'question': f"""
                Price a up-and-out barrier call option:
                - Current stock price: ${S}
                - Strike price: ${K}
                - Barrier level: ${barrier}
                - Time to maturity: {T} years
                - Risk-free rate: {r*100}%
                - Volatility: {sigma*100}%
                
                1. Calculate the option price
                2. Explain the impact of the barrier on delta hedging
                3. Compare with vanilla call option price
                4. Discuss volatility smile implications
                """
            }

    def generate_portfolio_problem(self, difficulty: str) -> Dict[str, Any]:
        """Generate a portfolio optimization problem."""
        if difficulty == 'easy':
            n_assets = 3
            returns = np.random.normal(0.10, 0.20, n_assets)
            volatilities = np.random.uniform(0.15, 0.35, n_assets)
            correlations = np.random.uniform(-0.2, 0.6, (n_assets, n_assets))
            np.fill_diagonal(correlations, 1)
            
            assets_info = []
            for i in range(n_assets):
                assets_info.append(f"Asset {i+1}: Return = {returns[i]:.2%}, Volatility = {volatilities[i]:.2%}")
            
            return {
                'type': 'portfolio_optimization',
                'difficulty': difficulty,
                'parameters': {
                    'returns': returns.tolist(),
                    'volatilities': volatilities.tolist(),
                    'correlations': correlations.tolist()
                },
                'question': f"""
                Consider a portfolio with {n_assets} assets having the following annual returns and volatilities:
                
                {chr(10).join(assets_info)}
                
                1. Find the optimal portfolio weights that maximize the Sharpe ratio
                2. Calculate the portfolio's expected return and volatility
                3. Explain the impact of correlations on diversification
                """
            }
        elif difficulty == 'medium':
            n_assets = 5
            returns = np.random.normal(0.12, 0.25, n_assets)
            volatilities = np.random.uniform(0.20, 0.40, n_assets)
            correlations = np.random.uniform(-0.3, 0.7, (n_assets, n_assets))
            np.fill_diagonal(correlations, 1)
            constraints = [
                "No single asset can exceed 30% of the portfolio",
                "At least 20% must be in low-risk assets (1 and 2)",
                "Maximum 40% in high-risk assets (4 and 5)"
            ]
            
            return {
                'type': 'portfolio_optimization',
                'difficulty': difficulty,
                'parameters': {
                    'returns': returns.tolist(),
                    'volatilities': volatilities.tolist(),
                    'correlations': correlations.tolist(),
                    'constraints': constraints
                },
                'question': f"""
                Optimize a portfolio with {n_assets} assets subject to constraints:
                
                Asset Information:
                {chr(10).join([f"Asset {i+1}: μ={returns[i]:.2%}, σ={volatilities[i]:.2%}" for i in range(n_assets)])}
                
                Constraints:
                {chr(10).join([f"- {c}" for c in constraints])}
                
                1. Find the optimal portfolio weights
                2. Calculate the efficient frontier
                3. Analyze the impact of constraints
                4. Discuss rebalancing considerations
                """
            }
        else:  # hard
            n_assets = 7
            returns = np.random.normal(0.15, 0.30, n_assets)
            volatilities = np.random.uniform(0.25, 0.45, n_assets)
            correlations = np.random.uniform(-0.4, 0.8, (n_assets, n_assets))
            np.fill_diagonal(correlations, 1)
            transaction_costs = np.random.uniform(0.001, 0.003, n_assets)
            
            return {
                'type': 'portfolio_optimization',
                'difficulty': difficulty,
                'parameters': {
                    'returns': returns.tolist(),
                    'volatilities': volatilities.tolist(),
                    'correlations': correlations.tolist(),
                    'transaction_costs': transaction_costs.tolist()
                },
                'question': f"""
                Dynamic portfolio optimization problem with transaction costs:
                
                Asset Information:
                {chr(10).join([f"Asset {i+1}: μ={returns[i]:.2%}, σ={volatilities[i]:.2%}, TC={transaction_costs[i]:.3%}" for i in range(n_assets)])}
                
                1. Develop a dynamic rebalancing strategy considering transaction costs
                2. Calculate the multi-period efficient frontier
                3. Implement a risk parity approach
                4. Compare with static Markowitz optimization
                5. Analyze the impact of estimation error
                6. Discuss practical implementation challenges
                """
            }

    def generate_probability_problem(self, difficulty: str) -> Dict[str, Any]:
        """Generate a probability/statistics problem."""
        if difficulty == 'easy':
            return {
                'type': 'probability',
                'difficulty': difficulty,
                'question': """
                A trader observes that a stock's daily returns follow a normal distribution with 
                mean 0.1% and standard deviation 1.5%. 
                
                1. What is the probability that tomorrow's return will be positive?
                2. What is the probability of observing a return greater than 2%?
                3. Calculate the 95% confidence interval for the daily returns
                """
            }
        elif difficulty == 'medium':
            return {
                'type': 'probability',
                'difficulty': difficulty,
                'question': """
                A trading strategy generates daily returns that are normally distributed with 
                mean 0.05% and standard deviation 1.2%. If you implement this strategy with 
                $1 million:
                
                1. What is the 95% Value at Risk (VaR)?
                2. What is the Expected Shortfall (ES)?
                3. What is the probability of losing more than $25,000 in a single day?
                4. Calculate the expected number of days in a year where losses exceed $20,000
                5. How would your calculations change if returns were Student's t-distributed?
                """
            }
        else:  # hard
            return {
                'type': 'probability',
                'difficulty': difficulty,
                'question': """
                Consider a high-frequency trading strategy with the following characteristics:
                - Trade arrival follows a Poisson process with mean 100 trades per hour
                - Profit per trade follows a mixture of two normal distributions:
                  * 80% of trades: N(0.5, 1)
                  * 20% of trades: N(-2, 2)
                
                1. Calculate the expected daily profit
                2. What is the probability of a losing day?
                3. Derive the distribution of the maximum drawdown
                4. How many trades do you need to be 99% confident about the strategy's profitability?
                5. If you observe 3 consecutive losing days, what is the probability that the strategy is broken?
                """
            }

    def generate_problem(self, problem_type: str = None, difficulty: str = None) -> Dict[str, Any]:
        """Generate a random problem based on type and difficulty."""
        if problem_type is None:
            problem_type = random.choice(self.problem_types)
        if difficulty is None:
            difficulty = random.choice(self.difficulty_levels)

        if problem_type == 'option_pricing':
            return self.generate_option_pricing_problem(difficulty)
        elif problem_type == 'portfolio_optimization':
            return self.generate_portfolio_problem(difficulty)
        elif problem_type in ['probability', 'statistics']:
            return self.generate_probability_problem(difficulty)
        else:
            raise ValueError(f"Unknown problem type: {problem_type}")

    def get_practice_problems(self) -> List[Dict[str, Any]]:
        """Return the list of practice problems."""
        return self.practice_problems

# Example usage:
# generator = ProblemGenerator()
# problem = generator.generate_problem(problem_type='option_pricing', difficulty='medium') 

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