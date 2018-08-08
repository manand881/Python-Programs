# Create a copy of its own source code
import sys

file = open(sys.argv[0],'r')
l = file.readline()
while(l!=''):
    print(l,end='')
    l = file.readline()