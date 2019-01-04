# NPTEL Assignment

# Write a function intreverse(n) that takes as input a positive integer n and returns the integer obtained by reversing the digits in n

print('Intreverse Problem')
number=int(input("enter a number : "))
def intreverse(number):
    reminder=0
    quotient=0
    temp=0
    while(number>0):
        temp=temp*10
        quotient=number%10
        temp=temp+quotient
        number=number//10
    print(temp)
intreverse(number)

# Write a function matched(s) that takes as input a string s and checks if the brackets "(" and ")" in s are matched: that is, every "(" has a matching ")" after it and every ")" has a matching "(" before it. Your function should ignore all other symbols that appear in s. Your function should return True if s has matched brackets and False if it does not.

print('Matching brackets')
entry=str(input("Enter your string here : "))
def matched(entry):
    flag=0
    count=0
    for check in entry:
        if check=='(':
            flag+=1
            count+=1
        if check==')':
            flag-=1
            count+=1
    if flag==0 and count!=0:
        return True
    else: 
        return False

print(matched(entry))

# Write a function sumprimes(l) that takes as input a list of integers l and retuns the sum of all the prime numbers in l

from math import sqrt
from itertools import count, islice
l=input("enter a list of numbers seperated by , : ")
L=list(l.split(","))
print(L)
def isPrime(n):
    if n < 2:
        return False

    for number in islice(count(2), int(sqrt(n) - 1)):
        if n % number == 0:
            return False

    return True  
def sumprimes(L):
    sum=0
    for entity in L:
        check=int(entity)
        if isPrime(check)==True:
            sum=sum+check
    print(sum)

sumprimes(L)