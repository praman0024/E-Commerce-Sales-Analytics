import pandas as pd

# Load data
df = pd.read_csv("data/ecommerce_sales.csv", encoding="latin1")

# Convert dates
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

# Check data types
print(df.dtypes)

# Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# Basic statistics
print("\nBasic Statistics:")
print(df[["Sales", "Quantity", "Discount", "Profit"]].describe())

# Sales and Profit by Category
category_analysis = df.groupby("Category")[["Sales", "Profit"]].sum()

print("\nSales and Profit by Category:")
print(category_analysis)