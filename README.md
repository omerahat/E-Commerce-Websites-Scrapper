# e-commerce-websites-scraper

This Python script allows you to extract data from e-commerce websites by providing their product URLs. The extracted data includes the product's name, price, rating, and review count 

## Supported Websites

- Amazon Global

- eBay

- Hepsiburada

- Trendyol

- Teknosa

- Vatan Bilgisayar

## Dependencies

This script uses the following dependencies:

- requests
- BeautifulSoup
- datetime
- json
- time

You can install all the dependencies using pip by running the following command:

```
pip install requests BeautifulSoup datetime json
```

## Usage
To use the web scraper, simply pass the URL of the product page you want to scrape to the function. The function will return a JSON object containing the product data.

Here's an example of how to use the scraper:
```
from scraper import get_data_from_amazon

url = "https://www.amazon.com/Apple-MU8F2AM-A-Pencil-Generation/dp/B07K1WWBJK/"
product_data = get_data_from_amazon(url)

print(product_data)
```
##### Output:
{"platform": "amazon", "time": "2023-04-09 20:41:29", "title": "Apple Pencil (2nd Generation)", "price": "$112.89", "review": 75343, "rating": "4.8"}

## Disclaimer
Please note that web scraping can potentially violate the terms of service of the websites being scraped. Use this script at your own risk and ensure that you comply with all relevant laws and regulations.
