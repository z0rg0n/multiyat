# multiyat
`multiyat` is a python script that will allow you to interact with yat API.
Apart from saving the API key and the optional saving of the yat account email; all features are simple interactions with the yat API.


## Features
- List emojis in yat library for simple copy and pasting
- List all owned yats
- Lookup the public information associated to a yat
- Assign a [yat record](https://api-docs.y.at/docs/categories) to multipule yats at once.
- Delete a specific yat record based on the [hash](https://api-docs.y.at/docs/api-ref#parameters-18) of that record (see Edit EmojiId section).

### Features to Add
- Continuous scanning of a list of owned and 'followed' yats and saving of any changes to those yats to a MongoDB database

### Quality of Life Improvements
- Allow copying and pasting of returned owned yat list directly into assign yat record function
- Allow grouping of owned yats based on yat properties and user assigned properties


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
# Run the head
python head.py
```
