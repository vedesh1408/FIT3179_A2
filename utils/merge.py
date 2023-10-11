import pandas as pd

# Load the first CSV file
df1 = pd.read_csv("C:/Users/vedes/Documents/GitHub/FIT3179_A2/data/Final.csv")

# Load the second CSV file
df2 = pd.read_csv("C:/Users/vedes/Documents/GitHub/FIT3179_A2/data/combined.csv")

df1 = df1.drop_duplicates(subset=['Country', 'Year'])
df2 = df2.drop_duplicates(subset=['Country', 'Year'])

# Merge the dataframes based on 'Country' and 'Year' columns
merged_df = pd.merge(df2, df1[['Country', 'Year', 'Code']], on=['Country', 'Year'], how='left')

# Save the merged dataframe to a new CSV file
merged_df.to_csv("merged_data.csv", index=False)