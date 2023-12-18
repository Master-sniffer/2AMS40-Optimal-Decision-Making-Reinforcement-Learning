# Task 2
gamma = 0.9  # Discounting factor
initial_inventory = 40  # Starting inventory
daily_order = 4  # Daily order quantity
max_order_size = 10  # Maximum order size
storage_capacity = 40  # Storage capacity
lead_time = 2  # Lead time in days
purchase_cost = 400  # Cost per item
selling_price = 2000  # Selling price per item
holding_cost = 150  # Holding cost per unsold item
num_days = 30  # Number of days to simulate

# Initialize variables
inventory = initial_inventory
orders_in_transit = [0] * lead_time  # Orders in transit for each day

# Data collection
data = []

# Sample demand from given binomial distribution
def binomial_demand():
    return np.random.binomial(n, p)

# Re-run the simulation loop
data = []
inventory = initial_inventory
orders_in_transit = [0] * lead_time  # Reset orders in transit

for day in range(1, num_days + 1):
    # Receive order from two days ago
    inventory += orders_in_transit.pop(0)
    # Limit inventory to storage capacity
    inventory = min(inventory, storage_capacity)

    # Generate demand and calculate sales
    demand = binomial_demand()
    sales = min(demand, inventory)
    inventory -= sales

    # Calculate revenue and costs
    revenue = sales * selling_price
    cost = daily_order * purchase_cost
    holding_cost_total = inventory * holding_cost

    # Update orders in transit
    orders_in_transit.append(daily_order)

    # Record data
    data.append({
        'Day': day,
        'Inventory': inventory,
        'Demand': demand,
        'Sales': sales,
        'Revenue': revenue,
        'Cost': cost,
        'Holding Cost': holding_cost_total,
        'Net Profit': revenue - cost - holding_cost_total
    })

# Convert data to DataFrame
df = pd.DataFrame(data)

plt.plot(df['Day'], df['Inventory'])
df.head()