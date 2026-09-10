# CodeAlpha Web Scraping Task 1

## Project Overview

This project demonstrates web scraping using Python. Data is collected from a public website using the Requests and BeautifulSoup libraries and stored as a CSV dataset using Pandas.

## Objective

The main objectives of this project are:

* Extract useful information from a public web page.
* Understand the basic HTML structure of a website.
* Use Python libraries for web scraping.
* Create a custom dataset from the scraped information.
* Store the collected data in CSV format.

## Technologies Used

* Python
* Requests
* BeautifulSoup
* Pandas
* GitHub

## Data Source

The project uses **Books to Scrape**, a website designed for practicing web scraping.

Website: https://books.toscrape.com/

## Data Collected

The following information was collected:

| Column       | Description         |
| ------------ | ------------------- |
| Title        | Name of the book    |
| Price        | Price of the book   |
| Availability | Availability status |

The dataset contains **20 book records** scraped from the website.

## Project Files

* `scraper.py` – Python script used to scrape the website.
* `books_dataset.csv` – Dataset generated from the scraped data.
* `README.md` – Project documentation.

## How to Run

1. Install Python.
2. Install the required libraries:

```bash
pip install requests beautifulsoup4 pandas
```

3. Run the Python script:

```bash
python scraper.py
```

4. The scraped data will be saved as:

```text
books_dataset.csv
```

## Output

The final dataset contains book titles, prices, and availability information collected from the website.

## Conclusion

This project helped demonstrate the basic process of web scraping, including sending HTTP requests, parsing HTML using BeautifulSoup, extracting relevant information, and creating a structured dataset using Pandas.
