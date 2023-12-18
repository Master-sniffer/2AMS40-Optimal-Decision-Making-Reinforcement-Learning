#Task 1
import scipy
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

purchase_cost = 400
price = 2000
return_cost_price = 150
mean = 25
variance = 20

n = (mean**2)/(mean - variance)
p = mean/n

possible_order_sizes = range(int(n) + 1)

def expected_net_profit(order_size, n, p, 
    purchase_cost, price, return_cost_price):
    profit = 0
    for demand in possible_order_sizes:
        sold_items = min(order_size, demand)
        unsold_items = max(0, order_size - demand)
        probability = scipy.stats.binom.pmf(demand, n, p)
        revenue = sold_items * price
        cost = order_size * purchase_cost
        return_cost = unsold_items * return_cost_price
        sol = probability * (revenue - cost - return_cost)
        profit += sol
    return profit

profits = [expected_net_profit(order_size, n, p, purchase_cost, 
            price, return_cost_price) for order_size in possible_order_sizes]
optimal_order_size = possible_order_sizes[np.argmax(profits)]

print(f"Optimal order size: {optimal_order_size}")
print(f"Expected profit: {max(profits)}")



plt.plot(possible_order_sizes, profits)