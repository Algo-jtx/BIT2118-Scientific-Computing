import numpy as np

# Adjacency matrix for a small undirected network.
# Node order: A, B, C, D
A = np.array([
    [0., 1., 1., 0.],
    [1., 0., 1., 1.],
    [1., 1., 0., 1.],
    [0., 1., 1., 0.]
])

eigenvalues, eigenvectors = np.linalg.eig(A)

# Dominant eigenvalue/eigenvector
index = np.argmax(np.real(eigenvalues))
dominant_value = np.real(eigenvalues[index])
dominant_vector = np.abs(np.real(eigenvectors[:, index]))
centrality = dominant_vector / dominant_vector.sum()

nodes = ["A", "B", "C", "D"]

print("Dominant eigenvalue:", dominant_value)
print("Eigenvector-based importance:")
for node, score in zip(nodes, centrality):
    print(f"{node}: {score:.4f}")

# Verify Av = lambda*v
v = np.real(eigenvectors[:, index])
print("Verification error:",
      np.linalg.norm(A @ v - dominant_value * v))

# Parameter change: add a connection between A and D
A_changed = A.copy()
A_changed[0, 3] = 1.
A_changed[3, 0] = 1.

values_new, vectors_new = np.linalg.eig(A_changed)
index_new = np.argmax(np.real(values_new))
vector_new = np.abs(np.real(vectors_new[:, index_new]))
centrality_new = vector_new / vector_new.sum()

print("Importance after adding connection A-D:")
for node, score in zip(nodes, centrality_new):
    print(f"{node}: {score:.4f}")
