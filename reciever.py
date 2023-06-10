"""
Script that plays the part of the receiver. Used for testing only.
"""
import time
from datetime import datetime
import requests


def format_message(item):
    """
    The helping function that formats a message
    :param item: Message
    :return: Formatted message
    """
    from_user = item['from']
    text = item['text']
    date_time = datetime.fromtimestamp(item['time']).strftime('%H:%M:%S %d.%m.%Y')
    return "from: {}\ntime: {}\ntext: {}\n".format(from_user, date_time, text)


while True:
    chat = input("Chat: ")
    user = input("User: ")
    print()
    response = requests.get('http://127.0.0.1:5000/messages', params={'chat': chat, 'user': user})
    if response.json()['status'] == 'false':
        print('Something went wrong!')
    else:
        messages = response.json()['messages']
        for message in messages:
            print(format_message(message))
    time.sleep(1)
