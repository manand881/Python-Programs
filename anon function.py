# Get numbers divisible by fifteen from a list using an anonymous function

numberlist=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
answer=list(filter(lambda x:(x%2==0),numberlist))
print("the numbers divisible by 2 are :\n",answer)

# lambda operator or lambda function is used for creating small, one-time and anonymous function objects in Python.
