#!/bin/env python3

# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
#   заданный случайными числами на промежутке [0; 50).
#   Выведите на экран исходный и отсортированный массивы.
from random import random 

################################################################################
def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

def my_merge_sort(arr):
    if len(arr) < 2:
        return arr.copy()
    else:
        middle = int(len(arr) / 2)
        left = my_merge_sort(arr[:middle])
        right = my_merge_sort(arr[middle:])
        return merge(left, right)
################################################################################
rnd_arr = [int(10000 * random() % 5000)/100 for _ in range (int(input("input count of random element: ")))]

print(rnd_arr)
print(my_merge_sort(rnd_arr))
