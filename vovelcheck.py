# Test whether a passed letter is a vowel or not
alpha=str(input("enter an alphabet"))
feedback=str(input("would you like to use an if statement? "))
if feedback == 'yes' or 'YES' or 'Yes' or'Y':
    if alpha == 'a' or 'e' or 'i'or'o'or'u':
        print('vowel')
else:
    def is_vowel(char):
        all_vowels = 'aeiou'
        #return statement valid only in functions
        return char in all_vowels
    print(is_vowel(alpha))
