import numpy as np

# x = number of Type A servers
# y = number of Type B servers
# Type A uses 4 CPU units and 8 GB memory
# Type B uses 2 CPU units and 12 GB memory
# Total: 20 CPU units and 72 GB memory

A = np.array([
    [4.0, 2.0],
    [8.0, 12.0]
])

b = np.array([20.0, 72.0])

solution = np.linalg.solve(A, b)
residual = b - A @ solution

print(f"Type A servers: {solution[0]:.0f}")
print(f"Type B servers: {solution[1]:.0f}")
print("Verification A @ solution:", A @ solution)
print("Residual:", residual)
print("Residual norm:", np.linalg.norm(residual))

# Parameter change: increase the available CPU total from 20 to 24
b_new = np.array([24.0, 72.0])
solution_new = np.linalg.solve(A, b_new)
print("With 24 CPU units:")
print(f"Type A servers: {solution_new[0]:.2f}")
print(f"Type B servers: {solution_new[1]:.2f}")
