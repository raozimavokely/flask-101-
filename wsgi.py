# wsgi.py
# pylint: disable=missing-docstring

from flask import Flask, jsonify, render_template, request
import itertools

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

PRODUCTS = [
    { 'id': 1, 'name': 'Skello' },
    { 'id': 2, 'name': 'Socialive.tv' },
    { 'id': 3, 'name': 'Le Wagon'},
]
@app.route('/api/v1/products')
def get_products():
    return jsonify(PRODUCTS)

@app.route('/api/v1/products/<int:id>')
def get_product(id):
    for p in PRODUCTS:
        if p['id'] == id:
            return jsonify(p)
        else:
            pass
    #return not_found(404)
    return "404 not found!"

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")

@app.route('/api/v1/products/<int:id>')
def del_product(id):
    for p in PRODUCTS:
        if p['id'] == id:
            PRODUCTS.remove(p)
        else:
            pass
    return jsonify(PRODUCTS)

@app.route('/api/v1/products')
def add_product(id):
    new_product = { 'id': 4, 'name': 'New Product 4' },
    for p in PRODUCTS:
        if new_product['id'] == p['id']:
            pass
        else:
            PRODUCTS.append(new_product)
    return jsonify(PRODUCTS)