soundex=[0,1,2,3,0,1,2,0,0,2,2,4,5,5,0,1,2,6,2,3,0,1,0,2,0,2]
 
word=input("Input the word be hashed: ")
 
word=word.upper()
 
coded=word[0]
unique_hash=coded 
for a in word[1:len(word)]:
    i=65-ord(a)
    coded=coded+str(soundex[i]) 
print("\nThe coded word is: "+coded)

# Experimental stuff
# Given a string of length one, return an integer representing the Unicode code point of the character when the argument is a unicode object, or the value of the byte when the argument is an 8-bit string. For example, ord(‘a’) returns the integer 97, ord(‘€’) (Euro sign) returns 8364.
# Raises Exception
value1 = ord('A')
 
# prints the unicode value
print (value1)
