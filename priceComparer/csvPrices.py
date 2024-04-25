import pandas as pd
import glob

# Get the list of all CSV files in the directory
discounted_price_files = glob.glob("/home/lasso/WebScrapper-A2T.ro/filesCSV/CSVproducts/*")
original_price_files = glob.glob("/home/lasso/WebScrapper-A2T.ro/filesCSV/CSVproductsdisc/*")

# Initialize empty lists to store the dataframes
discounted_prices_list = []
original_prices_list = []

# Read and append each CSV file to the respective list
for file in discounted_price_files:
    discounted_prices_list.append(pd.read_csv(file))

for file in original_price_files:
    original_prices_list.append(pd.read_csv(file))

# Concatenate the dataframes in the list
discounted_prices = pd.concat(discounted_prices_list, ignore_index=True).drop_duplicates()
original_prices = pd.concat(original_prices_list, ignore_index=True).drop_duplicates()

# Combine the DataFrames based on the "Product" column
combined_data = pd.merge(discounted_prices, original_prices, on="Product", how="inner")

# Save the combined data to a new CSV file
combined_data.to_csv("/home/lasso/WebScrapper-A2T.ro/filesCSV/CSVcombined/combined_data.csv", index=False)
