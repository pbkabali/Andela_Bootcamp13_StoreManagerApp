import pytest
from StoreManager import create_app

@pytest.fixture
def app():
    app = create_app()
    return app


@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def first_test_product():
    product_data = {
        "name": "arm_bands"
        ,"unit":"pcs"
        ,"unit_price": "4"
        ,"quantity": "200"
        ,"minimum_quantity": "15"
    }
    return product_data

@pytest.fixture
def second_test_product():
    product_data = {
        "name": "blue_jeans"
        ,"unit":"pairs"
        ,"unit_price": "25"
        ,"quantity": "80"
        ,"minimum_quantity": "5"
    }
    return product_data

@pytest.fixture
def three_test_products():
    product1 = {
        "name": "arm_bands"
        ,"unit":"pcs"
        ,"unit_price": "4"
        ,"quantity": "200"
        ,"minimum_quantity": "15"
    }
    product2 = {
        "name": "blue_jeans"
        ,"unit":"pairs"
        ,"unit_price": "25"
        ,"quantity": "80"
        ,"minimum_quantity": "5"
    }
    product3 = {
        "name": "baseball_hats"
        ,"unit":"pcs"
        ,"unit_price": "10"
        ,"quantity": "35"
        ,"minimum_quantity": "2"
    }
    product_data = [product1, product2, product3]
    return product_data