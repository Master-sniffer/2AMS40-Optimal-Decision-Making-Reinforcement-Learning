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
    array = np.zeros([41,11])
    for i in range(len(array)):
        for j in range(len(array[i])):
                temp_array=[]
                for k in range(125):
                    # Calculate the future inventory after placing the replenishment order
                    future_inventory = max(i -k,0)+j
            
                    # Calculate the number of sold items
                    sold_items = min(i, k)
            
                    # Calculate the purchase cost
                    purchase_cost = c * (sold_items)
            
                    # Calculate the revenue from sales
                    revenue = p * sold_items
            
                    # Calculate the holding cost for unsold items
                    holding_cost = r * (future_inventory - sold_items)
            
                    # Calculate the total reward
                    total_reward = purchase_cost + revenue - holding_cost
            
                    # Update the reward matrix
                    
                    
                    temp_array.append(scipy.stats.binom.pmf(k,125,0.2) * total_reward)
    
                    
                array[i][j]=sum(temp_array)
    return array