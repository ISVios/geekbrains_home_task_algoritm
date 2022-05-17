#!/bin/env python3

# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

"""
# 1 вариант через string

input_count = int(input())


def sum_num(var:str) -> int:
    answ = 0
    for ch in var:
        answ += int(ch)
    return answ

input_number_str = input()

max_numb_sum = (int(input_number_str), sum_num(input_number_str))

for _ in range(input_count - 1):
    input_number_str = input()
    test_sum = sum_num(input_number_str)
    if max_numb_sum[1] < test_sum:
        max_numb_sum = (int(input_number_str), test_sum)

print(max_numb_sum)

# """

# """
# 2 вариант через int

input_count = int(input("input count of number: "))


def sum_num(var:int) -> int:
    answ = 0
    while var > 0:
        answ += var % 10
        var //= 10
    return answ

input_number = int(input("input 1 number: "))

max_numb_sum = (input_number, sum_num(input_number))

for i in range(input_count - 1):
    input_number = int(input(f"input {i+2} number: "))
    test_sum = sum_num(input_number)
    if max_numb_sum[1] < test_sum:
        max_numb_sum = (input_number, test_sum)

print("res = max is", max_numb_sum)

# """
