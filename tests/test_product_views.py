import pytest
from flask import jsonify

def test_fetch_all_from_empty_store(client, db):
    response = client.get('/api/v1/products')
    assert b"There are no products in inventory" in response.data

def test_fetch_one_from_empty_inventory(client, db):
    response = client.get('/api/v1/products/1')
    assert b"There are no products in inventory" in response.data

def test_create_new_product(client,db, product):
    response = client.post(
        '/api/v1/products/create'
        ,data = product
        ,content_type='application/json'
        )
    assert b"product_added" in response.data

def test_create_duplicate_product(client,db, products, product):
    for product in products:
        client.post('/api/v1/products/create'
        ,data = product
        ,content_type='application/json')
    response = client.post('/api/v1/products/create'
        ,data = product
        ,content_type='application/json'
        )
    assert b"Product already exists!" in response.data

def test_create_product_empty_field(client, db, empty_field_product):
    response = client.post('/api/v1/products/create'
        ,data = empty_field_product
        ,content_type='application/json'
        )
    assert b"Required fields must be filled and non-zero!" in response.data

def test_create_product_str_in_number_field(client, db, string_in_product):
    response = client.post('/api/v1/products/create'
        ,data = string_in_product
        ,content_type='application/json'
        )
    assert b"Number fields must be Numbers!" in response.data

def test_fetch_products(client, db, products):
    for product in products:
        client.post('/api/v1/products/create'
        ,data = product
        ,content_type='application/json')
    response = client.get('/api/v1/products')
    assert b"available_products" in response.data

def test_fetch_product_by_id(client,db, products):
    for product in products:
        client.post('/api/v1/products/create'
        ,data = product
        ,content_type='application/json')
    response = client.get('/api/v1/products/2')
    assert b"Jewellery" in response.data

def test_fetch_nonexistent_product(client, products):
    for product in products:
        client.post('/api/v1/products/create'
        ,data = product
        ,content_type='application/json')
    response = client.get('/api/v1/products/6')
    assert b"Product not found!" in response.data
    