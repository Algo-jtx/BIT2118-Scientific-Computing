import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Cooling model: temperature approaches room temperature
# dT/dt = -k(T - room_temperature)

room_temperature = 25.0
initial_temperature = 90.0
k = 0.2
step = 0.5
total_time = 10.0

time = np.arange(0, total_time + step, step)
temperature = np.zeros(len(time))
temperature[0] = initial_temperature

# Euler's method
for i in range(len(time) - 1):
    rate = -k * (temperature[i] - room_temperature)
    temperature[i + 1] = temperature[i] + step * rate

print("Initial temperature:", temperature[0])
print("Temperature after 10 minutes:", temperature[-1])
print("Temperature after 5 minutes:", temperature[int(5 / step)])

# Parameter change: use a larger cooling constant
k_new = 0.3
temperature_new = np.zeros(len(time))
temperature_new[0] = initial_temperature

for i in range(len(time) - 1):
    rate = -k_new * (temperature_new[i] - room_temperature)
    temperature_new[i + 1] = temperature_new[i] + step * rate

print("Temperature after 10 minutes with faster cooling:",
      temperature_new[-1])

plt.plot(time, temperature, label="k = 0.2")
plt.plot(time, temperature_new, label="k = 0.3")
plt.xlabel("Time (minutes)")
plt.ylabel("Temperature (C)")
plt.title("Euler method: cooling over time")
plt.legend()
plt.grid(True)
plt.savefig("results/Task_17_euler_cooling.png", dpi=150)
print("Graph saved to results/Task_17_euler_cooling.png")
