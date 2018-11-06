import pytest
from StoreManager import create_app
from StoreManager.db.db import DbConnection
from StoreManager import config
import json


@pytest.fixture
def app():
    app = create_app(config.TestingConfig)
    return app

@pytest.fixture
def db():
    db = DbConnection()
    db.cursor.execute("""DROP TABLE sales CASCADE""")
    db.cursor.execute("""DROP TABLE products CASCADE""")
    db.cursor.execute("""DROP TABLE users CASCADE""")
    db.create_db_tables()
    return db


@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def product():
    product_data = json.dumps({
        "category":"Apparel"
        ,"name":"Baseball Hats"
        ,"unit":"pcs"
        ,"unit_price":10
        ,"quantity":35
        ,"minimum_quantity":2
    })
    return product_data
   

@pytest.fixture
def products():
    product1 = json.dumps({
        "category":"Apparel"
        ,"name":"Baseball Hats"
        ,"unit":"pcs"
        ,"unit_price":10
        ,"quantity":35
        ,"minimum_quantity":2
    })
    product2 = json.dumps({
        "category":"Jewellery"
        ,"name":"Esprit 200 watch"
        ,"unit":"pcs"
        ,"unit_price":150
        ,"quantity":3
        ,"minimum_quantity":0
    })
    product3 = json.dumps({
        "category":"Footwear"
        ,"name":"Addidas 270"
        ,"unit":"pairs"
        ,"unit_price":120
        ,"quantity":7
        ,"minimum_quantity":1
    })
    product_data = [product1, product2, product3]
    return product_data
   

@pytest.fixture
def empty_field_product():
    product_data = json.dumps({
        "category":"Apparel"
        ,"name":""
        ,"unit":"pcs"
        ,"unit_price":10
        ,"quantity":35
        ,"minimum_quantity":2
    })
    return product_data    

@pytest.fixture
def string_in_product():
    product_data = json.dumps({
        "category":"Apparel"
        ,"name":"Baseball Hats"
        ,"unit":"pcs"
        ,"unit_price":"two"
        ,"quantity":35
        ,"minimum_quantity":2
    })
    return product_data

@pytest.fixture
def user():
    user_details = json.dumps({
        "first_name":"kkkke",
	    "last_name":"Lube",
	    "username":"pabali",
	    "password":"polos123"       
    })
    return user_details
  
@pytest.fixture
def sale():
    sale_details = json.dumps({
        "product_id":1
        ,"quantity":3        
    })
    return sale_details

@pytest.fixture
def empty_field_sale():
    sale_details = json.dumps({
        "product_id":""
        ,"quantity":3        
    })
    return sale_details
       

@pytest.fixture
def string_sale():
    sale_details = json.dumps({
        "product_id":"str"
        ,"quantity":3        
    })
    return sale_details
     

@pytest.fixture
def sales():
    sale_details1 = json.dumps({
        "product_id":1
        ,"quantity":3        
    })
    sale_details2 = json.dumps({
        "product_id":2
        ,"quantity":2        
    })
    sale_details = [sale_details1, sale_details2]
    return sale_details
     
