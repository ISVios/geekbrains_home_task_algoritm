#!/bin/env python3

# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

"""

# 1 вариант если ввод является строкой

number_str = input("input number: ")

odd = 0
even = 0

for ch in number_str:
    if int(ch) % 2 == 0:
        even += 1
    else:
        odd += 1

print(number_str, f"have {even} even and {odd} odd number")

# """
##############################

# 2 вариант если ввод является числом

number = int(input("input number: "))

odd = 0
even = 0

tmp_number = number

while tmp_number > 0:
    if (tmp_number % 10) % 2 == 0:
        even += 1
    else:
        odd += 1

    tmp_number //= 10

print(number, f"have {even} even and {odd} odd number")
