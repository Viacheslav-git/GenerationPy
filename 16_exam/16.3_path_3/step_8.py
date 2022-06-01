"""Напишите функцию arithmetic_operation(), которая принимает символ одной из четырех операций (+, -, *, /)
и возвращает функцию двух аргументов для соответствующей операции."""
from operator import add, truediv, sub, mul


def arithmetic_operation(operation):
    def func(x, y):
        return eval(f'x {operation} y')
    return func


add = arithmetic_operation('+')
div = arithmetic_operation('/')
print(add(10, 20))
print(div(20, 5))
