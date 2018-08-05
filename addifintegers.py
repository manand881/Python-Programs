# Add two objects if both objects are an integer type

import sys

def add_ints(a, b):
    if type(a) == type(b) == int:
        return a + b
    else:
        sys.exit

print(add_ints(1,2)) # ===> 3
print(add_ints(1,'2')) # ===> None

# def add_numbers(a, b):
#     if not (isinstance(a, int) and isinstance(b, int)):
#          raise TypeError("Inputs must be integers")
#     return a + b

# print(add_numbers(10, 20))