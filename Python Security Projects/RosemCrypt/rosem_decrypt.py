#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet
files = []

for file in os.listdir():
    if file == "rosem_crypt.py" or file == "rosem_decrypt.py" or file == "thekey.key":
        continue
    if os.path.isfile(file):
        files.append(file)

    

print(files)

with open("thekey.key", "rb") as key:
    secretkey = key.read()

for file in files:
    with open(file, "rb") as thefile:
        contents_encrypted = thefile.read()
        contents = Fernet(secretkey).decrypt(contents_encrypted)
        with open(file, "wb") as thefile:
            thefile.write(contents)