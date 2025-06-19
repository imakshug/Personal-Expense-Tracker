# 💸 Personal Expense Tracker (Web App)

A beginner-friendly Flask + HTML/CSS project to track personal spending. Easily add, view, filter, and delete your expenses — all stored in a CSV file. Great for learning about:

- Backend (Flask API)
  
- Frontend (HTML/CSS + JS)
  
- File I/O in Python
  
- Fetch API usage

---

## ✨ Features

- ✅ Add new expenses (Date, Category, Amount, Description)
  
- 📂 View all expenses in a table
  
- 🔍 Filter by category and/or date range
  
- 💸 Currency displayed in Rs format
  
- 🗑️ Delete any entry from the table
  
- 💾 CSV file auto-managed in the backend (expenses.csv)



---

## 📦 Project Files

```bash
├── main.py            
├── app.py               # Flask backend
├── expenses.csv         # CSV log file (auto-created)
├── templates/
│   └── index.html       # Main HTML frontend
├── static/
│   └── style.css        # Custom styles
└── README.md            # Project documentation
```

---

## Getting Started

### 1. Install Dependencies

```bash
python pip install flask
```
### 2. Run the App

```bash
python app.py
```
App will start at http://127.0.0.1:5000

## 🖥️ How It Works
### ➕ Add Expense
Fill out the form and click "Add Expense" — the entry is saved to expenses.csv.

### 📋 View Table
All expenses are shown in a table, updated live via JavaScript and Flask API.

### 🔍 Filter
Enter a category, date range, or both — and hit "Apply Filter" to narrow down the results.

### 🗑️ Delete
Each row includes a "Delete" button to remove specific entries.

## 📌 Notes
- 💾 Your data is saved in expenses.csv locally.

- 🛑 No authentication — keep this for personal or learning use.

- 🧠 Designed for educational purposes and simplicity.

## 📷 Screenshot
