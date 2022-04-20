#!/bin/env python
# 4. Определить, какое число в массиве встречается чаще всего.


from random import randint

input_n = int(input("input count of random numers: "))

rnd_arr = [ randint(1, 10) for _ in range(input_n) ]

"""
# 1 вариант (опасный, исменяем длинну считываемого массива)

tmp_rnd_arr = rnd_arr.copy()

max_find = 0
answ = None

print(rnd_arr)

while len(tmp_rnd_arr):
    find = tmp_rnd_arr.pop()
    count = 1
    for i, elem in enumerate(tmp_rnd_arr):
        if elem == find:
            count += 1
            del tmp_rnd_arr[i]

    if max_find < count:
        max_find = count
        answ = find

print(answ, max_find)

# """

#"""

# 2 вариант

tmp_rnd_arr = rnd_arr.copy()

max_find = 0
answ = None

print(rnd_arr)

while len(tmp_rnd_arr):
    find = tmp_rnd_arr.pop()
    count = 1
    tmp_arr = []

    for i, elem in enumerate(tmp_rnd_arr):
        if elem == find:
            count += 1
        else:
            tmp_arr.append(elem)

    if max_find < count:
        max_find = count
        answ = find
    tmp_rnd_arr = tmp_arr

print(answ, max_find)

# """

