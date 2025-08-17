import csv
import os
from datetime import datetime
from prettytable import PrettyTable
import matplotlib.pyplot as plt
from collections import defaultdict

FILE = "data/expenses.csv"
CATEGORIES = ["Food", "Travel", "Bills", "Entertainment", "Education", "Misc", "Income"]

def init_file():
    """Create file with headers if not exists"""
    if not os.path.exists(FILE):
        os.makedirs(os.path.dirname(FILE), exist_ok=True)
        with open(FILE, mode="w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Category", "Amount", "Description"])

def add_transaction(category, amount, description=""):
    """Add a new income/expense transaction"""
    if category not in CATEGORIES:
        raise ValueError(f"Category must be one of {CATEGORIES}")

    with open(FILE, mode="a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M"),
                         category, amount, description])
    print("✅ Transaction added successfully!")

def get_current_balance():
    """Calculate current balance by summing all transactions"""
    balance = 0
    if not os.path.exists(FILE):
        return balance
    with open(FILE, mode="r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            amount = float(row["Amount"])
            if row["Category"] == "Income":
                balance += amount
            else:
                balance -= amount
    return balance

def show_transactions(limit=10):
    """Show last few transactions in table format"""
    table = PrettyTable(["Date", "Category", "Amount", "Description"])
    if not os.path.exists(FILE):
        print("No transactions to display.")
        return

    with open(FILE, mode="r") as f:
        rows = list(csv.reader(f))
        if len(rows) <= 1:
            print("No transactions to display.")
            return
        
        for row in rows[-limit:]:
            if row[0] != "Date":  # skip header
                table.add_row(row[:4]) # Only add relevant columns

    print(table)
    print(f"💰 Current Balance: ₹{get_current_balance()}")

def summary():
    """Show category-wise expense summary"""
    totals = defaultdict(float)
    if not os.path.exists(FILE):
        print("No transactions to display.")
        return

    with open(FILE, mode="r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            cat = row["Category"]
            amt = float(row["Amount"])
            totals[cat] += amt

    print("\n📊 Expense Summary:")
    for cat, total in sorted(totals.items()):
        if cat != "Income":
            print(f"{cat:15} : ₹{total}")
    print(f"💰 Current Balance: ₹{get_current_balance()}")

def monthly_report():
    """Generate a monthly bar chart of expenses"""
    if not os.path.exists(FILE):
        print("No transactions to display.")
        return

    monthly_data = defaultdict(lambda: defaultdict(float))
    with open(FILE, mode="r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                date = datetime.strptime(row["Date"], "%Y-%m-%d %H:%M")
                month = date.strftime("%Y-%m")
                cat = row["Category"]
                amt = float(row["Amount"])
                if cat != "Income":
                    monthly_data[month][cat] += amt
            except (ValueError, KeyError) as e:
                print(f"Skipping malformed row: {row}. Error: {e}")
                continue

    if not monthly_data:
        print("No expense data to generate a report.")
        return

    for month, cats in sorted(monthly_data.items()):
        categories = list(cats.keys())
        amounts = list(cats.values())

        plt.figure(figsize=(10, 6))
        plt.bar(categories, amounts, color='skyblue')
        plt.title(f"Monthly Expense Report - {month}", fontsize=16)
        plt.xlabel("Category", fontsize=12)
        plt.ylabel("Amount (₹)", fontsize=12)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()

# -------------------------------
# Example usage
# -------------------------------
if __name__ == "__main__":
    init_file()

    while True:
        print("\n--- Expense Tracker Menu ---")
        print("1. Add Transaction")
        print("2. Show Recent Transactions")
        print("3. Show Summary")
        print("4. Show Monthly Graph Report")
        print("5. Exit")

        choice = input("Choose option: ")

        try:
            if choice == "1":
                cat = input(f"Category {CATEGORIES}: ").strip().capitalize()
                amt_str = input("Amount: ")
                desc = input("Description: ").strip()
                if not amt_str:
                    print("Amount cannot be empty.")
                    continue
                amt = float(amt_str)
                add_transaction(cat, amt, desc)
            elif choice == "2":
                show_transactions()
            elif choice == "3":
                summary()
            elif choice == "4":
                monthly_report()
            elif choice == "5":
                print("Exiting Expense Tracker. Goodbye!")
                break
            else:
                print("❌ Invalid choice")
        except ValueError as e:
            print(f"❌ Error: {e}. Please enter valid data.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


