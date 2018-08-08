# Check if a file path is a file or a directory

import os  
path="BMI.py"  
if os.path.isdir(path):  
    print("\nIt is a directory\n")  
elif os.path.isfile(path):  
    print("\nIt is a normal file\n")  
else:  
    print("It is a special file (socket, FIFO, device file)" )
