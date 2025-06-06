#extract error lines from the logs
import re
log = "2025-05-28 10:20:00 - INFO - Start\n2025-05-28 10:22:00 - ERROR - Failed to connect\n2025-05-21 09:22:00 - ERROR - Failed to coerrr"
result=re.findall(r'.* - ERROR - .*',log)
print(result)

# .any charecter
# * 0 or more times
# mistakes
# last .*
# starting .*
#dont forget to pass file



#to capture error msg and timestamp
timestamp_errormsg=re.findall(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) - ERROR - (.*)',log)
print(timestamp_errormsg)
