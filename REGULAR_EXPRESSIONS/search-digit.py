#checks if the string contains a number
import re 
str="abhi123"
if re.search(r"\d+",str): # should give r /cant start with seq charecter /error
    print("yes u are right digits are there")
else:
    print("sorry no results")
