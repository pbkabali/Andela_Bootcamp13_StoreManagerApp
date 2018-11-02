import pytest
from flask import jsonify

def test_fetch_products_from_empty_store(client):
    response = client.get('/api/v1/products')
    assert b"available_products" in response.data

# def test_fetch_product_by_id_from_empty_inventory(client):
#     response = client.get('/api/v1/products/1')
#     assert b"There are no products in inventory" in response.data

# def test_create_new_product(client, first_test_product):
#     response = client.post(
#         '/api/v1/products/create'
#         ,data = first_test_product
#         ,content_type='application/json'
#         )
#     assert b"Product added successfully!" in response.data

# def test_create_duplicate_product(client, three_test_products, first_test_product):
#     for product in three_test_products:
#         client.post('/api/v1/products/create'
#         ,data = product
#         ,content_type='application/json')
#     response = client.post('/api/v1/products/create'
#         ,data = first_test_product
#         ,content_type='application/json'
#         )
#     assert b"Product already exists!" in response.data

# def test_create_product_empty_field(client, empty_field_product):
#     response = client.post('/api/v1/products/create'
#         ,data = empty_field_product
#         ,content_type='application/json'
#         )
#     assert b"Required fields must be filled and non-zero!" in response.data

# def test_create_product_str_in_number_field(client, string_in_number_field_product):
#     response = client.post('/api/v1/products/create'
#         ,data = string_in_number_field_product
#         ,content_type='application/json'
#         )
#     assert b"Number fields must be Numbers!" in response.data

# def test_fetch_products_from_filled_inventory(client, three_test_products):
#     for product in three_test_products:
#         client.post('/api/v1/products/create'
#         ,data = product
#         ,content_type='application/json')
#     response = client.get('/api/v1/products')
#     assert b"All available products" in response.data

# def test_fetch_product_by_id_from_filled_inventory(client, three_test_products):
#     for product in three_test_products:
#         client.post('/api/v1/products/create'
#         ,data = product
#         ,content_type='application/json')
#     response = client.get('/api/v1/products/2')
#     assert b"Jewellery" in response.data

# def test_fetch_nonexistent_product_from_filled_inventory(client, three_test_products):
#     for product in three_test_products:
#         client.post('/api/v1/products/create'
#         ,data = product
#         ,content_type='application/json')
#     response = client.get('/api/v1/products/6')
#     assert b"Product not found!" in response.data
    