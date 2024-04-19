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
        self.driver.maximize_window()

        # Wait for a few seconds to ensure that the page is fully loaded (you can adjust the time as needed)
        time.sleep(5)

        # Wait X second to login to get the special guest price
        time.sleep(1)
        print("Start Scraping")

        # Find all elements containing products with the specified filter
        filters  = self.driver.find_elements(By.CSS_SELECTOR, 'span[data-v-00c75b6d=""]')


        # Create a CSV file at the specified path
        csv_path = os.path.join(csv_filename)  # Replace "path" with the specific path
        with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
            # Create the CSV writer
            writer = csv.writer(csvfile)
            # Write headers
            writer.writerow(['Filter'])

            # Iterate over filter elements and extract names
            for filt in filters:
                # Extract filter name
                name = filt.text.strip()
                print(name)
                writer.writerow([name])

        print("All filters from {} have been saved in {}.".format(url, csv_path))

    def close(self):
        # Close the browser
        self.driver.quit()

