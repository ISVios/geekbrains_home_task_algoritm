#!/bin/env python3

# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем.
# После выполнения вычисления программа не должна завершаться, а должна запрашивать новые данные для вычислений.
# Завершение программы должно выполняться при вводе символа '0' в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
#   то программа должна сообщать ему об ошибке и снова запрашивать знак операции.
# Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.

# BNF = VAR OP VAR
# VAR = [-] FLOAT_OR_INT
# OP  = "+" | "-" | "*" | "/" | "0"

# как считыать значение по одному или парсит строку ? по одному

OPERATOR = '+-*/0' # 0 - exist
oper = " "

while True:
    first_num = float(input("input first number: "))
    while True:
        oper = input("input command: ")[0]
        if not oper in OPERATOR:
            print("please input support command (+, -, *, /, and 0 for exit)")
        else:
            break

    if oper == '0':
        break
    second_num = float(input("input second number: "))

    if(second_num == 0 and oper == '/'):
        print("Здесь на ноль делить нельзя.\n")
    else:
        if oper == '+':
            res = first_num + second_num
        elif oper == '-':
            res = first_num - second_num
        elif oper == '*':
            res = first_num * second_num
        elif oper == '/':
            res = first_num / second_num

        print(f"{first_num} {oper} {second_num} = {res}\n")
