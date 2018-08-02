# Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference
print('difference')
inpt=float(input("enter the number to compare "))
if inpt>17:
    print("%f is greater than 17"%inpt)
    absdiff=2*(inpt-17)
    print (absdiff)
else:
    print("%f"%(17-inpt))
