#program to learn to use funcitons in python
print('function demo')
side=float(input("enter the side of the square :\n"))
def area(side):
    print('the area is %f'%(side*side))
    return
def perimeter(side):
    print('the perimeter is %f'%(4*side))
    return
def volumee(side):
    print('the volume is %f'%(side**3))
    return
area(side)
perimeter(side)
volumee(side)

