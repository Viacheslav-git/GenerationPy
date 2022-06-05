"""Вам доступен CSV-файл data.csv, содержащий информацию в csv формате.
Напишите функцию read_csv для чтения данных из этого файла. Она должна возвращать список словарей,
интерпретируя первую строку как имена ключей, а каждую последующую строку как значения этих ключей."""


def read_csv():
    res = []
    with open('data.csv') as f:
        names = f.readline().strip().split(',')
        data = f.readline().strip()
        while data:
            res.append(dict(zip(names, data.split(','))))
            data = f.readline().strip()
    return res


print(read_csv())
