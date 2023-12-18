#Task 5
#Value iteration

import numpy as np
from .reward_matrix_mourad import get_reward_matrix
from scipy.stats import binom, norm


# Initialize Markov Decision Process model
maxCapacity = 40
# State space: inventory levels and incoming stock
states = [(a, b) for a in range(41) for b in range(11)]  
actions = list(range(11))  # Action space: number of items to order
demands = range(0,41) #demand space
rewards = get_reward_matrix()  # Direct rewards per state
gamma = 0.9  # discount factor

max_iter = 5
delta = 1e-400 
V = np.zeros([41*11,11])
pi = np.zeros([41*11])

def transition_probability(s, action, s_prime):
    a, b = s
    a_prime, b_prime = s_prime

    demand = a + b - a_prime

    if demand < 0:
        return 0
    
    return binom.pmf(demand, 125, 0.2)

# Start value iteration
for i in range(max_iter):
      # Initialize max difference
    V_new = np.zeros([41*11,11]) # Initialize values
    for s in states:
        max_diff = 0
        for act in actions:
            val = rewards[s[0] * 11 + s[1]][act]  # Get direct reward
            for a in actions:
                max_val = 0                
                for demand in demands:
                    new_inventory = min(s[0] - demand + s[1], maxCapacity)
                    if new_inventory < 0:
                        break
                    s_prime =  (s[0] + s[1] - demand, a)
                    prob = transition_probability(s, a, s_prime)
                    val += prob * (gamma * V[s_prime[0]][s_prime[1]])
    
                # Store value best action so far
                max_val = max(max_val, val)
    
            # Update best policy
            if V[s[0] * 11 + s[1]][act] < val:
                # Store action with highest value
                pi[s[0] * 11 + s[1]] = actions[a]  
                
            # Update value with highest value
            V_new[s[0] * 11 + s[1]][act] = max_val 
            max_diff = max(max_diff, 
                        abs(V[s[0] * 11 + s[1]][act] -
                        V_new[s[0] * 11 + s[1]][act]))

    # Update value functions
    V = V_new

    # If diff smaller than threshold delta for all states, algorithm terminates
    if max_diff < delta:
        break