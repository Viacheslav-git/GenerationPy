""" Операции над дробями
Даны две дроби в формате a/b.
Напишите программу, которая вычисляет и выводит их сумму, разность, произведение и частное."""

from fractions import Fraction as F

a, b = '2/3', '3/7'  # input(), input()
print(f'{a} + {b} = {F(a) + F(b)}')
print(f'{a} - {b} = {F(a) - F(b)}')
print(f'{a} * {b} = {F(a) * F(b)}')
print(f'{a} / {b} = {F(a) / F(b)}')



