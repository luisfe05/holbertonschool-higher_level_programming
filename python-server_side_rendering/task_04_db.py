#!/usr/bin/python3
"""Flask application displaying product data from JSON, CSV, or SQLite."""
import csv
import json
import os
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

DB_FILE = 'products.db'


def create_database():
    """Create and populate the SQLite products database if needed."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    cursor.execute('SELECT COUNT(*) FROM Products')
    if cursor.fetchone()[0] == 0:
        cursor.execute('''
            INSERT INTO Products (id, name, category, price)
            VALUES
            (1, 'Laptop', 'Electronics', 799.99),
            (2, 'Coffee Mug', 'Home Goods', 15.99)
        ''')
    conn.commit()
    conn.close()


def read_json(filepath='products.json'):
    """Read a list of products from a JSON file."""
    with open(filepath, 'r') as json_file:
        return json.load(json_file)


def read_csv(filepath='products.csv'):
    """Read a list of products from a CSV file."""
    products = []
    with open(filepath, 'r', newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            products.append({
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price']),
            })
    return products


def read_sql():
    """Read a list of products from the SQLite database."""
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, category, price FROM Products')
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]


@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')


@app.route('/about')
def about():
    """Render the about page."""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Render the contact page."""
    return render_template('contact.html')


@app.route('/items')
def items():
    """Render a dynamic list of items read from items.json."""
    try:
        with open('items.json', 'r') as items_file:
            data = json.load(items_file)
            item_list = data.get('items', [])
    except (FileNotFoundError, json.JSONDecodeError):
        item_list = []

    return render_template('items.html', items=item_list)


@app.route('/products')
def products():
    """Display product data from JSON, CSV, or SQL, optionally by id."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        data = read_json()
    elif source == 'csv':
        data = read_csv()
    elif source == 'sql':
        try:
            data = read_sql()
        except sqlite3.Error:
            return render_template(
                'product_display.html', error="Database error")
    else:
        return render_template('product_display.html', error="Wrong source")

    if product_id is not None:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template(
                'product_display.html', error="Product not found")

        data = [product for product in data if product['id'] == product_id]
        if not data:
            return render_template(
                'product_display.html', error="Product not found")

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    if not os.path.exists(DB_FILE):
        create_database()
    app.run(debug=True, port=5000)
