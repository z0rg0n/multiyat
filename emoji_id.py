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
    headers = credentials.create_xapi_head(account)  # Make header that will be passed later

# Get the yat or yats that we will be editing.
    ok = False
    while ok is False:
        print("Enter yats to edit or help:")
        yat = input(": ")
        while yat == 'help':
            print("Enter the emojis of a yat you own on this account to change the data stored in your yat.")
            print("You can also enter multiple yats separated by a \',\'")
            print("Enter yats to edit or help:")
            yat = input(": ")
        ok = True
    yat = yat.replace(" ", "")
    yat = yat.split(',')

# Get the data the user wants to store
    print("Enter data to be stored:")
    address = input(": ")

# Get the tag of the data from the user and helps them to determine the correct tag
    ok = False
    while ok is False:
        print("Enter tag of data or 'help':")
        tag = input(": ")
        while tag == 'help':
            print("Tags are how data type is determined on your yat page.")
            print("For example: a tag of \"0x0004\" is a redirect and a tag of \"0x0005\" is the rainbow title.")
            print("A reference with available tags can be found here: https://api-docs.y.at/docs/categories")
            print("Enter tag of data or 'help':")
            tag = input(": ")  # xmr wallet = 0x1001
        ok = True

    dict_data = {'insert': [{'data': address, 'tag': tag}]}

    for i in range(len(yat)):
        response = requests.patch(base_url + '/emoji_id/' + yat, json=dict_data, headers=headers)
        print(yat + "edit results:")
        print(response)
        print(response.text)

    return ()


def multi_set(base_url, account):
    headers = credentials.create_xapi_head(account)  # Make header that will be passed later
    print("Enter the yats you want to edit separated by a comma")


def emoji_characters(base_url, account):
    headers = credentials.create_zapi_head(account)  # Make header that will be passed later
    responce = requests.get(base_url + '/emoji', headers=headers)
    obj = json.loads(responce.text)
    print("Avaliable emojis are:")
    print(responce.text)


def owned_list(base_url, account):
    headers = credentials.create_zapi_head(account)  # Make header that will be passed later
    responce = requests.get(base_url + '/emoji_id', headers=headers)
    obj = json.loads(responce.text)
    if 'error' in responce:
        print(responce)
        print(responce.text)
        return ()
    print(responce)
    print("Owned yats:")
    pprint.pprint(obj)
    return ()


def lookup(base_url):
    print("enter a yat to lookup:")
    yat = input(": ")
    responce = requests.get(base_url + '/emoji_id/' + yat)
    print(responce)
    obj = json.loads(responce.text)
    print("Yat info:")
    pprint.pprint(obj)
    return ()


def delete_hash(base_url, account):
    headers = credentials.create_xapi_head(account)  # Make header that will be passed later
    print("Enter a yat target has is in:")
    yat = input(": ")  # Try 🤘🐺🤘
    print("Enter hash to delete:")
    target = input(": ")  # try cc99003dc1d247ee990267f5e7c0049971c698b1daefc31fbffa3c2f674c8a32
    dict_data = {
        'delete': [
            {
                'hash': target
            }
        ]
    }

    responce = requests.post(base_url + '/emoji_id/' + yat, json=dict_data, headers=headers)
    print(responce)
    print(responce.text)

    return ()
