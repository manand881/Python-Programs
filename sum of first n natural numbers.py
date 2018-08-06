# Sum of the first n positive integers
n=int(input("enter a value for 'n' to find the sum of first n natural numbers : "))
m,sum=0,0
while(m<=n):
    sum=sum+m
    m+=1
print(sum)