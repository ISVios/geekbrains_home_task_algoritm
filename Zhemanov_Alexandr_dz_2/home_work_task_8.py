#!/bin/env python3

# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

# цифра 0 1 2 3 4 5 6 7 8 9

"""

# 1 вариант через string

count_elm = int(input())
find_number = input()[0]
find_count = 0


for i in range(count_elm):
    input_n = input()
    find_count += len(input_n.split(find_number)) - 1

print(find_count)

# """

# 2 вариант через int 

count_elm = int(input("input count of numbers: "))
find_number = int(input("what number you find: ")[0])
find_count = 0


for _ in range(count_elm):
    input_n = int(input())
    while input_n > 0:
       
        if input_n % 10 == find_number:
            find_count += 1
        
        input_n //= 10

print(find_count)

