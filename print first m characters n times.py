#Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2.
def substring(string,n):
    result=""
    substr=string[:2]
    print(substr)
    if len(string)<3:
        for iteration in range(n):
            result=result+string
        return result
    else:
        for iteration in range(n):
            result=result+substr
        return result

strinput=str(input("enter a string : "))
n=int(input("enter the number of times it must be repeated : "))
print(substring(strinput,n))
