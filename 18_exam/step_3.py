"""Вам доступен текстовый файл grades.txt, содержащий оценки студента за три теста в каждом из триместров.
Строки файла имеют вид: фамилия оценка_1 оценка_2 оценка_3.
Напишите программу для подсчета количества студентов, сдавших все три теста. Тест считается сданным,
если количество баллов по нему не меньше 65."""

count = 0
with open('grades.txt') as file:
    student = file.readline()
    while student:
        grades = student.split()[1:]
        if len(list(filter(lambda x: int(x) >= 65, grades))) == 3:
            count += 1
        student = file.readline()
print(count)

