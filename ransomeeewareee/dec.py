from cryptography.fernet import Fernet
from loadkey import load_key
import os

def decrypt(filename,key):
    f = Fernet(key)
    with open(filename,"rb") as content:
        content = content.read()
        
    decrypted_data = f.decrypt(content)
    
    with open(filename+".dec","wb") as content:
        content.write(decrypted_data)

# path = "/home/pi/Documents/ransomware/text.txt.enc"
# key = load_key()
# decrypt(path,key)
    