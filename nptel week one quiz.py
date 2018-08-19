# What does g(31415927) return, for the following function definition? 


def g(x):
    (q,d) = (1,0)
    while q <= x:
      (q,d) = (q*10,d+1)
#*******************************
      print(d)
#*******************************  
    return(d)

g(31415927)
print("\n\n\n\n\n")


# What is the value of h(231,8) for the function below? 


def h(m,n):
    ans = 0
    while (m >= n):
      (ans,m) = (ans+1,m-n)
#*******************************
      print(ans)
#******************************* 
    return(ans)

h(231,8)
print("\n\n\n\n\n")


# Consider the following function h. 


def h(n):
    f = 0
    for i in range(1,n+1):
      if n%i == 0:
        f = f + 1
    return(f%2 == 1)

print(h(4))
print("\n\n\n\n\n")



# Consider the following function f. 


def f(m):
    if m == 0:
      return(0)
    else:
      return(m+f(m-1))

print(f(3))
print("\n\n\n\n\n")


# thats all folks