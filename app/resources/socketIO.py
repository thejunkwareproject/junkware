import os, time
import ast, json

from gevent import monkey
monkey.patch_all()

from flask import render_template,session
from flask.ext.socketio import SocketIO, emit

from resources import app
from lib.queue import RedisQueue
from threading import Thread

socketio = SocketIO(app)
q = RedisQueue('mindwave')


def emit_eeg_through_websocket():
    """Example of how to send server generated events to clients."""
    count = 0

    while True:
        # print count
        time.sleep(1)
        count += 1
        point = q.get()
        point = ast.literal_eval(point)
        # print point

        # print EEG_series
        # print "new point"
        point['count'] = count
        point["time"]=int(time.time())

        # print point
        socketio.emit('brain', point, namespace='')


def start_eeg_socket_emit():
    print "start socket emit thread"
    socket_thread = None
    socket_thread = Thread(target=emit_eeg_through_websocket)
    socket_thread.start()

def stop_eeg_socket_emit():
    print "stop data"
    socket_thread.stop()


# sockets
@socketio.on('my event', namespace='')
def test_message(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my response',
         {'data': message['data'], 'count': session['receive_count']})

@socketio.on('eeg_start', namespace='')
def headset_connected():
    print "eeg start"
    start_eeg_socket_emit()
    emit('socket_thread',{'data': "socket started"})

@socketio.on('connect', namespace='')
def test_connect():
    emit('my response', {'data': 'Connected', 'count': 0})

@socketio.on('disconnect', namespace='')
def test_disconnect():
    socket_thread = None
    print('Client disconnected')

