"""Вам доступен текстовый файл prices.txt с информацией о заказе из интернет магазина.
В нем каждая строка с помощью символа табуляции (\t) разделена на три колонки:"""


from functools import reduce


with open('prices.txt') as f:
    cost = list(map(lambda line: line.split()[1:], f))
print(reduce(lambda a, b: a + int(b[0]) * int(b[1]), cost, 0))

