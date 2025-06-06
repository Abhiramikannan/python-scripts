#qn: Write a Python script that reads a CSV file and calculates the average value for a specified column.
#csv.DictReader =  turns each row into a dictionary like {'Name': 'Alice', 'Age': '25'}
# csv.DictWriter= write the values of each row  from dict to csv


import csv
users=[{"name":"abhi","age":23,"place":"tvm"}]
file="01_users.csv"
fieldnames=["name","age","place"]
sum=0
count=0
try:
 with open("01_users.csv","w",newline='') as f:
    writer=csv.DictWriter(f,fieldnames=fieldnames)# captital W
    writer.writeheader()
    writer.writerows(users) # pass every rows 'writerows'
    print(f"succesfully wrote into '{file}'")
 with open("01_users.csv","r") as f:
    reader=csv.DictReader(f)
    for row in reader:
       print(row['age'])
       sum=sum+int(row['age'])
       count=count+1  # it can add the count how many times age calculated 
    print (f"sum is '{sum}'")
    avg=sum/count
    print(f"avg is '{avg}'")

    
except IOError as e:
        print("unexpected error:{e}")
except Exception as e:
        print("error:{e}")
