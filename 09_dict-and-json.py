#Write a Python dictionary representing configuration settings (e.g., theme, language, notifications_enabled) to a JSON file named config.json.
#dic to json =json.dump(dic,file)
#json to dic =json.load(file)
import json
config = {"theme":"dark",
          "language":"malayalam",
          "notification_enabled": "yes"}
file_name="dictojson.json"
file_name2="jsontodict.txt"
try:
 with open (file_name,"w") as f:
    writer= json.dump(config,f)
    print(f"succesfully wrote to json as '{file_name}'")
 with open(file_name,"r") as f:
    writer = json.load(f) # reading and converting into dictionary
    print(writer)
    with open(file_name2,"w") as f: # writing the dict to a file
        f.write(str(writer))
        print(f"succesfully write to dic '{file_name2}")
    
except IOError as e:
    print("error:{e}")
except Exception as e:
    print("error:{e }")
