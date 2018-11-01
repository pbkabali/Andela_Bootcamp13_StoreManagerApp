from flask import Flask, jsonify
import psycopg2


def create_app():
    app = Flask(__name__)

    
    @app.route("/")
    def homepage():
        return jsonify([
            "Welcome to Polos Store Manager API!"
            ,"Endpoints",{
                "/api/v1/products/create":"Create new product"
                ,"/api/v1/products": "Fetch all products"
                ,"/api/v1/products/<int:productId>": "Fetch product by Id"
                ,"/api/v1/sales/create_record": "Post sale record "
                ,"api/v1/admin/sales/all": "Fetch all sales records"
                ,"pai/v1/sales/<int:saleId>":"Fetch sale record by Id"
            }            
        ]), 200

    from .views import product_operations
    app.register_blueprint(product_operations.bp)

    from .views import sales_operations
    app.register_blueprint(sales_operations.bp)
        
    from .views import user_management
    app.register_blueprint(user_management.bp)

    return app 