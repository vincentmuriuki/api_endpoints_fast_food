# API tests
import json
import requests
import fast_food

client = fast_food.app.test_client()

def test_retrieve_all_orders():
    t = client.get('http://127.0.0.1:5000/orders')
    assert t.status_code == 200


def test_get_specific_order(request_mock):
    data = {
        "order_id" : 85,
        "customer_id" : 4324,
        "order_status" : ""
    }
    client.post('http://127.0.0.1:5000/orders', json=data)
    t = client.get('http://127.0.0.1:5000/orders/85')
    assert t.status_code == 200

    t_two = client.get('http://127.0.0.1:5000/orders/86')
    assert t_two.status_code == 404


def test_post_endpoint(request_mock):
    data = {
        "order_id" : 52,
        "customer_id": 1995,
        "status": ""
    }

    initial = client.get('http://127.0.0.1:5000/orders/52')
    client.post('http://127.0.0.1:5000/orders', json=data)
    final = client.get('http://127.0.0.1:5000/orders/52')
    assert initial.status_code == 404
    assert final.status_code == 200

def test_put(request_mock):
    data = {
        "order_id": 60,
        "customer_id": 1999,
        "status": ""
    }
    update = {
        "status": "completed"
    }
    updated = {
        "order_id": 60,
        "customer_id": 1999,
        "status": "completed"
    }

    client.post('http://127.0.0.1:5000/orders', json=data)
    client.put('http://127.0.0.1:5000/orders/60', json=data)
    output = client.get('http://127.0.0.1:5000/orders/60')
    assert json.loads(output.get_data()) == updated


