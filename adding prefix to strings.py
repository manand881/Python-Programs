# Get a new string from a given string where 'Is' has been added to the front. If the given string already begins with 'Is' then return the string unchanged
print('')
stringenter=str(input("enter a string : "))
print('%s is the entered string'%(stringenter))
def adder(stringenter):
    if len(stringenter)>1: 
        if stringenter[:2]=="is" or "IS" or "iS" or "Is":
            return stringenter
    else:
        return "is"+stringenter
print("%s is the resultant string"%(adder(stringenter)))