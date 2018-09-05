# 

import json
from flask import session, abort, request
from fast_food import app


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
