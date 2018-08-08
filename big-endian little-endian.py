# Test whether the system is a big-endian platform or little-endian platform

import sys
if sys.byteorder == "little":
    #intel, alpha
    print("\nLittle-endian platform.")
else:
    #motorola, sparc
    print("\nBig-endian platform.")
print("\nclick here to understand big endian and little endian system")
print("\nhttps://agilescientific.com/blog/2017/3/31/little-endian-is-legal\n")