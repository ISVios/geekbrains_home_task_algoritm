#!/bin/env python3
# 1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в
#  рамках практического задания первых трех уроков.
#  Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

from random import randint

import time

input_n = int(input("input count of random numers: "))
rnd_arr = [ randint(-10, 10) for _ in range(input_n) ]


# 7n - 7 + 3 + 3 = 7n - 1 => O(n)

str_time = time.time()

min_elem = rnd_arr[0]  # 2
pre_min_elem = min_elem # 1

for elem_ind in range(1, len(rnd_arr)): # (n-1)*7 + 3 
    curr_elem = rnd_arr[elem_ind] # 2

    if curr_elem < pre_min_elem: # 1
        pre_min_elem = curr_elem # 1

    if curr_elem < min_elem: # 1
        pre_min_elem = min_elem # 1
        min_elem = curr_elem # 1


print(time.time() - str_time)

print(rnd_arr)
print(list(sorted(rnd_arr)))
print(min_elem, pre_min_elem)


# для n = 10 time = 1.52587890625e-05
# для n = 100 time = 7.724761962890625e-05  
# для n = 1000 time = 0.0007183551788330078 
# для n = 10000 time = 0.001291513442993164
# для n = 100000 time = 0.013663053512573242
# для n = 1000000 time = 0.1422879695892334
# для n = 10000000 time = 1.3567099571228027
# для n = 100000000 time = 13.774113416671753  

