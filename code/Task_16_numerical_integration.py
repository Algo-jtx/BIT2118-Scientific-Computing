import numpy as np
from scipy.integrate import simpson, trapezoid

# Smart electricity meter readings
# Time in hours, power in kilowatts
time = np.array([0, 1, 2, 3, 4, 5], dtype=float)
power = np.array([1.0, 1.5, 2.0, 2.5, 2.0, 1.0])

# Integrating power over time gives energy in kWh
energy_trapezoid = trapezoid(power, x=time)
energy_simpson = simpson(power, x=time)

print(f"Energy using trapezoidal rule: {energy_trapezoid:.4f} kWh")
print(f"Energy using Simpson's rule: {energy_simpson:.4f} kWh")

# Parameter change: increase the power readings by 20%
higher_power = power * 1.2
print("Energy after 20% increase:",
      simpson(higher_power, x=time), "kWh")
