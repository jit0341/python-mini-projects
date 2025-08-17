import pandas as pd
from tabulate import tabulate

# Load the CSV file
df = pd.read_csv("01_expense_tracker/data/expenses.csv")

# Show as a pretty table
print(tabulate(df, headers="keys", tablefmt="fancy_grid", showindex=False))
