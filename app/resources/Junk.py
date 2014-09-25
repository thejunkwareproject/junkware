import os, time
import json
from threading import Thread

from gevent import monkey
monkey.patch_all()

from flask import request, abort, render_template, session, url_for
from flask.ext import restful
from flask.ext.restful import reqparse

from flask import make_response

from resources import app, api, mongo
from bson.objectid import ObjectId
from lib.queue import RedisQueue


# socketio = SocketIO(app)
thread = None

# data queue
q = RedisQueue('mindwave')

class Junk(restful.Resource):

    def get(self, junk_id):
        return mongo.db.junks.find_one_or_404({"_id": junk_id})

    def delete(self, junk_id):
        mongo.db.junks.find_one_or_404({"_id": junk_id})
        mongo.db.junks.remove({"_id": junk_id})
        return '', 204

class JunkList(restful.Resource):

    def __init__(self, *args, **kwargs):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('data', type=str)
        super(JunkList, self).__init__()

    def get(self):
        return  [x for x in mongo.db.junks.find()]

    def post(self):
        args = self.parser.parse_args()

        if not args['data']:
            abort(400)

        junk_id =  mongo.db.junks.insert(args)
        print junk_id
        return mongo.db.junks.find_one({"_id": junk_id})
