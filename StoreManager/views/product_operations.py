from flask import Blueprint, request, jsonify, make_response
from ..models.products import Product
import json

bp = Blueprint('products', __name__)


@bp.route('/api/v1/products/create', methods = ['POST'])
def create_product():
    # if request.method == 'POST':
        user_data = request.get_json()
        category =  user_data.get('category')
        name = user_data.get('name')
        unit = user_data.get('unit')
        unit_price = user_data.get('unit_price')
        quantity = user_data.get('quantity')
        minimum_quantity = user_data.get('minimum_quantity')

        error = None
        #confirm that required fields are not empty
        if not (name and unit_price and quantity):
            error = "Required fields must be filled and non-zero!"
            return jsonify({"response": error}), 400

        #confirm number fields have numbers
        if not isinstance(unit_price*quantity*minimum_quantity, int): 
            error = "Number fields must be Numbers!"
            return jsonify({"response": error}), 400

        #check if product is not already in inventory
        oduct for product in inventory if product['name'] == name]:
            response = "Product already exists! Choose edit instead"
            return jsonify({'response': response}), 200

        #create product if all tests are passed
        new_product = Product()
        new_product.add_a_product(name, unit, unit_price, quantity, minimum_quantity, category) 
        message = "Product added successfully!"  
        return jsonify(message), 200   

    
@bp.route('/api/v1/products/<int:productId>')
def get_product_by_id(productId):
    if  len(inventory) == 0:
        response = "There are no products in inventory!"
        return jsonify({"response":response}), 200

    elif int(productId) > len(inventory):
        response = "Product not found!" 
        return jsonify({'Response':response}), 404
    else:
        for product in inventory:
            if product['product_id']==int(productId):
                searched_product = product
        response = "Product found!" 
        return jsonify({response : searched_product}), 200

@bp.route('/api/v1/products')
def get_all_products():
    products = Product()
    response = products.get_products()
    if len(response) == 0:    
        message = "There are no products in inventory"
        return jsonify({"response":message}), 200
    
    message = "All available products" 
    return jsonify({message:response}), 200

        

