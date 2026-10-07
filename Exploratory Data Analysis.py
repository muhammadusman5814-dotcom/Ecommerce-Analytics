import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"end to end project\Ecommerce Analytics\clean_File.csv")

print(df.head())
print(df.info())
print(df.shape)
print(df.describe())

# Distribution of sales amount wrt to individual transactions 
plt.figure(figsize=(10,5))
sns.histplot(
    df["salesamount"],
    bins = 30,                                    # size of bars 
    kde = True                                    # kde mean curve on histogram 
)
plt.title("Sale Distribution ")
plt.xlabel("Sales Amount")
plt.ylabel("Number of Transactions")
plt.show()

# profit distribution
plt.figure(figsize=(10,5))
sns.histplot(
    df["profit"],
    bins = 30,                                    # size of bars 
    kde = True                                    # kde mean curve on histogram 
)
plt.title("Profit Distribution ")
plt.xlabel("Profit")
plt.ylabel("Number of Transactions")
plt.show()

# Sales Behaviour wrt Month
Month_Sales = (df[df["orderstatus"] == "Delivered" ].groupby
               ("Year_Month")["salesamount"].sum().reset_index()
               )
print(Month_Sales)

plt.figure(figsize=(10,5))
plt.plot(
    Month_Sales["Year_Month"],
    Month_Sales["salesamount"]
    
)
plt.title("Monthly Revenue Trend")
plt.xlabel("Year With Month")
plt.ylabel("Sales")
plt.xticks(rotation = 45)
plt.tight_layout()
plt.show()

# Monthly Profit Trend
Month_Profit = (df[df["orderstatus"] == "Delivered" ].groupby
               ("Year_Month")["profit"].sum().reset_index()
               )
print(Month_Profit)

plt.figure(figsize=(10,5))
plt.plot(
    Month_Profit["Year_Month"],
    Month_Profit["profit"]
    
)
plt.title("Monthly Profit Trend")
plt.xlabel("Year With Month")
plt.ylabel("profit")
plt.xticks(rotation = 45)
plt.tight_layout()
plt.show()

# Revenue W.R.T Category

Category_Revenue = (df[df["orderstatus"] == "Delivered"] . groupby("category")["salesamount"].sum().reset_index())
# print(Category_Revenue)

plt.figure(figsize = (10,5))
plt.bar(
     Category_Revenue["category"],
     Category_Revenue["salesamount"]
       
)

plt.title("Category Wise Revenue")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.xticks(rotation = 45 )
plt.show()

# Category Profit
Category_Profit = (df[df["orderstatus"] == "Delivered"] . groupby("category")["profit"].sum().reset_index())
print(Category_Revenue)

plt.figure(figsize = (10,5))
plt.bar(
     Category_Profit["category"],
     Category_Profit["profit"]
       
)

plt.title("Category Wise Profit")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.xticks(rotation = 45 )
plt.show()

# Region Wise Trend
Region_Revenue = (df[df["orderstatus"] == "Delivered"] . groupby("region")["salesamount"].sum().reset_index())
print(Region_Revenue)

plt.figure(figsize = (10,5))
plt.bar(
     Region_Revenue["region"],
     Region_Revenue["salesamount"]
       
)

plt.title("Region Wise Revenue")
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.xticks(rotation = 45 )
plt.show()

Region_Profit = (df[df["orderstatus"] == "Delivered"] . groupby("region")["profit"].sum().reset_index())
print(Region_Profit)

plt.figure(figsize = (10,5))
plt.bar(
     Region_Profit["region"],
     Region_Profit["profit"]
       
)

plt.title("Region Wise Profit")
plt.xlabel("Region")
plt.ylabel("Profit")
plt.xticks(rotation = 45 )
plt.show()

# Payment Method Analysis
Payment_Method = (df[df["orderstatus"] == "Delivered"] . groupby("paymentmethod")["orderid"].count().reset_index())
print(Payment_Method)

plt.bar(
    Payment_Method["paymentmethod"],
    Payment_Method["orderid"]


)
plt.title("Payment Method Trend")
plt.xlabel("Payment Method")
plt.ylabel("Number of Orders")
plt.xticks(rotation = 45)
plt.tight_layout()
plt.show()

# Relationship between discount and profit

sns.scatterplot(
    data = df[df["orderstatus"] == "Delivered"],
    x = "discountpct",
    y = "profit"
)
plt.title("Discount Vs Profit")
plt.xlabel("Discount %")
plt.ylabel("Profit %")
plt.show()

# Relationship Between Quantity and Salesamount
sns.scatterplot(
    data = df[df["orderstatus"] == "Delivered"],
    x = "quantity",
    y = "salesamount"
)
plt.title("Quantity Vs Revenue")
plt.xlabel("Quantity")
plt.ylabel("Revenue")
plt.show()

Numerical_Col = [
    "age",
    "quantity",
    "unitprice",
    "discountpct",
    "salesamount",
    "profit"
]

Correlation = df[Numerical_Col].corr()
print(Correlation)

sns.heatmap(
    Correlation,
    annot = True,
    fmt = ".2f"
)
plt.title("Correlation Matrix ")
plt.show()

# Outlier Detection

sns.boxplot(
    x = df["salesamount"]
)
plt.title("Sales Amount Outlier")
plt.xlabel("Sales Amount")
plt.show()

# top 10 products
Top_Rating_Product = (df[df["orderstatus"] == "Delivered"] . groupby("productname")
                  ["salesamount"].sum().sort_values(ascending = False).head(10).reset_index())
print(Top_Rating_Product)

plt.bar(
    Top_Rating_Product["productname"],
    Top_Rating_Product["salesamount"]
    
    
)
plt.title("Top 10 Product with highest Revenue")
plt.xlabel("Revenue")
plt.ylabel("Product ")
plt.show()

# Return Reason Analysis
plt.figure(figsize=(10,5))
sns.histplot(
    df["returnreason"],
    bins = 30,                                    # size of bars 
    kde = True                                    # kde mean curve on histogram 
)
plt.title("Return Reason Analysis ")
plt.xlabel("Return Reason")
plt.ylabel("Number of Order")
plt.show()



