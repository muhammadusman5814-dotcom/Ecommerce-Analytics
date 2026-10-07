import psycopg2
import pandas as pd 
import numpy as np

connector = psycopg2.connect(
    host = 'localhost',
    database = 'Ecommerce_Analytics',
    user = 'postgres',
    password = 'Usman0987',
    port = '5432'
)
print("Connected Sucessfully ")
Cust = pd.read_sql('select * from Customers',connector)
orderdetails = pd.read_sql('select * from OrderDetails' , connector)
orders = pd.read_sql('select * from Orders' , connector)
products = pd.read_sql('select * from Products' , connector)
returns = pd.read_sql('select * from Returns' , connector)

# all Files are fetch

print("Customer Table \n ",Cust.head(10))
print("Order Details Table \n " ,orderdetails.head(10))
print("Order Table  \n ",orders.head(10))
print("Products Table \n ",products.head(10))
print("Returns Table \n  ",returns.head(10))

# finding number of rows and columns 

print()
print("For Customers Table : ",Cust.shape)
print("For Order Details Table : ",orderdetails.shape)
print("For Order Table : ",orders.shape)
print("For Product Table : ",products.shape)
print("For Return Table : ",returns.shape)

# Correcting data types

cust = Cust.dtypes
print(cust)
Cust["signupdate"] = pd.to_datetime(Cust["signupdate"])
od = orderdetails.dtypes
print(od)
Order = orders.dtypes
print(Order)
orders["orderdate"] = pd.to_datetime(orders["orderdate"])
Order = orders.dtypes
print(Order)
Product = products.dtypes
print(Product)
Returns = returns.dtypes
print(Returns)
returns["returndate"] = pd.to_datetime(returns["returndate"])
Returns = returns.dtypes
print(Returns)

#  CHECKING MISSING VALUES 

print(Cust.isnull().sum())
print(orders.isnull().sum())
print(orderdetails.isnull().sum())
print(products.isnull().sum())
print(returns.isnull().sum())

# CHECKING DUPLICATION IN PRIMARY KEY
print("Duplication in primary key ")
print(Cust["customerid"].duplicated().sum())
print(returns["returnid"].duplicated().sum())
print(products["productid"].duplicated().sum())

# CHECKING  DUPLICATIONS 
print("Overall Duplication")
print(Cust.duplicated().sum())
print(orders.duplicated().sum())
print(orderdetails.duplicated().sum())
print(products.duplicated().sum())
print(returns.duplicated().sum())

# verifying numeric data

print("Customers \n ",Cust.describe())
print("Returns \n ",returns.describe())
print("Orders \n ",orders.describe())
print("Order details \n ",orderdetails.describe())
print("Products \n  ",products.describe())

# impossible value check 
print(orderdetails[orderdetails["salesamount"] < 0 ])
print(Cust[(Cust["age"] < 18 )  | (Cust["age"] > 100 )])
print(orderdetails[(orderdetails["discountpct"] < 0 ) | (orderdetails["discountpct"] > 100 )])

# store correct values if we have impossible values
# Cust = Cust[(Cust["age"] > 18 )  | (Cust["age"] < 100 )]

# Create analytical dataset
df = orders.merge(
    Cust,
    on = "customerid",
    how = "left"
)
df = df.merge(
    orderdetails,
    on = "orderid",
    how = "inner"
)
df = df.merge(
    products,
    on = "productid",
    how = "left"
)
df = df.merge(
    returns,
    on = "orderid",
    how = "left"
)    

print(df.shape)
print(df.head)
print(df.columns)

# create useful date column 

df["year"] = df["orderdate"].dt.year
df["month"] = df["orderdate"].dt.month
df["Month_Name"] = df["orderdate"].dt.month_name()
df["Year_Month"] = df["orderdate"].dt.to_period("M").astype(str)

print("Month  \n ",df["month"])
print("Month Name  \n ",df["Month_Name"])
print("Year with numeric month \n ",df["Year_Month"])
print("Year  \n ",df["year"])

# Find profit margin 

df["ProfitMarginPct"] = (df["profit"] / df["salesamount"]) * 100
print("Profit Margin % \n " , df["ProfitMarginPct"])

# Data Quality Check

print(df.info())
print("Missing Values \n " , df.isnull().sum())
print("Duplicate Values \n " , df.duplicated().sum())
print(df.shape)
df.to_csv("clean_File.csv" , index = False)