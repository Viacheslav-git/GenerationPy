"""Напишите функцию matrix(), которая создает, заполняет и возвращает матрицу заданного размера.
При этом (в зависимости от переданных аргументов) она должна вести себя так:"""

def matrix(n=1, m=None, value=0):
    if m is None:
        m = n
    return [[value for _ in range(m)] for __ in range(n)]

print(matrix(3))
