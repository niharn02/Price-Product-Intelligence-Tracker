# Price & Product Intelligence Tracker

An end-to-end data analytics project that collects product data from the web, cleans and analyses it using Python and SQL, and presents product and pricing insights through Power BI.

## 📌 Project Overview

This project simulates a **product price and availability monitoring system** using data collected from [Books to Scrape](https://books.toscrape.com/), a website designed for practicing web scraping.

The pipeline covers the complete analytics workflow:

**Web Scraping → Data Cleaning → SQLite → SQL Analysis → Power BI Dashboard**

The project tracks book titles, prices, availability, ratings, and scraping dates. By storing data from multiple scraping runs, the project can also analyse historical price movements.

---

## 🌐 Data Source

**Books to Scrape**  
https://books.toscrape.com/

The website provides an e-commerce-style catalogue of books across 50 pages.

For each product, the scraper collects:

- Book title
- Price
- Availability
- Star rating
- Scrape date

The scraper processes all 50 catalogue pages and stores the results in a CSV dataset.

---

## 🏗️ Project Structure

```text
price-product-intelligence-tracker/
│
│
├── notebooks/
│   ├── scraper.ipynb
│   └── analysis.ipynb
│
├── src/
│   └── scraper.py
│
├── dashboard/
│   └── Product Price Intelligence Tracker.pdf
│
├── screenshots/
│   └── dashboard.png
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 🕷️ Web Scraping — `scraper.py`

The main scraping pipeline is implemented in Python using:

- `Requests`
- `BeautifulSoup`
- `Pandas`

The script:

1. Visits all 50 catalogue pages.
2. Parses the HTML using BeautifulSoup.
3. Identifies each book product card.
4. Extracts the title, price, availability and rating.
5. Records the date of the scraping run.
6. Converts the collected data into a Pandas DataFrame.
7. Appends new scraping results to the existing CSV dataset.

Recording the `scrape_date` allows the same products to be tracked across multiple scraping runs and provides the foundation for historical price analysis.

---

## 📓 `scraper.ipynb`

The scraping notebook demonstrates the web-scraping process interactively.

It is used to:

- Explore the website structure.
- Extract product information.
- Inspect the collected dataset.
- Test and understand the scraping logic.

The reusable production-style scraper is maintained separately in `src/scraper.py`.

---

## 🧹 Data Preparation & Analysis — `analysis.ipynb`

The analysis notebook contains the main data preparation and analytical workflow.

It includes:

- Loading the scraped dataset
- Removing duplicate records
- Cleaning and converting prices
- Converting star ratings into numerical values
- Loading the cleaned data into SQLite
- Running SQL-based analysis
- Checking data quality
- Comparing prices across scraping dates

The cleaned data is stored in a SQLite database using the table:

```text
price_history
```
---

## 📊 Power BI Dashboard

The final results are presented in a Power BI dashboard titled:

**Price and Product Intelligence Tracker**

### Dashboard KPIs

- **Total Books:** 999
- **Out of Stock:** 0
- **Scrape Days:** 5
- **Average Price:** 35.07

### Dashboard Visualisations

- Average price by star rating
- Top 5 most expensive books
- Top 5 cheapest books
- Price movement over time
- Product availability

The current dataset did not contain actual price changes during the tracking period because Books to Scrape does not simulate continuously changing prices. However, the historical scraping and SQL comparison logic was built to support price tracking when connected to a live pricing source.

---

## 🔍 Data Quality

An important part of the project was validating the data before performing historical comparisons.

A duplicate-title issue was identified involving **The Star-Touched Queen**. This highlighted a limitation of using product titles as the primary identifier.

For a production implementation, a stable identifier such as a **product ID or product URL** would be captured during scraping to ensure accurate product matching across different scraping dates.

---

## 🛠️ Technologies Used

| Area | Technologies |
|---|---|
| Web Scraping | Python, Requests, BeautifulSoup |
| Data Processing | Python, Pandas |
| Database | SQLite |
| Data Analysis | SQL, Pandas |
| Visualisation | Microsoft Power BI |
| Development | Jupyter Notebook, Git, GitHub |

---

## 🚀 How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the scraper

```bash
python src/scraper.py
```

### 3. Run the analysis

Open:

```text
notebooks/analysis.ipynb
```

and execute the notebook.

### 4. View the dashboard

The completed Power BI dashboard is available in:

```text
dashboard/Product Price Intelligence Tracker.pdf
```

---

## ⚠️ Limitations & Future Improvements

The current project uses Books to Scrape as a practice data source, so prices do not change dynamically like a real e-commerce website.

Future improvements could include:

- Capturing stable product IDs or URLs
- Automated scheduled scraping
- Real-time price monitoring
- Price-change alerts
- Category-level analysis
- Availability trend analysis
- PostgreSQL or cloud database integration
- Automated Power BI data refresh

---

## 🎯 Key Skills Demonstrated

This project demonstrates practical experience in:

- Web scraping
- Data collection
- Data cleaning and transformation
- Python
- Pandas
- SQL
- SQLite
- Data quality validation
- Historical data analysis
- Power BI dashboard development
- Building an end-to-end analytics pipeline

---

## 👤 Author

**Nihar Nandanwar**

MSc Computer Science — University of Liverpool

**Interests:** Data Analytics • Business Intelligence • Python • SQL • Power BI • Data Visualisation • Machine Learning

## 📄 License

This project is licensed under the [MIT License](LICENSE).
