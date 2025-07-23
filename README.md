# Python Mini-Projects Collection

A collection of small, practical Python projects focusing on various applications like web scraping, data automation, and problem-solving. This repository serves as a showcase of my learning journey and practical skill development in Python.

---

## Project 1: Simple Quotes Web Scraper

**Description:**
This project demonstrates basic web scraping capabilities using Python. It will connect to a target website, extract specific textual content (quotes and their authors), and save the collected data into a structured CSV file.

**Problem Solved:**
Automating the collection of specific data from publicly accessible web pages for analysis, archival, or use in other applications.

**Features:**
* Fetches HTML content from `quotes.toscrape.com`.
* Parses the HTML to identify and extract quotes and their corresponding authors.
* Stores the extracted data in a list of dictionaries.
* Exports the collected quotes and authors into a clean CSV file (`quotes.csv`).

**Technologies Used:**
* Python 3.x
* `requests` library (for making HTTP requests)
* `BeautifulSoup4` library (for HTML parsing)
* `csv` module (for CSV file handling)

**How to Run:**
1. Clone this repository: `git clone https://github.com/jit0341/python-mini-projects.git`
2. Navigate to the project directory: `cd python-mini-projects`
3. Install the required libraries: `pip install requests beautifulsoup4`
4. Run the script: `python quotes_scraper.py` (once you create the file)

**Future Enhancements (Planned):**
* Implement pagination to scrape multiple pages.
* Add error handling for network issues or malformed HTML.
* Scrape additional information (e.g., tags for each quote).

---

*(More projects will be added here as I develop them.)*
