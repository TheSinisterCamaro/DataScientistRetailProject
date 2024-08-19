import pandas as pd
import numpy as np

# Load the final cleaned data
file_path = r'C:\File\Path\Here\final_online_retail_II.csv' # Add your file path to the data you want to use.
data = pd.read_csv(file_path, dtype={'Invoice': str})

# Convert InvoiceDate to datetime format
data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'])

# Set InvoiceDate as the index
data.set_index('InvoiceDate', inplace=True)

# Calculate total sales (Quantity * Price)
data['TotalSales'] = data['Quantity'] * data['Price']

# Step 1: Calculate Customer Lifetime Value (CLV)
customer_clv = data.groupby('Customer ID')['TotalSales'].sum().reset_index()
customer_clv.columns = ['Customer ID', 'Customer Lifetime Value']

# Step 2: Calculate Recency, Frequency, Monetary (RFM) Metrics

# Define current date as the latest date in the dataset
current_date = data.index.max()

# Recency: Days since last purchase
recency = data.groupby('Customer ID')['Invoice'].apply(lambda x: (current_date - x.index.max()).days).reset_index()
recency.columns = ['Customer ID', 'Recency']

# Frequency: Number of purchases
frequency = data.groupby('Customer ID')['Invoice'].nunique().reset_index()
frequency.columns = ['Customer ID', 'Frequency']

# Monetary: Total revenue (already calculated as CLV)
monetary = customer_clv.copy()

# Merge RFM metrics
rfm = recency.merge(frequency, on='Customer ID').merge(monetary, on='Customer ID')

# Step 3: Add Time-Based Features
data['DayOfWeek'] = data.index.dayofweek
data['Month'] = data.index.month
data['Quarter'] = data.index.quarter
data['Year'] = data.index.year

# Step 4: Calculate Average Order Value (AOV)
invoice_count = data.groupby('Customer ID')['Invoice'].nunique().reset_index()
invoice_count.columns = ['Customer ID', 'Invoice Count']

# Merge with the CLV data
aov = customer_clv.merge(invoice_count, on='Customer ID')

# Calculate AOV
aov['Average Order Value'] = aov['Customer Lifetime Value'] / aov['Invoice Count']

# Display the results
print("Customer Lifetime Value (CLV):")
print(customer_clv.head())

print("\nRecency, Frequency, Monetary (RFM) Metrics:")
print(rfm.head())

print("\nTime-Based Features:")
print(data[['DayOfWeek', 'Month', 'Quarter', 'Year']].head())

print("\nAverage Order Value (AOV):")
print(aov[['Customer ID', 'Average Order Value']].head())
