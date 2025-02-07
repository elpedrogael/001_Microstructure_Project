import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import weibull_min

#Price Distribution
def generate_price_distribution(lambda_= 50, k= 10, size = 1000):
    prices =weibull_min.rvs(k, scale = lambda_, size = size)
    return prices

def plot_price_distribution(price):
    plt.hist(price, bins=50, density=True, alpha=0.6, color='red')
    plt.title('Price_Distribution_(Weibull)')
    plt.xlabel('Price')
    plt.ylabel('Density')
    plt.show()

 #Expected Revenue
def expected_revenue_liquidity(S, π_I=0, π_LB=0.5, π_LS=0.5):
    return (π_LB *(0.5 - 0.08 * S)) + (π_LS * (0.5 - 0.08 * S))

def expected_revenue_informed_trades(S, π_I = 0.4, π_LB=0.5, π_LS=0.5):
    return  π_I * 0.4 + (π_LB * (0.5 - 0.08 * S)) + (π_LS * (0.5 - 0.08 *S))

#Optimal Bid-Ask Prices
def copeland_galai_bid_ask(P0, S_values):
    bid_prices = [P0 - 0.08 * S for S in S_values]
    ask_prices = [P0 + 0.08 * S for S in S_values]
    return bid_prices, ask_prices
