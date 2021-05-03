lst = ["aakash","hello","world"]

def list2file(lst):
    for i in lst:
        with open("file.txt","a") as line:
            line.write(i+"\n")
            
            