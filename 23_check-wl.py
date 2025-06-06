#Q4:Go through the string below and if the length of a word is even print "even!"

st = 'Print every word in this sentence that has an even number of letters'
#printing whole length
length=len(st)
print(length)
#splitting the sentenc to word
word=st.split()
print(word)


#checking the length of word is even or not
length=len(word)
for w in word:
    if(len(w)%2==0):
        print(w,len(w),"even")
    else:
        pass
