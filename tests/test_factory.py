from StoreManager import create_app


def test_homepage(client):
    response = client.get('/')
    assert b"Welcome to Polos Store Manager API!", 200 in response.data 
            