import numpy as np
import pandas as pd

# Sample dataset with missing values and outliers
data = {
    "Age": [25, 27, 29, np.nan, 35, 120, 28, 30, np.nan, 32],
    "Salary": [3000, 3200, 3500, 3700, np.nan, 100000, 3400, 3600, 3550, np.nan],
}

# Create DataFrame
df = pd.DataFrame(data)
print("Original Data:\n", df)

# ------------------------------
# 1. Identifying Missing Values
# ------------------------------
print("\nMissing Values Count:\n", df.isnull().sum())


# ------------------------------
# 2. Detecting Outliers (IQR Method)
# ------------------------------
def detect_outliers_iqr(column):
    Q1 = column.quantile(0.25)  # 25th percentile
    Q3 = column.quantile(0.75)  # 75th percentile
    IQR = Q3 - Q1  # Interquartile Range
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return column[(column < lower_bound) | (column > upper_bound)]

    print(f"\nOutliers in '{col}':\n", outliers.values)
