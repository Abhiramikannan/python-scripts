#create venv
#install packages inside it
#save package to requirements.txt

import venv
import os
import subprocess
import sys
venv="abhi-venv"
path=os.path.join(os.getcwd(),venv)

#create venv
#if the commnd fails raise an error (check=True)
#subprocess.run=helps u to execute commands on terminal
print("craeting venv")
subprocess.run([sys.executable,"-m","venv",venv],check=True)


#set the path as pip inside the venv
#if its windows path setting ,else linux
if os.name=="nt":
        pip_path=os.path.join(path,"Scripts","pip.exe")
else:
        pip_path=os.path.join(path,"bin","pip")


#install package using venv's pip
packages=["requests","flask"]
subprocess.run([pip_path,"install",*packages],check=True)
print("package installed",packages)

#save packagae installed to requirements.txt
req_file=os.path.join(os.getcwd(),"requirements.txt")
with open("req_file","w")as f:
 subprocess.run([pip_path,"freeze"], stdout=f)

print("all done")


# mistakes
# after freeze ] 
#*packages =no ""
