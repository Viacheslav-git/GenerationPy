"""Напишите функцию info_kwargs(), которая принимает произвольное количество именованных аргументов
и печатает именованные аргументы в соответствии с образцом: <имя аргумента>: <значение аргумента>,
при этом имена аргументов следуют в алфавитном порядке (по возрастанию)."""

def info_kwargs(**kwargs):
    for key, value in sorted(kwargs.items()):
        print(f'{key}: {value}')



info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher')
