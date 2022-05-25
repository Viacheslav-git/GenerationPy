"""Напишите функцию print_products(), которая принимает произвольное количество аргументов и выводит список продуктов
(любая непустая строка) по образцу: <номер продукта>) <название продукта> (нумерация продуктов начинается с единицы).
Если среди переданных аргументов нет ни одного продукта, необходимо вывести текст Нет продуктов."""


# def print_products(*args):
#     products = [product for product in args if product and type(product) is str]
#     lst = []
#     for i in range(len(products)):
#         lst.append(str(i+1) + ') ' + products[i])
#     print(*lst if lst else ['Нет продуктов'], sep='\n')

def print_products(*args):
    products = [i for i in args if type(i) == str and i]
    if products:
        for i in range(len(products)):
            print(f'{i+1}) {products[i]}')
    else:
        print('Нет продуктов')



print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)
print_products([4], {}, 1, 2, {'Beegeek'}, '')
