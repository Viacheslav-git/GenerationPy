'''Юный математик
На вход программе подается натуральное число n.
Напишите программу, которая находит наибольшую правильную несократимую дробь с суммой числителя и знаменателя равной n.'''

from fractions import Fraction

n = 23  # int(input())
l = []
for i in range(1, (n+1)//2):
    num = Fraction(i, n - i)
    if num.numerator + num.denominator == n:
        l.append(num)
print(max(l))
