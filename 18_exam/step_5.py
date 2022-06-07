"""На вход программе подается строка текста с именем текстового файла. Напишите программу,
выводящую на экран последние 1010 строк данного файла."""

with open('ledger.txt') as file:
    a,b,c,d,e,f,g,h,i,j = [file.readline() for _ in range(10)]
    last = file.readline()
    while last:
        a,b,c,d,e,f,g,h,i,j = b,c,d,e,f,g,h,i,j, last
        last = file.readline()

print(a,b,c,d,e,f,g,h,i,j, sep='', end='')
