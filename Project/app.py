from flask import Flask, render_template, redirect, url_for, request, session
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)


client = MongoClient("mongodb://localhost:27017/")
db = client['ecommerce']  
products_collection = db['products']  

def format_product(product):
    return {
        'id': str(product['_id']),
        'name': product['name'], 
        'description': product['description'],
        'price': product['price'],
        'image': product['image'],
        'stock': product['stock'],
        'category': product['category']
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products')
def products():
    products = products_collection.find()
    formatted_products = [format_product(product) for product in products]
    return render_template('products.html', products=formatted_products)

@app.route('/cart')
def cart():
    cart_items = session.get('cart', {})
    
    if isinstance(cart_items, list):  
        cart_items = {}  
        session['cart'] = cart_items

    products_in_cart = []
    for product_id, quantity in cart_items.items():
        product = products_collection.find_one({'_id': ObjectId(product_id)})
        if product:
            product_data = format_product(product)
            product_data['quantity'] = quantity 
            products_in_cart.append(product_data)
    return render_template('cart.html', cart_items=products_in_cart)

@app.route('/add_to_cart/<product_id>')
def add_to_cart(product_id):
    if 'cart' not in session:
        session['cart'] = {}

    cart = session['cart']
    if isinstance(cart, list):  
        cart = {}
        session['cart'] = cart 

    if product_id in cart:
        cart[product_id] += 1  
    else:
        cart[product_id] = 1 
    session.modified = True 
    return redirect(url_for('cart'))

if __name__ == '__main__':
    app.secret_key = 'Any'  
    app.run(debug=True)
