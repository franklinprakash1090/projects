# Import necessary libraries
import matplotlib.pyplot as plt

# Sample Data
experience = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
salary = [30, 35, 40, 50, 55, 60, 65, 70, 80, 85]
age = [22, 23, 25, 28, 30, 32, 35, 36, 40, 42]

# Create subplots (2 rows, 2 columns)
fig, axs = plt.subplots(2, 2, figsize=(10, 8))  # 2x2 grid

# Plot 1: Experience vs Salary
axs[0, 0].scatter(experience, salary, color="blue")
axs[0, 0].set_title("Experience vs Salary")
axs[0, 0].set_xlabel("Experience (Years)")
axs[0, 0].set_ylabel("Salary (in Thousands)")

# Plot 2: Experience vs Age
axs[0, 1].scatter(experience, age, color="green")
axs[0, 1].set_title("Experience vs Age")
axs[0, 1].set_xlabel("Experience (Years)")
axs[0, 1].set_ylabel("Age")

# Plot 3: Age vs Salary
axs[1, 0].scatter(age, salary, color="red")
axs[1, 0].set_title("Age vs Salary")
axs[1, 0].set_xlabel("Age")
axs[1, 0].set_ylabel("Salary (in Thousands)")

# Hide the empty subplot (bottom-right)
axs[1, 1].axis("off")

# Adjust layout for better spacing
plt.tight_layout()

# Show plots
plt.show()
