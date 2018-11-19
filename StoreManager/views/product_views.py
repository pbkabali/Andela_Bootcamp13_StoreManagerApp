from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..models.products import Product
from ..models.users import User
import json

bp = Blueprint('products', __name__)


@bp.route('/api/v1/products/create', methods = ['GET','POST'])
@jwt_required
def create_product():
    user = User()
    current_user = get_jwt_identity()
    if user.get_a_user(current_user)['role'] == 'user':
        response = "You are not authorised to perform this operation!"
        return jsonify({"response" : response}), 401
    if request.method == 'POST':
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

        #check that input is not space
        fields = [category, name, unit, unit_price, quantity, minimum_quantity]
        for field in fields:
            if field == " ":    
                error = "Required fields cannot be spaces!"
                return jsonify({"response": error}), 400

        #confirm number fields have numbers
        if not isinstance(unit_price*quantity*minimum_quantity, int): 
            error = "Number fields must be Numbers!"
            return jsonify({"response": error}), 400

        #check if product is not already in inventory
        new_product = Product()
        if new_product.duplicateProduct(name):
            response = "Product already exists! Choose modify instead"
            return jsonify({'response': response}), 400
       
        #create product if all tests are passed        
        response = new_product.addProduct(name, unit, unit_price, 
                                    quantity, minimum_quantity, category) 
        message = "product_added"  
        return jsonify({message:response}), 200   

    
@bp.route('/api/v1/products/<int:productId>', methods = ['GET','PUT','DELETE'])
@jwt_required
def product_by_id(productId):
    product = Product()
    response = product.getProducts()
    if response == []:
        message = "There are no products in inventory!"
        return jsonify({"response":message}), 200
    response = product.getProductbyId(productId)
    if response == None:
        message = "Product not found!" 
        return jsonify({'Response':message}), 404

    if request.method == "PUT":
        user = User()
        current_user = get_jwt_identity()
        if user.get_a_user(current_user)['role'] == 'user':
            response = "You are not authorised to perform this operation!"
            return jsonify({"response" : response}), 401
        user_data = request.get_json()
        key =  user_data.get('key')
        value = user_data.get('value')
        if key not in ["product_name", "unit", "unit_price","quantity",
        "minimum_quantity", "category"]:
            return jsonify({"response":"field to update unknown!"}), 400
        product.modifyProduct(productId, key, value)
        response = product.getProductbyId(productId)
        message = "modified_product"
        return jsonify ({message:response})

    if request.method == "DELETE":
        user = User()
        current_user = get_jwt_identity()
        if user.get_a_user(current_user)['role'] == 'user':
            response = "You are not authorised to perform this operation!"
            return jsonify({"response" : response}), 401
        product.deleteProduct(productId)
        message = "deleted_product"
        return jsonify({"response":message})   
    
    message = "found_product" 
    return jsonify({message : response}), 200

@bp.route('/api/v1/products')
@jwt_required
def get_all_products():
    products = Product()
    response = products.getProducts()
    if len(response) == 0:    
        message = "There are no products in inventory"
        return jsonify({"response":message}), 200
    
    message = "available_products" 
    return jsonify({message:response}), 200

        

