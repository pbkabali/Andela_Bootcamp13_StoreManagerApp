from flask import Blueprint, request, jsonify
from ..models.products import Product, inventory
import json

bp = Blueprint('products', __name__)


@bp.route('/api/v1/products/create', methods = ['GET','POST'])
def create_product():
    if request.method == 'POST':
        category =  request.json.get('category')
        name = request.json.get('name')
        unit = request.json.get('unit')
        unit_price = request.json.get('unit_price')
        quantity = request.json.get('quantity')
        minimum_quantity = request.json.get('minimum_quantity')

        #confirm that required fields are not empty
        if not (name and unit_price and quantity):
            response = "Required fields must be filled and non-zero!"
            return jsonify({"response": response}), 400

        #confirm number fields have numbers
        if not isinstance(unit_price*quantity*minimum_quantity, int): 
            response = "Number fields must be Numbers!"
            return jsonify({"response": response}), 400

        #check if product is not already in inventory
        if [product for product in inventory if product['name'] == name]:
            response = "Product already exists! Choose edit instead"
            return jsonify({'response': response}), 200

        #create product if all tests are passed
        new_product = Product(category, name, unit, unit_price, quantity, minimum_quantity)
        inventory.append(new_product.product_details) 
        response = "Product added successfully!"  
        return jsonify({response: new_product.product_details}), 200   

    
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
    if len(inventory) == 0:
        response = "There are no products in inventory"
        return jsonify({"response":response}), 200
    else:
        response = "All available products" 
        return jsonify({response : inventory}), 200

        

