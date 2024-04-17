# WebScraper-A2T.ro

This project is a web scraper designed specifically for the website [A2T.ro](https://www.a2t.ro/), which is a security company specialized in CCTV systems, security cameras, alarm systems, and other related products.

The web scraper gathers information about various products available on the A2T.ro website, such as surveillance kits, IP cameras, security accessories, alarm systems, home automation, access control, intercoms, fire alarm systems, sound systems, electrical installations, networks, and telephony, among others.

## Features

- **Data Scraping:** The scraper collects detailed information about products available in different categories on the A2T.ro website, including the product name and its price.

- **Export to CSV Files:** The collected data is exported to CSV files for further analysis and processing.

## Usage

1. Clone this repository to your local machine.

    git clone https://github.com/laasso/WebScraper-A2T.ro.git


2. Install the necessary dependencies. Make sure you have Python installed and the required libraries listed in `requirements.txt`.

    pip install -r requirements.txt


3. Set up the Python path if needed. If you have custom paths for your Python environment, make sure to update the `PYTHONPATH` accordingly.

    export PYTHONPATH=/your/python/path:$PYTHONPATH


4. Run the main script `main.py`.

    python3 main/main.py


The scraper will collect product data and save it to CSV files in the `CSV` folder.

## Screenshots

Here is a screenshot of the scraper in action:

![Scraper Screenshot](screenshots/scraper_screenshot.png)

## Contributions

Contributions are welcome. If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Make your changes and commit them (`git commit -am 'Add a new feature'`).
4. Push your changes to your forked repository (`git push origin feature/new-feature`).
5. Create a new pull request.

## Author

This project was created by [lasso](https://github.com/laasso).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
