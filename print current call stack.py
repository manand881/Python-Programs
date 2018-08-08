# Print the current call stack

import traceback
print()
def f1():
    return abc()
def abc():
    traceback.print_stack()
f1()
# I dont understand the point of this
# ok this is supposed to inform you as to what line of the program this is being called from?