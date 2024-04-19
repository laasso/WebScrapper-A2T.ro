import pandas as pd
import glob

# Get the list of all CSV files in the directory
discounted_price_files = glob.glob("../filesCSV/CSV/*.csv")
original_price_files = glob.glob("../filesCSV/CSVdiscount/*.csv")

# Read all CSV files and combine them into a single DataFrame
discounted_prices = pd.concat([pd.read_csv(file) for file in discounted_price_files], ignore_index=True)
original_prices = pd.concat([pd.read_csv(file) for file in original_price_files], ignore_index=True)

# Combine the DataFrames based on the "Product" column
combined_data = pd.merge(discounted_prices, original_prices, on="Product", how="inner")

# Save the combined data to a new CSV file
combined_data.to_csv("../filesCSV/CSVcombined/combined_data.csv", index=False)
