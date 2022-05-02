#!/bin/env python3

from collections import deque
"""
# 1 вариант (не честный)

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

# 2 вариант
from numpy import prod


NUM_BASE = ["0", "1" , "2", "3", "4", "5", "6", "7", "8", "9"] #, "A", "B", "C", "D", "E", "F"]
BASE_LEN = len(NUM_BASE)

################################################################################
def num_hex_sum(*nums):
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
    if num < BASE_LEN:
        return NUM_BASE[num]
    return [(int_to_hex(num // BASE_LEN))] + [(NUM_BASE[num % BASE_LEN])]

################################################################################
def hex_sum(first : deque, second : deque):
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
    answ = deque()

    if len(fist) < len(second):
        tmp_f, tmp_s = second.copy(), fist.copy()
    else:
        tmp_f, tmp_s = fist.copy(), second.copy()
    
    over = deque("0")
    pre_sum = deque()
   
    tmp_f.reverse()
    tmp_s.reverse()

    for i,f_num in enumerate(tmp_f):
        pre_sum.append(deque())
        for s_num in tmp_s:
            
            raw_prod = hex_sum(over, deque(num_hex_prod(f_num, s_num)))
            print(raw_prod[0], raw_prod[1], over)
            over = hex_sum( deque(raw_prod[0]), over)
            answ.appendleft(raw_prod[1])
    
    return answ
################################################################################
def hex_crazy_prod(fist:deque, second: deque):
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

