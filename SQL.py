import sqlite3
import pandas as pd
con = sqlite3.connect("mini_sales_project.db")

df = pd.read_sql("SELECT * FROM sales", con)
print(df)

categories_units_sold = pd.read_sql("SELECT category, COUNT(*) AS count FROM sales GROUP BY category", con)
print(categories_units_sold)

average_order_value = pd.read_sql(
    "SELECT city, AVG(revenue) as avg_rev FROM sales GROUP BY city"
    , con)
print(average_order_value)

revenue_by_category = pd.read_sql(
    "Select category, SUM(revenue) as total_revenue_per_category FROM sales GROUP BY category"
    , con
)


print(revenue_by_category)


con.close()