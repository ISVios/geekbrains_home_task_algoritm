#!/bin/env python3
# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

# "сколько между ними находится букв." => между 'a' и 'b' 0 букв, а для 'a' и 'a' -1 либо ошибка


# 1 вариант если ord доступен
# """
A_POS_fix = ord('a') - 1

pos_first = ord(input('input char: ')[0]) - A_POS_fix
print(f"position is {pos_first}")
pos_second = ord(input('input char: ')[0]) - A_POS_fix
print(f"position is {pos_second}")

if pos_first != pos_second:
    print(f"between {abs(pos_second - pos_first) - 1}")
else:
    print("the same leter")

# """

##############################
"""
# 2 вариант без ord

ALPHABET = "abcdefghijklmnopqrstuvwxyz" # const

begin = input('input char')[0]
end = input('input cahr')[0]

begin_pos = 0
end_pos = 0

for pos in range(len(ALPHABET)): # можно сразу написать 26
    if begin == ALPHABET[pos]:
        begin_pos = pos
    elif end == ALPHABET[pos]:
        end_pos = pos
print(f"position \'{begin}\'is {begin_pos}")
print(f"position \'{end}\'is {end_pos}")
print(abs(begin_pos - end_pos) - 1)

# """
