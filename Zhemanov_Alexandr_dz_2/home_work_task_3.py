#!/bin/env python3
# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.

"""
# 1 вариант через строку

rev_input_numer = int(input()[::-1])
print(rev_input_numer)
# не интересно
#"""
# 2 вариант через число
input_numer = int(input())

def rev(number : int, power:int = 0):
    if number < 10:
        print(f"end {number}")
        return(number, power)

    part = number % 10
    (res, next_power) = rev(number // 10, power + 1)
    print(f"max power({next_power}) - current({power}) ->  {next_power - power}", res)
    return (res + part * (10 ** (next_power - power )), next_power)

print(rev(input_numer)[0])

