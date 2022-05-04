#!/bin/env python3

from collections import deque
"""
# 1 вариант (нечестный)

class HexNum:
    __value:deque

    def __init__(self, input_str:str):
        self.__value = deque(input_str)

    def __dec(self):
        return int("".join(list(self.__value)), 16)

    def __add__(self, oth):
        return HexNum(hex(self.__dec() + oth.__dec()).upper()[2:])

    def __mul__(self, oth):
        return HexNum(hex(self.__dec() * oth.__dec()).upper()[2:])

    def __str__(self) -> str:
        return f"{list(self.__value)}"




f_num = HexNum(input("input first number in hex: ").upper())
s_num = HexNum(input("input second number in hex: ").upper())

print(f_num)
print(s_num)
print()
print("sum is ", f_num + s_num)
print("prod is ", f_num * s_num)

# """

#"""
# 2 вариант

# Данный метод решение работает на hex bin dec oct. Достаточно "оградить" NUM_BASE до нужной системы
# hex -> полный список
# oct -> 0 .. 8
# dec -> 0 .. 9
# bin -> 0 and 1

NUM_BASE = ["0", "1" , "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
BASE_LEN = len(NUM_BASE)

################################################################################
def num_hex_sum(*nums):
    # сложение единичных эленентов 
    raw_sum = sum(map(NUM_BASE.index, nums))
    answ = []
    norm = raw_sum % BASE_LEN
    
    over = raw_sum // BASE_LEN
    if over > 0 and over < BASE_LEN:
        answ.append(NUM_BASE[over])
    elif over > BASE_LEN:
        over = int_to_hex(over)
        answ.extend(over)
    
    answ.append(NUM_BASE[norm])
    
    return answ
################################################################################
def num_hex_prod(*nums):
    # умножение единичных эленентов 
    raw_prod = 1
    for number in nums:
        raw_prod *= NUM_BASE.index(number) 

    answ = []
    norm = raw_prod % BASE_LEN
    
    over = raw_prod // BASE_LEN
    if over > 0 and over < BASE_LEN:
        answ.append(NUM_BASE[over])
    elif over > BASE_LEN:
        over = int_to_hex(over)
        answ = over + answ
    
    answ.append(NUM_BASE[norm])
    
    return answ
################################################################################
def int_to_hex(num:int) -> list:
    # перевод числа в NUM_BASE основание
    if num < BASE_LEN:
        return NUM_BASE[num]
    return [(int_to_hex(num // BASE_LEN))] + [(NUM_BASE[num % BASE_LEN])]

################################################################################
def hex_sum(first : deque, second : deque):
    # сложение двух чисел
    over = ["0"]
    answ = deque()
    tmp_first = first.copy()
    tmp_second = second.copy()
    for _ in range(max(len(first), len(second))):

        fst_num = tmp_first.pop() if tmp_first else "0"
        snd_num = tmp_second.pop() if tmp_second else "0"
        
        
        if over == ["0"]:
            raw_sum = num_hex_sum(fst_num, snd_num)
        else:
            raw_sum = num_hex_sum(fst_num, snd_num, over.pop())
        
        if len(raw_sum) > 1:
            over = raw_sum[:-1]
        else:
            over = ["0"]
        
        answ.appendleft(raw_sum[-1])
    
    if over and over != ["0"]:
        answ.extendleft(over)
    return answ
################################################################################
def hex_prod(fist : deque, second : deque):
    # умножение двух чисел
    answ = deque("0")

    if len(fist) < len(second):
        tmp_f, tmp_s = second.copy(), fist.copy()
    else:
        tmp_f, tmp_s = fist.copy(), second.copy()
   
    tmp_f.reverse()
    tmp_s.reverse()

    row_sum = deque("0")
    for prod_offset, f_num in enumerate(tmp_f):
        row_sum = deque("0")

        for row_offset,s_num in enumerate(tmp_s):
            
            tmp_prod = num_hex_prod(f_num, s_num)
            tmp_prod.extend("0" * row_offset)
            row_sum = hex_sum(row_sum, deque(tmp_prod))

            #print(f_num, "*", s_num,  tmp_prod, row_sum)
       
        row_sum.extend("0" * prod_offset)
        answ = hex_sum(row_sum, answ)     

    return answ
################################################################################
def hex_crazy_prod(fist:deque, second: deque):
    # реализация умножение через многократное сложение
    if len(fist) < len(second):
        step = second
        end = fist
    else:
        step = fist
        end = second

    start = deque("0")
    prod = deque("0")
    while start != end:
        start = hex_sum(start, deque("1"))
        prod = hex_sum(prod, step)

    return prod
################################################################################

first = deque(input("input first number in hex: ").upper())
second = deque(input("input second number in hex: ").upper())

first_lst = list(first)
second_lst = list(second)

print(first_lst, "+", second_lst, "=", list(hex_sum(first, second)))
print(first_lst, "*", second_lst, "=", list(hex_prod(first, second)))
print(first_lst, "*", second_lst, "=", list(hex_crazy_prod(first, second)))

# """
