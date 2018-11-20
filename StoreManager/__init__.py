from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from . import config

def create_app(config_name):

    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(config_name)

    return app 

app = create_app(config.DevelopmentConfig)    

jwt = JWTManager(app)

@app.route("/")
def homepage():
    return jsonify("Welcome to new Polos with security!"), 200

from .views import product_views
app.register_blueprint(product_views.bp)

from .views import sales_views
app.register_blueprint(sales_views.bp)

from .views import users_views
app.register_blueprint(users_views.bp)

 

