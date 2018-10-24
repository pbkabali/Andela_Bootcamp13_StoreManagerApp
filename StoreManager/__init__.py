from flask import Flask, jsonify

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def homepage():
        return jsonify([
            "Welcome to Polos Store Manager API!"
            ,"Endpoints",{
                "/v1/products/create":"Create new product"
                ,"/v1/products": "Fetch all products"
                ,"/v1/products/<int:productId>": "Fetch product by Id"
                ,"/v1/sales/shopping_cart":"Add item to shopping cart"
                ,"/v1/sales/create_record": "Post sale record from shopping cart"
                ,"/v1/sales/get_all_records": "Fetch all sales records"
                ,"/v1/sales/<saleId>":"Fetch sale record by Id"
            }            
        ]), 200

    from .views import product_operations
    app.register_blueprint(product_operations.bp)

    from .views import sales_operations
    app.register_blueprint(sales_operations.bp)
    

    return app 