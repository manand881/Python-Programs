#  Check whether a file exists using Python

import os.path
name=input("enter file name : ")
filename=name+".py"
open(filename, 'w')
print(os.path.isfile(filename))
print("done")

#this is creating a file in the directory that is open! O_O