#simple program to find out greater number
first=int(input("enter the first number:\n"))
second=int(input("enter the second number:\n"))
if first>second:
    print("%d is greater than %d"%(first,second))
else:
    if first==second:
        print("%d and %d are equal"%(first,second))
    else:
        print("%d is greater than %d"%(second,first))
