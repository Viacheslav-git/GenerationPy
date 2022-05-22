'''На вход программе подается натуральное число n.
Напишите программу, которая вычисляет и выводит рациональное число, равное значению выражения '''

from fractions import Fraction

n = 2  # int(input())
res = Fraction(0)
for i in range(1, n + 1):
    res += Fraction(1, i**2)
print(res)
