#Test whether a number is within 100 of 1000 or 2000
print('Test whether a number is within 100 of 1000 or 2000')
for i in range(100):

    n=float(input("enter the number n : "))
    def near_thousand(n):
      return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))
    print(near_thousand(n))
    feedback=(input("enter yes if you want to continue : "))
    #feedback.lower didnt seem to work
    if feedback in ['no','No','NO','nO']:
        break
        