import pandas as pd

# Read the combined CSV file of discounted and original prices
combined_prices = pd.read_csv("../filesCSV/CSVcombined/combined_data.csv")

# Read the CSV file containing names and codes
provided_data = pd.read_csv("../filesCSV/CSVsku/sku_names.csv")

# Combine the DataFrames based on the "Product" column
final_data = pd.merge(combined_prices, provided_data, on="Product", how="inner")

# Select and reorder the necessary columns
final_data = final_data[["SKU", "Product", "Original Price", "Discounted Price"]]

# Save the final data to a new CSV file
final_data.to_csv("../filesCSV/CSVfinale/final_data.csv", index=False)
