from service import app
from service.socketIO import socketio

#run app
socketio.run(app)

