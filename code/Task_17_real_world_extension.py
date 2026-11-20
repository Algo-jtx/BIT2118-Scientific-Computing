import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Real-world case: Cooling of freshly boiled drinking water

initial_temperature = 95.0
room_temperature = 22.0
cooling_constant = 0.12
time_step = 0.5
total_time = 15.0

time = np.arange(0, total_time + time_step, time_step)
temperature = np.zeros(len(time))
temperature[0] = initial_temperature

# Euler's numerical method
for i in range(len(time) - 1):
    rate = -cooling_constant * (
        temperature[i] - room_temperature
    )
    temperature[i + 1] = temperature[i] + time_step * rate

# Estimate when water reaches 60 degrees
target_temperature = 60.0
reached = np.where(temperature <= target_temperature)[0]

if len(reached) > 0:
    target_time = time[reached[0]]
else:
    target_time = None

print("HOT WATER COOLING CASE STUDY")
print("--------------------------------")
print("Initial temperature:", initial_temperature, "C")
print("Room temperature:", room_temperature, "C")
print("Cooling constant:", cooling_constant)
print("Temperature after 5 minutes:",
      round(temperature[int(5 / time_step)], 2), "C")
print("Temperature after 10 minutes:",
      round(temperature[int(10 / time_step)], 2), "C")
print("Temperature after 15 minutes:",
      round(temperature[-1], 2), "C")

if target_time is not None:
    print("Estimated time to reach 60 C:",
          target_time, "minutes")
else:
    print("Water did not reach 60 C during the simulation.")

# Generate graph
plt.plot(time, temperature, label="Water temperature")
plt.axhline(target_temperature, linestyle="--", label="60 C target")
plt.axhline(room_temperature, linestyle=":", label="Room temperature")

plt.xlabel("Time (minutes)")
plt.ylabel("Temperature (C)")
plt.title("Cooling of Hot Drinking Water")
plt.legend()
plt.grid(True)

plt.savefig(
    "results/Task_17_water_cooling_extension.png",
    dpi=150
)

print("Graph saved to results/Task_17_water_cooling_extension.png")
