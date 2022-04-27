#!/bin/env python3

# 3. По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b, проходящей через эти точки.

coords = [] # x1 -> 0 | y1 -> 1 | x2 -> 2 | y2 -> 3

for i in range(4):
    print(f"введите координату {'x' if i % 2 == 0 else 'y'} {'первой' if i < 2 else 'второй'} точки")
    coords.append(float(input()))

x1_min_x2 = coords[0] - coords[2]

if x1_min_x2 == 0:
    raise ValueError

k = (coords[1] - coords[3]) / x1_min_x2
b = coords[3] - k * coords[2]
res = f"y = {k:.3f}x + {b:.3f}"

print(f"уравнение прямой {res}")


