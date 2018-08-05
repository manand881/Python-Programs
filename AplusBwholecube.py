# Python program to solve (a+b)^3
a=int(input("enter a : "))
b=int(input("enter b : "))
result= a**3+b**3+(3*a*b*(a+b))
print("\n({}+{})^3={}\n".format(a,b,result))