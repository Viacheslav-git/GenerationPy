"""Вам доступен текстовый файл file.txt, набранный латиницей. Напишите программу,
которая выводит количество букв латинского алфавита, слов и строк.
Выведите три найденных числа в формате, приведенном в примере."""

with open('file.txt') as f:
    text = f.read()

lines = text.count('\n') + 1
words = len(text.split())
letters = len(list(filter(str.isalpha, text)))
print(f'''Input file contains:
{letters} letters
{words} words
{lines} lines''')







# Input file contains:
# 108 letters
# 20 words
# 4 lines

