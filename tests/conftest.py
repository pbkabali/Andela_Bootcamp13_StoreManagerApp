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
   

# @pytest.fixture
# def three_test_products():
#     product1 = json.dumps({
#         "category":"Apparel"
#         ,"name":"Baseball Hats"
#         ,"unit":"pcs"
#         ,"unit_price":10
#         ,"quantity":35
#         ,"minimum_quantity":2
#     })
#     product2 = json.dumps({
#         "category":"Jewellery"
#         ,"name":"Esprit 200 watch"
#         ,"unit":"pcs"
#         ,"unit_price":150
#         ,"quantity":3
#         ,"minimum_quantity":0
#     })
#     product3 = json.dumps({
#         "category":"Footwear"
#         ,"name":"Addidas 270"
#         ,"unit":"pairs"
#         ,"unit_price":120
#         ,"quantity":7
#         ,"minimum_quantity":1
#     })
#     product_data = [product1, product2, product3]
#     yield product_data
#     inventory.clear()

# @pytest.fixture
# def empty_field_product():
#     product_data = json.dumps({
#         "category":"Apparel"
#         ,"name":""
#         ,"unit":"pcs"
#         ,"unit_price":10
#         ,"quantity":35
#         ,"minimum_quantity":2
#     })
#     yield product_data
#     inventory.clear()

# @pytest.fixture
# def string_in_number_field_product():
#     product_data = json.dumps({
#         "category":"Apparel"
#         ,"name":"Baseball Hats"
#         ,"unit":"pcs"
#         ,"unit_price":"two"
#         ,"quantity":35
#         ,"minimum_quantity":2
#     })
#     yield product_data
#     inventory.clear()   

# @pytest.fixture
# def first_sale():
#     sale_details = json.dumps({
#         "product_id":1
#         ,"quantity":3        
#     })
#     yield sale_details
#     sales_records["records"].clear() 

# @pytest.fixture
# def empty_field_sale():
#     sale_details = json.dumps({
#         "product_id":""
#         ,"quantity":3        
#     })
#     yield sale_details
#     sales_records["records"].clear()     

# @pytest.fixture
# def string_in_number_field_sale():
#     sale_details = json.dumps({
#         "product_id":"str"
#         ,"quantity":3        
#     })
#     yield sale_details
#     sales_records["records"].clear()  

# @pytest.fixture
# def two_test_sales():
#     sale_details1 = json.dumps({
#         "product_id":1
#         ,"quantity":3        
#     })
#     sale_details2 = json.dumps({
#         "product_id":2
#         ,"quantity":2        
#     })
#     sale_details = [sale_details1, sale_details2]
#     yield sale_details
#     sales_records["records"].clear()  
