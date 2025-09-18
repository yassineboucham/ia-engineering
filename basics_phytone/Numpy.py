# Introduction to NumPy Arrays
import numpy as np
# Creating a NumPy array from a list
array_from_list = np.array([1, 2, 3, 4, 5])
print("Array from list:", array_from_list)
"""
أنشئ متجهين u=[2,3] و v=[-1,4] واحسب:

الطول ديال كل واحد. المسافة بيناتهم.
"""
u = np.array([2, 3])
v = np.array([-1, 4])
length = np.linalg.norm(u)
distance = np.linalg.norm(u - v)
cos_theta = np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))
print("Length of u:", length)
print("Distance between u and v:", distance)
print("Cosine of angle between u and v:", cos_theta)

# --- Exercise 2: Least Squares Linear Regression ---
# 1. Represent x (hours studied) and y (scores) as NumPy arrays
x = np.array([1, 2, 3, 4, 5])  # Example: hours studied
y = np.array([2, 4, 5, 4, 5])  # Example: scores

# 2. Add a column of ones to x for the intercept (bias)
X = np.column_stack((np.ones(x.shape[0]), x))

# 3. Apply the least squares formula: θ = (X.T @ X)^(-1) @ X.T @ y
theta = np.linalg.inv(X.T @ X) @ X.T @ y
b, w = theta  # Intercept and slope
print(f"Intercept (b): {b:.2f}")
print(f"Slope (w): {w:.2f}")

# 4. Predict the score for a student who studied 6 hours
hours_studied = 6
predicted_score = b + w * hours_studied
print(f"Predicted score for 6 hours studied: {predicted_score:.2f}")