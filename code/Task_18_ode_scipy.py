import numpy as np
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# RC circuit model
# Voltage across capacitor:
# dV/dt = (Vin - V) / (R*C)

input_voltage = 12.0
resistance = 1000.0
capacitance = 0.001
initial_voltage = 0.0

def circuit_model(t, voltage):
    return [(input_voltage - voltage[0]) /
            (resistance * capacitance)]

time_span = (0, 5)
time_points = np.linspace(0, 5, 100)

solution = solve_ivp(
    circuit_model,
    time_span,
    [initial_voltage],
    t_eval=time_points
)

print("Solver successful:", solution.success)
print("Initial capacitor voltage:", solution.y[0][0])
print("Final capacitor voltage:", solution.y[0][-1])
print("Voltage after 1 second:",
      np.interp(1, solution.t, solution.y[0]))

# Parameter change: increase capacitance
capacitance = 0.002

changed_solution = solve_ivp(
    circuit_model,
    time_span,
    [initial_voltage],
    t_eval=time_points
)

print("Final voltage with doubled capacitance:",
      changed_solution.y[0][-1])

plt.plot(solution.t, solution.y[0], label="Original capacitance")
plt.plot(changed_solution.t, changed_solution.y[0],
         label="Doubled capacitance")
plt.xlabel("Time (seconds)")
plt.ylabel("Capacitor voltage (V)")
plt.title("RC circuit charging")
plt.legend()
plt.grid(True)
plt.savefig("results/Task_18_rc_circuit.png", dpi=150)
print("Graph saved to results/Task_18_rc_circuit.png")
