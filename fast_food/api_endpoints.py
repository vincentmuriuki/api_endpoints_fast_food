# Post order to /orders with method POST
import json
from flask import session, abort, request
from fast_food import app
from fast_food import models
from fast_food.models import orders


@app.route('/orders' , methods=['GET'])
def all_orders ():
    session.clear()
    session['order_list'] = models.orders
    return json.dumps(session['order_list'])

@app.route('/orders/<int:order_id>' , methods=['GET'])
def specific_order (order_id):
    session.clear()
    session['order_list'] = models.orders
    for i in session['order_list']:
        order = i.get(str('id'))
        if order == order_id:
            return json.dumps(i)
    abort(404)

@app.route('/orders', methods=['POST'])
def add_order ():
    order = request.get_json(silent=True)
    session['order_list'] = models.orders
    for i in session['order_list']:
        found = i.get(str('id'))
        if order['id'] == found:
            return "Exists"
    session['order_list'].append(order)
    return json.dumps(session['order_list'])


@app.route('/api/v1/orders/<int:order_id>', methods = ['PUT'])
def update_order(order_id):
    order = filter(lambda t: t['id'] == order_id, orders)
    if len(order) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'category' in request.json and type(request.json['category']) != unicode:
        abort(400)
    if 'food_type' in request.json and type (request.json['food_type']) is not unicode:
        abort(400)

    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)

    order[0]['id'] = request.json.get('category', order[0]['category'])
    order[0]['client_id'] = request.json.get('food_type', order[0]['food_type'])
    order[0]['status'] = request.json.get('price', order[0]['price']) 
    session['order_list'].append(order)
    return json.dumps(session['order_list'])