#Calculate the sum of three given numbers, if the values are equal then return thrice of their sum
print('Calculate the sum of three given numbers, if the values are equal then return thrice of their sum')
x=int(input("enter the value of x : "))
y=int(input("enter the value of y : "))
z=int(input("enter the value of z : "))
if x+y+z==3*x:
    print('%d is the return value'%(3*x))
else:
    print('%d is the return value'%(x+y+z))
