import requests
from bs4 import BeautifulSoup
import csv # Will use this later for CSV output

# 1. Define the URL of the target website
URL = "http://quotes.toscrape.com"

# 2. Send a GET request to the URL
try:
    response = requests.get(URL)
    response.raise_for_status() # Raise an HTTPError for bad responses (4xx or 5xx)
    print("Successfully fetched the page!")
    # print(response.text[:500]) # Print first 500 characters of the page content (for debugging)

    # 3. Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    print("Successfully parsed the HTML!")

    # Now, we'll add code here later to extract quotes and authors

except requests.exceptions.RequestException as e:
    print(f"Error fetching the page: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


