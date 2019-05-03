# Get the least common multiple (LCM) of two positive integers
import time

def lcm(x,y):
    start_time=time.perf_counter()
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
    end_time=time.perf_counter()
    run_time=end_time-start_time
    print(run_time)

lcm(3698,1789)