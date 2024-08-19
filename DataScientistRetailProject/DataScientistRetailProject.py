import pandas as pd

# Define the correct path to the final cleaned file on your local system
final_cleaned_file_path = r'C:\Add\Path\Here' # Add path to where your .CSV file is stored

# Load the final cleaned CSV file
final_cleaned_data = pd.read_csv(final_cleaned_file_path)

# Ensure the Invoice column is consistently treated as a string
final_cleaned_data['Invoice'] = final_cleaned_data['Invoice'].astype(str)

# Save the final cleaned data after resolving the DtypeWarning
final_output_path = r'C:\Add\Path\Here\final_online_retail_II.csv' # Add path to where you want the cleaned .CSV file to be stored
final_cleaned_data.to_csv(final_output_path, index=False)

print("Final cleaning and saving completed to:", final_output_path)
