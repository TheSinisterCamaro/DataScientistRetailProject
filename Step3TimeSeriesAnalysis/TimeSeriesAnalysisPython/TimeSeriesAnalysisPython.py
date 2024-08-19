# The 2 virtualized charts for monthly and quarterly have a random "le6" on the top left.
# Tried updating matplot, using seaborn, and even saving them as images to remove the text with no success.
# Data looks great and charts work fine, but the "le6" on the top left is not clean.
# Any idea on how to fix?

import pandas as pd
import matplotlib.pyplot as plt

# Load the final cleaned data with specified data types to avoid DtypeWarning
file_path = r'C:\File\Path\Here\final_online_retail_II.csv' # Add your file path to the data you want to use.
data = pd.read_csv(file_path, dtype={'Invoice': str})

# Convert InvoiceDate to datetime format
data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'])

# Set InvoiceDate as the index
data.set_index('InvoiceDate', inplace=True)

# Calculate total sales (Quantity * Price)
data['TotalSales'] = data['Quantity'] * data['Price']

# Resample the data to daily, monthly, and quarterly sales
daily_sales = data['TotalSales'].resample('D').sum()
monthly_sales = data['TotalSales'].resample('ME').sum()
quarterly_sales = data['TotalSales'].resample('QE').sum()

# Display the first few entries of each resampled series
print("Daily Sales:\n", daily_sales.head())
print("\nMonthly Sales:\n", monthly_sales.head())
print("\nQuarterly Sales:\n", quarterly_sales.head())

# Plot daily sales trend
plt.figure(figsize=(14, 7))
plt.plot(daily_sales.index, daily_sales.values, color='blue')
plt.title('Daily Sales Trend', fontsize=16)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Total Sales', fontsize=14)
plt.show()

# Plot monthly sales trend
plt.figure(figsize=(14, 7))
plt.plot(monthly_sales.index, monthly_sales.values, color='green')
plt.title('Monthly Sales Trend', fontsize=16)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Total Sales', fontsize=14)
plt.show()

# Plot quarterly sales trend
plt.figure(figsize=(14, 7))
plt.plot(quarterly_sales.index, quarterly_sales.values, color='red')
plt.title('Quarterly Sales Trend', fontsize=16)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Total Sales', fontsize=14)
plt.show()