"""
Script that plays the part of the sender. Used for testing only.
"""
import requests


while True:
    """
    from_user = input('From: ')
    to_user = input('To: ')
    text = input('Text: ')
    response = requests.get('http://127.0.0.1:5000/connect', params={'name': from_user, 'signin': 'true'})
    if response.json()['status'] == 'true':
        response = requests.get('http://127.0.0.1:5000/connect', params={'name': to_user, 'signin': 'false'})
        if response.json()['status'] == 'true':
            message = {'from': from_user, 'to': to_user, 'text': text}
            response = requests.post('http://127.0.0.1:5000/send', json=message)
        else:
            print('to user is not found')
    else:
        print('from user cannot sign in')
    """
    if input('add chat (y/n): ') == 'y':
        chat = input('Chat: ')
        user = input('User: ')
        response = requests.get('http://127.0.0.1:5000/connect', params={'name': user})
        response = requests.get('http://127.0.0.1:5000/addchat', params={'chat': chat, 'user': user})
        if response.json()['status'] == 'true':
            print('Success\n')
        else:
            print('Something went wrong\n')
    elif input('add user (y/n): ') == 'y':
        chat = input('Chat: ')
        user = input('User: ')
        new = input('New user: ')
        response = requests.get('http://127.0.0.1:5000/connect', params={'name': user})
        response = requests.get('http://127.0.0.1:5000/adduser', params={'chat': chat, 'who': user, 'user': new})
        if response.json()['status'] == 'true':
            print('Success\n')
        else:
            print('Something went wrong\n')
    else:
        chat = input('Chat: ')
        user = input('User: ')
        text = input('Text: ')
        response = requests.post('http://127.0.0.1:5000/send', json={'from': user, 'chat': chat, 'text': text})
        if response.json()['status'] == 'true':
            print('Success\n')
        else:
            print('Something went wrong\n')