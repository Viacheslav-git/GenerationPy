"""Вам доступен текстовый файл ledger.txt с данными о продажах фирмы за месяц. На каждой строке файла указано,
сколько клиент заплатил за товар, в долларах"""
# something
from functools import reduce
with open('ledger.txt') as file:
    money = reduce(lambda a, b: a + int(b.strip('$\n')), file.readlines(), 0)
print('$', money, sep='')
