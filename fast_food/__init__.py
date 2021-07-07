from flask import Flask




app = Flask(__name__) 
app.config['SECRET_KEY'] = 'choco'
app.config['SESSION_TYPE'] = 'session'

from fast_food import api_endpoints
from fast_food import models


# Get all orders at /orders