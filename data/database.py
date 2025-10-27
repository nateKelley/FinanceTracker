import sqlite3
import os

# path to database file
DB_PATH = os.path.join(os.path.dirname(__file__), "finance.db")

def init_db():
    """create the expenses table if it doesn't exist"""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT NOT NULL,
            amount REAL NOT NULL,
            date TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def add_expense(category, amount, date):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("INSERT INTO expenses (category, amount, date) VALUES (?, ?, ?)",
                (category, amount, date))
    conn.commit()
    conn.close()

def get_expenses():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT * FROM expenses ORDER BY date DESC")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete_expense(expense_id):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    conn.commit()
    conn.close()

def update_expense(expense_id, category, amount, date):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        "UPDATE expenses SET category = ?, amount = ?, date = ? WHERE id = ?",
        (category, amount, date, expense_id)
    )
    conn.commit()
    conn.close()


