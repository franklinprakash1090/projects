# Import necessary library
import pandas as pd

# Sample data: Employees
data = {
    "Department": ["HR", "HR", "IT", "IT", "Sales", "Sales", "IT", "HR", "Sales", "IT"],
    "Gender": [
        "Male",
        "Female",
        "Male",
        "Female",
        "Male",
        "Female",
        "Female",
        "Male",
        "Female",
        "Male",
    ],
    "Experience_Level": [
        "Junior",
        "Senior",
        "Junior",
        "Senior",
        "Junior",
        "Senior",
        "Junior",
        "Senior",
        "Senior",
        "Junior",
    ],
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a three-variable contingency table using pd.crosstab
contingency_table = pd.crosstab(
    [df["Department"], df["Gender"]],  # Rows: Department + Gender
    df["Experience_Level"],  # Columns: Experience Level
)

# Display the table
print("Three-variable Contingency Table:")
print(contingency_table)
