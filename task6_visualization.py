import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("retail_sales.csv")   
print(df.head())
print(df.info())
print(df.describe())
top10 = df.groupby("Category")["Sales"].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10,5))
top10.plot(kind='bar')
plt.title("Top 10 Categories by Sales")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.grid()
plt.show()
# Convert Date safely
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# Remove invalid dates if any
df = df.dropna(subset=["Date"])

# Monthly sales
monthly_sales = df.groupby(df["Date"].dt.month)["Sales"].sum()

plt.figure(figsize=(10,5))
plt.plot(monthly_sales, marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid()
plt.show()

plt.figure(figsize=(8,5))
plt.hist(df["Profit"], bins=20)
plt.title("Profit Distribution")
plt.xlabel("Profit")
plt.ylabel("Frequency")
plt.grid()
plt.show()
plt.figure(figsize=(8,5))
plt.scatter(df["Sales"], df["Profit"])
plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.grid()
plt.show()



