import os 
from flask import Flask
from flask.ext import restful
from flask.ext.pymongo import PyMongo
from flask import make_response
from bson.json_util import dumps
import jinja2

MONGO_URL = os.environ.get('MONGO_URL')
if not MONGO_URL:
    MONGO_URL = "mongodb://localhost:27017/junks";

ASSETS_DIR=os.path.join(os.path.dirname(os.path.abspath(__file__)), '../static')

app = Flask(__name__)
app._static_folder = ASSETS_DIR
app.config['SECRET_KEY'] = 'secret!'
app.debug = True
app.jinja_loader=jinja2.FileSystemLoader('templates')

app.config['MONGO_URI'] = MONGO_URL
mongo = PyMongo(app)

def output_json(obj, code, headers=None):
    resp = make_response(dumps(obj), code)
    resp.headers.extend(headers or {})
    return resp

DEFAULT_REPRESENTATIONS = {'application/json': output_json}
api = restful.Api(app)
api.representations = DEFAULT_REPRESENTATIONS

import resources.routes
