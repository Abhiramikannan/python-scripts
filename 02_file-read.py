import os
file_name="aami.txt"
file_path=os.path.join(os.getcwd(),file_name)
with open(file_path,"r") as f:
    f.read()
    print("read successfully")
