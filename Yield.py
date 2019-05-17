#   This program demonstrates how to use yield in pything while trying to generate fibonacci numbers
import threading
import multiprocessing

a=1
b=2
c=a+b
iterator=1

print("0")
print("0")
print(a)
print(b)

while(iterator<10):
    print(c)
    a=b
    b=c
    c=a+b
    iterator+=1

print("\nUsing Yield\n")

print("0")
print("0")
print("1")
print("2")

def fibonacci():
    a=1             #   Calling global variable   
    b=2             #   Calling global variable
    c=a+b           #   Calling global variable
    while(True):    #   Infinite Loop
        yield c
        a=b
        b=c
        c=a+b

def printer():
    for num in fibonacci():
        if num>144:
            break
        print(num)

t1 = threading.Thread(target=printer) 
t2 = threading.Thread(target=printer)
t1.start()
t2.start()
t1.join()
t2.join()
print("Process")
if __name__ == "__main__": 
    p1 = multiprocessing.Process(target=printer)
    p2 = multiprocessing.Process(target=printer)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
print("Done")    