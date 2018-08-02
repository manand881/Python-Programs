#area of triangle and sphere
import math
print('area of triangle and sphere')
radius=float(input("enter the radius of the sphere\n"))
print('the volume is %f'%((4/3)*math.pi*(radius**3)))
print('volume of pyramid')
# (L*H*B)/3
length=float(input("enter the length of pyramid "))
height=float(input("enter the height of the pyramid "))
base=float(input("enter the base of the pyramid "))
print('the volume is %f'%((length*height*base*(1/3))))