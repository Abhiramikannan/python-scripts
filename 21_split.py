# Q1: Use for, .split(), and if to create a Statement that will print out words that start with 's':



st = 'Print only the words that start with s in this sentence'
a=st.split() #result=list
print(a)

#print only the things are letters
for words in a:
    if words.isalpha():
        pass
      #  print(words)
   
#print only if the lettter starts with s
    if words.startswith("s") or words.startswith("S"):
        print(words)
