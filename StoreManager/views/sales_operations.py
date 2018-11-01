from flask import Blueprint, request, jsonify
from ..models.products import Product
from ..models.sales import Sale


bp = Blueprint("sales", __name__)

@bp.route('/api/v1/sales/create_record', methods = ['GET', 'POST'])
def create_record():

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
        sale.addSale(
            product_id                        
            ,quantity
            ,searched_product["unit_price"]*quantity
            )
        #reduce inventory quantiy by sale quantity 
        new_quantity = searched_product['quantity']-quantity
        sale.updateProductQuantity(product_id, new_quantity)                                                            
        message = "Sales Record Created Successfully"  
        return jsonify({"Response":message}), 200

    message = "All available products" 
    return jsonify({message:response}), 200    

@bp.route('/api/v1/admin/sales/all')
def get_all_records():
    sale=Sale()
    response = sale.getAllRecords()
    if response == []:
        message = "There are no sales records to show!"
        return jsonify({"Response":message}), 200
    message = "All sales records"
    return jsonify({message : response}), 200

@bp.route('/api/v1/sales/<int:saleId>')
def get_record_by_id(saleId): 
    sale=Sale()

    if  sale.getAllRecords() == None:
        message = "There are no sales records to show!"
        return jsonify({"response": message})

    response = sale.getRecordById(saleId)
    if response == None:
        message = "Sale record not found!" 
        return jsonify({'Response': message}), 404

    message = "Sales record found!" 
    return jsonify({message: response}), 200

    