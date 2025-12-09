import pandas as pd
import numpy as np

df = pd.read_csv('financial_data.csv')

# Handle Missing Values
df['closing_price'] = df['closing_price'].interpolate(method='linear')
df['volume'] = df['volume'].interpolate(method='linear')
df['closing_price'] = df['closing_price'].bfill()

# Create Lag Features
df['1_day_return'] = df['closing_price'].pct_change(periods=1)
df['7_day_return'] = df['closing_price'].pct_change(periods=7)

# Normalize Volume
df['volume'] = np.log1p(df['volume'])

# Detect Outliers (and remove if desired, but for this task, just detection was specified)
Q1 = df['closing_price'].quantile(0.25)
Q3 = df['closing_price'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers = df[(df['closing_price'] < lower_bound) | (df['closing_price'] > upper_bound)]

print("Final Preprocessed Data Head:")
display(df.head())

print("\nFinal Preprocessed Data Info:")
df.info()

print("\nOutliers in 'closing_price' (if any):")
print(outliers)