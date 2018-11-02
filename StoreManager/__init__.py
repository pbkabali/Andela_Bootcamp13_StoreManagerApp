from flask import Flask, jsonify
from . import config

def create_app(config_name):

    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(config_name)

    
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

    from .views import product_views
    app.register_blueprint(product_views.bp)

    from .views import sales_views
    app.register_blueprint(sales_views.bp)

    from .views import users_views
    app.register_blueprint(users_views.bp)

    return app 