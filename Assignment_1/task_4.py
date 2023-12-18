#Task 4
import numpy as np
from scipy.stats import binom, norm


# Parameters
n = 125  # Number of trials in the binomial distribution for demand
p = 0.2  # Probability of success (demand) in each trial
selling_price = 2000  # Price per carton
cost_per_order = 400  # Cost per carton ordered
holding_cost = 150  # Holding cost per carton
order_quantity = 4  # Number of items ordered per day
initial_inventory = 40  # Initial inventory
gamma = 0.9  # Discount factor
lead_time = 2  # Lead time in days


# Function to simulate one episode
def simulate_episode():
    inventory = initial_inventory
    total_discounted_cost = 0
    discount_factor = 1
    orders_in_transit = [0] * lead_time  # Orders in transit for each day

    for _ in range(100):  # Simulating for 100 days
        # Generate demand
        demand = binom.rvs(n, p)

        # Calculate sales and update stock
        # Receive order from two days ago
        inventory += orders_in_transit.pop(0)
        inventory = min(inventory, 40)  # Limit stock based on storage capacity
        sales = min(inventory, demand)
        inventory -= sales

        # Calculate costs
        revenue = sales * selling_price
        order_cost = order_quantity * cost_per_order
        holding_cost_total = max(0, inventory) * holding_cost

        # Update total cost with discounting
        daily_cost = order_cost + holding_cost_total - revenue
        total_discounted_cost += discount_factor * daily_cost

        # Place an order and discount factor for next day
        orders_in_transit.append(order_quantity)
        discount_factor *= gamma

    return total_discounted_cost

# Run multiple episodes to compute mean and standard deviation
num_episodes = 10000  # Number of episodes
costs = [simulate_episode() for _ in range(num_episodes)]
mean_cost = np.mean(costs)
std_dev_cost = np.std(costs)

# Compute 99% confidence interval
z_score = norm.ppf(0.995)  # 99% confidence level
margin_error = z_score * std_dev_cost / np.sqrt(num_episodes)
confidence_interval = (mean_cost - margin_error, mean_cost + margin_error)

print("Mean Total Expected Discounted Cost:", mean_cost)
print("99% Confidence Interval:", confidence_interval)