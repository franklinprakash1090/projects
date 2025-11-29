# Import necessary libraries
import numpy as np
import pandas as pd

# Sample time series data with missing/inconsistent timestamps
data = {
    "Timestamp": [
        "2025-10-01 09:00",
        "2025-10-01 10:00",
        "2025-10-01 12:00",
        "2025-10-01 13:00",
        "2025-10-01 15:00",
    ],
    "Value": [100, 110, 130, 120, 150],
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert Timestamp column to datetime
df["Timestamp"] = pd.to_datetime(df["Timestamp"])

# Set Timestamp as index
df.set_index("Timestamp", inplace=True)

# Resample data to hourly frequency to fill missing timestamps
df = df.resample("H").asfreq()

# Fill missing values (interpolation)
df["Value"] = df["Value"].interpolate(method="linear")

# Display cleaned time series
print("Cleaned Time Series Data:")
print(df)
