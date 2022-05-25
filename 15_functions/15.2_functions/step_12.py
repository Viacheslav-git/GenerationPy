"""Напишите функцию mean(), которая принимает произвольное количество аргументов
и возвращает среднее арифметическое переданных в нее числовых (int или float) аргументов."""

def mean(*args):
    lst = [c for c in args if type(c) in (int, float)]
    if len(lst):
        return sum(lst)/len(lst)
    else:
        return 0


print(mean())
print(mean(7))
print(mean(1.5, True, ['stepik'], 'beegeek', 2.5, (1, 2)))
print(mean(True, ['stepik'], 'beegeek', (1, 2)))
print(mean(-1, 2, 3, 10, ('5')))
print(mean(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
