# Create a bytearray from a list

print()
nums = [10, 20, 56, 35, 17, 99]
# Create bytearray from list of integers.
values = bytearray(nums)
for x in values: print(x)
print()

print("type of nums",type(nums))
print("type of values",type(values))