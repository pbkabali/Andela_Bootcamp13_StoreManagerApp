from flask import Blueprint, request, jsonify
from ..models.products import Product, inventory
from ..models.sales import Sale, sales_records
from datetime import datetime

bp = Blueprint("sales", __name__)

"""dictionary to hold shopping cart temporarily"""
current_shopping_cart = {"total_price":0, "total_items_in_cart":0}

"""dictionary to initialize shopping cart after sale"""
initial_shopping_cart = {"total_price":0, "total_items_in_cart":0}




@bp.route('/v1/sales/shopping_cart', methods = ['GET', 'POST'])
def shopping_cart():
    if request.method == 'POST':        
        product_id = int(request.form.get('product_id'))
        quantity = int(request.form.get('quantity'))

        if product_id > len(inventory):
            response = "Product not found!"
            return jsonify ({"Response":response})

        elif inventory[product_id]["quantity"] < quantity:
            response = "Not enough quantity in inventory!"
            return jsonify ({"Response":response})
        else: 
            id_in_cart = len(current_shopping_cart)-1 # subtract the two addional rows of 
                                                        #total items and total price         
            current_shopping_cart[str(id_in_cart)] = {
                "product_name":inventory[product_id]["product_name"]
                ,"quantity_ordered":quantity
                ,"price": quantity*inventory[product_id]["unit_price"]
            }           
            current_shopping_cart["total_price"] += quantity*inventory[product_id]["unit_price"]
            current_shopping_cart["total_items_in_cart"] += quantity         

            inventory[product_id]["quantity"] -= quantity # reduce quantity of product in inventory

            response = "Product added to cart successfully!"
            return jsonify ({"Response":response, "Items in Cart":current_shopping_cart}), 200

    if len(current_shopping_cart) > 2:        
        return jsonify ({"Items in Cart": current_shopping_cart}), 200  

    response = "Cart is empty!"
    return jsonify ({"Response":response, "Items in Cart": current_shopping_cart})  

@bp.route('/v1/sales/create_record')
def create_sales_record():
    global current_shopping_cart
    attendant = "Attendant 1"
    date = datetime.now()            
    details = current_shopping_cart            
    total_price = current_shopping_cart["total_price"]
    items= current_shopping_cart["total_items_in_cart"]
    sale = Sale(attendant, details, date, items, total_price)
    sale.create_record()
    current_shopping_cart = initial_shopping_cart

    response = "Sales Record Created Successfully"  
    
    return jsonify({"Response": response}), 200

@bp.route('/v1/sales/get_all_records')
def get_all_records():
    if len(sales_records) <= 2:
        response = "There are no sales records to show"
        return jsonify({"Response":response, "Sales Records":sales_records})

    response = "All sales records are shown"
    return jsonify({"Response":response, "Sales Records":sales_records}), 200

@bp.route('/v1/sales/<saleId>')
def get_record_by_id(saleId): 
    if  len(sales_records) == 2:
        response = "There are no records to show!"
        return jsonify({"response":response})

    elif int(saleId) > len(sales_records)-2:
        response = "Sale record not found!" 
        return jsonify({'Response':response})
    else:
        response = "Sales record found!" 
        return jsonify({"response":response, "Record details":sales_records[saleId]})

    