#access value from a dict
data={"name":"alice"}
print(data['name'])

#access value from a nested dictionary
data={"person":{"name":"alice"}}
print(data['person']['name'])

#Convert a path string to access keys
key_path="person/name"
keys=key_path.split('/')
print(keys)


#Use a loop to access deep values
def nested_loop(data,key_path):
    keys=key_path.split('/')
    current=data
    for key in keys:
        if key in current:
            current=current[key]
        else:
            return None 
    return current


d1={"a":{"b":{"c":"d"}}}
path="a/b/c"
nested_loop(d1,path)

print(nested_loop(d1,path))
