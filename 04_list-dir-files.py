#listing dirs and files
import os
path=os.path.abspath(".")
x=os.listdir(path)
for item in x:
    full_path=os.path.join(path,item)
    if os.path.isfile(full_path):
        print(item,"file")
    elif os.path.isdir(full_path):
        print(item,"directory")
    else:
        print("not a directory,not a file")
