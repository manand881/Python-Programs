# Check if a string is numeric

str = 'a123'
# str = '123'
try:
    i = float(str)
except (ValueError, TypeError):
    print('\nNot numeric')

#i'm guessing that this is similar to try catch
# i=float(str) is used to convert string to str