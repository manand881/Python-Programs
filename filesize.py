# Get the size of a file

import os
name=input("enter the filename : ")
file_size = os.path.getsize(name)

if(file_size>1024):
    print("file is larger than one KB")
    file_size=file_size/1024
    print("\nThe size of ",name," is :",file_size,"KiloBytes")
else:
    print("\nThe size of ",name," is :",file_size,"Bytes")