# Sum of three given integers. However, if the sum is between 15 to 20 it will return 20

a=int(input("enter a number a: "))
b=int(input("enter a number b: "))
c=int(input("enter a number c: "))

if a+b+c in range(15,20):
    print(20)
else:
    print("%d"%(a+b+c))