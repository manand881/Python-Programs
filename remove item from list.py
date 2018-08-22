letterlist=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
array_num=0
for var in letterlist:
    if var != 'a'or'e'or'i'or'o'or'u':
       del letterlist[array_num]
    array_num+=1 
             
print(letterlist)