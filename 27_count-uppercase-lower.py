#Q10:Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.



Sample_String = 'Hello Mr. Rogers, how are you this fine Tuesday?'
lower=0
upper=0

for word in Sample_String:
    if word.isupper():
        upper+=1
    elif word.islower():
        lower+=1
print(Sample_String)
print(upper)
print(lower)
