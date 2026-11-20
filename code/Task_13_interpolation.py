import numpy as np
from scipy.interpolate import interp1d

# Hourly water-level measurements in a storage tank
hours = np.array([0, 2, 4, 6, 8], dtype=float)
water_level = np.array([1.2, 1.8, 2.5, 3.1, 3.8], dtype=float)

# Create a linear interpolation function
linear_model = interp1d(hours, water_level, kind="linear")

# Estimate water level at times not directly measured
requested_hours = np.array([1, 3, 5, 7], dtype=float)
estimated_levels = linear_model(requested_hours)

print("Measured hours:", hours)
print("Measured water levels:", water_level)
for hour, level in zip(requested_hours, estimated_levels):
    print(f"Estimated level at hour {hour}: {level:.3f} m")

# Parameter change: change the measurement at hour 4
changed_levels = water_level.copy()
changed_levels[2] = 2.9
changed_model = interp1d(hours, changed_levels, kind="linear")

print("Level at hour 3 with original data:", float(linear_model(3)))
print("Level at hour 3 with changed data:", float(changed_model(3)))
