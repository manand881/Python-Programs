print('area of a circle')
from math import pi
# i'm assuming that pi os a predefined value and is called from somewhere called math
r=float(input("enter the radius measurement\n"))
print(3.141*(r**2))
# unwanted space manifests upon calling \n on print
print('\n',3.141*(r**2))
# will try using pi cannot use pi just by calling pi*(r**2) for some reason
type(pi)
#does not return value
print(str(pi*(r**2)))
#bantappa nodi
#for some reason pi needs to be used with str