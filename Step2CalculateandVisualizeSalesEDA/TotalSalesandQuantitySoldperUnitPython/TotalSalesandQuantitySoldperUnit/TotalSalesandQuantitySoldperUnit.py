import pandas as pd
import matplotlib.pyplot as plt

# Load the final cleaned data
file_path = r'C:\Users\jdick\source\repos\DataScientistRetailProject\final_online_retail_II.csv'
data = pd.read_csv(file_path)

# Calculate total sales (Quantity * Price)
data['TotalSales'] = data['Quantity'] * data['Price']

# Group by StockCode (product identifier) to calculate total sales and quantity sold per product
product_sales = data.groupby('StockCode').agg({'TotalSales': 'sum', 'Quantity': 'sum'}).sort_values(by='TotalSales', ascending=False)

# Display the top 10 products by total sales
print("Top 10 products by total sales:")
print(product_sales.head(10))

# Display the top 10 products by quantity sold
print("\nTop 10 products by quantity sold:")
print(product_sales.sort_values(by='Quantity', ascending=False).head(10))

# Visualize the top 10 products by total sales
product_sales.head(10).plot(kind='bar', y='TotalSales', figsize=(10, 6), color='green')
plt.title('Top 10 Products by Total Sales')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Visualize the top 10 products by quantity sold
product_sales.sort_values(by='Quantity', ascending=False).head(10).plot(kind='bar', y='Quantity', figsize=(10, 6), color='orange')
plt.title('Top 10 Products by Quantity Sold')
plt.xlabel('Product')
plt.ylabel('Quantity Sold')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

