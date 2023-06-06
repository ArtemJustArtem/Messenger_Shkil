from flask import Flask, request, abort
from datetime import datetime
import time

app = Flask(__name__)
messages = [
    {'from': 'Mike', 'to': 'Jack', 'text': 'Hi, wanna hang out today?', 'time': time.time()},
    {'from': 'Jack', 'to': 'Mike', 'text': 'Sorry, have to prepare for my finals((', 'time': time.time()}
]
users = ['Mike', 'Jack']


@app.route("/")
def start():
    return 'Connection initialized. <a href="/status">See status</a>'


@app.route("/status")
def status():
    return {
        'status': True,
        'name': 'Server',
        'time': datetime.now().strftime('%H:%M:%S %d.%m.%Y')
    }


@app.route("/connect")
def check_user():
    try:
        user = request.args['name']
        signin = request.args['signin']
    except:
        abort(400)
    if user in users:
        return {'status': 'true'}
    else:
        if signin == 'true':
            users.append(user)
            return {'status': 'true'}
        else:
            return {'status': 'false'}


@app.route("/send", methods=['POST'])
def send_view():
    from_user = request.json.get('from')
    to_user = request.json.get('to')
    text = request.json.get('text')

    for token in [from_user, to_user, text]:
        if not isinstance(token, str) or not token or len(token) > 1024:
            abort(400)

    messages.append({'from': from_user, 'to': to_user, 'text': text, 'time': time.time()})
    return {'status': True}


def filter_messages(items, from_user, to_user):
    result = []

    for item in items:
        if item['from'] in [from_user, to_user] and item['to'] in [from_user, to_user]:
            result.append(item)

    return result


@app.route("/messages")
def messages_view():
    try:
        from_user = request.args['from']
        to_user = request.args['to']
    except:
        abort(400)
    filtered_messages = filter_messages(messages, from_user, to_user)
    return {'messages': filtered_messages}


app.run()