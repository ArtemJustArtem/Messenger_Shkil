"""
Script that plays the part of the sender. Used for testing only.
"""
import requests


while True:
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