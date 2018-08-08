# Test whether all numbers of a list is greater than a certain number

num = [1,2,3,4,5,6,7,8,9,10]
print()
print(all(x > 1 for x in num))
print(all(x > 4 for x in num))
print(all(x < 4 for x in num))