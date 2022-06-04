"""Вам доступны два текстовых файла first_names.txt и last_names.txt, один с именами, другой с фамилиями.
Напишите программу, которая c помощью модуля random создает 33 случайные пары имя + фамилия, а затем выводит их,
каждую на отдельной строке."""
from random import choice
with open('first_names.txt') as f:
    names = f.readlines()

with open('last_names.txt') as f:
    last_names = f.readlines()

for _ in "___":
    print(choice(names).strip(), choice(last_names).strip())
