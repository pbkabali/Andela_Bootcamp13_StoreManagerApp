import pytest
from flask import jsonify

def test_fetch_products_from_empty_inventory(client):
    response = client.get('/v1/products')
    assert b"There are no products in inventory" in response.data

def test_fetch_product_by_id_from_emptyinventory(client):
    response = client.get('/v1/products/1')
    assert b"There are no products in inventory" in response.data

def test_create_new_product(client, first_test_product):
    response = client.post('/v1/products/create', data = first_test_product)
    assert b"Product added successfully!" in response.data

def test_create_duplicate_product(client, three_test_products, first_test_product):
    # client.post('/v1/products/create', data = first_test_product)
    for product in three_test_products:
        client.post('/v1/products/create', data = product)
    response = client.post('/v1/products/create', data = first_test_product)
    assert b"Product already exists!" in response.data

