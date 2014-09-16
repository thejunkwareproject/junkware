import os, time
from threading import Thread
import ast, json

from gevent import monkey
monkey.patch_all()

from flask import render_template,session
from flask.ext.socketio import SocketIO, emit
from lib.queue import RedisQueue
from service import app, api, mongo

thread = None
socketio = SocketIO(app)

# data queue
q = RedisQueue('mindwave')

def background_thread():
    """Example of how to send server generated events to clients."""
    count = 0

    while True:
        time.sleep(1)
        count += 1
        point = q.get()
        point = ast.literal_eval(point)

        # print EEG_series
        print "new point"
        point['count'] = count
        point["time"]=int(time.time())

        # print point
        socketio.emit('brain', point, namespace='')

@app.route('/junkware')
def index():

    global thread
    if thread is None:
        print 'start thread'
        thread = Thread(target=background_thread)
        thread.start()

    return render_template('index.html')

# sockets
@socketio.on('my event', namespace='')
def test_message(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my response',
         {'data': message['data'], 'count': session['receive_count']})

@socketio.on('connect', namespace='')
def test_connect():
    emit('my response', {'data': 'Connected', 'count': 0})

@socketio.on('disconnect', namespace='')
def test_disconnect():
    print('Client disconnected')
