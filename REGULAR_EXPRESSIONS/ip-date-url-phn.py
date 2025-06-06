import re
a="192.78.89.1   abhi 132.176.34.3   192.78.89.1"
c=re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b",a)
print(c)
unique=set(c)
print(unique)


email="Contact us at support@example.com or sales@my-site.org"
pattern=r"[a-zA-Z0-9+-]+@[a-zA-Z0-9-]+\.[a-z]{2,}"
z=re.findall(pattern,email)
print(z)


date="Today is 25/06/2025, tomorrow is 26/06/2025"
pattern=r"\d{2}/\d{2}/\d{4}"
print(re.findall(pattern,date))

#extract url starting with http or https
url="Visit http://example.com or https://secure.org for info"
pattern=r"https?://[^\s]+" #matches either http or https :// matches this [^\s]+=any charec except white space 1 or more times
print(re.findall(pattern,url))

#phone num
num="Call me at (123) 456-7890 or 987-654-3210"
pattern = r'\(?\d{3}\)?[-\s]?\d{3}-\d{4}' 
print(re.findall(pattern,num))
