def load_key():
    with open("key.key","rb") as key:
        key = key.read()
    return key