# emoji_id.py
"""
Endpoints for interacting and managing your yats.
https://api-docs.y.at/docs/api-ref#emoji-id
"""

import credentials

import json
import requests

def owned_list(base_url, account):
    headers = credentials.create_xapi_head(account) # Make header that will be passed later
    print("headers sent")
    print(headers)
    responce = requests.get(base_url + '/emoji_id', headers=headers)
    print(responce)
    print(responce.text)