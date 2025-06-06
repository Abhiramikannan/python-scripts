# a file have lot of error msg
#     error msg line(msg+time)=stores to other  file

# 2023-10-27 10:00:00,123 - INFO - Application started 
# 2023-10-27 10:00:05,456 - DEBUG - Processing request: /api/data
# 2023-10-27 10:00:12,789 - ERROR - Database connection failed: Connection refused
# 2023-10-27 10:00:15,000 - INFO - Request completed: /api/data
# 2023-10-27 10:00:20,321 - ERROR - Invalid user input: Username cannot be empty
# 2023-10-27 10:00:22,654 - DEBUG - Data retrieved from cache
# 2023-10-27 10:00:28,987 - ERROR - File not found: /path/to/missing/file
# 2023-10-27 10:00:35,210 - WARNING - High CPU usage detected
# 2023-10-27 10:00:40,543 - ERROR - An unexpected error has occurred


import json
 
inputfile= "timestamp.txt"
outputfile= "warning.txt"
error=[]
 
try:
    with open (inputfile,"r") as file:
        content = file.read()
        lines = content.split("\n")
        for line in lines:
            if line.__contains__(' - ERROR - '):
                Logarr = line.split(" - ERROR -")
                error.append({"time":  Logarr[0] , "error message" :  Logarr[1]})
    print ("successfull read")
except Exception as e:
    print (f"error read {e}" )
 
try:
    with open (outputfile,"w") as file:
        json.dump(error,file)
except Exception as e:
    print (f"error write {e}" )  
