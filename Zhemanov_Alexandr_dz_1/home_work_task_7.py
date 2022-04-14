#!/bin/env python3
# 7. По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника, составленного из этих отрезков. Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным или равносторонним.

edge = [float(input(f"input {i + 1} edge: ")) for i in range(3)]

exist = (edge[0] + edge[1] > edge[2]) and \
        (edge[1] + edge[2] > edge[0]) and \
        (edge[0] + edge[2] > edge[1])

if exist:
    triangle = "разносторонний"
    if edge[0] == edge[1] and edge[1] == edge[2]:
        triangle = "равносторонний"
    elif edge[0] == edge[1] or edge[0] == edge[2] or edge[1] == edge[2]:
        triangle = "равнобедренный"
else:
    triangle = "не существует"

print("треугольник", triangle)

