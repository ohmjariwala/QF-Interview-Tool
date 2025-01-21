import numpy as np
from scipy.stats import norm
import yfinance as yf

def black_scholes_call(S, K, T, r, sigma):
    """
    Calculate Black-Scholes call option price.
    
    Parameters:
    S: Current stock price
    K: Strike price
    T: Time to maturity (in years)
    r: Risk-free interest rate
    sigma: Volatility
    
    Returns:
    call_price: Black-Scholes call option price
    """
    d1 = (np.log(S/K) + (r + sigma**2/2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    
    call_price = S*norm.cdf(d1) - K*np.exp(-r*T)*norm.cdf(d2)
    return call_price

def calculate_portfolio_metrics(weights, returns):
    """
    Calculate portfolio metrics including return, volatility, and Sharpe ratio.
    
    Parameters:
    weights: Array of portfolio weights
    returns: DataFrame of asset returns
    
    Returns:
    dict: Portfolio metrics
    """
    portfolio_return = np.sum(returns.mean() * weights) * 252
    portfolio_vol = np.sqrt(np.dot(weights.T, np.dot(returns.cov() * 252, weights)))
    sharpe_ratio = portfolio_return / portfolio_vol
    
    return {
        "return": portfolio_return,
        "volatility": portfolio_vol,
        "sharpe_ratio": sharpe_ratio
    }

def fetch_stock_data(ticker, start_date, end_date):
    """
    Fetch stock data using yfinance.
    
    Parameters:
    ticker: Stock ticker symbol
    start_date: Start date for data
    end_date: End date for data
    
    Returns:
    DataFrame: Stock price data
    """
    stock = yf.Ticker(ticker)
    df = stock.history(start=start_date, end=end_date)
    return df

def calculate_implied_volatility(option_price, S, K, T, r, option_type='call'):
    """
    Calculate implied volatility using Newton-Raphson method.
    
    Parameters:
    option_price: Market price of option
    S: Current stock price
    K: Strike price
    T: Time to maturity (in years)
    r: Risk-free interest rate
    option_type: Type of option ('call' or 'put')
    
    Returns:
    float: Implied volatility
    """
    sigma = 0.5  # Initial guess
    max_iterations = 100
    tolerance = 1e-5
    
    for i in range(max_iterations):
        if option_type == 'call':
            price = black_scholes_call(S, K, T, r, sigma)
        else:
            # Add put option calculation if needed
            continue
            
        diff = option_price - price
        if abs(diff) < tolerance:
            return sigma
            
        # Calculate vega
        d1 = (np.log(S/K) + (r + sigma**2/2)*T) / (sigma*np.sqrt(T))
        vega = S * np.sqrt(T) * norm.pdf(d1)
        
        # Update sigma
        sigma = sigma + diff/vega
        
    return sigma 