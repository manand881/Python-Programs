# Prove that two string variables of same value point same memory location

str1= "anand"
str2= "anand"

print("\nmemory location of str1",hex(id(str1)))
print("\nmemory location of str2",hex(id(str1)))

if hex(id(str1))==hex(id(str2)):
    print("\n\nmemory location matches")