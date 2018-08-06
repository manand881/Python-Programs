# List all files in a directory in Python

import os

d = os.getcwd()
for i in os.listdir(d):
    print(i)
