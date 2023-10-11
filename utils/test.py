import pandas as pd

# Replace 'your_data.csv' with the actual file path
file_path = 'C:/Users/vedes/Documents/GitHub/FIT3179_A2/data/Final.csv'

# Read the CSV file
df = pd.read_csv(file_path)

# Check the first few rows to verify the data
print(df.head())
