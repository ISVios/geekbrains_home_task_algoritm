#!/bin/env python3

from collections import deque

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
