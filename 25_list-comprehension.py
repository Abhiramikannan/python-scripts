#Q6:Use List Comprehension to create a list of the first letters of every word in the string below:



st = 'Create a list of the first letters of every word in this string'
list=[]
#splitted
a=st.split()
l=[i[0] for i in a ]
print(l)
#for i in range(0,len(a)):
