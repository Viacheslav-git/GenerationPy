"""Напишите функцию concat(), принимающую переменное количество аргументов и объединяющую их в одну строку
через разделитель (sep). Если разделитель не задан, им служит пробел."""


def concat(*args, sep=' '):
    return sep.join(map(str, args))


print(concat('hello', 'python', 'and', 'stepik'))
print(concat('hello', 'python', 'and', 'stepik', sep='*'))
print(concat('hello', 'python', sep='()()()'))
print(concat('hello', sep='()'))
print(concat(1, 2, 3, 4, 5, 6, 7, 8, 9, sep='$$'))
