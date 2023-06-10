"""
The server part of the messenger. Needs to be executed along with the main part
"""
from flask import Flask, request, abort
from datetime import datetime
import time

app = Flask(__name__)

chats = {
    'testing': {
        'length': 2,
        'members': {'Mike', 'Jack'},
        'messages': [
            {'id': 0, 'from': 'Mike', 'text': 'Hi, wanna hang out today?', 'time': time.time()},
            {'id': 1, 'from': 'Jack', 'text': 'Sorry, have to prepare for my finals((', 'time': time.time()}
        ]
    }
}

users = ['Mike', 'Jack']


@app.route("/")
def start():
    """
    The staring function
    """
    return 'Connection initialized. <a href="/status">See status</a>'


@app.route("/status")
def status():
    """
    The function that prints server status
    """
    return {
        'status': True,
        'name': 'Server',
        'time': datetime.now().strftime('%H:%M:%S %d.%m.%Y')
    }


@app.route("/connect")
def register():
    try:
        user = request.args['name']
    except:
        abort(400)
    if not isinstance(user, str) or not user or len(user) > 1024:
        abort(400)
    if user not in users:
        users.append(user)
    return {'status': 'true'}


@app.route("/adduser")
def add_user():
    try:
        chat = request.args['chat']
        user = request.args['user']
        who = request.args['who']
    except:
        abort(400)
    for token in [user, chat]:
        if not isinstance(token, str) or not token or len(token) > 1024:
            abort(400)
    if chat in chats and who in chats[chat]['members'] and user in users:
        chats[chat]['members'].add(user)
        return {'status': 'true'}
    else:
        return {'status': 'false'}


@app.route("/addchat")
def add_chat():
    try:
        chat = request.args['chat']
        user = request.args['user']
    except:
        abort(400)
    for token in [user, chat]:
        if not isinstance(token, str) or not token or len(token) > 1024:
            abort(400)
    if chat in chats:
        return {'status': 'false'}
    else:
        chats[chat] = {
            'length': 0,
            'members': {user},
            'messages': []
        }
        return {'status': 'true'}


@app.route("/send", methods=['POST'])
def send_view():
    user = request.json.get('from')
    chat = request.json.get('chat')
    text = request.json.get('text')
    for token in [user, chat, text]:
        if not isinstance(token, str) or not token or len(token) > 1024:
            abort(400)
    if chat in chats:
        room = chats[chat]
        if user in room['members']:
            room['messages'].append({'id': room['length'], 'from': user, 'text': text, 'time': time.time()})
            room['length'] += 1
            return {'status': 'true'}
        else:
            return {'status': 'false'}
    else:
        return {'status': 'false'}


@app.route("/messages")
def messages_view():
    try:
        chat = request.args['chat']
        user = request.args['user']
    except:
        abort(400)
    for token in [user, chat]:
        if not isinstance(token, str) or not token or len(token) > 1024:
            abort(400)
    if chat in chats:
        room = chats[chat]
        if user in room['members']:
            messages = room['messages']
            return {'status': 'true', 'messages': messages}
        else:
            return {'status': 'false', 'messages': []}
    else:
        return {'status': 'false', 'messages': []}


app.run()
