#!/bin/env python
#9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

# т.е поиск седловой точки ? (нет)

from random import randint

input_row_size = int(input("input count of row: "))
input_column_size = int(input("input count of column: "))

matrix = [] # array of array

for column_ind in range(input_column_size):

    row_matrix = []

    for row_ind in range(input_row_size):
        row_matrix.append(randint(-100, 100))

    matrix.append(row_matrix)

# start algorith

max_of_min_column = None

matrix_rows_size = len(matrix)
matrix_colums_size = len(matrix[0])

for colums_ind in range(matrix_colums_size):

    min_in_colum = matrix[0][colums_ind]

    for row_matrix in range(1, matrix_rows_size):
        curr_elem = matrix[row_matrix][colums_ind]

        if min_in_colum > curr_elem:
            min_in_colum = curr_elem

    if not max_of_min_column or max_of_min_column < min_in_colum:
        max_of_min_column = min_in_colum

print(matrix)
print(max_of_min_column)

