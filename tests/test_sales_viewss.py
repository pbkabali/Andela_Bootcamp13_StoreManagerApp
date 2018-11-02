# import pytest

# def test_fetch_all_sales_records_before_creating_any(client):
#     response = client.get('/api/v1/admin/sales/all')
#     assert b"There are no sales records to show!" in response.data

# def test_fetch_sale_record_byId_before_creating_any(client):
#     response = client.get('/api/v1/sales/1')
#     assert b"There are no sales records to show!" in response.data

# def test_create_sale_record(client, three_test_products, first_sale):
#     for product in three_test_products:
#         client.post(
#             '/api/v1/products/create'
#             ,data = product
#             ,content_type='application/json'
#             )
#     response = client.post('/api/v1/sales/create_record'
#         ,data = first_sale
#         ,content_type='application/json'
#         )
#     assert b"Sales Record Created Successfully" in response.data


# def test_create_sale_empty_field(client, empty_field_sale):
#     response = client.post('/api/v1/sales/create_record'
#         ,data = empty_field_sale
#         ,content_type='application/json'
#         )
#     assert b"Required fields must be filled and non-zero!" in response.data

# def test_create_sale_str_in_number_field(client, string_in_number_field_sale):
#     response = client.post('/api/v1/sales/create_record'
#         ,data = string_in_number_field_sale
#         ,content_type='application/json'
#         )
#     assert b"Number fields must be Numbers!" in response.data

# def test_fetch_sales_from_filled_sales_records(client,three_test_products, two_test_sales):
#     for product in three_test_products:
#         client.post(
#             '/api/v1/products/create'
#             ,data = product
#             ,content_type='application/json'
#             )
#     for sale in two_test_sales:
#         client.post('/api/v1/sales/create_record'
#             ,data = sale
#             ,content_type='application/json')
#     response = client.get('/api/v1/admin/sales/all')
#     assert b"All sales records" in response.data

# def test_fetch_sale_by_id_from_filled_sales_records(client, three_test_products,two_test_sales):
#     for product in three_test_products:
#         client.post(
#             '/api/v1/products/create'
#             ,data = product
#             ,content_type='application/json'
#             )
#     for sale in two_test_sales:
#         client.post('/api/v1/sales/create_record'
#             ,data = sale
#             ,content_type='application/json')
#     response = client.get('/api/v1/sales/2')
#     assert b"Esprit 200 watch" in response.data

# def test_fetch_nonexistent_sale_by_id_from_filled_sales_records(client, three_test_products,two_test_sales):
#     for product in three_test_products:
#         client.post(
#             '/api/v1/products/create'
#             ,data = product
#             ,content_type='application/json'
#             )
#     for sale in two_test_sales:
#         client.post('/api/v1/sales/create_record'
#             ,data = sale
#             ,content_type='application/json')
#     response = client.get('/api/v1/sales/6')
#     assert b"Sale record not found!" in response.data
