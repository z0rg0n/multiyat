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
Prequisits:
- git
- python
```
# Navigate to the folder you want to install in and clone with git
# Note a new folder 'multiyat' will be created for the contents of the git
git clone https://github.com/z0rg0n/multiyat.git

# Navigate to the newly created folder
cd multiyat/

# Install the requirements
pip install -r requirements.txt
```

## Usage
```
# Run the head from the folder in the cloned reposotory
python head.py
```
