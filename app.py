from flask import Flask, render_template, request, jsonify
import csv
import os

app = Flask(__name__)

CSV_FILE = 'expenses.csv'

if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Date', 'Category', 'Amount', 'Description'])


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add', methods=['POST'])
def add_expense():
    data = request.json
    with open(CSV_FILE, mode='a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([data['date'], data['category'], data['amount'], data['description']])
    return jsonify({'message': 'Expense added successfully'}), 200


@app.route('/expenses', methods=['GET'])
def get_expenses():
    expenses = []
    with open(CSV_FILE, mode='r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            expenses.append({
                "date": row["Date"],
                "category": row["Category"],
                "amount": row["Amount"],
                "description": row["Description"]
            })
    return jsonify(expenses), 200
@app.route('/filter', methods=['GET'])
def filter_expenses():
    category = request.args.get('category')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    filtered_expenses = []
    with open(CSV_FILE, mode='r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if (not category or row['Category'].lower() == category.lower()) and \
            (not start_date or row['Date'] >= start_date) and \
            (not end_date or row['Date'] <= end_date):

                filtered_expenses.append(row)

    return jsonify(filtered_expenses), 200


@app.route('/delete', methods=['POST'])
def delete_expense():
    data = request.json
    date = data['date']
    category = data['category']
    amount = data['amount']
    description = data['description']

    expenses = []
    with open(CSV_FILE, mode='r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if not (row['Date'] == date and row['Category'] == category and
                    row['Amount'] == amount and row['Description'] == description):
                expenses.append(row)

    with open(CSV_FILE, mode='w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['Date', 'Category', 'Amount', 'Description'])
        writer.writeheader()
        writer.writerows(expenses)

    return jsonify({'message': 'Expense deleted successfully'}), 200
@app.route('/summary', methods=['GET'])
def summary():
    total_expenses = 0
    category_totals = {}

    with open(CSV_FILE, mode='r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            amount = float(row['Amount'])
            total_expenses += amount
            category = row['Category']
            if category in category_totals:
                category_totals[category] += amount
            else:
                category_totals[category] = amount

    return jsonify({
        'total_expenses': total_expenses,
        'category_totals': category_totals
    }), 200
if __name__ == '__main__':
    app.run(debug=True)
#     except ValueError:
#         print("Invalid date or amount format.")
#         print("Invalid date or amount format.")
#         return
