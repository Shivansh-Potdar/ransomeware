import os
from cryptography.fernet import Fernet

print('-'*50)
print("Welcome to your saving grace")
print("-"*50)

files = []

for filename in os.listdir(os.getcwd()):
    if filename == "ransomware.py" or filename == "thekey.key" or filename == "decryptor.py":
            continue
    if os.path.isfile(filename):
        files.append(filename)

with open("thekey.key", "rb") as thekey:
    key = thekey.read()

print(key)

#note works ok if individual file namea are manually entered
for file in files:
    with open(file, "rb") as m:
        contents = m.read()
    deM = Fernet(key).decrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(deM)

print('-'*50)
print("these files have been unfucked: {}".format(files))
print("-"*50)