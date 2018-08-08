# Convert a byte string to a list of integers

x = b"Anand Mahesh"
y = []
for i in [x]:
    y += i

print("\n",y,"\n")
print("Assuming Python 3 (in Python 2, this difference is a little less well-defined) - a string is a sequence of characters, ie unicode codepoints; these are an abstract concept, and can't be directly stored on disk. A byte string is a sequence of, unsurprisingly, bytes - things that can be stored on disk. The mapping between them is an encoding - there are quite a lot of these (and infinitely many are possible) - and you need to know which applies in the particular case in order to do the conversion, since a different encoding may map the same bytes to a different string:\n")