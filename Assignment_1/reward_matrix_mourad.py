#Making reward matrix

import numpy as np
import math
import statistics,scipy
#from statistics import sum

# Define constants
c = 400  # Cost of purchasing an item
p = 2000  # Price of selling an item
r = 150  # Holding cost per unsold item

def get_reward_matrix():
    array = np.zeros([41*11,11])
    for i in range(41):
        for j in range(11):
            for k in range(11):
                reward_per_demand = []
                for l in range(125):
                    prob_demand = scipy.stats.binom.pmf(l,125,0.2)
                    sales = min(i, l)
                    ordered_items = k
                    unsold_items = max(0, i - l)
                    revenue = sales * p
                    cost = ordered_items * c
                    holding_cost_total = unsold_items * r
                    total_reward = prob_demand * (revenue - cost - holding_cost_total)
                    reward_per_demand.append(total_reward)
                
                array[i*11+j][k]=sum(reward_per_demand)
    return array