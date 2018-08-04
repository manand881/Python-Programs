def factorial(number):
    if number==0:
        return 1
    else:
        return number*factorial(number-1)

inputt=int(input("enter the number to find factorial of : "))
print(factorial(inputt))