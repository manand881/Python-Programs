startmsg = "hello"
endmsg = ""
for i in range(0,len(startmsg)):
    endmsg = startmsg[i] + endmsg
print(endmsg)

def mystery(l):
    l = l + l
    return()

mylist = [31,24,75]
mystery(mylist)
print(mylist)