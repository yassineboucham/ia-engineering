import matplotlib.pyplot as plt
import numpy as np

# Define the vertices of the triangle
A = np.array([0, 0, 0])
B = np.array([4, 0, 0])
C = np.array([0, 3, 0])

# Create 3D plot
fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot(111, projection='3d')

# Plot points
ax.scatter(*A, color='k', s=50, label="A(0,0,0)")
ax.scatter(*B, color='r', s=50, label="B(4,0,0)")
ax.scatter(*C, color='b', s=50, label="C(0,3,0)")

# Plot triangle edges
triangle = np.array([A, B, C, A])
ax.plot(triangle[:,0], triangle[:,1], triangle[:,2], 'g-')

# Vectors AB and AC
AB = B - A
AC = C - A
ax.quiver(*A, *AB, color='r', arrow_length_ratio=0.1, label="AB")
ax.quiver(*A, *AC, color='b', arrow_length_ratio=0.1, label="AC")

# Cross product vector (normal to triangle plane)
cross = np.cross(AB, AC)
ax.quiver(*A, *cross, color='m', arrow_length_ratio=0.1, label="AB x AC (normal)")

# Formatting
ax.set_xlim(0, 5)
ax.set_ylim(0, 4)
ax.set_zlim(0, 5)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Triangle ABC and Cross Product")
ax.legend()
plt.show()
