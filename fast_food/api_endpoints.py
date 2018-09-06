# API endpoints

import json
from flask import session, abort, request
from fast_food import app
from fast_food import models
from fast_food.models import orders


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

@app.route('/orders' , methods=['GET'])
def all_orders ():
    session.clear()
    session['order_list'] = models.orders
    return json.dumps(session['order_list'])

# API endpoint to fetch a specific order
@app.route('/orders/<int:order_id>', methods = ['GET'])
def specific_order(order_id):
    session.clear()
    session['order_list'] = models.orders
    for j in session['order_list']:
        order = j.get(str('id'))
        if order == order_id:
            return json.dumps(j)
        abort(404)
