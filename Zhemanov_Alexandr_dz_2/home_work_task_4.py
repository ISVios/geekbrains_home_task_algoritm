#!/bin/env python3

# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.

# +1 -(1/2)=-0.25 (1/4)=0.25 -(1/8)=-0.125...(1/2^n)  or (1/2)^n * (-1)^(n+1)

to_n = int(input("input count of elemets of (1 -0.5 0.25 -0.125 .. n)"))
answ = 0

for i in range(to_n):
    answ +=  ((1/2)**i)  * (-1)**i 

print(f"sum = {answ}") # 0.666015625




# test in haskell
# f n = sum $ zipWith (*) ((1:) $ map (\x -> 1/2^x ) [1..n-1])$ take 10 $ concat $ repeat [1,-1]
# f 10 = 0.666015625
# or
# f n = sum $ [if rem x 2 == 0 then (1/2)^x else -(1/2)^x | x <- [0..n-1]] 
# f 10 = 0.666015625
# or
# f n = sum $ [(1/2)^x * (-1)^x | x <- [0..n-1]] 
# f 10 = 0.666015625

