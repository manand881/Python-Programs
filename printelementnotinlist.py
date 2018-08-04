# Print out a set containing all the colors from a list which are not present in other list

# userentry=input("enter list of colours")
# userentry_l=userentry.split(',')
# usercompare=input("enter list of colours to compare")
# usercompare_l=usercompare.split(',')
# for usercompare_l in userentry_l:
#     userentry_l=usercompare_l-usercompare_l
# print(usercompare_l)
## wont work

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

print(color_list_1.difference(color_list_2))