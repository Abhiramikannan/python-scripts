#Q3:Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
list=[]
for i in range(1,51):
    if(i%3==0):
        print(i)
        #to convert to list
        list.append(i)
print(list)
