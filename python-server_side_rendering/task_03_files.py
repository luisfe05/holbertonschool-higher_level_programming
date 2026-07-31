#!/usr/bin/python3
"""Flask application displaying product data from JSON or CSV files."""
import csv
import json
from flask import Flask, render_template, request

app = Flask(__name__)


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
    """Display product data from a JSON or CSV source, optionally by id."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        data = read_json()
    elif source == 'csv':
        data = read_csv()
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
    app.run(debug=True, port=5000)
