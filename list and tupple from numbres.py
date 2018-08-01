values=input("enter numbers seperated by commas\n")
#values.split splits when , is encountered
list=values.split(",")
tuple=tuple(list)
print(list)
print(tuple)
#trying to get list from tupple
value2=input("enter numbers seperated by commas\n")
tuple=value2.split(",")
list=list(tuple)
print(list)
print(tuple)
#this does not work