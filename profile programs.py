# Determine profiling of Python programs

# Note: A profile is a set of statistics that describes how often and for how long various parts of the program executed. These statistics can be formatted into reports via the pstats module.

import cProfile
def lcm(x,y):
    if x>y:
        z=x
    elif x==0 or y==0:
        print("no lcm")
    else:
        z=y
    while(True):
        if z%x==0 and z%y==0:
            print(z)
            break
        z=z+1

lcm(15,17)
cProfile.run('lcm(15,17)')
cProfile.run('lcm(1500,1735)')