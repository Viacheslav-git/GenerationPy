"""Вам доступен текстовый файл words.txt со словами, разделенными пробелом. Напишите программу,
которая находит и выводит самые длинные слова этого файла, не меняя порядка их следования."""

with open('words.txt') as file:
    words = file.read().split()
biggest = len(max(words, key=len))
print(*filter(lambda x: biggest == len(x), words), sep='\n')
