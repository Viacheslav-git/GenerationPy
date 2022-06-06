"""Вам доступен текстовый файл goats.txt в первой строке которого написано слово COLOURS,
далее идет список всех возможных цветов козлов. Затем идет строка со словом GOATS,
и далее непосредственно перечисление козлов разных цветов. Перечень козлов включает только строки из первого списка.
Напишите программу создания файла answer.txt и вывода в него списка козлов,
которые удовлетворяют условию загадки от Жака Фреско ( > 7%)."""


with open('goats.txt') as goats:
    temp = [s.strip() for s in goats]


text = temp[temp.index('GOATS') + 1:]
d = {}
for c in text:
    d[c] = d.get(c, 0) + 1

answer = []
for key, value in d.items():
    if value >= sum(d.values())*0.07:
        answer.append(key)

with open('answer.txt', 'w') as out:
    print(*sorted(answer), file=out, sep='\n', end='')
