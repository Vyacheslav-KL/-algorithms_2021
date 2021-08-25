"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.

Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.

Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, / - ШАГ РЕКУРСИИ
- условие завершения рекурсии - введена операция 0 - БАЗОВЫЙ СЛУЧАЙ

Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def calculator():
    value = input('Please enter an operation "+" "-" "*" "/"\n'
                  'or "0" to exit and push "enter"\n')
    if value != '0':
        if value not in '+-*/' or value == '':
            print('You entered an invalid type try again\n')
            return calculator()
        try:
            first_num = float(input('Please enter first number'))
            second_num = float(input('Please enter second number'))
            if value == '+':
                print(f'Result: {first_num + second_num}')
                return calculator()
            if value == '-':
                print(f'Result: {first_num - second_num}')
                return calculator()
            if value == '*':
                print(f'Result: {first_num * second_num}')
                return calculator()
            if value == '/':
                try:
                    print(f'Result: {first_num / second_num}')
                except ZeroDivisionError:
                    print('Error: "ZeroDivisionError"\n')
                return calculator()
        except ValueError:
            print('Error: "You entered an invalid type try again"\n')
            return calculator()
    exit()


calculator()
