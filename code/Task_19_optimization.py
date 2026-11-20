import numpy as np
from scipy.optimize import minimize

# Electricity production planning
# x = units of electricity from Source A
# y = units of electricity from Source B
#
# Source A costs 5 units per kWh.
# Source B costs 8 units per kWh.
# We need at least 100 kWh.
# Source A can supply at most 80 kWh.
# Source B can supply at most 70 kWh.

def total_cost(energy):
    x, y = energy
    return 5 * x + 8 * y

constraints = [
    {
        "type": "ineq",
        "fun": lambda energy: energy[0] + energy[1] - 100
    }
]

bounds = [(0, 80), (0, 70)]
initial_guess = [50, 50]

result = minimize(
    total_cost,
    initial_guess,
    method="SLSQP",
    bounds=bounds,
    constraints=constraints
)

print("Optimization successful:", result.success)
print("Energy from Source A:", round(result.x[0], 4), "kWh")
print("Energy from Source B:", round(result.x[1], 4), "kWh")
print("Total energy supplied:", round(sum(result.x), 4), "kWh")
print("Minimum total cost:", round(result.fun, 4))

# Parameter change: increase demand from 100 to 120 kWh
constraints_changed = [
    {
        "type": "ineq",
        "fun": lambda energy: energy[0] + energy[1] - 120
    }
]

changed_result = minimize(
    total_cost,
    initial_guess,
    method="SLSQP",
    bounds=bounds,
    constraints=constraints_changed
)

print("\nAfter increasing demand to 120 kWh:")
print("Optimization successful:", changed_result.success)
print("Energy from Source A:", round(changed_result.x[0], 4), "kWh")
print("Energy from Source B:", round(changed_result.x[1], 4), "kWh")
print("Minimum total cost:", round(changed_result.fun, 4))
