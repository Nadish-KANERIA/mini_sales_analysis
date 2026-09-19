import pandas as pd
import math
import matplotlib.pyplot as mp

df = pd.read_csv('mini_sales_project.csv')

highest_revenue = df['revenue'].idxmax()
lowest_revenue = df['revenue'].idxmin()
lowest_revenue_order = df.loc[[lowest_revenue]]
highest_revenue_order = df.loc[[highest_revenue]]
#print(hro)

#print(lro)
#med = df['revenue'].median()
#print(df['revenue'].median())
#print(df['revenue'].mean())


def total_revenue():
    rev = 0
    for i in range(len(df['revenue'])):
        rev += df['revenue'][i]
    return rev

#print(df.head(10))

def total_units_sold():
    units = 0
    for i in range(len(df['quantity'])):
        units += df['quantity'][i]
    return units

def best_selling_product():
    quantity_location = df['quantity'].idxmax()
    best_selling_product = df.loc[quantity_location, 'product']
    return best_selling_product

def city_revenue():
    city_revenue = df.groupby('city')['revenue'].sum()
    return city_revenue


revenue = total_revenue()
print(revenue)
units_sold = total_units_sold()
print(units_sold)
best_selling_product_name = best_selling_product()
print(best_selling_product_name)
City_revenue = city_revenue()
print(City_revenue)
missing_data = df.isnull().sum()
print(missing_data) 
# No missing data in the dataset

product_revenue = df.groupby('product')['revenue'].sum()

product_revenue.plot(kind='bar')
mp.ylabel('$ US Dollar')
mp.xlabel('Products')
mp.title('Revenue by Product')

mp.figure()
units_to_product = df.groupby('product')['quantity'].sum()
units_to_product.plot(kind='bar', color='orange')
mp.ylabel('Units Sold')
mp.xlabel('Products')
mp.title('Units Sold by Product')

mp.figure()
cities_to_revenue = df.groupby('city')['revenue'].sum()
cities_to_revenue.plot(kind = 'bar', color = 'green')
mp.title('Revenue by cities')
mp.xlabel('City')
mp.ylabel('Revenue')
mp.show()










