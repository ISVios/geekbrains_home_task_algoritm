#!/bin/env python
# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
#  Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
#  В конце следует вывести полученную матрицу.
#

"""
X X X X I
X X X X I
X X X X I
X X X X I
"""

ROW    = 4
COLUMN = 4
INPUT_SIZE = ROW * COLUMN

matrix = []
sum_row = 0

row = []
for ind in range(INPUT_SIZE):
        row_index = ind % ROW
        elem = int(input(f"input elem[{row_index}][{ind // COLUMN}]: "))
        row.append(elem)
        sum_row += elem
        if row_index == COLUMN - 1:
            row.append(sum_row)
            matrix.append(row)
            sum_row = 0
            row = []

print(matrix)
