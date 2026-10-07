# Imports
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind


print("our question : \n Is our revenue effect by discount ? \n H0 : No discount does not effect revenue \n h1 : Yes discount affect revenue")
print()
df = pd.read_csv(r"end to end project\Ecommerce Analytics\clean_File.csv")
test_df = df[df["orderstatus"] == 'Delivered'].copy()
print(test_df.describe)

# Create two group

order_level = (
    test_df.groupby("orderid").
    agg(
        ordervalue = ("salesamount" , "sum"),
        Discountpct = ("discountpct" , "mean") 
    ).reset_index()
)
print(order_level)

# First Group
print("Discount Group")
discount_group = order_level[order_level["Discountpct"] > 0]["ordervalue"] 
print(discount_group)
print()
# Second Group 
print("No Discount Group")
no_discount_group = order_level[order_level["Discountpct"] == 0]["ordervalue"]
print(no_discount_group)
print()

# Group AOV  : AOV = Average Order Value
print("Discount AOV:", discount_group.mean())
print("No Discount AOV:", no_discount_group.mean())
print()


# Group Median
print(
    "Discount Median:",
    discount_group.median()
)

print(
    "No Discount Median:",
    no_discount_group.median()
)

# Independent t-test

result = ttest_ind(
    discount_group,
    no_discount_group,
    equal_var=False
)
t_statistics = float(result.statistic)
P_value = float(result.pvalue)
degree_of_freedom = result.df

print("T Statistics : \n " , t_statistics)
print("P-Value : \n ", P_value)
print("Degree of Freedom : \n " , degree_of_freedom)
print()

# Decision Rule
alpha = 0.05

if P_value < alpha:
    print("Reject H0")
else:
    print("Fail to Reject H0")
print()



# Confidence Interval
CI = result.confidence_interval(confidence_level = 0.95)
print("Confidence interval ")
print("Lower limit : \n " , float(CI.low))
print("Upper limit : \n " , float(CI.high))

print()
# Effect Difference
aov_difference = (
    discount_group.mean()
    -
    no_discount_group.mean()
)

print(aov_difference)
print()

# Final Hypothesis Testing Summary
hypothesis_result = pd.DataFrame({
    "Metric": [
        "Discount AOV",
        "No Discount AOV",
        "Difference",
        "T-Statistic",
        "P-Value",
        "Alpha"
    ],
    "Value": [
        discount_group.mean(),
        no_discount_group.mean(),
        aov_difference,
        t_statistics,
        P_value,
        alpha
    ]
})

print(hypothesis_result)