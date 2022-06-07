"""На вход программе подается строка текста с именем текстового файла, в котором написан код на языке Python.
Напишите программу, выводящую на экран имена всех функций для которых отсутствует поясняющий комментарий. Будем считать,
что любая строка, начинающаяся со слова def и пробела, является началом определения функции.
Функция содержит комментарий, если первый символ предыдущей строки - #."""

with open('test.py') as f:
    file = f.readlines()
answer = []
for i in range(len(file)):
    if 'def ' in file[i]:
        if i and file[i-1][0] == '#':
            continue
        else:
            fun = file[i].lstrip('def')
            answer.append(fun[:fun.index('(')].strip())

print(*answer if answer else ['Best Programming Team'], sep='\n', end='')
