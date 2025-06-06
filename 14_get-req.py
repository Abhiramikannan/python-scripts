# crete a req and sent req to google.com

import requests

res=requests.get("https://www.google.com",verify=False) # python dont trust ssl certicate and gave error so this command required(verify=False)
print(res)

#statuscode =200 =working good
