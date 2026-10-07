create table Customers(
	CustomerID VARCHAR(10) PRIMARY KEY,
	CustomerName VARCHAR(100),
	Gender VARCHAR(20),
	Age INT,
	City Varchar(50),
	SignupDate DATE,
-	Region Varchar(30)
);

create table Products(
	ProductID VARCHAR(10) PRIMARY KEY,
	ProductName VARCHAR(100),
-	Category VARCHAR(50),
	CostPrice DECIMAL(12,2),
	SellingPrice DECIMAL(12,2)
);

create table Orders(
	OrderID Varchar(10) PRIMARY KEY,
	OrderDate DATE,
	CustomerID VARCHAR(10),
	PaymentMethod VARCHAR(30),
	OrderStatus VARCHAR(20),

	FOREIGN KEY (CustomerID)
	REFERENCES Customers(CustomerID)
);

create table OrderDetails(
	OrderDetailID Varchar(12) PRIMARY KEY,
	OrderID VARCHAR(10),
	ProductID VARCHAR(10),
	Quantity INT,
	UnitPrice DECIMAL(12,2),
	DiscountPct DECIMAL(5,2),
-	SalesAmount DECIMAL(14,2),
	Profit DECIMAL(14,2),

	
	FOREIGN KEY (OrderID)
		REFERENCES Orders(OrderID),

	FOREIGN KEY (ProductID)
		REFERENCES Products(ProductID)
);

create table Returns(
	ReturnID VARCHAR(10) PRIMARY KEY,
	OrderID VARCHAR(10),
	ReturnDate DATE,
	ReturnReason VARCHAR(50),

	FOREIGN KEY (OrderID)
		REFERENCES Orders(OrderID)
);

--------------------copying data from excel------------------

copy customers(customerid, customername, gender, age, city, signupdate, region)
from 'E:\Data Analytics Projects\Ecommerce Analytics\Data\Customers.csv'
WITH (FORMAT csv, HEADER true, ENCODING 'utf8');

copy products(ProductID, ProductName, Category, CostPrice, SellingPrice)
from 'E:\Data Analytics Projects\Ecommerce Analytics\Data\Products.csv'
WITH (FORMAT csv, HEADER true, ENCODING 'utf8');

copy orders(Orderid, OrderDate, CustomerID, PaymentMethod, OrderStatus)
from 'E:\Data Analytics Projects\Ecommerce Analytics\Data\Orders.csv'
WITH (FORMAT csv, HEADER true, ENCODING 'utf8');
 
copy Orderdetails(OrderDetailID, OrderID, ProductID, Quantity, UnitPrice, DiscountPct, SalesAmount, Profit)
from 'E:\Data Analytics Projects\Ecommerce Analytics\Data\OrderDetails.csv'
WITH (FORMAT csv, HEADER true, ENCODING 'utf8');

copy Returns(ReturnID, OrderID, ReturnDate, ReturnReason)
from 'E:\Data Analytics Projects\Ecommerce Analytics\Data\Returns.csv'
WITH (FORMAT csv, HEADER true, ENCODING 'utf8');

----------------------- Data validation-----------------------
--------------Row Count-----------------
select 'Customers' ,Count(*) AS Total_Customers
from customers

union all 

select 'Orders' , Count(*) AS Total_Orders
from orders

Union All

select 'Products' ,  Count(*) AS Total_Products
from products

union all

select 'Returns' , Count(*) AS Total_Returns
from returns

union all

select 'Order Details' ,Count(*) As Total_Order_Details
from orderdetails;

--------------Display First 10 rows-------------
select *
from customers
limit 10;

select *
from orderdetails
limit 10;

select *
from orders
limit 10;

select *
from products
limit 10;

select *
from returns
limit 10;

----------------Duplicate Check------------------- 

select CustomerID , Count(*) AS Count_of_CustID
from customers
group by CustomerID
having Count(*) > 1;

select ProductID , Count(*) AS Count_of_ProdID
from products
group by ProductID
having Count(*) > 1;

select OrderID , Count(*) AS Count_of_OrderID
from orders
group by OrderID
having Count(*) > 1;

select OrderDetailID , Count(*) AS Count_of_OrderDetailsID
from orderdetails
group by OrderDetailID
having Count(*) > 1;

select ReturnID , Count(*) AS Count_of_returnid
from returns
group by ReturnID
having Count(*) > 1;

--------------------Null Check-------------------

---------Customers------
SELECT
    COUNT(*) FILTER (WHERE CustomerID IS NULL)   AS null_id,
    COUNT(*) FILTER (WHERE CustomerName IS NULL) AS null_name,
    COUNT(*) FILTER (WHERE Gender IS NULL)       AS null_gender,
    COUNT(*) FILTER (WHERE Age IS NULL)          AS null_age,
    COUNT(*) FILTER (WHERE City IS NULL)         AS null_city,
    COUNT(*) FILTER (WHERE SignupDate IS NULL)   AS null_signup,
    COUNT(*) FILTER (WHERE Region IS NULL)       AS null_region
FROM customers;

-----------Products-----------
SELECT
    COUNT(*) FILTER (WHERE ProductID IS NULL)    AS null_id,
    COUNT(*) FILTER (WHERE ProductName IS NULL)  AS null_name,
    COUNT(*) FILTER (WHERE Category IS NULL)     AS null_category,
    COUNT(*) FILTER (WHERE CostPrice IS NULL)    AS null_cost,
    COUNT(*) FILTER (WHERE SellingPrice IS NULL) AS null_price
FROM products;

-----------Orders-----------
SELECT
    COUNT(*) FILTER (WHERE OrderID IS NULL)       AS null_orderid,
    COUNT(*) FILTER (WHERE OrderDate IS NULL)     AS null_date,
    COUNT(*) FILTER (WHERE CustomerID IS NULL)    AS null_custid,
    COUNT(*) FILTER (WHERE PaymentMethod IS NULL) AS null_payment,
    COUNT(*) FILTER (WHERE OrderStatus IS NULL)   AS null_status
FROM orders;

------------OrderDetails-----------
SELECT
    COUNT(*) FILTER (WHERE OrderDetailID IS NULL) AS null_detailid,
    COUNT(*) FILTER (WHERE OrderID IS NULL)       AS null_orderid,
    COUNT(*) FILTER (WHERE ProductID IS NULL)     AS null_productid,
    COUNT(*) FILTER (WHERE Quantity IS NULL)      AS null_qty,
    COUNT(*) FILTER (WHERE UnitPrice IS NULL)     AS null_unitprice,
    COUNT(*) FILTER (WHERE DiscountPct IS NULL)   AS null_discount,
    COUNT(*) FILTER (WHERE SalesAmount IS NULL)   AS null_sales,
    COUNT(*) FILTER (WHERE Profit IS NULL)        AS null_profit
FROM orderdetails;

-------------Returns------------
SELECT
    COUNT(*) FILTER (WHERE ReturnID IS NULL)     AS null_returnid,
    COUNT(*) FILTER (WHERE OrderID IS NULL)      AS null_orderid,
    COUNT(*) FILTER (WHERE ReturnDate IS NULL)   AS null_date,
    COUNT(*) FILTER (WHERE ReturnReason IS NULL) AS null_reason
FROM returns;



-------------- foreign key validations -----------------
---------- orders and customers---------------
select o.OrderID , c.CustomerID
from Customers c
left join Orders o
	on c.CustomerID = o.CustomerID
where c.CustomerID is null;
------------orders and orderdetails---------------
select o.OrderID , od.OrderID
from Orders o
left join Orderdetails od
	on o.OrderID = od.OrderID
where o.orderID is null;
-------------Product & Order--------------
select *
from Products p
left Join OrderDetails od
	on p.ProductID = od.OrderID
where p.ProductID is null;

-----------------------------------Basic Business Questions---------------------------------------
select
	Min(OrderDate) as FirstOrderDate,
	Max(OrderDate) as LastOrderDate,
	Count(Distinct CustomerID) As TotalCustomers
from Orders;

-- Unique Customers and orders
select 'Total Customers',Count(Distinct CustomerID) As Total_Customers
from Orders

union all 

Select 'Total Orders',Count(*) AS Total_Order
from Orders;

--Analysis by Order Status
select OrderStatus , Count(*) As Total_Order
from orders
group by OrderStatus;

-- sum of Revenue by Delivered
select 'Revenue by Delivered',Sum(od.SalesAmount) AS Revenue
from Orders o
join OrderDetails od
	on o.OrderID = od.OrderID
where o.OrderStatus = 'Delivered'

union all 

select 'Profit by Delivered',Sum(od.Profit) AS Revenue
from Orders o
join OrderDetails od
	on o.OrderID = od.OrderID
where o.OrderStatus = 'Delivered'

union all 

select 'Revenue by Cancelled',Sum(od.SalesAmount) AS Revenue
from Orders o
join OrderDetails od
	on o.OrderID = od.OrderID
where o.OrderStatus = 'Cancelled'

union all 

select 'Profit by Cancelled',Sum(od.Profit) AS Revenue
from Orders o
join OrderDetails od
	on o.OrderID = od.OrderID
where o.OrderStatus = 'Cancelled'

union all 

select 'Revenue by Returned',Sum(od.SalesAmount) AS Revenue
from Orders o
join OrderDetails od
	on o.OrderID = od.OrderID
where o.OrderStatus = 'Returned'

union all 

select 'Profit by Returned',Sum(od.Profit) AS Revenue
from Orders o
join OrderDetails od
	on o.OrderID = od.OrderID
where o.OrderStatus = 'Returned';

--Category Wise Revenue when order status is delivered 
select p.category , Sum(od.SalesAmount) As Total_Revenue
from Products As p
join OrderDetails As od
	on p.ProductID = od.ProductID 
join Orders as o
	on od.OrderID = o.OrderID
where o.OrderStatus = 'Delivered'
group by p.category;

-- Category wise Profit when order status is delivered
select p.category , Sum(od.Profit) As Total_Profit
from Products As p
join OrderDetails As od
	on p.ProductID = od.ProductID 
join Orders as o
	on od.OrderID = o.OrderID
where o.OrderStatus = 'Delivered'
group by p.category;

-- Category wise Profit , Revenue and Profit Percent when status is Delivered
select 
	p.category, 
	Sum(od.Profit) As Total_Profit , 
	Sum(od.SalesAmount) As Total_Revenue,
	Sum(od.Profit) / Sum(od.SalesAmount) * 100 AS Profit_Percent
from OrderDetails As od
join Products As p
	on p.ProductID = od.ProductID
join Orders As O
	on o.OrderID = od.OrderID
where o.OrderStatus = 'Delivered'
group by p.Category;

-- Monthly Sales Trend 
select 
	Extract(Year From o.OrderDate) As SalesYear,
	Extract(Month From o.OrderDate) As SalesMonth,
	Sum(od.SalesAmount) As Revenue
From Orders as o
join OrderDetails AS od
	on o.OrderID = Od.OrderID
where o.OrderStatus = 'Delivered'
Group by 
	Extract (Year from o.OrderDate),
	Extract (Month from o.OrderDate);

-- Region wise revenue 
Select c.region , Sum(od.SalesAmount) as Total_Amount
from Customers AS c
join Orders As o
	on o.CustomerID = c.CustomerID
join OrderDetails As od
	on od.OrderID = o.OrderID
group by c.region;

--top 10 customers
Select 
	c.CustomerID,
	c.CustomerName,
	Sum(od.SalesAmount) AS Total_Revenue,
	Sum(Od.Profit) As Total_Profit
From Customers As c
join Orders As o 
	on o.CustomerID = c.CustomerID
join OrderDetails As od 
	on od.OrderID = o.OrderID
where o.OrderStatus = 'Delivered'
group by c.CustomerID
Order by Sum(od.SalesAmount) Desc 
limit 10;




-- top 10 Products
Select 
	p.ProductID,
	p.ProductName,
	Sum(od.SalesAmount) AS Total_Revenue,
	Sum(Od.Profit) As Total_Profit
From Products As p
join OrderDetails As od 
	on p.ProductID = od.ProductID
join Orders As o 
	on o.OrderID = od.OrderID
where o.OrderStatus = 'Delivered'
group by p.ProductID
Order by Sum(od.SalesAmount) Desc 
limit 10;

-- payment method analysis
Select 
	o.PaymentMethod , Sum(od.SalesAmount) As Total_Revenue
from Orders as o
join OrderDetails As od
	on od.OrderID = o.OrderID
group by o.PaymentMethod
order by Sum(od.SalesAmount) Desc
limit 10;

-- Return Analysis 
Select
	r.returnreason,
	Count(*) as TotalReturn
from Returns as r
group by r.returnreason
order by TotalReturn Desc

--Return Rate
select 
	count(Distinct r.OrderID) As ReturnedOrder,
	count(Distinct o.OrderID) As TotalOrder,
	count(Distinct r.orderID) / 
		Count(Distinct o.orderID) * 100 AS return_rate
from Orders as o 
join Returns as r
	on o.OrderID = r.OrderID;




	