import os, time
import ast, json

from gevent import monkey
monkey.patch_all()

from flask import render_template,session
from flask.ext.socketio import SocketIO, emit
from service import app, api, mongo

socketio = SocketIO(app)


# @app.route('/junkware')
# def index():

#     global thread
#     if thread is None:
#         print 'start thread'
#         thread = Thread(target=background_thread)
#         thread.start()

#     return render_template('index.html')

# sockets
@socketio.on('my event', namespace='')
def test_message(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my response',
         {'data': message['data'], 'count': session['receive_count']})

@socketio.on('connect', namespace='')
def text_connect():
    emit('my response', {'data': 'Connected', 'count': 0})

@socketio.on('disconnect', namespace='')
def test_disconnect():
    print('Client disconnected')
