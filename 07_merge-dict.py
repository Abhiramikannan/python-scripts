#Write a Python function that merges two dictionaries, combining values for keys that appear in both dictionaries

d1={'a':1,'b':6}
d2={'b':1,'d':8}


result = d1.copy()
print ("result is",result)
for key,value in d2.items():
    if key in result:
        print("result of key before adding",result[key]) # printing value
        result[key]+=value #6+1
        print(result[key])
        
    else:
        result[key]=value
print(result)

