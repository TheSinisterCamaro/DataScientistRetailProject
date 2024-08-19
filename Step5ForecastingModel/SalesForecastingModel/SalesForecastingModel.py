import pandas as pd
from sklearn.model_selection import train_test_split

# Load the final cleaned data
file_path = r'C:\Users\jdick\source\repos\DataScientistRetailProject\final_online_retail_II.csv'
data = pd.read_csv(file_path, dtype={'Invoice': str})

# Convert InvoiceDate to datetime format
data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'])

# Set InvoiceDate as the index
data.set_index('InvoiceDate', inplace=True)

# Calculate total sales (Quantity * Price)
data['TotalSales'] = data['Quantity'] * data['Price']

# Resample the data to daily sales
daily_sales = data['TotalSales'].resample('D').sum()

# Reset the index to prepare for modeling
daily_sales = daily_sales.reset_index()

# Rename the columns for clarity
daily_sales.columns = ['Date', 'TotalSales']

# Display the first few rows
print(daily_sales.head())

# Split the data into training and testing sets
train, test = train_test_split(daily_sales, test_size=0.2, shuffle=False, stratify=None)

# Display the size of the training and testing sets
print(f"Training set size: {len(train)}")
print(f"Testing set size: {len(test)}")

