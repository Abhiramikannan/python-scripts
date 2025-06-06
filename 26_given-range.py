#Q9:Write a function that checks whether a number is in a given range (inclusive of high and low)

#ran_check(5,2,7)  Note:example check whther 5 is between 2 and 7

def ran_check(num,low,high):
    if low<=num<=high:
        print(num, "is in the given range")
    else:
        print("not in given range")


ran_check(5,2,7)
