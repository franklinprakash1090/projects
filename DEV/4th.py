# Import necessary libraries
import matplotlib.pyplot as plt

# Sample Employee Data
# Let's assume we have employee experience (years) and salary (in thousands)
employee_experience = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
employee_salary = [30, 35, 40, 50, 55, 60, 65, 70, 80, 85]

# Create a scatter plot
plt.scatter(employee_experience, employee_salary, color="green")

# Add title and labels
plt.title("Scatter Plot: Employee Experience vs Salary")
plt.xlabel("Experience (Years)")
plt.ylabel("Salary (in Thousands)")

# Show the plot
plt.show()
