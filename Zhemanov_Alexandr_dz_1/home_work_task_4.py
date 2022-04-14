#!/bin/env python3

# 4. Написать программу, которая генерирует в указанных пользователем границах:
#  случайное целое число;
#  случайное вещественное число;
#  случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы. Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

# что делать если ввести целое и вещественное (реализовал как ошибку, но можно преобразовать)

from time import time

# ф-ия для определения типа (float, int, char)
def get_type(var : str):
    # test float
    test_float = var.split('.')
    if len(test_float) == 2 and test_float[0].isnumeric() and test_float[1].isnumeric():
        return ('f', float(var))
    # test int
    if var.isnumeric():
        return ('i', int(var))
    # test char
    if len(var) == 1 and var.isalpha() and (97 <= ord(var) <= 122):
        return ('c', var)
    # Error
    raise ValueError(f"unknow type {var}")

start = get_type(input("input start. Support type(float, int, char): "))
end = get_type(input("input end: "))

# проверка на тип
if(start[0] != end[0]):
    raise ValueError(f"type({start[1]}) != type({end[1]})")

# что считать если начало и конец равны
if start[1] == end[1]:
    answ = start[1]
else:

    # сортировка с преобразование char -> int (если требуется)
    if(start[0] == 'c'):
        [b, e] = [ord(start[1]),ord(end[1])] if start[1] < end[1] else [ord(end[1]), ord(start[1])]
    else:
        [b, e] = [start[1], end[1]] if start[1] < end[1] else [end[1], start[1]]

    # генирация
    answ = b + time() % (e - b + 1)

    # обратное преобразование
    if start[0] == 'c':
        answ = chr(int(answ))
    elif start[0] == 'i':
        answ = int(answ)

print(answ)

