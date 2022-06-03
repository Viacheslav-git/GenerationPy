"""Вам доступен текстовый файл lines.txt, в котором записаны строки текста. Напишите программу,
которая выводит все строки наибольшей длины из файла, не меняя их порядок."""
with open('lines.txt') as f:
    lines = f.readlines()
lines.sort(key=len)
bigest = filter(lambda line: len(lines[-1]) == len(line), lines)
print(*bigest, sep='')
