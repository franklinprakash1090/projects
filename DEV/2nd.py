import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# ------------------------------
# Sample Dataset
# ------------------------------
data = {
    "Age": [22, 25, 27, 29, 30, 32, 35, 36, 40, 41, 50, 60],
    "Salary": [2500, 3000, 3200, 3500, 4000, 4200, 4500, 4700, 5000, 5200, 6000, 8000],
}

df = pd.DataFrame(data)

print("Original Data:\n", df)

# ------------------------------
# 1. Summary Table
# ------------------------------
summary = df.describe()  # Creates summary statistics table
print("\nSummary Table:\n", summary)

# ------------------------------
# 2. Visualization of Data Distribution
# ------------------------------

# Histogram
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
sns.histplot(df["Age"], kde=True, bins=8)
plt.title("Age Distribution")

plt.subplot(1, 2, 2)
sns.histplot(df["Salary"], kde=True, bins=8)
plt.title("Salary Distribution")
plt.tight_layout()
plt.show()

# Boxplots
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
sns.boxplot(x=df["Age"])
plt.title("Boxplot of Age")

plt.subplot(1, 2, 2)
sns.boxplot(x=df["Salary"])
plt.title("Boxplot of Salary")
plt.tight_layout()
plt.show()
