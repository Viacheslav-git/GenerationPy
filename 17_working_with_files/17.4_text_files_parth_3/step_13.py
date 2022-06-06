"""На вход программе подается натуральное число nn и nn строк с названиями файлов. Напишите программу,
которая создает файл output.txt и выводит в него содержимое всех файлов с указанными именами, не меняя их порядка."""

with open('output.txt', 'a') as out:
    for _ in range(int(input())):
        with open(input()) as file:
            out.write(file.read())
