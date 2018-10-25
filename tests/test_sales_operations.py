import pytest

def test_fetch_all_sales_records_before_creating_any(client):
    response = client.get('/v1/sales/get_all_records')
    assert b"There are no sales records to show!" in response.data

def test_fetch_sale_record_byId_before_creating_any(client):
    response = client.get('/v1/sales/1')
    assert b"There are no sales records to show!" in response.data

