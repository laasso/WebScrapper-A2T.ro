# scraper/webscraper.py
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time
import os

class FilterScrapper:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options=self.options)

    def scrape(self, url, csv_filename):
        # Load the web page
        self.driver.get(url)

        # Wait for a few seconds to ensure that the page is fully loaded (you can adjust the time as needed)
        time.sleep(5)

        # Wait X second to login to get the spoecial geust price
        time.sleep(60)
        print("Start Scrapping")

        # Simulate scrolling down to load more elements
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        while True:
            # Scroll down
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # Wait for new elements to load
            time.sleep(2)
            # Calculate new height of the page
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        # Find all elements containing product details
        products = self.driver.find_elements(By.CLASS_NAME, 'product-item')

        # Create a CSV file at the specified path
        csv_path = os.path.join(csv_filename)  # Replace "path" with the specific path
        with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
            # Create the CSV writer
            writer = csv.writer(csvfile)
            # Write headers
            writer.writerow(['Product', 'Price'])

            # Iterate over product elements and extract names and prices
            for product in products:
                # Extract product name
                name = product.find_element(By.CLASS_NAME, 'product-item-link').text.strip()

                # Extract product price
                price = product.find_element(By.CLASS_NAME, 'price').text.strip()
                parts = price.split()
                price = parts[0] + "." + parts[2]
                print(price)
                writer.writerow([name, price])

        print("All products from {} have been saved in {}.".format(url, csv_path))

    def close(self):
        # Close the browser
        self.driver.quit()
