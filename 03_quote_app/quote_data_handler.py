import json
import argparse

# Setup command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("--file", default="quotes.json", help="JSON file to load")
parser.add_argument("--filter", help="Filter quotes containing keyword")
args = parser.parse_args()

# Load data from the given file
with open(args.file, "r") as f:
    data = json.load(f)

# Filter and print quotes
for q in data["quotes"]:
    if args.filter:
        if args.filter.lower() in q["quote"].lower():
            print(f"{q['quote']} - {q['author']}")
    else:
        print(f"{q['quote']} - {q['author']}")

# Optional: save all quotes to another file (make sure `all_quotes` is defined if used)
with open("quotes_100.json", "w") as f:
   json.dump(data, f, indent=4)





