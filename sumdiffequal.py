# Return true if the two given int values are equal or their sum or difference is 5

def checker(a,b):
    print(a,b)
    if a==b or a+b==5 or a-b==5:
        # return True
        print(True)
    else:
        # return False
        print(False)

checker(1,2)
checker(2,3)
checker(7,2)
checker(9,5)