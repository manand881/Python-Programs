#Get a string which is n (non-negative integer) copies of a given string
#
#function to display the string
def dispfunc(iteration):
    output=str("")
    for i in range(iteration):
        output=output+entry
    print(output)
#
entry=str(input("\nenter a string : "))
displaynumber=int(input("how many times must it be displayed? : "))
dispfunc(displaynumber)
#experimental
feedback=str(input("\nwould you try it for the stringlength? : "))
if feedback == "yes" or "Yes" or "YES" or "yeah":
    dispfunc(len(entry))
#program ends here