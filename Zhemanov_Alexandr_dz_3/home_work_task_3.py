#!/bin/env python
# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

from random import randint

input_n = int(input("input count of random numers: "))

rnd_arr = [ randint(-100, 100) for _ in range(input_n) ]

max_ind = 0
min_ind = 0

for i in range(1, input_n):
    arr_i = rnd_arr[i]

    if arr_i > rnd_arr[max_ind]:
        max_ind = i
    elif arr_i < rnd_arr[min_ind]:
        min_ind = i

print(rnd_arr)

rnd_arr[max_ind], rnd_arr[min_ind] = rnd_arr[min_ind], rnd_arr[max_ind]

print(rnd_arr)
