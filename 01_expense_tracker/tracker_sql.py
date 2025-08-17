import csv
import os
import matplotlib.pyplot as plt

CSV_FILE = "expenses.csv"

# Ensure CSV exists
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "Category", "Amount", "Description"])

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    with open(CSV_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([date, category, amount, description])
    print("✅ Expense added successfully!")

def view_expenses():
    with open(CSV_FILE, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

def show_summary():
    total = 0
    with open(CSV_FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            total += float(row["Amount"])
    print(f"💰 Total Expenses: {total}")

def show_graph():
    dates, amounts = [], []
    with open(CSV_FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            dates.append(row["Date"])
            amounts.append(float(row["Amount"]))

    plt.plot(dates, amounts, marker="o")
    plt.xticks(rotation=45)
    plt.title("Expenses Over Time")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.tight_layout()
    plt.show()

def menu():
    while True:
        print("\n==== Expense Tracker Menu ====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Summary")
        print("4. Show Graph")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            show_summary()
        elif choice == "4":
            show_graph()
        elif choice == "5":
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
