#Q13:Write a Python function to check whether a string is pangram or not.
#Note : Pangrams are words or sentences containing every letter of the alphabet at least once.


s="The quick brown fox jumps over the lazy dog".lower()
b="abcdefghijklmnopqrstuvwxyz"
found=[0]*26 # now not found anythg
for letter in s:
    if letter in b: 
        index=b.index(letter) #checks where this alphabet is present in b and find the index and save to index
        found[index]=1 #found 


if sum(found)==26:
    print("pangrame")
else:
    print("not pangrame")

