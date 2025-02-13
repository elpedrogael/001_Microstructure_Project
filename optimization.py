import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import weibull_min
from scipy.optimize import minimize
from scipy.integrate import quad

# Price Distribution
def generate_price_distribution(lambda_=50, k=10, size=1000):
    prices = weibull_min.rvs(k, scale=lambda_, size=size)
    return prices

def plot_price_distribution(price):
    plt.hist(price, bins=50, density=True, alpha=0.6, color='red')
    plt.title('Price Distribution (Weibull)')
    plt.xlabel('Price')
    plt.ylabel('Density')
    plt.show()

# Expected Revenue Functions
def expected_revenue_liquidity(S, π_I=0, π_LB=0.5, π_LS=0.5):
    return S

def expected_revenue_informed_trades(S, π_I=0.4, π_LB=0.5, π_LS=0.5):
    return S * (1 - π_I)

#Optimal Bid-Ask Prices
def copeland_galai_bid_ask(P0, S_values,π_I=0.4):
    bid_prices = [(.5 - 0.08 * S) * (S * (1- π_I)) for S in S_values]
    ask_prices = [(.5 + 0.08 * S) * (S * (1- π_I)) for S in S_values]
    return bid_prices, ask_prices

# Liquidity constraints
def pi_lb(ka, s0):
    return max(0, min(0.5, 0.5 - 0.08 * (ka - s0)))

def pi_ls(kb, s0):
    return max(0, min(0.5, 0.5 - 0.08 * (s0 - kb)))

# Weibull probability density function
def weibull_pdf(x, k=10, lamb=50):
    return (k / lamb) * (x / lamb) ** (k - 1) * np.exp(-(x / lamb) ** k)

# Objective Function for Optimal Bid-Ask Pricing
def objective_function(K, s0, π_I=0.4):
    ka, kb = K
    income = (1 - π_I) * (pi_lb(ka, s0) * (ka - s0) + pi_ls(kb, s0) * (s0 - kb))
    int_k_a, _ = quad(lambda S: (S - ka) * weibull_pdf(S), ka, np.inf)
    int_k_b, _ = quad(lambda S: (kb - S) * weibull_pdf(S), 0, kb)
    cost = π_I * (int_k_a + int_k_b)
    return -(income - cost)

# Optimize bid-ask spread
def optimize_bid_ask(s0, π_I=0.4):
    initial_guess = [s0 + 3, s0 - 3]
    bounds = [(s0, s0 + 10), (s0 - 10, s0)]

    result = minimize(objective_function, initial_guess, args=(s0, π_I), bounds=bounds)

    return result.x[1], result.x[0], -result.fun  # bid, ask, expected revenue
