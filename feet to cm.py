# Convert height (in feet and inches) to centimeters

print("Input your height: ")
h_ft = int(input("Feet: "))
h_inch = int(input("Inches: "))

h_inch += h_ft * 12
h_cm = round(h_inch * 2.54, 2)

print("Your height is : %f cm." % h_cm)