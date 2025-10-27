from flask import Flask, render_template, request, redirect
from data.database import add_expense, get_expenses, delete_expense, update_expense

app = Flask(__name__)

@app.route("/")
def index():
    expenses = get_expenses()
    return render_template("index.html", expenses=expenses)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        category = request.form["category"]
        amount = request.form["amount"]
        date = request.form["date"]

        add_expense(category, amount, date)
        return redirect("/")
    return render_template("add_expense.html")

@app.route("/delete/<int:expense_id>")
def delete(expense_id):
    delete_expense(expense_id)
    return redirect("/")

@app.route("/edit/<int:expense_id>", methods=["GET", "POST"])
def edit(expense_id):
    if request.method == "POST":
        category = request.form["category"]
        amount = request.form["amount"]
        date = request.form["date"]
        update_expense(expense_id, category, amount, date)
        return redirect("/")
    expenses = get_expenses()
    expense = next((e for e in expenses if e[0] == expense_id), None)
    return render_template("edit_expense.html", expense=expense)

if __name__ == "__main__":
    app.run(debug=True)
