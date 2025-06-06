#extract all email from a text file

import re
text="aamiabhirami242@gmail.com hyby 242 dev@gmail.com/n"
email=re.findall(r'[a-zA-Z0-9.%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',text)
print(email)

#mistakes
#forgot to give + after +@[a-zA-Z0-9.-]+
#\. not completed still there to add
#. means any charector
#\. exactly matching with dot
