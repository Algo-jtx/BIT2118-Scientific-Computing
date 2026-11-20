import numpy as np

# GPS position measurements along a straight road
# Time is in seconds; position is in metres
time = np.array([0, 1, 2, 3, 4, 5], dtype=float)
position = np.array([0, 4, 10, 18, 28, 40], dtype=float)

# Numerical differentiation estimates velocity from position
velocity = np.gradient(position, time)

print("Time (s):", time)
print("Position (m):", position)
print("Estimated velocity (m/s):", velocity)

# Estimate acceleration by differentiating velocity
acceleration = np.gradient(velocity, time)
print("Estimated acceleration (m/s^2):", acceleration)

# Parameter change: use a slightly different position measurement
changed_position = position.copy()
changed_position[3] = 20
changed_velocity = np.gradient(changed_position, time)

print("Velocity after changing the position at 3 seconds:",
      changed_velocity)
