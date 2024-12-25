from scipy.optimize import linprog

def optimize_transportation(costs, demand, supply):
    """
    Solve a transportation problem using linear programming.
    Args:
        costs (list of list): Cost matrix.
        demand (list): Demand values for each destination.
        supply (list): Supply values for each source.
    Returns:
        dict: Optimization results.
    """
    num_sources = len(supply)
    num_destinations = len(demand)
    
    # Flatten cost matrix and set up bounds
    cost_vector = [cost for row in costs for cost in row]
    bounds = [(0, None)] * (num_sources * num_destinations)
    
    # Set up constraints
    A_eq = []
    for i in range(num_sources):
        row = [1 if j // num_destinations == i else 0 for j in range(num_sources * num_destinations)]
        A_eq.append(row)
    for j in range(num_destinations):
        col = [1 if i % num_destinations == j else 0 for i in range(num_sources * num_destinations)]
        A_eq.append(col)
    
    b_eq = supply + demand

    # Solve the problem
    result = linprog(c=cost_vector, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')
    return {
        "status": result.status,
        "message": result.message,
        "solution": result.x if result.success else None
    }
