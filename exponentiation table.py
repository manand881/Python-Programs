#prints exponentiation table for numbers
mul_no=int(input("enter the number for which you want the exonentiation table : "))
for n in [1,2,3,4,5,6,7,8,9,10]:
    answer=mul_no**n
    print("%d ** %d = %d"%(mul_no,n,answer))