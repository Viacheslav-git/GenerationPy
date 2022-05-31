"""Учитель Тимур проверял контрольные работы по математике в нескольких классах онлайн-школы BEEGEEK
и решил убедиться, что в каждом классе есть хотя бы один отличник – ученик с оценкой 55 по контрольной работе.
Напишите программу с использованием встроенных функций all() для помощи Тимуру в проверке."""

students = []
for clas in range(int(input())):
    tmp = []
    for student in range(int(input())):
        tmp.append(int(input().split()[1]))
    students.append(tmp)
print(('NO', 'YES')[all((5 in x) for x in students)])
