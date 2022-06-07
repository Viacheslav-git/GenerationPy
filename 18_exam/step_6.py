"""На вход программе подается строка текста с именем текстового файла. Напишите программу,
выводящую на экран содержимое этого файла, но с заменой всех запрещенных слов звездочками *
(количество звездочек равно количеству букв в слове).
Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле forbidden_words.txt.
Гарантируется, что все слова в этом файле записаны в нижнем регистре."""

import re

with open('forbidden_words.txt') as f1, open('grades.txt') as f2:
    banned = f1.read().split()
    file = f2.read()


for i in banned:
    file = re.sub(i, '*' * len(i), file, flags=re.IGNORECASE)
print(file)

# with open(input()) as inp, open('forbidden_words.txt') as fw:
#     text, bad = inp.read(), fw.read().split()
#
# for i in bad:
#     text = re.sub(i, '*' * len(i), text, flags=re.IGNORECASE)
# print(text)
