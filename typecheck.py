# Input a number, if it is not a number generate an error message

while True:
    try:
        a = int(input("Input a number: "))

    except ValueError:
        print("\nThis is not a number. Try again...")
    
    else:
        print("no errors")
        break
    
    finally:
        print("change is the only constant in life")

#try:
#     this code
# except:
#     do this if there are excptions
# else:
#     do this since there are no exceptions
# finally:
#     always do this