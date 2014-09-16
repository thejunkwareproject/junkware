import os, time
import json
from threading import Thread

from gevent import monkey
monkey.patch_all()

from flask import request, abort, render_template, session, url_for
from flask.ext import restful
# from flask.ext.socketio import SocketIO, emit
from flask.ext.restful import reqparse
# from flask.ext.pymongo import PyMongo

from flask import make_response

from service import app, api, mongo
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
        self.parser.add_argument('junk', type=str)
        super(JunkList, self).__init__()

    def get(self):
        return  [x for x in mongo.db.junks.find()]

    def post(self):
        args = self.parser.parse_args()
        if not args['junk']:
            abort(400)

        jo = json.loads(args['junk'])
        junk_id =  mongo.db.junks.insert(jo)
        return mongo.db.junks.find_one({"_id": junk_id})

api.add_resource(JunkList, '/api/junks')
api.add_resource(Junk, '/api/junk/<ObjectId:junk_id>')

# STATIC
@app.route('/js/<path:path>')
def js_static_proxy(path):
    # send_static_file will guess the correct MIME type
    return app.send_static_file(os.path.join('js', path))

@app.route('/css/<path:path>')
def css_static_proxy(path):
    print path
    # send_static_file will guess the correct MIME type
    return app.send_static_file(os.path.join('css', path))

@app.route('/lib/<path:path>')
def lib_static_proxy(path):
    # send_static_file will guess the correct MIME type
    return app.send_static_file(os.path.join('lib', path))

@app.route('/libs/<path:path>')
def libs_static_proxy(path):
    # send_static_file will guess the correct MIME type
    return app.send_static_file(os.path.join('libs', path))

# SOCKET.IO

# data queue
# q = RedisQueue('mindwave')

# def background_thread():
#     """Example of how to send server generated events to clients."""
#     count = 0

#     while True:
#         time.sleep(1)
#         count += 1
#         point = q.get()
#         point = ast.literal_eval(point)

#         # print EEG_series
#         print "new point"
#         point['count'] = count
#         point["time"]=int(time.time())

#         # print point
#         socketio.emit('brain', point, namespace='/junkware')

# @app.route('/')
# def index():

#     global thread
#     if thread is None:
#         print 'start thread'
#         thread = Thread(target=background_thread)
#         thread.start()

#     return render_template('index.html')

# # sockets
# @socketio.on('my event', namespace='')
# def test_message(message):
#     session['receive_count'] = session.get('receive_count', 0) + 1
#     emit('my response',
#          {'data': message['data'], 'count': session['receive_count']})

# @socketio.on('connect', namespace='')
# def test_connect():
#     emit('my response', {'data': 'Connected', 'count': 0})

# @socketio.on('disconnect', namespace='')
# def test_disconnect():
#     print('Client disconnected')
