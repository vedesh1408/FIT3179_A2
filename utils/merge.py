import pandas as pd

# Load the first CSV file
df1 = pd.read_csv("C:/Users/vedes/Documents/GitHub/FIT3179_A2/data/Final.csv")

# Load the second CSV file
df2 = pd.read_csv("C:/Users/vedes/Documents/GitHub/FIT3179_A2/data/combined.csv")

# Check for and remove duplicates in both dataframes
df1 = df1.drop_duplicates(subset=['Country', 'Year'])
df2 = df2.drop_duplicates(subset=['Country', 'Year'])

# Merge the dataframes based on 'Country' and 'Year' columns
merged_df = pd.merge(df2, df1[['Country', 'Year', 'Code']], on=['Country', 'Year'], how='left')

# Convert "Score" to float and "Year" to integer
merged_df['Score'] = pd.to_numeric(merged_df['Score'], errors='coerce').astype(float)
merged_df['Year'] = pd.to_numeric(merged_df['Year'], downcast='integer', errors='coerce').astype(int)

# Fill missing 'Code' values with an invalid code (e.g., -1)
merged_df['Code'].fillna(-1, inplace=True)

# Add an "ID" column starting from 0
merged_df.insert(0, 'ID', range(len(merged_df)))

# Save the merged dataframe to a new CSV file
merged_df.to_csv("data/merged_data.csv", index=False)