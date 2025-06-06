# create a directory named ust and create a text file inside that directory and ensure that the directory not existed before
import os 
directory_name = "abhi-dir"
filename="abhi-file"
file_path=os.path.join("abhi-dir","abhi-file")

try:
    os.makedirs(directory_name,exist_ok=True)
    print(f"directory '{directory_name}' created")
    with open(file_path,"w") as f:
        f.write("congrats")
        print(f"succesfully wrote to '{filename}'")
except IOError as e:
    print("error:{e}")
except Exception as e:
    print("error:{e}")
