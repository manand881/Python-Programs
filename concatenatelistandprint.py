#Concatenate all elements in a list into a string and return it
def concatenate(processlist):
    output=""
    for element in proceslist:
        output+=str(element)
    return output

inputlist=input("enter the list seperated by , : ")
proceslist=inputlist.split(',')
print(proceslist)
print(concatenate(proceslist))