#!/bin/env python3

# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

# трехзначное число => 100 ... 999

input_num = int(input())

# проверка на корректность данных
if input_num < 100 or input_num > 999:
    raise ValueError

sum_nums = 0
prod_nums = 1

# если нужно сохранить input_num
tmp = input_num

while tmp > 0:
    sum_nums += tmp % 10
    prod_nums *= tmp % 10
    tmp //= 10

print(f"sum {sum_nums}\t prod {prod_nums}")
