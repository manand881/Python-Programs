#Check whether a specified value is contained in a group of values
def groupcheck(array,num):
    for iteration in array:
        if num == iteration:
            return num in array

arrayint=input("enter the list : ")
array=arrayint.split(',')
print(array)
num=input("enter the num to search : ")
print(groupcheck(array,num))
#Should do more of these
