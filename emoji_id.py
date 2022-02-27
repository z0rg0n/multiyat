# emoji_id.py
"""
Endpoints for interacting and managing your yats.
https://api-docs.y.at/docs/api-ref#emoji-id
"""

import credentials

import json
import requests
import pprint

def store(base_url, account):
    headers = credentials.create_zapi_head(account) # Make header that will be passed later
    print("Enter yat to edit:")
    yat = input(": ")
    print("Enter data to be stored:")
    stored_data = input(": ")
    print("Enter tag (https://api-docs.y.at/docs/categories) of data:")
    tag_data = input(": ")
    dictData = {
        'data': None,
        'linked_tags': [
            {
                'data': stored_data,
                'tag': tag_data
            }
        ]
    }
    responce = requests.post(base_url + '/emoji_id/'+yat+"YatPageData", json=dictData, headers=headers)
    print("responce is: ")
    print(responce)
    print(responce.text)
    return()

def emoji_characters(base_url, account):
    headers = credentials.create_zapi_head(account) # Make header that will be passed later
    responce = requests.get(base_url + '/emoji', headers=headers)
    obj = json.loads(responce.text)
    print("Avaliable emojis are:")
    print(responce.text)

def owned_list(base_url, account):
    headers = credentials.create_zapi_head(account) # Make header that will be passed later
    responce = requests.get(base_url + '/emoji_id', headers=headers)
    print(responce)
    obj = json.loads(responce.text)
    print("Owned yats:")
    pprint.pprint(obj)
    return()

def lookup(base_url):
    print("enter a yat to lookup:")
    yat = input(": ")
    responce = requests.get(base_url + '/emoji_id/' + yat)
    print(responce)
    obj = json.loads(responce.text)
    print("Yat info:")
    pprint.pprint(obj)
    return()