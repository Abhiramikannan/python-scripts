# Use os.walk() to list all .txt files in a directory and its subdirectories.
import os
path=os.path.abspath(".")
for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith(".txt"):
            full_path=os.path.join(root,file)
            print(full_path)
