import json
import random

# Load quotes from JSON file
with open("quotes_100.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    quotes = data.get("quotes", [])

# Function to show a random quote
def show_random_quote():
    quote = random.choice(quotes)
    print(f"\n📝 \"{quote['quote']}\" — {quote['author']}\n")

# Function to show all quotes by a specific author
def show_quotes_by_author():
    name = input("Enter author's name: ").lower()
    found = False
    for q in quotes:
        if q['author'].lower() == name:
            print(f"\n📚 \"{q['quote']}\"")
            found = True
    if not found:
        print("\n❌ No quotes found for that author.\n")

# Function to search quotes by a keyword
def search_by_keyword():
    keyword = input("Enter a keyword: ").lower()
    results = [q for q in quotes if keyword in q['quote'].lower()]
    if results:
        for q in results:
            print(f"\n🔎 \"{q['quote']}\" — {q['author']}")
    else:
        print("\n❌ No quotes matched that keyword.\n")

# Function to show a motivational quote (basic filter)
def show_motivational_quote():
    keywords = ["success", "life", "motivation", "inspire", "dream", "future", "goal"]
    filtered = [q for q in quotes if any(k in q['quote'].lower() for k in keywords)]
    if filtered:
        q = random.choice(filtered)
        print(f"\n💡 \"{q['quote']}\" — {q['author']}\n")
    else:
        print("\n❌ No motivational quotes found.\n")

# Menu loop
def run():
    while True:
        print("\n📘 Quote CLI App")
        print("1. Show random quote")
        print("2. Show all quotes by author")
        print("3. Search quotes by keyword")
        print("4. Show a motivational quote")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            show_random_quote()
        elif choice == "2":
            show_quotes_by_author()
        elif choice == "3":
            search_by_keyword()
        elif choice == "4":
            show_motivational_quote()
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("❗Invalid choice. Try again.")

if __name__ == "__main__":
    run()
