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
                "title": "Card Deck Choice",
                "type": "probability",
                "difficulty": "medium",
                "question": "Two decks of cards. One deck has 52 cards, the other has 104. You pick two cards separately from a same pack. If both of two cards are red, you win. Which pack will you choose?",
                "solution": "104 card pack - (52/104)*(51/103) > (26/52)*(25/51), or 51/103 > 25/51",
                "description": "A probability problem involving card selection"
            },
            {
                "id": 4,
                "title": "Mental Math",
                "type": "probability",
                "difficulty": "easy",
                "question": "What is 39*41?",
                "solution": "1599 - 39*41 = (40-1)*(40+1) = 40*40 - 1 = 1599",
                "description": "A mental math problem using algebraic patterns"
            },
            {
                "id": 5,
                "title": "Salary Average Problem",
                "type": "probability",
                "difficulty": "medium",
                "question": "A group of people wants to determine their average salary on the condition that no individual would be able to find out anyone else's salary. Can they accomplish this, and, if so, how?",
                "solution": "Yes, it's possible - The first person thinks of a random number, say X. This person adds this number to her salary. The rest of the group simply adds their salary to the initial number. Then, the first person subtracts the random number X and divides the total salary sum by the size of the group to obtain the average.",
                "description": "A problem solving question involving privacy and mathematics"
            },
            {
                "id": 6,
                "title": "Digit Count Problem",
                "type": "probability",
                "difficulty": "hard",
                "question": "How many digits are in 99 to the 99th power?",
                "solution": "198 - 99^99 = (100)^(99) * (.99)^99 = (10)^(198) * (.99)^99. You can convince yourself 10^198 has 199 digits, and 0.99^.99 approaches 1/e. Thus, (10)^(198) * (.99)^99 has 198 digits.",
                "description": "A mathematical reasoning problem involving exponents"
            },
            {
                "id": 7,
                "title": "Airplane Seating Probability",
                "type": "probability",
                "difficulty": "hard",
                "question": "A line of 100 passengers is waiting to board a plane. They each hold a ticket to one of the 100 seats on that flight. Unfortunately, the first person in line is crazy, and will ignore the seat number on their ticket, picking a random seat to occupy. All of the other passengers are quite normal, and will go to their proper seat unless it is already occupied. If it is occupied, they will then find a free seat to sit in, at random. What is the probability that the last (100th) person to board the plane will sit in their proper seat (#100)?",
                "solution": "0.5 - The fate of the last passenger is determined the second either the first or last seat on the plane is taken. This statement is true because the last person will either get the first seat or the last seat. All other seats will necessarily be taken by the time the last passenger gets to pick his/her seat. Since at each choice step, the first or last seat has an equal probability of being taken, the last person will get either the first or last with equal probability: 0.5.",
                "description": "A complex probability problem involving sequential decisions"
            },
            {
                "id": 8,
                "title": "Sum of Numbers",
                "type": "probability",
                "difficulty": "easy",
                "question": "What is the sum of the numbers one to 100?",
                "solution": "5050 - Sum of numbers from 1,2....n = n*(n+1)/2. You can also think about this problem by pairing off numbers - 1 and 100, 2 and 99, 3 and 98, 4 and 97, etc. We have 50 of these pairs, and each pair sums up to 101, so the final sum = 50*101 = 5050.",
                "description": "A mathematical problem involving series and patterns"
            },
            {
                "id": 9,
                "title": "Water Jug Problem",
                "type": "probability",
                "difficulty": "medium",
                "question": "You have a 3 gallon jug and 5 gallon jug, how do you measure out exactly 4 gallons? Is this possible?",
                "solution": "Yes, it's possible - Fill up the 3 gallon jug. Then, pour the liquid into the 5 gallon jug. Fill the 3 gallon jug again, and then fill the 5 gallon jug until it is full. We now have 1 gallon remaining in the 3 gallon jug. We empty the five gallon jug and pour the remaining 1 gallon into our 5 gallon jug. Finally, we fill the 3 gallon jug and add this to the 5 gallon jug (which already had 1 gallon). We are left with 4 gallons in the 5 gallon jug.",
                "description": "A problem solving question involving liquid measurements"
            },
            {
                "id": 10,
                "title": "Coin Flip Probability",
                "type": "probability",
                "difficulty": "medium",
                "question": "You have 17 coins and I have 16 coins, we flip all coins at the same time. If you have more heads then you win, if we have the same number of heads or if you have less then I win. What's your probability of winning?",
                "solution": "0.5 - Use recursion - The initial 16 flips have the same probability of everything. Thus, the game completely depends on if the last coin flip is tails or head (50/50 chance of H vs. T).",
                "description": "A probability problem involving coin flips"
            },
            {
                "id": 11,
                "title": "Card Color Probability",
                "type": "probability",
                "difficulty": "easy",
                "question": "What is the probability you draw two cards of the same color from a standard 52-card deck? You are drawing without replacement.",
                "solution": "25/51 - You either draw a black or a red card first. Then, there are 51 cards left in the deck and 25 of these cards have the same color. Thus, the probability is 25/51.",
                "description": "A probability problem involving card drawing"
            },
            {
                "id": 12,
                "title": "Light Bulb Problem",
                "type": "probability",
                "difficulty": "medium",
                "question": "You're in a room with three light switches, each of which controls one of three light bulbs in the next room. You need to determine which switch controls which bulb. All lights are off to begin, and you can't see into one room from the other. You can inspect the other room only once. How can you find out which switches are connected to which bulbs? Is this possible?",
                "solution": "Yes, it's possible - Leave switch 1 off. Then, turn switch 2 on for ten minutes. After the ten minutes, turn it off and quickly turn on switch 3. Now, go into the room. The currently lit up bulb connects to switch 3. The bulb that off but still warm is from switch 2, and the remaining bulb is from switch 1.",
                "description": "A logical reasoning problem"
            },
            {
                "id": 13,
                "title": "World Series Probability",
                "type": "probability",
                "difficulty": "medium",
                "question": "In world series, what are the odds it goes 7 games if each team equal chance of winning?",
                "solution": "20/64 - Out of the first three games, each team needs to win three. Thus, (6 choose 3)*(.5^6) = 20/64, as each team has a 1/2 probability of winning each game.",
                "description": "A probability problem involving sports"
            },
            {
                "id": 14,
                "title": "Even Heads Probability",
                "type": "probability",
                "difficulty": "medium",
                "question": "Given 100 coin flips, what is the probability that you get an even number of heads?",
                "solution": "1/2 - Whether there is an odd or even number of heads is ultimately determined by the final flip (50/50 chance of being heads vs. tails), for any number of flips.",
                "description": "A probability problem involving coin flips"
            },
            {
                "id": 15,
                "title": "Ball Ordering Problem",
                "type": "probability",
                "difficulty": "medium",
                "question": "There are 5 balls, 3 red, and 2 black. What is the probability that a random ordering of the 5 balls does not have the 2 black balls next to each other?",
                "solution": "0.6 - Because of repeats of black/red balls, there are 10 combinations of red/black balls: (5 choose 2) or (5 choose 3) spots to put the black or red balls, respectively. There are 4 places that 2 black balls can be next to each other, so the other 6 combinations do NOT have two black balls next to each other.",
                "description": "A probability problem involving ball arrangements"
            },
            {
                "id": 16,
                "title": "Multiple of 15",
                "type": "probability",
                "difficulty": "medium",
                "question": "What is the least multiple of 15 whose digits consist only of 1's and 0's?",
                "solution": "1110 - The last digit must be zero (30, 45, 60, 75, etc.). Multiples of 15 never end in 1. Then, starting checking numbers. 10, 100, 110, 1000, 1100, 1110. You will quickly arrive at the answer if you are good with your mental math.",
                "description": "A number theory problem"
            },
            {
                "id": 17,
                "title": "Prime Number Check",
                "type": "probability",
                "difficulty": "medium",
                "question": "Is 1027 a prime number?",
                "solution": "No - 1027 = 1000 + 27 = 10^3 + 3^3. We know a^3 + b^3 can be factored, so 1027 is NOT prime.",
                "description": "A number theory problem"
            },
            {
                "id": 18,
                "title": "Option Volatility",
                "type": "option_pricing",
                "difficulty": "easy",
                "question": "Does the price of a call option increase when volatility increases?",
                "solution": "Yes - sometimes a rare finance question is included in these interviews; remember that both time and volatility increase the prices of both calls and puts",
                "description": "An option pricing concept question"
            },
            {
                "id": 19,
                "title": "Ball Color Game",
                "type": "probability",
                "difficulty": "medium",
                "question": "2 blue and 2 red balls, in a box, no replacing. Guess the color of the ball, you receive a dollar if you are correct. What is the dollar amount you would pay to play this game?",
                "solution": "17/6 dollars - You'll always get the last ball right as your sampling w/o replacement. The first ball you have a 50% chance of getting right. The second ball you have a 2/3 chance of getting right.",
                "description": "A probability problem involving expected value"
            },
            {
                "id": 20,
                "title": "Power of 2",
                "type": "probability",
                "difficulty": "easy",
                "question": "What is the singles digit for 2^230?",
                "solution": "4 - Repeating patterns -- 2,4,8,6,2 -- follow the pattern.",
                "description": "A number theory problem involving patterns"
            }
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

    def generate_stochastic_process_problem(self, difficulty: str) -> Dict[str, Any]:
        """Generate a stochastic process problem."""
        if difficulty == 'easy':
            return {
                'type': 'stochastic_processes',
                'difficulty': difficulty,
                'question': """
                Consider a standard Brownian motion W(t) and the process X(t) = W(t) - t/2.
                
                1. Show that X(t) is a martingale
                2. Calculate E[X(t)] and Var[X(t)]
                3. What is the distribution of X(t) at any fixed time t?
                4. Explain why this process has independent increments
                """
            }
        elif difficulty == 'medium':
            return {
                'type': 'stochastic_processes',
                'difficulty': difficulty,
                'question': """
                Consider the following questions about stochastic processes:

                1. Define and compare:
                   - Brownian Motion
                   - Geometric Brownian Motion
                   - Ornstein-Uhlenbeck Process
                
                2. For a standard Brownian motion W(t):
                   - What is its PDF at time t?
                   - What is its CDF?
                   - What are its key properties?
                
                3. For a process X(t) = exp(W(t) - t/2):
                   - Show that this is a martingale
                   - Calculate E[X(t)]
                   - Is this process stationary?
                """
            }
        else:  # hard
            return {
                'type': 'stochastic_processes',
                'difficulty': difficulty,
                'question': """
                Consider a stock price following Geometric Brownian Motion:
                dS(t) = μS(t)dt + σS(t)dW(t)

                1. Derive the solution for S(t) using Itô's lemma
                2. Show that log(S(t)) follows a normal distribution
                3. Calculate:
                   - E[S(t)]
                   - Var[S(t)]
                   - The probability that S(t) > S(0)
                
                4. Now consider a more complex process:
                   X(t) = W(t)² - t
                   where W(t) is a standard Brownian motion
                   
                   a) Is this a martingale? Prove your answer
                   b) Calculate E[X(t)] and Var[X(t)]
                   c) Find the quadratic variation of X(t)
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
        elif problem_type == 'stochastic_processes':
            return self.generate_stochastic_process_problem(difficulty)
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