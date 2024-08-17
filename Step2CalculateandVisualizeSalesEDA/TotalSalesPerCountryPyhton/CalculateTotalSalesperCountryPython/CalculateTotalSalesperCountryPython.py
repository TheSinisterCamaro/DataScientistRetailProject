import pandas as pd
import matplotlib.pyplot as plt

# Define the file path
file_path = r'C:\Users\jdick\source\repos\DataScientistRetailProject\final_online_retail_II.csv'

# Load the data, specifying dtype for Invoice to avoid DtypeWarning
data = pd.read_csv(file_path, dtype={'Invoice': str})

# Calculate total sales (Quantity * Price)
data['TotalSales'] = data['Quantity'] * data['Price']

# Group by Country and sum the TotalSales
sales_by_country = data.groupby('Country')['TotalSales'].sum().sort_values(ascending=False)

# Display the top 10 countries by total sales
print("Top 10 countries by total sales:")
print(sales_by_country.head(10))

# Visualize the top 10 countries by total sales
sales_by_country.head(10).plot(kind='bar', figsize=(10, 6), color='skyblue')
plt.title('Top 10 Countries by Total Sales')
plt.xlabel('Country')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Optionally, save the result to a CSV file for reference
sales_by_country.to_csv(r'C:\Users\jdick\source\repos\DataScientistRetailProject\sales_by_country.csv')

