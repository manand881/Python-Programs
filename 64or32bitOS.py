# Check whether Python shell is executing in 32bit or 64bit mode on OS
# For 32 bit it will return 32 and for 64 bit it will return 64
import struct
print("")
print(struct.calcsize("P") * 8)