import pytest

def test_fetch_sales_before_creating_record(client,db):
    response = client.get('/api/v1/admin/sales/all')
    assert b"There are no sales records to show!" in response.data

def test_fetch_single_record_before_creating(client, db):
    response = client.get('/api/v1/sales/1')
    assert b"There are no sales records to show!" in response.data

def test_create_sale_record(client, db, products, user, sale):
    client.post(
            '/auth/api/v1/signup'
            ,data = user
            ,content_type='application/json'
            )
    for product in products:
        client.post(
            '/api/v1/products/create'
            ,data = product
            ,content_type='application/json'
            )
    response = client.post('/api/v1/sales/create_record'
        ,data = sale
        ,content_type='application/json'
        )
    assert b"created_record" in response.data


def test_create_sale_empty_field(client, empty_field_sale):
    response = client.post('/api/v1/sales/create_record'
        ,data = empty_field_sale
        ,content_type='application/json'
        )
    assert b"Required fields must be filled and non-zero!" in response.data

def test_create_sale_str_in_number_field(client, string_sale):
    response = client.post('/api/v1/sales/create_record'
        ,data = string_sale
        ,content_type='application/json'
        )
    assert b"Number fields must be Numbers!" in response.data

def test_fetch_sales(client, db, user, products, sales):
    client.post(
            '/auth/api/v1/signup'
            ,data = user
            ,content_type='application/json'
            )
    for product in products:
        client.post(
            '/api/v1/products/create'
            ,data = product
            ,content_type='application/json'
            )
    for sale in sales:
        client.post('/api/v1/sales/create_record'
            ,data = sale
            ,content_type='application/json')
    response = client.get('/api/v1/admin/sales/all')
    assert b"sales_records" in response.data

def test_fetch_sale_by_id(client, db, user, products, sales):
    client.post(
            '/auth/api/v1/signup'
            ,data = user
            ,content_type='application/json'
            )
    for product in products:
        client.post(
            '/api/v1/products/create'
            ,data = product
            ,content_type='application/json'
            )
    for sale in sales:
        client.post('/api/v1/sales/create_record'
            ,data = sale
            ,content_type='application/json')
    response = client.get('/api/v1/sales/2')
    assert b"Esprit 200 watch" in response.data

def test_fetch_nonexistent_sale(client, db, user, products, sales):
    client.post(
            '/auth/api/v1/signup'
            ,data = user
            ,content_type='application/json'
            )
    for product in products:
        client.post(
            '/api/v1/products/create'
            ,data = product
            ,content_type='application/json'
            )
    for sale in sales:
        client.post('/api/v1/sales/create_record'
            ,data = sale
            ,content_type='application/json')
    response = client.get('/api/v1/sales/6')
    assert b"Sale record not found!" in response.data
