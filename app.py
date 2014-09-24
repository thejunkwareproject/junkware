from resources import app
from resources.socketIO import socketio, emit
from threading import Thread
from lib.queue import RedisQueue
from flask import render_template

import os, sys, time, ast
from lib.generator import ObjectGenerator
from lib.nlp import NLP
from lib.corpus import *

# set encoding to UTF-8
reload(sys)  
sys.setdefaultencoding('utf8')

# init patents db
patents=PatentCorpus('../junkware-data/patents/Patents.sqlite3')

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

@app.route('/junkware')
def index():


    global thread
    if thread is None:
        create_data_thread()
    return render_template('index.html')

def get_description():
    test_corpus_path = os.path.join(os.getcwd(), 'corpus')
    weird_object = ObjectGenerator(test_corpus_path)

    # add random records from patents db
    for patent in patents.get_records(10, random=True):
        weird_object.add_to_corpus(patent)

    # create corpus
    weird_object.load_corpus()

    # print "weird_object",len(weird_object.corpus)
    descriptions = weird_object.generate_definition(1, 15)
    return descriptions


@socketio.on('getdesc', namespace='')
def test_message(message):

    # Create an object
    desc = get_description()

    socketio.emit("description", desc, namespace='')

#run app
if __name__ == '__main__':
    socketio.run(app)

# deployment notes :http://spapas.github.io/2014/06/30/rest-flask-mongodb-heroku/
