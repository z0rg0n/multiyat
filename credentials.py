# credentials.py
"""
This is how all the other functions interact with stored credentials.
Anything in the wherehouse can only be accessed through here.
"""
# Instead of passing the account name I should make a def in accounts that pulls it,

import getpass
import json
import requests


def new_account(base_url, new_name):
    # This will walk through creating a new API key and save it in the accountstorage.json file
    # email will also be stored at the users request else it will store 'email' = None
    print("Because this is a new account we need to get an API key.")
    print(
        "Follow the instructions at https://api-docs.y.at/docs/api_keys to generate an API Key and enter the access token below:")
    access_token = input(": ")

    bear_token = 'Bearer ' + access_token
    headers = {
        'Authorization': bear_token,
        'Content-Type': 'application/json'
    }  # Create the header used to request a new API key.

    available_accounts = requests.post(base_url + '/api_keys', json={'name': 'fromz0rgWith<3'},
                             headers=headers)  # Request a new API key.
    available_accounts = json.loads(available_accounts.text)

    if 'api_key' in available_accounts:  # Check if API key in available_accounts then write to file.
        with open('accountstorage.json', 'r') as file:  # Open account storage file.
            avaliable_accounts = json.load(file)  # Make it a dictionary

        # find the max value of 'order' and set new order to n+1
        # Save new order to dict
        new_order = 1 + find_max_order(avaliable_accounts)
        # 🎵 I'll find my soul as I go home 🎵#
        print("new_order to be added to dict:")
        print(new_order)

        # Will ask if they want to save an email and save result to dict
        print("Would you like to save email address locally?")
        new_email = save_email()

        avaliable_accounts[new_name] = {
            'order': new_order,
            'email': new_email,
            'account_cred': available_accounts,
            'Authorization': bear_token
        }

        print("New account added")

        with open('accountstorage.json', 'w+', encoding='utf-8') as file:
            json.dump(avaliable_accounts, file, ensure_ascii=False, indent=4)
        print(new_name + " api key and account stored.")
        return (new_order)
    else:
        print("No API key returned.")
        print(available_accounts)
        exit()


def save_email():
    # Return an email to be saved in accountstorage.json
    save_prompt = None
    while save_prompt is None:
        save_prompt = input("y/n: ")
        if save_prompt == 'y':
            print("Enter email to save: ")
            saved_email = input(": ")
            return (saved_email)
        elif save_prompt == 'n':
            saved_email = None
            return (saved_email)
        else:
            print("Enter y or n.")
            save_email = None


def find_max_order(accounts):
    # This finds the max value of 'order' so a new order value can be given to a new account
    max_order = 0
    for key in accounts:
        if accounts[key]['order'] > max_order:
            max_order = accounts[key]['order']
    return (max_order)


def login(base_url, account):
    # This will log in using a stored api key.
    # After sending the api key, email and, and password it will check if 2fa is required
    # If required it will ask to refresh 2fa from refresh_2fa
    # With the refreshed 2fa data it will submit a new 2fa code with submit_2fa
    # Then it will return a True status and account dict appended with refresh and auth tokens
    headers = create_xapi_head(account)  # Make header that will be passed later
    email = account['email']
    if email is None:
        print("Enter account email:")
        email = input(": ")

    print("Enter account password:")
    password = getpass.getpass(prompt=": ", stream=None)

    credentials = {
        'email': email,
        'password': password
    }
    json_credentials = json.dumps(credentials, skipkeys=True, separators=(',', ':')) # I don't know why but it doesn't work unless all the spaces are stripped out

    available_accounts = requests.post(base_url + '/auth/token', data=json_credentials, headers=headers)
    available_accounts = json.loads(available_accounts.text)  # Make the response a string so Python cand read it

    if 'error' in available_accounts:
        print(available_accounts)
        exit()
    elif 'requires_2fa' in available_accounts is not None:
        status, account = refresh_2fa(base_url, available_accounts, account)
        return(status, account)
    else:  # No 2fa required
        print("Log in successful")
        return(True, account)


def create_xapi_head(account):
    # Will create a header with the API key.
    # Need to be passed with 'api_key' as a key
    # Will pass header as dictonary (I think)
    api_key = str(account['account_cred']['api_key'])
    headers = {
        'Content-Type': 'application/json',
        'X-Api-Key': api_key
    }
    return (headers)


def create_yapi_head(account):
    # Attempt to try other headers because I keep getting returned following from emoji_id GET:
    # {"error":"Unauthorized: Missing auth token"}
    api_key = str(account['account_cred']['api_key'])
    access_token = str(account['access_token'])
    refresh_token = str(account['refresh_token'])
    headers = {
        'Content-Type': 'application/json',
        'X-Api-Key': api_key,
        'access_token': access_token,
        'refresh_token': refresh_token
    }
    return (headers)


def create_zapi_head(account):
    # Maybe I need to send the 'Access_Token' in the header as well.
    # This is the same authorizatiohn header used in new_account.
    api_key = str(account['account_cred']['api_key'])
    bear_token = str(account['Authorization'])

    headers = {
        'Content-Type': 'application/json',
        'X-Api-Key': api_key,
        'Authorization': bear_token
    }
    return (headers)


def refresh_2fa(base_url, available_accounts, account):
    # This asks for a new refresh ID. Then goes to submit_2fa with that new ID
    # submit_2fa will allow user to enter a new key and 'refresh' the auth token
    # Returns True and a dictonary with logged in account info
    headers = create_xapi_head(account)

    print("2fa required.")
    refresh_token = available_accounts['refresh_token']
    json_data = {
        'refresh_token': refresh_token
    }
    available_accounts = requests.post(base_url + '/auth/token/refresh', json=json_data, headers=headers)
    available_accounts = json.loads(available_accounts.text)
    access_token = available_accounts["access_token"]
    refresh_token = available_accounts["refresh_token"]
    status, account = submit_2fa(base_url, refresh_token, account)
    return (status, account)


def submit_2fa(base_url, refresh_token, account):
    # Refreshes the 2fa
    # Returns True and a dictonary with logged in account info
    # Shoulr return to refresh_2fa
    headers = create_xapi_head(account)
    print("account is:")
    print("Enter your 2fa code:")
    mfa_code = input(": ")  # Needs to have no spaces. Could steralize.
    data = {
        'code': mfa_code,
        'refresh_token': refresh_token
    }
    data = json.dumps(data)
    available_accounts = requests.post(base_url + '/auth/2fa', data=data, headers=headers)
    available_accounts = json.loads(available_accounts.text)

    access_token = available_accounts["access_token"]
    refresh_token = available_accounts["refresh_token"]
    account['access_token'] = access_token
    account['refresh_token'] = refresh_token

    print("Login successful")
    return (True, account)
