"""Вам доступен текстовый файл population.txt с названиями стран и численностью их населения, разделенными символом табуляции '\t'.
Напишите программу выводящую все страны, название которых начинается с буквы 'G',
численность населения которых больше чем 500000 человек, не меняя их порядок."""

with open('population.txt') as f:
    country = f.readline()
    while country:
        name, pop = country.split('\t')
        if name[0] == 'G' and int(pop) > 500000:
            print(name)
        country = f.readline()
