'''На вход программе подается натуральное число nn.
Напишите программу, которая вычисляет и выводит рациональное число, равное значению выражения '''

from fractions import Fraction
from math import factorial

n = 5  # int(input())

print(sum([Fraction(1, factorial(i)) for i in range(1, n + 1)]))
