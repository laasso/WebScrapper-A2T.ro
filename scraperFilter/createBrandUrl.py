import csv
import os
import re

base_url = "https://www.a2t.ro/"

def construct_url(category, attribute=None, value=None):
    url = base_url + category.replace(" ", "").lower()  # Remove spaces and convert to lowercase
    if value:
        url += f"?brand={value.replace(' ', '').lower()}"  # Remove spaces and convert to lowercase
    return url

import re

def read_csv_and_construct_urls(csv_file, brands):
    urls = []
    base_url_length = len(base_url + "acces-point")  # Length of the base URL
    category_name = os.path.splitext(os.path.basename(csv_file))[0]
    with open(csv_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header
        for row in reader:
            if not row or not row[0].strip():  # Skip empty rows and rows with empty first column
                continue
            brand_name = row[0].strip().lower()  # Convert to lowercase and remove leading/trailing whitespaces
            brand_name = re.sub(r'\s*\([^)]*\)', '', brand_name)  # Remove parentheses and their content
            for brand in brands:
                if brand_name.startswith(brand):  # Check if the brand name starts with any brand in the list
                    url = construct_url(category_name, 'brand', brand_name)
                    if len(url) > base_url_length:  # Check if the URL is longer than the base URL
                        urls.append(url)
                    break  # Break the loop once a match is found
    return urls


def process_csv_files_in_directory(directory, brands):
    all_urls = []
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            csv_file = os.path.join(directory, filename)
            print(f"Processing CSV file: {csv_file}")
            urls = read_csv_and_construct_urls(csv_file, brands)
            all_urls.extend(urls)
    print("All URLs:", all_urls)  # Print all URLs to check if they are populated correctly

    # Save URLs to CSV file
    with open("../../filesCSV/CSVfinale/brandsurl.csv", "w", newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for url in all_urls:
            writer.writerow([url])


if __name__ == "__main__":
    csv_directory = "../../filesCSV/CSVfilter/"  # Replace with your directory containing CSV files
    brands_list = [
        "active", "adata", "adel", "adeleq", "afore", "ajax", "aleph", "alien", "allied telesis", "amc",
        "ampevo", "anviz", "aoc", "aqara", "asytech networking", "atlo", "atra", "atu tech", "autone",
        "avatto", "avs electronics", "azusa", "baseus", "beninca", "bentel", "boomx", "braun group", "braytron",
        "bst pro", "cabletech", "cablexpert", "cambox", "cammpro", "canadian solar", "combi arialdo", "commax",
        "comunello", "crow", "d-link", "dablerom", "dahua", "ddpai", "deli", "delta", "detnov", "dibeisi", "ditec",
        "dorcas", "dsc", "dsc neo", "dsppa", "eldes", "electra", "elmes", "emtex", "eonboom", "etk", "ezviz",
        "fac", "fireclass", "freder", "fronius", "gembird", "gewiss", "goobay", "goodwe", "gosund", "gp batteries",
        "grandstream", "growatt", "habotest", "hanbang", "heyi", "hikvision", "hisense", "hiwatch", "huawei",
        "ibiza sound", "imou", "inim", "itc", "kale", "kano", "kantech", "kemot", "king gates", "kingston", "kosmo",
        "kruger matz", "lapp", "laxihub", "lg", "life", "linomatik", "logilink", "longi", "ltc", "mean well",
        "mekas kablo", "mikrotik"
    ]
    process_csv_files_in_directory(csv_directory, brands_list)
