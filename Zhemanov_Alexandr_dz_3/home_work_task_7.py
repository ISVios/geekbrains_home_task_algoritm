#!/bin/env python
#7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба являться минимальными), так и различаться.

# вариант 1 (через сортировку)

"""
from random import randint

input_n = int(input("input count of random numers: "))
rnd_arr = [ randint(-100, 100) for _ in range(input_n) ]

# n*log(n)
def quicksort(nums):
   if len(nums) <= 1:
       return nums
   else:
       q = nums[len(nums)//2]
   l_nums = [n for n in nums if n < q]

   e_nums = [q] * nums.count(q)
   b_nums = [n for n in nums if n > q]
   return quicksort(l_nums) + e_nums + quicksort(b_nums)

tmp_arr = rnd_arr.copy()

print(tmp_arr)
tmp_arr = quicksort(tmp_arr)
print(tmp_arr[0], tmp_arr[1])

# """

# 2 вариант n 

from random import randint

input_n = int(input("input count of random numers: "))
rnd_arr = [ randint(-10, 10) for _ in range(input_n) ]

min_elem = rnd_arr[0]
pre_min_elem = min_elem

for elem_ind in range(1, len(rnd_arr)):
    curr_elem = rnd_arr[elem_ind]

    if curr_elem < pre_min_elem:
        pre_min_elem = curr_elem

    if curr_elem < min_elem:
        pre_min_elem = min_elem
        min_elem = curr_elem


print(rnd_arr)
print(list(sorted(rnd_arr)))
print(min_elem, pre_min_elem)


