from cryptography.fernet import Fernet
import os

def write_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    #print(key)
    with open("key.key", "wb") as key_file:
        key_file.write(key)
        #print("key is saved successfully in " + os.path.abspath("key.key"))
    #return key
        