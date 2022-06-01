"""Напишите функцию pretty_print(), которая выводит содержимое списка с рамкой. """


def pretty_print(data, side='-', delimiter='|'):
    body = f' {delimiter} '.join(map(str, data))
    print('', side * (len(body)+2)+'\n'+delimiter, body, delimiter+'\n', side * (len(body)+2))



pretty_print([1, 2, 10, 23, 123, 3000])
pretty_print(['abc', 'def', 'ghi', '12345'])
pretty_print(['abc', 'def', 'ghi'], side='*')
pretty_print(['abc', 'def', 'ghi'], delimiter='#')
pretty_print(['abc', 'def', 'ghi'], side='*', delimiter='#')
