import numpy as np
from scipy.optimize import curve_fit
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Daily electricity consumption measurements
days = np.array([1, 2, 3, 4, 5, 6, 7, 8], dtype=float)
consumption = np.array([12, 14, 15, 18, 19, 22, 23, 26], dtype=float)

# Linear model: consumption = slope * day + intercept
def linear_model(x, slope, intercept):
    return slope * x + intercept

parameters, covariance = curve_fit(linear_model, days, consumption)
slope, intercept = parameters

predicted = linear_model(days, slope, intercept)
residuals = consumption - predicted

print(f"Fitted slope: {slope:.4f}")
print(f"Fitted intercept: {intercept:.4f}")
print("Predicted consumption:", predicted)
print("Residuals:", residuals)

# Estimate consumption on day 9
print("Predicted consumption on day 9:",
      float(linear_model(9, slope, intercept)))

plt.scatter(days, consumption, label="Measured data")
plt.plot(days, predicted, label="Fitted linear model")
plt.xlabel("Day")
plt.ylabel("Electricity consumption (kWh)")
plt.title("Electricity consumption curve fitting")
plt.legend()
plt.grid(True)
plt.savefig("results/Task_14_curve_fit.png", dpi=150)
print("Graph saved to results/Task_14_curve_fit.png")

# Parameter change: increase the last measurement by 3 kWh
changed_consumption = consumption.copy()
changed_consumption[-1] += 3

new_parameters, _ = curve_fit(linear_model, days, changed_consumption)
print("New slope after changing final measurement:",
      new_parameters[0])
