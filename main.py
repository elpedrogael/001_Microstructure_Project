from hmac import digest_size

import numpy as np
import matplotlib.pyplot as plt

from optimization import generate_price_distribution, plot_price_distribution,expected_revenue_liquidity, expected_revenue_informed_trades, copeland_galai_bid_ask

prices = generate_price_distribution()
plot_price_distribution(prices)

S_values = np.linspace(0, 0.5, 100)

rev_liquidity = [expected_revenue_liquidity(S) for S in S_values]
rev_informed = [expected_revenue_informed_trades(S) for S in S_values]

P0 = 51
bid_prices, ask_prices = copeland_galai_bid_ask(P0, S_values)

plt.figure(figsize=(10,5))
plt.plot(S_values, rev_liquidity, label= 'Liquidity Revenue', linestyle= 'solid')
plt.plot(S_values,rev_informed, label= 'Informed Trades', linestyle = 'solid')
plt. xlabel('S')
plt.ylabel('Expected Revenue')
plt.title('Expected Revenue - S')
plt.show()

plt.figure(figsize=(10,5))
plt.plot(S_values,bid_prices,label='Bid Price')
plt.plot(S_values, ask_prices, label = 'Ask Price')
plt.xlabel('S')
plt.ylabel('Price')
plt.title('Bid-Ask prices - S(Copeland & Galai)')
plt.show()