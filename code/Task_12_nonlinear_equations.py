import numpy as np
from scipy.optimize import root

# Find intersections of:
# Circle: x^2 + y^2 = 4
# Parabola: y = x^2 - 1

def equations(z):
    x, y = z
    return [
        x**2 + y**2 - 4,
        y - (x**2 - 1)
    ]

for guess in ([1.0, 1.0], [-1.0, 1.0]):
    solution = root(equations, guess)

    print("Initial guess:", guess)
    print("Intersection:", solution.x)
    print("Residuals:", equations(solution.x))
    print("Converged:", solution.success)
    print()

# Parameter change: use a larger circle of radius 3
def changed_equations(z):
    x, y = z
    return [
        x**2 + y**2 - 9,
        y - (x**2 - 1)
    ]

changed_solution = root(changed_equations, [1.0, 2.0])
print("Intersection with radius-3 circle:", changed_solution.x)
print("Changed-case residuals:", changed_equations(changed_solution.x))
print("Changed case converged:", changed_solution.success)
