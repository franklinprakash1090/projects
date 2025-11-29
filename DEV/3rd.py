# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Sample student marks data
students = ["A", "B", "C", "D", "E"]
marks = np.array([45, 78, 56, 89, 67])

# --- Before Scaling ---
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.bar(students, marks, color="orange")
plt.title("Student Marks Before Scaling")
plt.xlabel("Students")
plt.ylabel("Marks")

# --- Apply Min-Max Scaling ---
scaler = MinMaxScaler()
marks_scaled = scaler.fit_transform(marks.reshape(-1, 1))

# --- After Scaling ---
plt.subplot(1, 2, 2)
plt.bar(students, marks_scaled.flatten(), color="green")
plt.title("Student Marks After Min-Max Scaling")
plt.xlabel("Students")
plt.ylabel("Scaled Marks (0 to 1)")

plt.tight_layout()
plt.show()
