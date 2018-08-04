# Get the least common multiple (LCM) of two positive integers
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