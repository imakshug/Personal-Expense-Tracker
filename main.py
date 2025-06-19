import csv
import os
from datetime import datetime
from collections import defaultdict

CSV_FILE = 'expenses.csv'

# Initialize the CSV file if it doesn't exist
def initialize_file():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])

# Add a new expense
def add_expense():
    date = input("Enter date (YYYY-MM-DD) [Leave blank for today]: ").strip()
    if not date:
        date = datetime.today().strftime('%Y-%m-%d')

    category = input("Enter category (e.g., Food, Transport): ").strip()
    amount = input("Enter amount: ").strip()
    description = input("Enter description: ").strip()

    try:
        float(amount)  # Validate amount
        datetime.strptime(date, '%Y-%m-%d')  # Validate date format
    except ValueError:
        print("Invalid date or amount format.")
        return

    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])

    print("✅ Expense added successfully.")

# View all expenses
def view_expenses():
    print("\n--- All Expenses ---")
    try:
        with open(CSV_FILE, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(', '.join(row))
    except FileNotFoundError:
        print("No expense records found.")

# Filter expenses by category or date range
def filter_expenses():
    print("\n--- Filter Expenses ---")
    print("1. By Category")
    print("2. By Date Range")
    choice = input("Choose filter type (1-2): ").strip()

    if choice == '1':
        category = input("Enter category to filter: ").strip().lower()
        with open(CSV_FILE, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            found = False
            for row in reader:
                if row[1].strip().lower() == category:
                    print(', '.join(row))
                    found = True
            if not found:
                print("No matching records found.")

    elif choice == '2':
        start = input("Start date (YYYY-MM-DD): ").strip()
        end = input("End date (YYYY-MM-DD): ").strip()
        try:
            start_date = datetime.strptime(start, '%Y-%m-%d')
            end_date = datetime.strptime(end, '%Y-%m-%d')
        except ValueError:
            print("Invalid date format.")
            return

        with open(CSV_FILE, mode='r') as file:
            reader = csv.reader(file)
            next(reader)
            found = False
            for row in reader:
                try:
                    expense_date = datetime.strptime(row[0], '%Y-%m-%d')
                    if start_date <= expense_date <= end_date:
                        print(', '.join(row))
                        found = True
                except ValueError:
                    continue
            if not found:
                print("No matching records found.")
    else:
        print("Invalid choice.")

# Calculate and show total spending
def show_total_spending():
    total = 0.0
    try:
        with open(CSV_FILE, mode='r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                try:
                    total += float(row[2])
                except (ValueError, IndexError):
                    continue
        print(f"\n💰 Total Spending: ${total:.2f}")
    except FileNotFoundError:
        print("No data available.")

# Show monthly spending report
def monthly_report():
    report = defaultdict(float)
    try:
        with open(CSV_FILE, mode='r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                try:
                    date = datetime.strptime(row[0], '%Y-%m-%d')
                    amount = float(row[2])
                    key = date.strftime('%Y-%m')  # e.g., 2025-06
                    report[key] += amount
                except (ValueError, IndexError):
                    continue

        print("\n📅 Monthly Report:")
        if report:
            for month, total in sorted(report.items()):
                print(f"{month}: ${total:.2f}")
        else:
            print("No data to report.")
    except FileNotFoundError:
        print("No data available.")

# Main menu loop
def main_menu():
    while True:
        print("\n=== Personal Expense Tracker ===")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Filter Expenses")
        print("4. Show Total Spending")
        print("5. Monthly Report")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            filter_expenses()
        elif choice == '4':
            show_total_spending()
        elif choice == '5':
            monthly_report()
        elif choice == '6':
            print("👋 Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    initialize_file()
    main_menu()
