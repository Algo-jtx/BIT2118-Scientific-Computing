import numpy as np

# Estimate pi using the Monte Carlo method.
# Random points are generated inside a square from -1 to 1.
# Points inside the unit circle satisfy x^2 + y^2 <= 1.

rng = np.random.default_rng(42)

def estimate_pi(number_of_points):
    x = rng.uniform(-1, 1, number_of_points)
    y = rng.uniform(-1, 1, number_of_points)

    inside_circle = x**2 + y**2 <= 1
    proportion_inside = np.mean(inside_circle)

    return 4 * proportion_inside

# Initial simulation using 10,000 random points
estimate_small = estimate_pi(10_000)

# Larger simulation using 1,000,000 random points
estimate_large = estimate_pi(1_000_000)

print("Actual value of pi:", np.pi)
print("Estimate using 10,000 points:", estimate_small)
print("Estimate using 1,000,000 points:", estimate_large)
print("Error with 10,000 points:",
      abs(np.pi - estimate_small))
print("Error with 1,000,000 points:",
      abs(np.pi - estimate_large))

# Parameter change: use a different sample size
estimate_changed = estimate_pi(100_000)
print("Estimate using 100,000 points:", estimate_changed)
