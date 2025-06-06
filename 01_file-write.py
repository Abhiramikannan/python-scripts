import os
def file_writing():
    file_path=os.path.join(os.getcwd(),"aami.txt")
    with open(file_path,"w") as f:
        f.write("hello aami")
        print("written succesfully")

file_writing()
