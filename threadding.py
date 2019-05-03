import threading
from numba import jit

@jit(parallel=True)  
def print_cube(num): 

    for i in range(1,1000):
        print("Cube: {}\n".format(num * num * num * i)) 
@jit(parallel=True)  
def print_square(num): 

    for j in range(1,1000):
        print("Square: {}\n".format(num * num * j)) 
  
if __name__ == "__main__": 
    # creating thread 
    t1 = threading.Thread(target=print_square, args=(10,)) 
    t2 = threading.Thread(target=print_cube, args=(10,)) 
  
    # starting thread 1 
    t1.start() 
    # starting thread 2 
    t2.start() 
  
    # wait until thread 1 is completely executed 
    t1.join() 
    # wait until thread 2 is completely executed 
    t2.join() 
  
    # both threads completely executed 
    print("Done!") 