#Traverse all files in a given directory and print their full paths.
import os
path=os.path.abspath(".")
for root,files,dirs in os.walk(path): #go to every folders path
    for file in files:
        file_path=os.path.join(root,file)
        print(file_path)

