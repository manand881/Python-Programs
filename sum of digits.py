# Calculate the sum of the digits in an integer

entry=int(input("enter a number: "))
output=0
while(entry>0):
    answer=entry%10
    output=output+answer
    entry=entry//10
print(output)
