from flask import Blueprint, request, jsonify
from ..models.products import Product, inventory

bp = Blueprint('products', __name__)


@bp.route('/v1/products/create', methods = ['GET','POST'])
def create_product():
    if request.method == 'POST':
        name = request.form.get('name')
        unit = request.form.get('unit')
        unit_price = int(request.form.get('unit_price'))
        quantity = int(request.form.get('quantity'))
        minimum_quantity = int(request.form.get('minimum_quantity'))
        new_product = Product(name, unit, unit_price, quantity, minimum_quantity)

        if not new_product.create_product():
            response = "Product already exists! Choose edit instead"
            return jsonify({'Response':response}), 401

        else:
            response = "Product added successfully!"    
            return jsonify({"response":response, "Products in inventory":inventory}), 200

    return jsonify({"Products in inventory: inventory":inventory}), 200

@bp.route('/v1/products/<int:productId>')
def get_product_by_id(productId):
    if  len(inventory) == 0:
        response = "There are no products in inventory"
        return jsonify({"response":response})

    elif int(productId) > len(inventory):
        response = "Product not found!" 
        return jsonify({'Response':response}), 401
    else:
        response = "Product found!" 
        return jsonify({"response":response, "Product details":inventory[productId]})

@bp.route('/v1/products')
def get_all_products():
    if len(inventory) == 0:
        response = "There are no products in inventory"
        return jsonify({"response":response})
    else:
        response = "All available products!" 
        return jsonify({"response":response, "Products details":inventory})

        

