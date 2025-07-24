import requests
from bs4 import BeautifulSoup
import csv  # For saving data to CSV

# 1. Define the URL of the target website
URL = "http://quotes.toscrape.com"

# 2. Send a GET request to the URL
try:
    response = requests.get(URL)
    response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
    print("Successfully fetched the page!")

    # 3. Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    print("Successfully parsed the HTML!")

    # 4. Extract quotes
    quotes_data = []  # list to hold all quote data

    quotes = soup.find_all("div", class_="quote")

    for quote in quotes:
        text = quote.find("span", class_="text").text.strip()
        author = quote.find("small", class_="author").text.strip()
        tags = [tag.text.strip() for tag in quote.find_all("a", class_="tag")]

        quotes_data.append([text, author, ", ".join(tags)])
        print(f"\nQuote: {text}\nAuthor: {author}\nTags: {', '.join(tags)}")

except requests.exceptions.RequestException as e:
    print(f"Error fetching the page: {e}")
    quotes_data = []  # Ensure this variable exists even if error occurs
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    quotes_data = []

# 5. Save to CSV (only if data was extracted)
if quotes_data:
    with open("quotes.tsv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f,quoting= csv.QUOTE_ALL)
        writer.writerow(["Quote", "Author", "Tags"])
        writer.writerows(quotes_data)

    print("\nQuotes saved to quotes.csv")
else:
    print("No data to save.")
