#!/bin/env python3

# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
# что делать если pos > 26 (остаток от числа)
# что делать если pos <= 0

#"""
# 1 вариант с ord/chr

pos = int(input("input alphabet position: "))

ch = chr(ord('a') - 1 + pos % 26 ) if pos > 0 else chr(ord('z') - (abs(pos + 1) % 26))

print(f"{ch} in {pos} position")

# """
##############################


"""
# 2 вариант без ord/chr

ALPHABET = "abcdefghijklmnopqrstuvwxyz" # const
ALPHABET_LEN = len(ALPHABET) # or 26

pos = int(input("input alphabet position: "))

pos = ALPHABET_LEN - (abs(pos) % ALPHABET_LEN) if pos < 0 else (pos - 1) % ALPHABET_LEN

ch = ALPHABET[pos]

print(f"{ch} in {pos + 1} position")

# """
