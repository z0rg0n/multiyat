# login.py
"""
Were user can manage accounts available to app
"""

import credentials
import json


# need to make delete_account()

def select_account(base_url):
    # This will select an account and return the avaliable account info as a dict.

    with open('accountstorage.json', 'r') as file:
        available_accounts = json.load(file)  # Load the stored account info as dictonary

    for key in available_accounts:
        print(available_accounts[key]['order'], end='   :   ')
        print(key)
    print("key : account")
    print("Pick a key or send 'new'")
    # Prints out the avaliable accounts and presents keys to select
    selected_account = input(": ")

    # if a new account is selected it will send credentials.new_account the url and the name
    # credentials will then walk through creating an API key and return the dict
    if selected_account == 'new':
        print("Enter a local name for the new account:")
        new_name = input(": ")
        account_key = credentials.new_account(base_url, new_name)
        with open('accountstorage.json', 'r') as file:
            available_accounts = json.load(file)  # Load the stored account info as dictionary
        selected_account = int(account_key)
        for key in available_accounts:
            if available_accounts[key]['order'] == selected_account:
                account = available_accounts[key]
        return (account)
    else:  # If an available account is selected it will just return a dict of that account info.
        for key in available_accounts:
            selected_account = int(selected_account)
            print("Looking for selected account :")
            print(selected_account)
            if available_accounts[key]['order'] == selected_account:
                account = available_accounts[key]
        return (account)
