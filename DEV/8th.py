# Import libraries
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# --- Part 1: Correlation Heatmap ---

# Sample employee dataset
data = {
    "Experience": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Salary": [30, 35, 40, 50, 55, 60, 65, 70, 80, 85],
    "Age": [22, 23, 25, 28, 30, 32, 35, 36, 40, 42],
    "Training_Hours": [5, 6, 5, 7, 8, 6, 9, 10, 8, 9],
}

df = pd.DataFrame(data)

# Compute correlation matrix
corr = df.corr()

# Plot heatmap
plt.figure(figsize=(6, 5))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap of Employee Data")
plt.show()


# --- Part 2: Map-based Plot ---

# Sample location data (Latitude and Longitude)
locations = {
    "Employee": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Latitude": [12.9716, 13.0827, 12.2958, 11.0168, 10.8505],
    "Longitude": [77.5946, 80.2707, 76.6394, 76.9558, 76.2711],
}

loc_df = pd.DataFrame(locations)

# Simple scatter plot on map
plt.figure(figsize=(8, 6))
plt.scatter(loc_df["Longitude"], loc_df["Latitude"], color="red", s=100)

# Annotate employee names
for i, row in loc_df.iterrows():
    plt.text(row["Longitude"] + 0.1, row["Latitude"] + 0.1, row["Employee"])

plt.title("Employee Locations Map")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.grid(True)
plt.show()
