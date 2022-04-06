# multiyat
`multiyat` is a python script that will allow you to interact with yat API.
Apart from saving the API key and the optional saving of the yat account email; all features are simple interactions with the yat API.


## Features
- List emojis in yat library for simple copy and pasting
- List all owned yats [(implemented with workaround)](https://github.com/z0rg0n/multiyat/issues/5)
- Lookup the public information associated to a yat
- Assign a [yat record](https://api-docs.y.at/docs/categories) to multipule yats at once.
- Delete a specific yat record based on the [hash](https://api-docs.y.at/docs/api-ref#parameters-18) of that record (see Edit EmojiId section in yat API guide).


### Features to Add
- Continuous scanning of a list of owned and 'followed' yats and saving of any changes to those yats to a MongoDB database

### Quality of Life Improvements
- Allow grouping of owned yats based on yat properties and user assigned properties
- Instead of prompting a user for a tag have a list of supported data and insert tag from that selection


## Installation

### Debian
Prerequisites:
- git
- python
```
# Navigate to the folder you want to install in and clone with git
git clone https://github.com/z0rg0n/multiyat.git

# Navigate to the newly created folder
cd multiyat/

# Install the requirements
pip install -r requirements.txt
```

### Windows
Prerequisite:
- python
- pip
(https://www.liquidweb.com/kb/install-pip-windows/)
```
# Download the app
Click the code button on the https://github.com/z0rg0n/multiyat page and download the zip.
Extract the zip

# Running the app
Open up a command prompt and navigate into the folder created when you extracted the zip to.

# Install the requirements by typing this into the console:
pip install -r requirements.txt
```


## Usage
```
# Run the head from the folder in the cloned reposotory
python head.py

# You should see the splash line '♾️💻⛓️💻♾️'
```

### Associate Monero address to your yat
```
# Login to your yat account
Enter 'login'
Enter 'new'
Pick a name for the account that will be stored locally

# Generate a new API key (https://api-docs.y.at/docs/api_keys)
Login to your yat account from a browser.
Open a console on the page (right click inspect element then find the 'Console' section)
Paste and send this command:
JSON.parse(localStorage.getItem('tokens')).access_token
Copy the returned text without the 's and paste it back into the console

# Save an email to the account if you want
Enter the email address that has the yat you want to associate a Monero address to.
Enter your password
Enter your 2fa code if applicable
You should get a 'Login successful' message

# Set the Monero address
Type 'set'
Enter the yat you want to associate the Monero address to (note you can use the 'list yats' or 'char' commands to help with entering emojis
For the data to be stored enter your Monero address
For the 'tag' enter 0x1001 for a standard Monero address and 0x1002 for a sub address
You should be returned a 200 code

# Verify it worked
Type 'yat lookup'
Enter the yat you want to lookup
You should see the tag and Monero address you entered.


Note: You can enter multipule yats seperated by ' , [ and/or ] when using the set command
```
