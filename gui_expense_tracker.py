import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import csv
import os
from collections import defaultdict

CSV_FILE = 'expenses.csv'

# Ensure CSV file exists
def init_file():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Category", "Amount", "Description"])

def save_expense(date, category, amount, description):
    with open(CSV_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([date, category, amount, description])

def read_expenses():
    with open(CSV_FILE, 'r') as f:
        return list(csv.reader(f))[1:]

class ExpenseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Expense Tracker")

        self.tab_control = ttk.Notebook(root)

        self.add_tab = ttk.Frame(self.tab_control)
        self.view_tab = ttk.Frame(self.tab_control)
        self.summary_tab = ttk.Frame(self.tab_control)

        self.tab_control.add(self.add_tab, text='Add Expense')
        self.tab_control.add(self.view_tab, text='View Expenses')
        self.tab_control.add(self.summary_tab, text='Reports')

        self.tab_control.pack(expand=1, fill='both')

        self.build_add_tab()
        self.build_view_tab()
        self.build_summary_tab()

    def build_add_tab(self):
        ttk.Label(self.add_tab, text="Date (YYYY-MM-DD):").grid(row=0, column=0, pady=5, sticky='e')
        self.date_entry = ttk.Entry(self.add_tab)
        self.date_entry.grid(row=0, column=1)
        self.date_entry.insert(0, datetime.today().strftime('%Y-%m-%d'))

        ttk.Label(self.add_tab, text="Category:").grid(row=1, column=0, pady=5, sticky='e')
        self.category_entry = ttk.Entry(self.add_tab)
        self.category_entry.grid(row=1, column=1)

        ttk.Label(self.add_tab, text="Amount:").grid(row=2, column=0, pady=5, sticky='e')
        self.amount_entry = ttk.Entry(self.add_tab)
        self.amount_entry.grid(row=2, column=1)

        ttk.Label(self.add_tab, text="Description:").grid(row=3, column=0, pady=5, sticky='e')
        self.desc_entry = ttk.Entry(self.add_tab)
        self.desc_entry.grid(row=3, column=1)

        add_button = ttk.Button(self.add_tab, text="Add Expense", command=self.add_expense)
        add_button.grid(row=4, column=0, columnspan=2, pady=10)

    def add_expense(self):
        date = self.date_entry.get()
        category = self.category_entry.get()
        amount = self.amount_entry.get()
        description = self.desc_entry.get()

        try:
            float(amount)
            datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            messagebox.showerror("Error", "Invalid date or amount")
            return

        save_expense(date, category, amount, description)
        messagebox.showinfo("Saved", "Expense added!")

        self.category_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)

    def build_view_tab(self):
        self.tree = ttk.Treeview(self.view_tab, columns=("Date", "Category", "Amount", "Description"), show='headings')
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
        self.tree.pack(fill='both', expand=True)

        refresh_btn = ttk.Button(self.view_tab, text="Refresh", command=self.load_expenses)
        refresh_btn.pack(pady=5)

    def load_expenses(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for expense in read_expenses():
            self.tree.insert('', tk.END, values=expense)

    def build_summary_tab(self):
        ttk.Label(self.summary_tab, text="Filter by Category:").grid(row=0, column=0)
        self.filter_category = ttk.Entry(self.summary_tab)
        self.filter_category.grid(row=0, column=1)
        ttk.Button(self.summary_tab, text="Filter", command=self.filter_by_category).grid(row=0, column=2, padx=5)

        ttk.Label(self.summary_tab, text="Date Range (YYYY-MM-DD):").grid(row=1, column=0, columnspan=3, pady=5)
        self.start_entry = ttk.Entry(self.summary_tab)
        self.end_entry = ttk.Entry(self.summary_tab)
        self.start_entry.grid(row=2, column=0)
        self.end_entry.grid(row=2, column=1)
        ttk.Button(self.summary_tab, text="Filter by Date", command=self.filter_by_date).grid(row=2, column=2, padx=5)

        ttk.Button(self.summary_tab, text="Total Spending", command=self.show_total).grid(row=3, column=0, columnspan=3, pady=5)
        ttk.Button(self.summary_tab, text="Monthly Report", command=self.monthly_report).grid(row=4, column=0, columnspan=3, pady=5)

        self.result_box = tk.Text(self.summary_tab, height=15, width=60)
        self.result_box.grid(row=5, column=0, columnspan=3, padx=5, pady=5)

    def filter_by_category(self):
        category = self.filter_category.get().strip().lower()
        result = []
        for row in read_expenses():
            if row[1].strip().lower() == category:
                result.append(', '.join(row))
        self.show_result(result)

    def filter_by_date(self):
        start = self.start_entry.get()
        end = self.end_entry.get()
        result = []
        try:
            start_date = datetime.strptime(start, '%Y-%m-%d')
            end_date = datetime.strptime(end, '%Y-%m-%d')
        except ValueError:
            messagebox.showerror("Error", "Invalid date format")
            return
        for row in read_expenses():
            try:
                expense_date = datetime.strptime(row[0], '%Y-%m-%d')
                if start_date <= expense_date <= end_date:
                    result.append(', '.join(row))
            except ValueError:
                continue
        self.show_result(result)

    def show_total(self):
        total = 0.0
        for row in read_expenses():
            try:
                total += float(row[2])
            except ValueError:
                continue
        self.result_box.delete(1.0, tk.END)
        self.result_box.insert(tk.END, f"Total Spending: ${total:.2f}")

    def monthly_report(self):
        report = defaultdict(float)
        for row in read_expenses():
            try:
                date = datetime.strptime(row[0], '%Y-%m-%d')
                amount = float(row[2])
                key = date.strftime('%Y-%m')
                report[key] += amount
            except ValueError:
                continue
        lines = [f"{month}: ${total:.2f}" for month, total in sorted(report.items())]
        self.show_result(lines)

    def show_result(self, lines):
        self.result_box.delete(1.0, tk.END)
        if not lines:
            self.result_box.insert(tk.END, "No matching records found.")
        else:
            for line in lines:
                self.result_box.insert(tk.END, line + "\n")

if __name__ == '__main__':
    init_file()
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop()
