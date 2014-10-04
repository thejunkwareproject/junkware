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
q_mindwave = RedisQueue('mindwave')
q_oxymeter = RedisQueue('oxymeter')


def emit_eeg_through_websocket():
    """Send oxymeter server generated events to clients."""
    count = 0

    while True:

        print "brain ",count
        time.sleep(1)
        count += 1
        point = q_mindwave.get()
        point = ast.literal_eval(point)

        # send
        point['count'] = count
        point["time"]=int(time.time())

        # print "emit brain"
        # print q_mindwave.qsize()
        socketio.emit('brain', point, namespace='')

def emit_oxymeter_through_websocket():
    """Example of how to send server generated events to clients."""
    count = 0

    while True:
        print "oxy ", count
        time.sleep(1)
        count += 1
        point = q_oxymeter.get()

        point = ast.literal_eval(point)

        point['count'] = count
        point["time"]=int(time.time())

        # print point
        socketio.emit('oxymeter', point, namespace='')

def start_eeg_socket_emit():
    print "start socket emit thread"
    # print q_mindwave.qsize()
    q_mindwave.clean()
    # print q_mindwave.qsize()
    eeg_socket_thread = None
    eeg_socket_thread = Thread(target=emit_eeg_through_websocket)
    eeg_socket_thread.start()

def stop_eeg_socket_emit():
    print "stop data"
    eeg_socket_thread.stop()

def start_oxymeter_socket_emit():
    print "start oxymeter socket emit thread"
    q_oxymeter.clean()
    oxymeter_socket_thread = None
    oxymeter_socket_thread = Thread(target=emit_oxymeter_through_websocket)
    oxymeter_socket_thread.start()

def stop_oxymeter_socket_emit():
    print "stop eeg data"
    oxymeter_socket_thread.stop()

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
    return {'message': "EEG socket started"}
    # emit('eeg_socket_thread',{'data': "EEG socket started"})

@socketio.on('oxymeter_start', namespace='')
def headset_connected():
    print "oxymeter start"
    start_oxymeter_socket_emit()
    return {'message': "Oxymeter socket started"}
    # emit('oxymeter_socket_thread',{'data': "oxymeter socket started"})

@socketio.on('connect', namespace='')
def test_connect():
    emit('my response', {'data': 'Connected', 'count': 0})

@socketio.on('disconnect', namespace='')
def test_disconnect():
    oxymeter_socket_thread = None
    print('Client disconnected')

