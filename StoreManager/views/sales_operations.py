from flask import Blueprint, request, jsonify
from ..models.products import Product
from ..models.sales import Sale, sales_records

bp = Blueprint("sales", __name__)

@bp.route('/api/v1/sales/create_record', methods = ['GET', 'POST'])
def shopping_cart():
    if request.method == 'POST':        
        product_id = request.json.get('product_id')
        quantity = request.json.get('quantity')
        requester = "requester"

        #confirm that required fields are not empty
        if not (product_id and quantity):
            response = "Required fields must be filled and non-zero!"
            return jsonify({"response": response}), 400

        #confirm number fields have numbers
        if not isinstance(product_id*quantity, int):
            response = "Number fields must be Numbers!"
            return jsonify({"response": response}), 400

        #check if supplied id is in sales records
        if product_id > len(inventory):
            response = "Sale record not found!"
            return jsonify ({"Response":response}), 400        

        #if id is available in sales records, get product details from inventory
        for product in inventory:
            if product['product_id']==product_id:
                searched_product = product  

        #check if requested quantity is available in inventory
        if searched_product["quantity"] < quantity:
            response = "Not enough quantity in inventory!"
            return jsonify ({"Response":response})
        
        #if there is enough quantity in inventory, continue with sale
        sale = Sale(
            searched_product["name"]
            ,quantity
            ,searched_product["unit_price"]
            ,requester
        )
        sales_records["records"].append(sale.record_details) #add record to storage                
        sales_records["total_sales"] += sale.total_price #update total sales

        #reduce inventory quantiy by sale quantity  
        inventory[inventory.index(searched_product)]["quantity"] -= quantity                                                  
        
        response = "Sales Record Created Successfully"  
        return jsonify({response: sale.record_details}), 200

@bp.route('/api/v1/admin/sales/all')
def get_all_records():
    if len(sales_records['records']) == 0:
        response = "There are no sales records to show!"
        return jsonify({"Response":response}), 200

    response = "All sales records"
    return jsonify({response : sales_records["records"]}), 200

@bp.route('/api/v1/sales/<int:saleId>')
def get_record_by_id(saleId): 
    if  len(sales_records['records']) == 0:
        response = "There are no sales records to show!"
        return jsonify({"response":response})

    if int(saleId) > len(sales_records['records']):
        response = "Sale record not found!" 
        return jsonify({'Response':response}), 404

    for sale in sales_records['records']:
        if sale['sale_id']==int(saleId):
            searched_sale = sale
    response = "Sales record found!" 
    return jsonify({response: searched_sale}), 200

    