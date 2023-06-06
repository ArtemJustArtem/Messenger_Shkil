import time
from datetime import datetime
import requests


def format_message(item):
    from_user = item['from']
    to_user = item['to']
    text = item['text']
    date_time = datetime.fromtimestamp(item['time']).strftime('%H:%M:%S %d.%m.%Y')
    return "from: {}\nto: {}\ntime: {}\ntext: {}\n".format(from_user, to_user, date_time, text)


while True:
    user_from = input("From: ")
    user_to = input("To: ")
    print()
    response = requests.get('http://127.0.0.1:5000/messages', params={'from': user_from, 'to': user_to})
    messages = response.json()['messages']
    for message in messages:
        print(format_message(message))

    time.sleep(1)
