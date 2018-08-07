#  Calculate body mass index

height = float(input("Input your height in meters: "))
weight = float(input("Input your weight in kilogram: "))
print("Your body mass index is: ", round(weight / (height**2), 2))
print("Your body mass index is: ",(weight / (height**2)))