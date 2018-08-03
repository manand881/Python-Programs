#  Find whether a given number is even or odd, print out an appropriate message to the user
entry=int(input("enter a number : "))
if entry == 0:
    print("neither")
elif entry %2 == 0:
    print("even")
else:
    print("odd")