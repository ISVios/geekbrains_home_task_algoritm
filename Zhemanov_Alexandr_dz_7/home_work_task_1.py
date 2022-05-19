#!/bin/env python3

#   1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
#       заданный случайными числами на промежутке [-100; 100).
#   Выведите на экран исходный и отсортированный массивы.
#   Сортировка должна быть реализована в виде функции.
#   По возможности доработайте алгоритм (сделайте его умнее).
from random import randrange 

################################################################################
def my_buble_sort(arr:list) -> list:
    "return new array with sorted elems"
    tmp_arr = arr.copy()

    for i in range(len(tmp_arr)):
        for j in range(len(tmp_arr)-i):
            if(i != j):
                if(tmp_arr[i] > tmp_arr[j]):
                    tmp_arr[i], tmp_arr[j] = tmp_arr[j], tmp_arr[i]

    return tmp_arr
################################################################################
# ToDo add my_buble_sort_mod
################################################################################

rnd_arr = [randrange(-100,100) for _ in range (int(input("input count of random element: ")))]

print(rnd_arr)
print(my_buble_sort(rnd_arr))



