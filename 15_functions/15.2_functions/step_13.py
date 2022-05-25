"""Напишите функцию greet(), которая принимает произвольное количество аргументов строк имен (как минимум одно)
и возвращает приветствие в соответствии с образцом."""

def greet(name, *args):
    return f'Hello, {" and ".join((name,) + args)}!'





print(greet('Timur'))
print(greet('Timur', 'Roman'))
print(greet('Timur', 'Roman', 'Ruslan'))
