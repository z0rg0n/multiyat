# head.py
"""
This will be where you call functions via a list of available actions.
"""

import accounts
import credentials
import emoji_id

base_url = 'https://a.y.at'


def user_request (user_input):
    print("Type 'help' for a list of commands.")

    if user_input == 'help':
        print("Available Commands:")
        print("help      : print this list")
        print("login     : login to a yat account:")
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



def logged_in_menu(account):
    print("Type 'help' for a list of commands.")

    while True:
        user_input = input(": ")
        if user_input == 'help':
            print("help       : print this message")
            print("list yats  : list owned yats")
            print("yat lookup : lookup the info of a yat")
            print("char       : valid emoji characters")
            print("set        : set crypto address")
            print("delete     : delete hash data")
            print("calc rs    : calculate a yat RS")
        elif user_input == 'list yats':
            emoji_id.owned_list(base_url, account)
        elif user_input == 'yat lookup':
            emoji_id.lookup(base_url)
        elif user_input == 'char':
            emoji_id.emoji_characters(base_url, account)
        elif user_input == 'set':
            emoji_id.store(base_url, account)
        elif user_input == 'delete':
            emoji_id.delete_hash(base_url, account)
        elif user_input == 'calc rs':
            emoji_id.calc_rs(base_url)

while True:
   print("Type 'help' for a list of commands.")
   user_input = input(": ")
   user_request(user_input)
