#!/bin/env python
# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
#  Сами минимальный и максимальный элементы в сумму не включать.
"""

# 1 вариант (через array.sort())

from random import randint

input_n = int(input("input count of random numers: "))
rnd_arr = [ randint(-10, 10) for _ in range(input_n) ]


tmp_arr = rnd_arr.copy()
tmp_arr.sort()

print(tmp_arr)
print(sum(tmp_arr[1:-1]))

# """

# 2 вариант (нужно просто качественно отсортировать)

"""

from random import randint

input_n = int(input("input count of random numers: "))
rnd_arr = [ randint(-10, 10) for _ in range(input_n) ]

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

print(tmp_arr)

sum_btw_min_max = 0

for i in range(1,len(tmp_arr)-1):
    sum_btw_min_max += tmp_arr[i]

print(sum_btw_min_max)

# """
# 3 вариант (сложить все и вычисть мин и мах) все равно нужны все элементы

from random import randint

input_n = int(input("input count of random numers: "))
rnd_arr = [ randint(-10, 10) for _ in range(input_n) ]


tmp_arr = rnd_arr.copy()


max_elem = tmp_arr[0]
min_elem = max_elem
sum_btw_min_max = max_elem 

for ind in range(1, len(tmp_arr)):

    curr_n = tmp_arr[ind]

    if max_elem < curr_n:
        max_elem = curr_n
    elif min_elem > curr_n:
            min_elem = curr_n

    sum_btw_min_max += curr_n


sum_btw_min_max -= (max_elem + min_elem)

print(tmp_arr)

print(sum_btw_min_max)


