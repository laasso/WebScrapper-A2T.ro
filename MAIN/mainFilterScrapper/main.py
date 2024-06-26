# main.py
from scraperFilter.filterScraper import FilterScrapper

def read_urls_and_filenames(filename):
    urls_and_filenames = []
    with open(filename, 'r') as file:
        for line in file:
            url, csv_filename = line.strip().split(', ')
            urls_and_filenames.append((url.strip(), csv_filename.strip()))
    return urls_and_filenames
def main():
    scraper = FilterScrapper()
    urls_and_filenames = read_urls_and_filenames('../../INFO/informacion.txt')
    for url, csv_filename in urls_and_filenames:
        scraper.scrape(url, csv_filename)
    scraper.close()

if __name__ == "__main__":
    main()
