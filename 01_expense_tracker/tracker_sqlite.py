#!/usr/bin/env python3
"""
tracker_sqlite.py
A simple interactive expense tracker using SQLite with monthly graph reporting.
"""

import sqlite3
from datetime import datetime, date
import os
import csv

# Try to import matplotlib but keep program usable without it
try:
    import matplotlib.pyplot as plt
    HAS_MPL = True
except Exception:
    HAS_MPL = False

DB_FILENAME = "expenses.db"
DATE_FORMAT = "%Y-%m-%d"

def get_connection(db_path: str = DB_FILENAME) -> sqlite3.Connection:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def init_db(conn: sqlite3.Connection) -> None:
    cur = conn.cursor()
    cur.executescript(
        """
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            category TEXT NOT NULL,
            amount REAL NOT NULL,
            description TEXT
        );
        """
    )
    conn.commit()

def add_expense(conn, date_str, category, amount, description):
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO expenses (date, category, amount, description) VALUES (?, ?, ?, ?)",
        (date_str, category, amount, description),
    )
    conn.commit()

def parse_date(input_str: str) -> str:
    input_str = input_str.strip()
    if not input_str:
        return date.today().strftime(DATE_FORMAT)
    for fmt in (DATE_FORMAT, "%d-%m-%Y", "%d/%m/%Y", "%Y/%m/%d"):
        try:
            dt = datetime.strptime(input_str, fmt)
            return dt.strftime(DATE_FORMAT)
        except Exception:
            continue
    raise ValueError("Invalid date format! Use YYYY-MM-DD or DD-MM-YYYY")

def list_expenses(conn, limit: int = 100):
    cur = conn.cursor()
    cur.execute("SELECT * FROM expenses ORDER BY date DESC, id DESC LIMIT ?", (limit,))
    return cur.fetchall()

def monthly_summary(conn):
    cur = conn.cursor()
    cur.execute(
        "SELECT substr(date,1,7) as month, SUM(amount) as total FROM expenses GROUP BY month ORDER BY month"
    )
    return {row["month"]: float(row["total"] or 0.0) for row in cur.fetchall()}

def export_csv(conn, filename="expenses_export.csv"):
    cur = conn.cursor()
    cur.execute("SELECT * FROM expenses ORDER BY date DESC")
    rows = cur.fetchall()
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "date", "category", "amount", "description"])
        for r in rows:
            writer.writerow([r["id"], r["date"], r["category"], r["amount"], r["description"]])
    return os.path.abspath(filename)

def print_table(rows):
    if not rows:
        print("(no records)")
        return
    header = f"{'id':>4}  {'date':10}  {'category':12}  {'amount':10}  {'description':30}"
    print(header)
    print("-" * len(header))
    for r in rows:
        desc = (r["description"] or "")
        if len(desc) > 30:
            desc = desc[:27] + "..."
        print(f"{r['id']:>4}  {r['date']:10}  {r['category'][:12]:12}  {r['amount']:10.2f}  {desc:30}")

def show_monthly_graph(conn):
    summary = monthly_summary(conn)
    if not summary:
        print("No data to plot.")
        return
    if not HAS_MPL:
        print("matplotlib not installed. Run: pip install matplotlib")
        return
    months = list(summary.keys())
    totals = [summary[m] for m in months]
    plt.figure(figsize=(8, 4))
    plt.bar(months, totals)
    plt.xticks(rotation=45, ha="right")
    plt.ylabel("Total spent")
    plt.title("Monthly expenses")
    plt.tight_layout()
    plt.savefig("monthly_expenses.png")
        print("Graph saved as monthly_expenses.png")

def main_menu(conn):
    while True:
        print("\nExpense Tracker - Menu")
        print("1) Add expense")
        print("2) View recent expenses")
        print("3) Monthly summary (table)")
        print("4) Show monthly graph")
        print("5) Export CSV")
        print("0) Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            try:
                date_str = parse_date(input("Date (YYYY-MM-DD, blank=today): "))
                category = input("Category: ").strip() or "Other"
                amount = float(input("Amount: "))
                description = input("Description: ").strip()
                add_expense(conn, date_str, category, amount, description)
                print("Added.")
            except Exception as e:
                print("Error:", e)
        elif choice == "2":
            rows = list_expenses(conn)
            print_table(rows)
        elif choice == "3":
            summ = monthly_summary(conn)
            if not summ:
                print("No data.")
            else:
                for m, t in summ.items():
                    print(f"{m}\t{t:.2f}")
        elif choice == "4":
            show_monthly_graph(conn)
        elif choice == "5":
            path = export_csv(conn)
            print("Exported to:", path)
        elif choice == "0":
            break
        else:
            print("Invalid choice.")

def ensure_db():
    conn = get_connection()
    init_db(conn)
    return conn

if __name__ == "__main__":
    conn = ensure_db()
    try:
        main_menu(conn)
    finally:
        conn.close()
