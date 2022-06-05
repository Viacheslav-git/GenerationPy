"""Вам доступен текстовый файл class_scores.txt с оценками за итоговый тест на строках вида: фамилия оценка
(фамилия и оценка разделены пробелом). Оценка - целое число от 00 до 100100 включительно.
Напишите программу для добавления 5 баллов к каждому результату теста и вывода фамилий
и новых результатов тестов в файл new_scores.txt."""

with open('class_scores.txt') as old, open('new_scores.txt', 'w') as new:
    for student in old.readlines():
        name, score = student.split()
        num = min(100, int(score) + 5)
        new.write(f'{name} {num}\n')
