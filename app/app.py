from resources import app
from resources.socketIO import socketio, emit
from threading import Thread
from lib.queue import RedisQueue
from flask import render_template

import os, sys, time, ast
# from lib.generator import MarkovGenerator
from lib.corpus import *

# set encoding to UTF-8
reload(sys)  
sys.setdefaultencoding('utf8')

# init patents db
patents=PatentCorpus('../../junkware-data/patents/Patents.sqlite3')

# init mindwave data thread
thread = None
q = RedisQueue('mindwave')

def background_data_thread():
    """Example of how to send server generated events to clients."""
    count = 0

    while True:
        print count
        time.sleep(1)
        count += 1
        point = q.get()
        point = ast.literal_eval(point)
        print point

        # print EEG_series
        print "new point"
        point['count'] = count
        point["time"]=int(time.time())

        # print point
        socketio.emit('brain', point, namespace='')

def create_data_thread():
    thread = Thread(target=background_data_thread)
    thread.start()

def start_data_thread():
    print 'start thread'
    thread.start()

def stop_data_thread():
    print "stop data"
    thread.stop()

# @app.route('/junk/<objectId>')
# def junwkare(objectId):
#     global thread
#     if thread is None:
#         create_data_thread()
#     return render_template('junk/view.html', objectId=objectId)

# @socketio.on('getdesc', namespace='')
# def test_message(message):

#     # Create an object
#     desc = get_description()

#     socketio.emit("description", desc, namespace='')

#run app
if __name__ == '__main__':
    socketio.run(app)

# deployment notes :http://spapas.github.io/2014/06/30/rest-flask-mongodb-heroku/

