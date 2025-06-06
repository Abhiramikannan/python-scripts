#rename,delete,move to another dir
import os

old_name="venv1.py"
new_name="venv2.py"
if os.path.exists(old_name):
    x=os.rename(old_name,new_name)
    print("renamed")
else:
    print("file not exists")


#delete
if os.path.exists("largefile.txt"):
    os.remove("largefile.txt")
    print("removed")
else:
    print("file not present")

#move
import shutil
file="pv.yaml"
destination =os.path.join(".","practice","pv.yaml")
if os.path.exists(file):
    shutil.move(file,destination)
    print("moved")
else:
    print("sorry pls try again ")


shutil.rmtree= deletes folder and subfolder
os.rmdir=dlte folder if folder is empty
