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
    headers = credentials.create_xapi_head(account) # Make header that will be passed later
#    print("Enter yat to edit:")
 #   yat = input(": ")#Try 🤘🐺🤘
 #   print("Enter data to be stored:")
 #   address = input(": ") #try 48bPRVkgvHwjG2VUTkPLaGazynZ6RxETuNGsYZNBrtb7ZkAUqY1NE2iGqoLd8EFsvhbDGW8gNb96Jce8fg2aiY8A5mbd8zf
  #  print("Enter tag (https://api-docs.y.at/docs/categories) of data:")
 #   tag = input(": ")#xmr wallet = 0x1001
    dict_data ={'insert':[{'data':'48bPRVkgvHwjG2VUTkPLaGazynZ6RxETuNGsYZNBrtb7ZkAUqY1NE2iGqoLd8EFsvhbDGW8gNb96Jce8fg2aiY8A5mbd8zf','tag':'0x1001'}]}

    print("URL is:")
    print(base_url+'/emoji_id/🤘🐺🤘')
    print("sent json_string:")
    print(dict_data)
    print(type(dict_data))
    print("Sent head:")
    print(headers)
    count = 0
    while (count < 2):
        responce1 = requests.post(base_url + '/emoji_id/🤘🐺🤘', json=dict_data, headers=headers)
        print("responce json is: ")
        print(responce1)
        print(responce1.text)
        responce = requests.post(base_url+'/emoji_id/🤘🐺🤘', data=dict_data, headers=headers)
        print("responce data is: ")
        print(responce)
        print(responce.text)
        dict_data = json.dumps(dict_data, skipkeys=True, separators=(',', ':'))
        dict_data = dict_data.replace("\\", "")
        count = count + 1
    print("json string in second two requests:")
    print(dict_data)
    print(type(dict_data))

    params = {'insert':[{'data':'48bPRVkgvHwjG2VUTkPLaGazynZ6RxETuNGsYZNBrtb7ZkAUqY1NE2iGqoLd8EFsvhbDGW8gNb96Jce8fg2aiY8A5mbd8zf','tag':'0x1001'}]}
    payload = {'insert': json.dumps(params, skipkeys=True, separators=(',', ':'))}
    count = 0
    while (count < 2):
        responce1 = requests.post(base_url + '/emoji_id/🤘🐺🤘', json=payload, headers=headers)
        print("responce json is: ")
        print(responce1)
        print(responce1.text)
        responce = requests.post(base_url+'/emoji_id/🤘🐺🤘', data=payload, headers=headers)
        print("responce data is: ")
        print(responce)
        print(responce.text)
        payload = json.dumps(payload, skipkeys=True, separators=(',', ':'))
        payload = payload.replace("\\", "")
        count = count + 1
    print("json string in second two requests:")
    print(payload)
    print(type(payload))

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

def delete_hash(base_url, account):
    headers = credentials.create_xapi_head(account) # Make header that will be passed later
#    print("Enter a yat target has is in:")
#    yat = input(": ")#Try 🤘🐺🤘

#    string_del = ('"delete":["cc99003dc1d247ee990267f5e7c0049971c698b1daefc31fbffa3c2f674c8a32"]')
#    print("Enter hash to delete:")
#    target = input(": ")
    dict_data = {
        'delete': [
            {
                'hash': 'cc99003dc1d247ee990267f5e7c0049971c698b1daefc31fbffa3c2f674c8a32'
            }
        ]
    }

    print("dict_data:")
    print(dict_data)
    print(type(dict_data))

    count = 0
    while (count < 2):
        responce1 = requests.post(base_url + '/emoji_id/🤘🐺🤘', json=dict_data, headers=headers)
        print("responce json:")
        print(responce1)
        print(responce1.text)
        responce = requests.post(base_url+'/emoji_id/🤘🐺🤘', data=dict_data, headers=headers)
        print("responce data:")
        print(responce)
        print(responce.text)
        dict_data = json.dumps(dict_data, skipkeys=True, separators=(',', ':'))
        dict_data = dict_data.replace("\\", "")
        count = count + 1
    print("json string in second two requests:")
    print(dict_data)
    print(type(dict_data))

    params = {'hash':'cc99003dc1d247ee990267f5e7c0049971c698b1daefc31fbffa3c2f674c8a32'}
    payload = {'delete': json.dumps(params, skipkeys=True, separators=(',', ':'))}
    count = 0
    while (count < 2):
        responce1 = requests.post(base_url + '/emoji_id/🤘🐺🤘', json=payload, headers=headers)
        print("responce json:")
        print(responce1)
        print(responce1.text)
        responce = requests.post(base_url+'/emoji_id/🤘🐺🤘', data=payload, headers=headers)
        print("responce data:")
        print(responce)
        print(responce.text)
        payload = json.dumps(payload, skipkeys=True, separators=(',', ':'))
        payload = payload.replace("\\", "")
        count = count + 1
    print("json payload in second two requests:")
    print(payload)
    print(type(payload))

    return()