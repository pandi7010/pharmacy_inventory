from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Initialize DB
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS inventory (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    quantity INTEGER NOT NULL,
                    price REAL NOT NULL
                )''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM inventory")
    items = c.fetchall()
    conn.close()
    return render_template('index.html', items=items)

@app.route('/add', methods=['POST'])
def add_item():
    name = request.form['name']
    quantity = int(request.form['quantity'])
    price = float(request.form['price'])

    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO inventory (name, quantity, price) VALUES (?, ?, ?)", (name, quantity, price))
    conn.commit()
    conn.close()

    return redirect('/')

@app.route('/delete/<int:item_id>')
def delete_item(item_id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("DELETE FROM inventory WHERE id=?", (item_id,))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
