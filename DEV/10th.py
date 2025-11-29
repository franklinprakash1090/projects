# Install plotly if not installed
# !pip install plotly

import pandas as pd
import plotly.express as px

# Sample data
data = {
    "Employee": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Experience": [2, 5, 3, 7, 4],
    "Salary": [3000, 5000, 4000, 7000, 4500],
}

df = pd.DataFrame(data)

# --- Interactive Bar Chart ---
fig_bar = px.bar(
    df,
    x="Employee",
    y="Salary",
    color="Experience",
    title="Employee Salary and Experience",
    hover_data=["Experience"],
)
fig_bar.show()

# --- Interactive Scatter Plot ---
fig_scatter = px.scatter(
    df,
    x="Experience",
    y="Salary",
    color="Employee",
    size="Salary",
    title="Experience vs Salary",
    hover_data=["Employee", "Salary"],
)
fig_scatter.show()
