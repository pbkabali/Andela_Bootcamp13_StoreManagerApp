from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..models.products import Product
from ..models.sales import Sale
from ..models.users import User


bp = Blueprint("sales", __name__)

@bp.route('/api/v1/sales/create_record', methods = ['GET', 'POST'])
@jwt_required
def create_record():
    user = User()
    current_user = get_jwt_identity()
    if user.get_a_user(current_user)['role'] == 'admin':
        response = "This operation is only for attendants!"
        return jsonify(response), 401

    #check that products records is not empty
    product=Product()
    if  product.getProducts == []:
        message = "There are no products in inventory!"
        return jsonify({"response":message}), 200
    if request.method == 'POST':  
        user_data=request.get_json()      
        product_id = user_data.get('product_id')
        quantity = user_data.get('quantity')
                
        #confirm that required fields are not empty
        if not (product_id and quantity):
            message = "Required fields must be filled and non-zero!"
            return jsonify({"response": message}), 400

        #confirm number fields have numbers
        if not isinstance(product_id*quantity, int):
            message = "Number fields must be Numbers!"
            return jsonify({"response": message}), 400        

        #check if supplied id is in products records
        if product.getProductbyId(product_id) == None:
            message = "Product not found!" 
            return jsonify({'Response':message}), 400        

        #if id is available in products records, get product details from database
        searched_product = product.getProductbyId(product_id)

        #check if requested quantity is available in inventory
        if searched_product["quantity"] < quantity:
            response = "Not enough quantity in inventory!"
            return jsonify ({"Response":response})
        
        #if there is enough quantity in inventory, continue with sale
        sale = Sale()
        response =sale.addSale(
                        product_id                        
                        ,quantity
                        ,searched_product["unit_price"]*quantity
                        )
        #reduce inventory quantiy by sale quantity 
        new_quantity = searched_product['quantity']-quantity
        sale.updateProductQuantity(product_id, new_quantity)                                                            
        message = "created_record"  
        return jsonify({message:response}), 200

    message = "available_products" 
    return jsonify({message:response}), 200    

@bp.route('/api/v1/admin/sales/all')
@jwt_required
def get_all_records():
    user = User()
    current_user = get_jwt_identity()
    if user.get_a_user(current_user)['role'] == 'user':
        response = "You are not authorised to perform this operation!"
        return jsonify(response), 401
    sale=Sale()
    response = sale.getAllRecords()
    if response == []:
        message = "There are no sales records to show!"
        return jsonify({"Response":message}), 200
    message = "sales_records"
    return jsonify({message : response}), 200

@bp.route('/api/v1/sales/<int:saleId>')
@jwt_required
def get_record_by_id(saleId): 
    user = User()
    current_user = get_jwt_identity()
    if user.get_a_user(current_user)['role'] == 'user':
        response = "You are not authorised to perform this operation!"
        return jsonify(response), 401
    sale=Sale()
    response = sale.getAllRecords()
    if response == []:
        message = "There are no sales records to show!"
        return jsonify({"response": message})

    response = sale.getRecordById(saleId)
    if response == None:
        message = "Sale record not found!" 
        return jsonify({'Response': message}), 404

    message = "found_record" 
    return jsonify({message: response}), 200

    