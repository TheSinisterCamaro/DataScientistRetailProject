import pandas as pd
import matplotlib.pyplot as plt

# Load the final cleaned data
file_path = r'C:\File\Path\Here\final_online_retail_II.csv' # Add your file path to the data you want to use here
data = pd.read_csv(file_path)

# Calculate total sales (Quantity * Price)
data['TotalSales'] = data['Quantity'] * data['Price']

# Group by Customer ID to calculate total sales, number of orders, and average order value per customer
customer_metrics = data.groupby('Customer ID').agg({
    'TotalSales': 'sum',
    'Invoice': 'nunique',
    'Quantity': 'sum'
}).rename(columns={
    'TotalSales': 'TotalSpend',
    'Invoice': 'OrderCount',
    'Quantity': 'TotalQuantity'
})

# Calculate Average Order Value (TotalSpend / OrderCount)
customer_metrics['AvgOrderValue'] = customer_metrics['TotalSpend'] / customer_metrics['OrderCount']

# Display the first few rows of the customer metrics
print("Customer Metrics (first 5 rows):")
print(customer_metrics.head())

# Create segments based on TotalSpend
customer_metrics['Segment'] = pd.qcut(customer_metrics['TotalSpend'], q=[0, .5, .8, 1.], labels=['Low-Value', 'Mid-Value', 'High-Value'])

# Display the distribution of customers across segments
segment_distribution = customer_metrics['Segment'].value_counts()
print("\nCustomer Segment Distribution:")
print(segment_distribution)

# Visualize the distribution of customer segments
segment_distribution.plot(kind='bar', color='blue', figsize=(8, 5))
plt.title('Customer Segmentation by Total Spend')
plt.xlabel('Customer Segment')
plt.ylabel('Number of Customers')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

