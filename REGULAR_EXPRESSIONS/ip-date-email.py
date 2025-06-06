#regularexp
import re
log = "2025-05-28 10:20:00 - INFO - Start\n2025-05-28 10:22:00 - ERROR - Failed to connect\n2025-05-21 09:22:00 - ERROR - Failed to coerrr"
x=re.findall(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) - ERROR - (.*)', log)
print(x)

#email
text="abhiabhirami242@gmail.com12abhiaami@gmail.com134597"
y=re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}',text)
print(y)


ip = "Client connected from 192.168.1.10, another from 10.0.0.5 and invalid 999.999.999.999"
z=re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b',ip)
print(z)
