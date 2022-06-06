"""Вам доступен текстовый файл logfile.txt с информацией о времени входа пользователя в систему и выхода из нее.
Каждая строка файла содержит три значения, разделенные запятыми и символом пробела: имя пользователя, время входа,
время выхода, где время указано в 24-часовом формате.
Напишите программу, которая создает файл output.txt и выводит в него имена всех пользователей
(не меняя порядка следования), которые были в сети не менее часа."""


def minutes(time):
    return int(time.split(':')[0]) * 60 + int(time.split(':')[1])


with open('logfile.txt') as file, open('output.txt', 'w') as out:
    user = file.readline()
    while user:
        name, time1, time2 = user.split(', ')
        if minutes(time2) - minutes(time1) >= 60:
            print(name, file=out)
        user = file.readline()
