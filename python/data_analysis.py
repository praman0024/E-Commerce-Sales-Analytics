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

# Sales and Profit by Sub-Category
subcategory_analysis = df.groupby("Sub-Category")[["Sales", "Profit"]].sum()

print("\nSales and Profit by Sub-Category:")
print(subcategory_analysis.sort_values("Sales", ascending=False))

# Sales and Profit by Year
df["Year"] = df["Order Date"].dt.year

yearly_analysis = df.groupby("Year")[["Sales", "Profit"]].sum()

print("\nSales and Profit by Year:")
print(yearly_analysis)

import matplotlib.pyplot as plt

#sales nd profit by category
category_analysis.plot(kind="bar")

plt.title("Sales and Profit by Category")
plt.xlabel("Category")
plt.ylabel("Amount")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

#sales by year
yearly_analysis["Sales"].plot(kind="bar")

plt.title("Sales by Year")
plt.xlabel("Year")
plt.ylabel("Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

#profit by sub-category
subcategory_analysis["Profit"].short_values().plot(kind="bar")

plt.title("Profit by Sub-Category")
plt.xlabel("Sub-Category")
plt.ylabel("profit")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()