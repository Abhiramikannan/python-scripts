#dict to json file
import json
d1={"name":"abhi","age":"23","subject":"devops"}
file_name="dic1.json"
file_path=os.path.join(os.getcwd(),file_name)
with open(file_path,"w") as f:
    json.dump(d1,f)
    print("written succesfully")
with open(file_path,"r") as f:
    read=json.load(f)
    print(read)
