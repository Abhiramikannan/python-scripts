import requests
import re

url="http://books.toscrape.com/"
response=requests.get(url,verify=False)
html=response.text #to get html format
print(html)

#re for extracting titles
a=re.findall(r'<a[^>]* title="([^"]+)"',html) # any charec except >,0 to more,title= except " any charecter 1 or more
print(a)



for i in a [:5]: # print 5 titles
    print(i)

#re for extracting prices
#i done
b=re.findall(r'<[^>]* class="[^"]+">.+(\d[0-9]+\.\d[0-9]+)</p>',html)
print(b)
#+ 1 0r more
#* 0 or more
#? 0 or 1
