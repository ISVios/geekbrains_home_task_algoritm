#!/bin/env python
# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

from random import randint

input_n = int(input("input count of random numers: "))

rnd_arr = [ randint(-100, 100) for _ in range(input_n) ]

ind = 0
find = rnd_arr[0]
for i in range(1, input_n):
    curr_n = rnd_arr[i]
    if curr_n < 0 and find > curr_n:
        ind = i
        find = curr_n

print(rnd_arr)
print(find, ind)

