import json
import random

# Load quotes from file (same directory)
with open("quotes_100.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    quotes = data.get("quotes", [])

# Pick a random quote
quote = random.choice(quotes)

# Print quote nicely
print("\n★ Quote of the Day ★\n")
print(f'"{quote["quote"]}"')
print(f"\n— {quote['author']}")
