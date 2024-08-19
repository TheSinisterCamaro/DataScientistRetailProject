import pandas as pd
from sklearn.model_selection import train_test_split
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

# Load the final cleaned data
file_path = r'C:\File\Path\Here\final_online_retail_II.csv' # Add your file path to the data you want to use.
data = pd.read_csv(file_path, dtype={'Invoice': str})

# Convert InvoiceDate to datetime format
data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'])

# Set InvoiceDate as the index
data.set_index('InvoiceDate', inplace=True)

# Calculate total sales (Quantity * Price)
data['TotalSales'] = data['Quantity'] * data['Price']

# Resample the data to daily sales
daily_sales = data['TotalSales'].resample('D').sum()

# Split the data into training and testing sets
train, test = train_test_split(daily_sales, test_size=0.2, shuffle=False)

# Fit the ARIMA model with order (5, 1, 0)
arima_model = ARIMA(train, order=(5, 1, 0))
arima_fitted = arima_model.fit()

# Make predictions on the test set
arima_predictions = arima_fitted.forecast(steps=len(test))

# Plot the actual vs predicted sales
plt.figure(figsize=(14, 7))
plt.plot(train.index, train, label='Training Data')
plt.plot(test.index, test, label='Test Data')
plt.plot(test.index, arima_predictions, label='ARIMA Predictions', color='red')
plt.title('Sales Forecasting with ARIMA')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.legend()
plt.show()
