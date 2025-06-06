
import os
#dir creating
dir_name= "aami-dir1"
dir_path=os.path.join(os.getcwd(),dir_name)
os.makedirs(dir_path,exist_ok=True)
print(dir_name,"created succesfully")
file_name="aami.txt"
file_path=os.path.join(dir_path,file_name)
with open("file_path","w") as f:
    f.write("succeeded kutta") #pass.//create without content
    print("wrote to",file_name)
