import numpy as np

# Four corners of a square: each row is [x, y]
points = np.array([
    [0.0, 0.0],
    [1.0, 0.0],
    [1.0, 1.0],
    [0.0, 1.0]
])

angle = np.deg2rad(45)

rotation = np.array([
    [np.cos(angle), -np.sin(angle)],
    [np.sin(angle), np.cos(angle)]
])

scale = np.array([
    [2.0, 0.0],
    [0.0, 1.5]
])

# Combined transformation
transformation = rotation @ scale

# Row-vector form requires multiplication by transpose
transformed_points = points @ transformation.T

print("Original points:\n", points)
print("Transformation matrix:\n", transformation)
print("Transformed points:\n", transformed_points)
print("Determinant:", np.linalg.det(transformation))

# Parameter change: rotate by 90 degrees instead of 45
angle_2 = np.deg2rad(90)
rotation_2 = np.array([
    [np.cos(angle_2), -np.sin(angle_2)],
    [np.sin(angle_2), np.cos(angle_2)]
])
transformation_2 = rotation_2 @ scale
print("Points after changing rotation to 90 degrees:\n",
      points @ transformation_2.T)
