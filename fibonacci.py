def fibonacci(number):
    a=0
    print(a)
    b=1
    print(b)
    n=1
    while n <=number:
        c=a+b
        a=b
        b=c
        n+=1
        print(c)

fibonacci(10)