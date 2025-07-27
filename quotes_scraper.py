import requests
from bs4 import BeautifulSoup
import json

# Target website
BASE_URL = "http://quotes.toscrape.com"

def scrape_quotes(min_count=100):
    quotes = []
    page = 1

    while len(quotes) < min_count:
        print(f"Scraping page {page}...")
        res = requests.get(f"{BASE_URL}/page/{page}")
        if res.status_code != 200:
            print(f"Failed to fetch page {page}")
            break

        soup = BeautifulSoup(res.text, "html.parser")
        quote_blocks = soup.find_all("div", class_="quote")

        if not quote_blocks:
            print("No more quotes found.")
            break

        for block in quote_blocks:
            text = block.find("span", class_="text").get_text(strip=True)
            author = block.find("small", class_="author").get_text(strip=True)
            quotes.append({
                "quote": text,
                "author": author
            })
            if len(quotes) >= min_count:
                break

        page += 1

    return quotes

def save_to_json(quotes, filename="quotes_100.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump({"quotes": quotes}, f, indent=4, ensure_ascii=False)
    print(f"\n✅ Saved {len(quotes)} quotes to '{filename}'")

if __name__ == "__main__":
    all_quotes = scrape_quotes(min_count=100)
    save_to_json(all_quotes)
