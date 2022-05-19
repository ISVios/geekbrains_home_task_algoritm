#!/bin/env python3

# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы. Задачу можно решить без сортировки исходного массива. Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках

# достаточно найти (m+1) максимум 
from random import randrange

rnd_arr = [randrange(0, 10) for _ in range(2 * int(input("input n of (2*n+1) count random elem: ")) + 1) ]

def find_median(arr, count) -> int:
    m_id = 0
    for i, scan_elm in enumerate(arr[1:] , start=1):
        if arr[m_id] < scan_elm:
            m_id = i

    if count <= 0:
        return arr[m_id]
    else:
        return find_median(arr[:m_id] + arr[m_id + 1:] ,count - 1)

print(*rnd_arr)
print("median ",find_median(rnd_arr, (len(rnd_arr)-1)//2))

print("для проверки")
sort = list(sorted(rnd_arr))
center = (len(sort) - 1 ) // 2
print(*sort[:center] , f"[{sort[center]}]", *sort[center+1:])
