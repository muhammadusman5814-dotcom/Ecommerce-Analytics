# Ecommerce Analytics

An end-to-end ecommerce data analytics project combining SQL, Python, statistical analysis, and Power BI to uncover sales, profitability, product, payment, regional, discount, and return insights.

---

## 📊 Project Overview

This project analyzes ecommerce transaction data across **customers, orders, order details, products, and returns**. It follows a complete analytics workflow, from storing and querying the data in SQL, through cleaning, exploration, and statistical testing in Python, to an interactive Power BI dashboard, a written report, and a presentation.

**Why it matters:** the goal is to turn raw transactional data into clear answers a business can act on, such as which categories and products drive revenue, which regions underperform, which payment methods customers prefer, how discounts affect profit, and why customers return products.

**How the tools work together**

| Stage | Tool | Role |
|---|---|---|
| Data storage and querying | SQL (pgAdmin 4) | Organize the five source tables and query them for analysis |
| Data preparation | Python | Clean and prepare the data for analysis |
| Exploration | Python (Matplotlib / Seaborn visuals) | Study distributions, trends, relationships, and outliers |
| Statistical validation | Python | Test hypotheses about the data |
| Business intelligence | Power BI | Interactive KPI dashboard with filters |
| Communication | Word report and PowerPoint deck | Share findings with stakeholders |

---

## 🔄 Project Workflow

```text
Data → SQL → Data Cleaning → Exploratory Data Analysis → Hypothesis Testing
     → Power BI Dashboard → Business Insights → Report → Presentation
```

1. **Data**: Five CSV files (Customers, Orders, OrderDetails, Products, Returns).
2. **SQL**: Queries written for pgAdmin 4 (`Ecommerce Analytics pgadmin4.sql`).
3. **Data Cleaning**: `Data Cleaning.py` prepares the data for analysis.
4. **Exploratory Data Analysis**: `Exploratory Data Analysis.py` produces the visual analysis shown below.
5. **Hypothesis Testing**: `Hypothesis_Testing.py` applies statistical tests.
6. **Power BI Dashboard**: `Ecommerce Analytics Dashboard.pbix` presents the KPIs and interactive visuals.
7. **Business Insights**: Findings from the dashboard and EDA.
8. **Report and Presentation**: Documented in the `.docx` report and `.pptx` deck.

---

## 🎯 Business Objectives

- Measure overall **sales, revenue, and profit performance**, including profit margin
- Track **monthly revenue and profit trends**
- Compare **category-wise and region-wise** revenue and profit
- Identify **top-selling products**
- Understand **payment method** usage and revenue contribution
- Analyze **sales by gender** and customer segments through dashboard filters
- Evaluate the **impact of discounts** on profit
- Study the relationship between **quantity, unit price, sales amount, and profit**
- Detect **outliers** in sales amounts
- Analyze **returns**: return rate and return reasons
- Validate relationships in the data through **hypothesis testing**

---

## 🗂️ Repository Structure

```text
Ecommerce-Analytics/
│
├── Customers.csv
├── OrderDetails.csv
├── Orders.csv
├── Products.csv
├── Returns.csv
│
├── Data Cleaning.py
├── Exploratory Data Analysis.py
├── Hypothesis_Testing.py
├── Ecommerce Analytics pgadmin4.sql
│
├── Ecommerce Analytics Dashboard.pbix
├── Ecommerce Analytics Report.docx
├── Ecommerce Analytics Presentation.pptx
│
├── images/            # dashboard and EDA screenshots used in this README
│
└── README.md
```

| File | Description |
|---|---|
| `Customers.csv`, `Orders.csv`, `OrderDetails.csv`, `Products.csv`, `Returns.csv` | Source data tables |
| `Ecommerce Analytics pgadmin4.sql` | SQL script for pgAdmin 4 |
| `Data Cleaning.py` | Data cleaning and preparation |
| `Exploratory Data Analysis.py` | Exploratory analysis and visualizations |
| `Hypothesis_Testing.py` | Statistical hypothesis testing |
| `Ecommerce Analytics Dashboard.pbix` | Power BI dashboard |
| `Ecommerce Analytics Report.docx` | Written analysis report |
| `Ecommerce Analytics Presentation.pptx` | Presentation of findings |

---

## 🧰 Tools & Technologies

- **SQL** (pgAdmin 4)
- **Python** (data cleaning, EDA, statistical testing; charts built with Matplotlib/Seaborn-style plots)
- **Power BI** (dashboard and DAX measures)
- **Microsoft Word / PowerPoint** (report and presentation)

---

## 📈 Power BI Dashboard

The **Ecommerce Performance Dashboard** gives a single-page view of business performance.

![Ecommerce Performance Dashboard](images/dashboard.png)

**KPI cards**

| Total Orders | Total Revenue | Total Profit | Profit % | Average Revenue | Return Rate |
|---|---|---|---|---|---|
| 4.386K | 153.31M | 52.52M | 34.26% | 13.98K | 5.14% |

**Interactive filters:** Category, Gender, Region, Order Status, Month

**Visuals**
- Sales amount and profit by month
- Top 10 selling products
- Total revenue by payment method
- Regional share of sales
- Key Insights panel

---

## 🔍 Exploratory Data Analysis

The EDA script produces the following analyses.

| Analysis | What it shows |
|---|---|
| Sale Distribution | Sales amounts are right-skewed, with most transactions at the lower end and a long tail of high-value sales |
| Profit Distribution | Right-skewed; most transactions earn modest profit, and a small number show negative profit |
| Monthly Revenue and Profit Trends | Month-by-month movement from January 2024 to July 2026 |
| Category-wise Revenue and Profit | Beauty, Books, Electronics, Fashion, and Home compared |
| Region-wise Revenue and Profit | East, North, South, and West compared |
| Payment Method Trend | Order counts by COD, Credit Card, Debit Card, Net Banking, and UPI |
| Discount vs Profit | Profit across discount levels from 0% to 25% |
| Quantity vs Revenue | How revenue scales with quantity (1 to 4 units) |
| Correlation Matrix | Relationships between age, quantity, unit price, discount %, sales amount, and profit |
| Sales Amount Outliers | Box plot highlighting high-value outliers |
| Top 10 Products by Revenue | Highest-revenue products |
| Return Reason Analysis | Distribution of return reasons |

<details>
<summary>View EDA charts</summary>

![Sale Distribution](images/Figure_1.png)
![Profit Distribution](images/Figure_2.png)
![Monthly Revenue Trend](images/Figure_3.png)
![Monthly Profit Trend](images/Figure_4.png)
![Category Wise Revenue](images/Figure_5.png)
![Category Wise Profit](images/Figure_6.png)
![Region Wise Revenue](images/Figure_7.png)
![Region Wise Profit](images/Figure_8.png)
![Payment Method Trend](images/Figure_9.png)
![Discount Vs Profit](images/Figure_10.png)
![Quantity Vs Revenue](images/Figure_11.png)
![Correlation Matrix](images/Figure_12.png)
![Sales Amount Outlier](images/Figure_13.png)
![Top 10 Products](images/Figure_14.png)
![Return Reason Analysis](images/Figure_15.png)

</details>

---

## 🧪 Hypothesis Testing

`Hypothesis_Testing.py` applies statistical tests to check whether patterns observed during EDA hold up statistically, rather than relying on visual inspection alone. See the report (`Ecommerce Analytics Report.docx`) for the full methodology and results.

<!-- TODO: list the specific hypotheses, tests used, and results from Hypothesis_Testing.py -->

---

## 💡 Key Business Insights

These observations come from the dashboard and EDA visuals in this repository.

- **Profitability:** The overall profit margin is **34.26%** and the return rate is **5.14%**.
- **Categories:** **Home** and **Electronics** generate the highest revenue and profit; **Books** is the lowest.
- **Regions:** **South** leads in revenue and profit, followed by West and North. **East is the weakest region** (about 10.71% of sales on the dashboard), a clear growth opportunity.
- **Payments:** **UPI** is the most used and highest-revenue payment method, ahead of Credit Card, Debit Card, COD, and Net Banking.
- **Products:** **Bedsheet** is the top-selling product by revenue.
- **Seasonality:** July is the strongest month on the dashboard's monthly view, and the monthly trend shows noticeable peaks and dips over time.
- **Discounts:** Higher discount levels are associated with lower profit, and negative-profit transactions appear at the highest discount levels (20% to 25%).
- **Drivers of profit:** Sales amount (0.91) and unit price (0.70) show the strongest correlation with profit; discount % shows a mild negative correlation (-0.24).
- **Returns:** "Not Satisfied" and "Late Delivery" are the most frequent return reasons.

---

## 🚀 How to Use

1. **Clone the repository**
   ```bash
   git clone https://github.com/muhammadusman5814-dotcom/<repository-name>.git
   ```
2. **SQL:** Open `Ecommerce Analytics pgadmin4.sql` in pgAdmin 4 and run it against your PostgreSQL database.
3. **Python:** Run `Data Cleaning.py`, then `Exploratory Data Analysis.py`, then `Hypothesis_Testing.py`.
4. **Dashboard:** Open `Ecommerce Analytics Dashboard.pbix` in Power BI Desktop.
5. **Report and slides:** Open the `.docx` and `.pptx` files for the full write-up.

---

## 🎓 Skills Demonstrated

- SQL querying and database work
- Data cleaning and preparation
- Exploratory data analysis and data visualization
- Statistical hypothesis testing
- Power BI dashboard design (KPIs, slicers, interactive visuals)
- Translating data into business insights
- Reporting and presenting analytical findings

---

## 👤 Author

**Muhammad Usman**
BS Data Analytics, PMAS-Arid Agriculture University Rawalpindi

GitHub: [muhammadusman5814-dotcom](https://github.com/muhammadusman5814-dotcom)
