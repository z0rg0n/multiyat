# head.py
"""
This will be where you call functions via a list of avaliable actions.
"""

import accounts
import credentials
import emoji_id

base_url = 'https://a.y.at'


def user_request (user_input):
    if user_input == 'help':
        print("Avaliable Commands:")
        print("help      : print this list")
        print("login     : login to a yat account:")
        print("manage    : manage yat accounts")
        print("exit      : exit program")
        return()
    elif user_input == 'login':
        account_info = accounts.select_account(base_url) # Returns a dictonary of account info
        print("sending account info to credentials...")
        logged_in, account = credentials.login(base_url, account_info)
        if logged_in: # If log in successful it will take to logged in menu
            logged_in_menu(account) # This menu will have tools avaliable when auththenticated by apiKey
        else:
            print("login failed")
    elif user_input == 'manage':
        print("Not built yet...")
        #accounts.manage(base_url)
        return ()
    elif user_input == 'exit':
        exit() # should also revoke all access and log out of yat or whatever.

print("Type 'help' for a list of commands.")


def logged_in_menu(account): # Currently a dead end. Can't get past error.
    print("list yats : list owned yats")
    user_input = input(": ")
    if user_input == 'list yats':
        emoji_id.owned_list(base_url, account)

while True:
   user_input = input(": ")
   user_request(user_input)