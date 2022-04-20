#!/bin/env python
# 2. Во втором массиве сохранить индексы четных элементов первого массива.
#  Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1, 4, 5, 6
#  (или 0, 3, 4, 5 - если индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.



input_count = int(input("input count of elements: "))

arr = []
answ = []

for i in range(input_count):

    input_n = int(input())

    if input_n % 2 == 0:
        answ.append(i)

    arr.append(input_n)

print(f" array is {arr}. Even index number is {answ}")
