#!/bin/env python3
#  9. Вводятся три разных числа. 
#     Найти, какое из них является средним (больше одного, но меньше другого).

# какой тип "числа" (взял float)

nums = [float(input(f"input {i + 1} number: ")) for i in range(3)]

if ((nums[0] < nums[1] < nums[2]) or (nums[2] < nums[1] < nums[0])):
    res = nums[1]
elif ((nums[1] <  nums[0] < nums[2]) or (nums[2] < nums[0] < nums[1])):
    res = nums[0]
else:
    res = nums[2]

print(f"{res} is middle from {nums}")

