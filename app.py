from flask import Flask, request, jsonify
import store_manager

app = Flask(__name__)

action = store_manager.Product_Operation()

@app.route('/')
def home_page():
    return "Welcome to Store-Manager app!"

@app.route('/v1/products/create', methods = ['GET','POST'])
def create_product():
    if request.method == 'POST':
        name = request.form.get('name')
        unit = request.form.get('unit')
        unit_price = int(request.form.get('unit_price'))
        quantity = int(request.form.get('quantity'))
        minimum_quantity = int(request.form.get('minimum_quantity'))      
        action.admin_create_product(name, unit, unit_price, quantity, minimum_quantity)       
        return jsonify(store_manager.inventory)

@app.route('/v1/products')
def get_all_products():
    return jsonify(store_manager.inventory)





if __name__ == "__main__":
    app.run(debug=True)
