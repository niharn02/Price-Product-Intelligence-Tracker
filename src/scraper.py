# Import libraries required for web scraping, data processing, file handling, and date tracking
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import os
from datetime import datetime


# Record the date on which the scraping process is executed
scrape_date = datetime.now().strftime("%Y-%m-%d")

# Store all scraped book records before creating the final DataFrame
all_data = []


# Scrape all 50 catalogue pages from the source website
for page in range(1, 51):
    url = f"http://books.toscrape.com/catalogue/page-{page}.html"

    # Send a request to the current catalogue page and parse its HTML content
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all book product cards on the current page
    books = soup.find_all("article", class_="product_pod")

    # Extract the required product information from each book
    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        availability = book.find("p", class_="instock availability").text.strip()
        rating = book.p["class"][1]

        # Store the extracted information along with the scrape date
        all_data.append({
            "title": title,
            "price": price,
            "availability": availability,
            "rating": rating,
            "scrape_date": scrape_date
        })

    # Pause between requests to avoid sending requests too rapidly
    time.sleep(1)


# Convert all scraped records into a pandas DataFrame
df_all = pd.DataFrame(all_data)


# Identify the project root directory
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Define the path for the historical raw dataset
file_path = os.path.join(project_root, "data", "raw", "all_books.csv")


# Append new scraping results if the file already exists;
# otherwise, create a new CSV file with column headers
if os.path.exists(file_path):
    df_all.to_csv(file_path, mode='a', header=False, index=False)
else:
    df_all.to_csv(file_path, mode='w', header=True, index=False)


# Display a confirmation message showing the scrape date and number of records collected
print(f"Scrape completed for {scrape_date}. {len(df_all)} rows collected.")
