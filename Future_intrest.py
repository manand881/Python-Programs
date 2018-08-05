# Future value of a specified principal amount, rate of interest, and a number of years

amt,int,years = 10000,3.5,7

future_value  = amt*((1+(0.01*int)) ** years)
print(future_value)
print(round(future_value,2))
print(round(future_value,3))
print(round(future_value,4))

