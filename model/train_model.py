import pandas as pd

# Load the CSV file with correct headers
df = pd.read_csv("erp_data.csv")

# Show the data
print(df.head())

# Optional: check column names
print(df.columns)

