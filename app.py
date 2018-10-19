from flask import Flask, request, jsonify
import store_manager

app = Flask(__name__)

action = store_manager.Product_Operation("Yivanna Biles")

@app.route('/')
def home_page():
    return "Welcome to Polos Store-Manager app!"

@app.route('/v1/products/create', methods = ['GET','POST'])
def create_product():
    if request.method == 'POST':
        name = request.form.get('name')
        unit = request.form.get('unit')
        unit_price = int(request.form.get('unit_price'))
        quantity = int(request.form.get('quantity'))
        minimum_quantity = int(request.form.get('minimum_quantity'))      
        action.admin_create_product(name, unit, unit_price, quantity, minimum_quantity)  
        return action.response
        # return jsonify(store_manager.inventory)

@app.route('/v1/products/<int:productId>')
def get_product_by_id(productId):    
    return jsonify(action.get_product_by_id(productId))


@app.route('/v1/products')
def get_all_products():
    return jsonify(store_manager.inventory)

@app.route('/v1/sales/shopping_cart', methods = ['GET', 'POST'])
def shopping_cart():
    if request.method == 'POST':
        product_id = int(request.form.get('product_id'))
        quantity = int(request.form.get('quantity'))
        action.add_to_cart_by_id(product_id,quantity)
        return action.response       

    return jsonify(store_manager.shopping_cart) 

@app.route('/v1/sales/create_record')
def create_sales_record():
    action.create_sales_record()
    return action.response
   

@app.route('/v1/sales/get_all_records')
def get_all_records():
    return jsonify(store_manager.sales_records)


@app.route('/v1/sales/<saleId>')
def get_record_by_id(saleId):    
    return jsonify(action.get_record_by_id(saleId))


if __name__ == "__main__":
    app.run(debug=True)
