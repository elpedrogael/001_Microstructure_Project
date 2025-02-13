import numpy as np
import matplotlib.pyplot as plt
from optimization import (generate_price_distribution, plot_price_distribution, expected_revenue_liquidity,
                          expected_revenue_informed_trades, optimize_bid_ask, copeland_galai_bid_ask)

# Main Code
if __name__ == "__main__":
    P0 = 51
    S_values = np.linspace(0, 10, 100)

    prices = generate_price_distribution()
    plot_price_distribution(prices)

    rev_liquidity = [expected_revenue_liquidity(S) for S in S_values]
    rev_informed = [expected_revenue_informed_trades(S) for S in S_values]

    bid, ask, expected_revenue = optimize_bid_ask(P0)
    bid_prices, ask_prices = copeland_galai_bid_ask(P0, S_values)

    plt.figure(figsize=(10,5))
    plt.plot(S_values, rev_liquidity, label='Liquidity Revenue', linestyle='solid')
    plt.plot(S_values, rev_informed, label='Informed Trades', linestyle='solid')
    plt.plot(S_values, bid_prices, label='Expected revenue', linestyle='dashed')
    plt.xlabel('Spread')
    plt.ylabel('Revenue')
    plt.title('The Bid-Ask spread')
    plt.legend()
    plt.show()

    plt.figure(figsize=(10, 5))
    plt.hist(prices, bins=50, density=True, alpha=0.6, color='red', label='Weibull Distribution')
    plt.axvline(P0, color='green', linestyle='--', label=f'Spot Price: {P0}')
    plt.axvline(bid, color='blue', linestyle='--', label=f'Optimal Bid: {bid:.2f}')
    plt.axvline(ask, color='orange', linestyle='--', label=f'Optimal Ask: {ask:.2f}')
    plt.xlabel('Price')
    plt.ylabel('Density')
    plt.title('Price Distribution and Optimal Prices')
    plt.legend()
    plt.show()

    print(f"The expected revenue is {expected_revenue:.4f} with a optimal bid price of {bid:.2f} and an optimal ask price of {ask:.2f}")
