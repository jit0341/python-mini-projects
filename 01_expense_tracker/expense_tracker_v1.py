#!/usr/bin/env python3
"""
Expense Tracker v1 (CLI)
- Add expenses (date, category, amount, description)
- View all expenses
- Data saved to CSV: data/expenses.csv
"""

from pathlib import Path
from datetime import datetime
import csv
import sys

# ---------- Paths & constants ----------
ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"
CSV_FILE = DATA_DIR / "expenses.csv"
HEADERS = ["date", "category", "amount", "description"]

DEFAULT_CATEGORIES = [
    "Food", "Travel", "Groceries", "Shopping", "Bills", "Health",
    "Education", "Entertainment", "Utilities", "Other"
]

# ---------- Setup ----------
def ensure_store():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    if not CSV_FILE.exists():
        with CSV_FILE.open("w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(HEADERS)

# ---------- Helpers ----------
def parse_date(s: str) -> str:
    """Return YYYY-MM-DD; if blank -> today; if invalid -> raise ValueError."""
    if not s.strip():
        return datetime.today().strftime("%Y-%m-%d")
    try:
        dt = datetime.strptime(s.strip(), "%Y-%m-%d")
        return dt.strftime("%Y-%m-%d")
    except ValueError:
        raise ValueError("Date must be in YYYY-MM-DD format.")

def parse_amount(s: str) -> float:
    try:
        amt = float(s.strip())
        if amt <= 0:
            raise ValueError
        return round(amt, 2)
    except Exception:
        raise ValueError("Amount must be a positive number.")

def title_case(s: str) -> str:
    return s.strip().title()

# ---------- Core features ----------
def add_expense():
    print("\nAdd a new expense:")
    date = input("Date (YYYY-MM-DD, blank = today): ")
    try:
        date = parse_date(date)
    except ValueError as e:
        print(f"✖ {e}")
        return

    print("\nCategories:", ", ".join(DEFAULT_CATEGORIES))
    category = input("Category (free text allowed): ")
    category = title_case(category) or "Other"

    amount = input("Amount: ")
    try:
        amount = parse_amount(amount)
    except ValueError as e:
        print(f"✖ {e}")
        return

    description = input("Description (optional): ").strip()

    with CSV_FILE.open("a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([date, category, amount, description])

    print("✅ Expense added!")

def read_rows():
    if not CSV_FILE.exists():
        return []
    with CSV_FILE.open("r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)

def view_expenses():
    rows = read_rows()
    if not rows:
        print("\n(no expenses yet)\n")
        return

    # compute column widths
    def w(key, minw):
        return max(minw, max(len(str(r[key])) for r in rows + [dict(zip(HEADERS, HEADERS))]))  # include header

    w_date = w("date", 10)
    w_cat = w("category", 10)
    w_amt = max(8, len("amount"))
    w_desc = max(12, len("description"))

    # header
    print()
    print(f"{'date':<{w_date}}  {'category':<{w_cat}}  {'amount':>{w_amt}}  {'description':<{w_desc}}")
    print("-" * (w_date + w_cat + w_amt + w_desc + 6))

    total = 0.0
    for r in rows:
        amt = float(r["amount"])
        total += amt
        print(f"{r['date']:<{w_date}}  {r['category']:<{w_cat}}  {amt:>{w_amt}.2f}  {r['description']:<{w_desc}}")

    print("-" * (w_date + w_cat + w_amt + w_desc + 6))
    print(f"{'TOTAL':<{w_date + w_cat + 2}}  {total:>{w_amt}.2f}\n")

# ---------- Menu ----------
def menu():
    print("\n==== Expense Tracker v1 ====")
    print("1) Add expense")
    print("2) View expenses")
    print("3) Exit")
    return input("Choose: ").strip()

def main():
    ensure_store()
    while True:
        choice = menu()
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Bye!")
            sys.exit(0)
        else:
            print("Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
