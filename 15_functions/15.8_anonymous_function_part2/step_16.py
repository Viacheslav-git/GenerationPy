"""На вход программе на первой строке подаются коэффициенты многочлена, разделенные символом пробела и целое число x
на второй строке. Напишите программу, которая вычисляет значение указанного многочлена при заданном значении x."""
from functools import reduce

def evaluate(coefficients, x):
    terms = map(lambda a, b, p: b**p * int(a), coefficients, [x]*len(coefficients), list(range(len(coefficients))[::-1]))
    return reduce(lambda a, b: a+b, terms)


print(evaluate('2 4 3'.split(), 10))
