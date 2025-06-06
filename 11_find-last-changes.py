#Question: Write a function which finds changes in a directory since you last searched using

# os.listdir() to get file names
# os.path.getmtime() to get file modification times
# json to save and load previous scan info


#Write a function which finds changes in a directory since you last searched using
import os
import json
dir_path=os.path.abspath(".")
snapshot={} # empty dictionary
if os.path.exists("snapshot.json"):
    with open('snapshot.json',"r") as f:
        old_snapshot=json.load(f)
        
else:
    old_snapshot={}

x=os.listdir(dir_path)
print(x)
for items in x:
    full_path=os.path.join(dir_path,items)
    if os.path.isfile(full_path):
        print("file")
        snapshot[items]=os.path.getmtime(full_path)
    elif os.path.isdir(full_path):
        print("directory")
    else:
        print("not a directory and not a file")
#compare
added=[f for f in snapshot if f not in old_snapshot]
deleted=[f for f in old_snapshot if f not in snapshot]
modified=[f for f in snapshot if f in old_snapshot and snapshot[f]!=old_snapshot[f]]

if added:
    print("added")
elif deleted:
    print("deleted")
elif modified:
    print("modified")
else:
    print("u fucked up")

#old snapshot is the one we added..after running the new snapshot pickedup 
with open("snapshot.json","w") as f:
        json.dump(snapshot,f)
        print("succesfully wrote")
