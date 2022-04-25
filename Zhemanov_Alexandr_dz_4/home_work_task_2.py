#!/bin/env python3
# 2. Написать два алгоритма нахождения i-го по счёту простого числа.

import timeit

#  ● Без использования Решета Эратосфена;

"""
find_i = int(input("input index of number you find (0,1,2...n): "))

lst = [2]

test_num = 3

norm = True

time = timeit.timeit()

# не понимаю ка считать сложность(не помню)
while find_i > len(lst):         # 1 .. N
    for elem in lst:               # 1 .. M
        if test_num % elem == 0:     # 3
            norm = False               # 1
            break                      # 1

    if norm:                        # 1
        lst.append(test_num)        # 2

    norm = True                    # 1
    test_num += 1                  # 1

print("time: ", abs(timeit.timeit() - time))

print(lst)
print(lst[-1])



# """
#"""
#  ● Использовать алгоритм решето Эратосфена O(n * log( log(n) ))

k = int(input("input index of number you find (0,1,2...n): "))

time = timeit.timeit()

if k == 1:
    print(2)
    exit()
 
a = k * 17
prime = [True] * (a + 1)
prime[0] = prime[1] = False
for i in range(2, a + 1):
    if not prime[i]:
        continue
    for j in range(i * i, a + 1, i):
        prime[j] = False
 
count = 0
for i in range(a):
    if prime[i]:
        count += 1
    if count == k:
        print(i)
        break
        
print()
print(f"time: ", abs(timeit.timeit() - time))

#"""
