#Compute the greatest common divisor (GCD) of two positive integers
def gcd(x,y):
    bigger=0
    smaller=0
    output=1
    if x or y == 0:
        return "no gcd available"
    if x>y:
        bigger=x
        smaller=y
    else:
        bigger=y
        smaller=x
    temp=smaller
    while(temp>0):
        if bigger%temp==0 and smaller%temp==0:
            return temp
        temp=temp-1
        
input1=int(input("enter a number "))
input2=int(input("enter a number "))
print(gcd(input1,input2))