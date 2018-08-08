# Get the size of an object in bytes
import sys
str1 = "one"
str2 = "four"
str3 = "three"
number=1
number2=2
number3=1024
number4=2048

print("Memory size of '"+str1+"' = "+str(sys.getsizeof(str1))+ " bytes")
print("Memory size of '"+str2+"' = "+str(sys.getsizeof(str2))+ " bytes")
print("Memory size of '"+str3+"' = "+str(sys.getsizeof(str3))+ " bytes")
print("\nMemory size of ",number,"=",(sys.getsizeof(number))," bytes")
print("Memory size of ",number2,"=",(sys.getsizeof(number2))," bytes")
print("Memory size of ",number3,"=",(sys.getsizeof(number3))," bytes")
print("Memory size of ",number4,"=",(sys.getsizeof(number4))," bytes")