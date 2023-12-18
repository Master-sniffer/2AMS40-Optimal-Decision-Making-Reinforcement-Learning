#Task 6
import numpy as np
from .making_reward_function import get_reward_matrix

# Supply chain homework  - policy iteration


# Set policy iteration parameters
max_policy_iter = 100  # Maximum number of policy iterations
max_value_iter = 100  # Maximum number of value iterations

# Initialize Markov Decision Process model
maxCapacity = 40
actions = range(0,10+1) #action space
states = range(0,maxCapacity+1) #state space
demands = range(0,41) #demand space
rewards = get_reward_matrix()  # Direct rewards per state
gamma = 0.9  # discount factor

max_iter = 5
delta = 1e-400 
V = np.zeros([41,11])
pi = np.zeros([41,11])



for i in range(max_policy_iter):
    # Initial assumption: policy is stable
    optimal_policy_found = True

    # Policy evaluation
    # Compute value for each state under current policy
    for j in range(max_value_iter):
        max_diff = 0  # Initialize max difference

        for s in states:
            for act in actions:
                
                for a in actions:
                    max_val = 0
                    # Compute state value
                    val = rewards[s][act]  # Get direct reward
                    for demand in demands:
                        metDemand = min(s, demand); #compute met demand
                        unmetDemand = max((demand-s), 0); #compute unmet demand
        
                        s_next = min(s-metDemand+a, maxCapacity) #update state
        
                        val += (1/5) * (gamma * V[s_next][act])  # Add discounted downstream values
                        
                    max_diff = max(max_diff, abs(val - V[s][act]))
                    V[s][act] = val 
            if max_diff < delta:
                break

    # Policy iteration
    # With updated state values, improve policy if needed
    for s in states:
        for act in actions:
            val_max = V[s][act]
            for a in actions:
                val = rewards[s][act]  # Get direct reward
                for demand in demands:
                    metDemand = min(s, demand); #compute met demand
                    unmetDemand = max((demand-s), 0); #compute unmet demand
    
                    s_next = min(s-metDemand+a, maxCapacity) #update state
    
                    val += (1/5) * (gamma * V[s_next][act])  # Add discounted downstream values
    
                # Update policy if (i) action improves value and 
                # (ii) action different from current policy
                if val > val_max and pi[s][act] != a:
                    pi[s][act] = a
                    val_max = val
                    optimal_policy_found = False

        # If policy did not change, algorithm terminates
        if optimal_policy_found:
            break