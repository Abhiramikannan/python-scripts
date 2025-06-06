#give a public post api call, using requests 
import requests

d1={"name":"sheily","age":23,"maturity": "low"}
params={"id":1} 
response=requests.post("https://jsonplaceholder.typicode.com/posts/",json=d1,params=params,verify=False)#should store into json=mandatory field
print(response)  # if use response.json()=print in json formT

#workinggg
