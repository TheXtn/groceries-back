
import sqlite3

DB_FILE = "products.db"

def get_connection():
    return sqlite3.connect(DB_FILE)
def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      name TEXT NOT NULL,
                      weight REAL,
                      quantity INTEGER,
                      price REAL,
                      category TEXT
                   )''')
    conn.commit()