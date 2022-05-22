"""Упорядоченные дроби
На вход программе подается натуральное число n.
Напишите программу, которая выводит в порядке возрастания все несократимые дроби, заключённые между 0 и 1,
знаменатель которых не превосходит n."""

from fractions import Fraction

n = 3  # int(input())
res = set()
for i in range(1, n):
    for j in range(i + 1, n + 1):
        res.add(Fraction(i, j))
print(*sorted(res), sep='\n')
