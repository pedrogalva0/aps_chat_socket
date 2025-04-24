from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, join_room, leave_room
import uuid

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

users = {}
rooms = {}

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    user_id = f"temp_{str(uuid.uuid4().int)[:12]}"
    users[request.sid] = user_id
    emit('user_list', list(users.values()), broadcast=True)
    emit('assign_id', user_id)

@socketio.on('set_username')
def set_username(data):
    users[request.sid] = data
    emit('user_list', list(users.values()), broadcast=True)

@socketio.on('create_or_join_room')
def handle_room(data):
    join_room(data['room'])
    rooms[request.sid] = data['room']
    emit('message', {'msg': f"{users[request.sid]} entrou na sala {data['room']}"}, room=data['room'])

@socketio.on('send_message')
def handle_message(data):
    room = rooms.get(request.sid)
    if room:
        emit('message', {'msg': f"{users[request.sid]}: {data['msg']}"}, room=room)

@socketio.on('disconnect')
def handle_disconnect():
    user = users.pop(request.sid, None)
    room = rooms.pop(request.sid, None)
    emit('user_list', list(users.values()), broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
