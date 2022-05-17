#!/bin/env python3

# 6. В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число, чем то, что загадано.
# Если за 10 попыток число не отгадано, то вывести загаданное число.

from time import time

rand_num = int(time() % 100) 
count_of_try = 10
win_flag = False
for _ in range(count_of_try):
    try_gess = int(input())

    if try_gess > rand_num:
        print("меньше")
    elif try_gess < rand_num:
        print("больше")
    else:
        win_flag = True
        break


if win_flag:
    res = "Угадал. это"
else:
    res = "Нет. это было"

print(res, rand_num)
