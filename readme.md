# 💸 Personal Expense Tracker (Web App)
## Visit- https://personal-expense-tracker-y2zt.onrender.com/

A beginner-friendly Flask + HTML/CSS project to track personal spending. Easily add, view, filter, and delete your expenses — all stored in a CSV file. Great for learning about:

- Backend (Flask API)
  
- Frontend (HTML/CSS + JS)
  
- File I/O in Python
  
- Fetch API usage

---
## ✨ Features

- ➕ **Add Expense**: Record your purchases with date, category, amount, and description.
  
- 🔍 **Filter Expenses**: Search your entries by category or date range.
  
- 📂 **Apply Filter**: Instantly view only the data you need.
  
- 📋 **All Expenses**: Sorted neatly by date for easy tracking.
  
- 🌓 **Dark & Light Mode**: Stylish day/night themes for any vibe.
  
- 🎨 **Modern UI/UX**: Elegant fonts, responsive layout, and a chic colour palette.

---

## 📦 Project Structure

```bash
expense-tracker/
├── app.py                  # Main Flask app
├── expenses.csv            # Data storage
├── requirements.txt        # Dependencies
├── static/
│   └── style.css           # Light/Dark themed CSS
├── templates/
│   └── index.html          # Main UI
└── README.md               # You're reading this :)
```

---

## Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/expense-tracker.git
cd expense-tracker
```

### 2. Install Dependencies

```bash
python pip install flask
```
### 3. Run the App

```bash
python app.py
```
App will start at http://127.0.0.1:5000

## 📸 UI
<img src="https://github.com/user-attachments/assets/502acb9c-9933-41b0-aaf5-1067be356ea2" alt="App Snapshot" width="500" height="400" /> <img src="https://github.com/user-attachments/assets/85aa3505-592c-49c6-a9e1-ed058ac08482" alt="App Snapshot" width="500" height="400" /> 


## 🖥️ How It Works
### ➕ Add Expense
Fill out the form and click "Add Expense" — the entry is saved to expenses.csv.

### 📋 View Table
All expenses are displayed in a table, updated in real-time via a JavaScript and Flask API.

### 🔍 Filter
Enter a category, date range, or both, and hit "Apply Filter" to narrow down the results.

### 🗑️ Delete
Each row includes a "Delete" button to remove specific entries.

## 📌 Notes
- 💾 Your data is saved in expenses.csv locally.

- 🛑 No authentication — keep this for personal or learning use.

- 🧠 Designed for educational purposes and simplicity.



