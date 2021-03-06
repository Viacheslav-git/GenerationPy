"""Для вычисления гематрии слова в этой задаче:

1. переведём слово в верхний регистр;
2. числовое значение буквы вычислим как код(буквы) - код(буквы A).
На вход программе подается натуральное число nn, а затем nn строк английских слов в разных регистрах.

Напишите программу, которая выводит слова в начальном регистре (каждое на отдельной строке) в порядке возрастания
их гематрии. Если гематрия слов совпадает, они выводятся в алфавитном (лексикографическом) порядке."""

import functools as f


def gematria(word):
    return f.reduce(lambda x, y: x + ord(y) - ord('A'), word.upper(), 0)


n = int(input())
words = [input() for _ in range(n)]
print(*sorted(words, key=lambda x: (gematria(x), x)), sep = '\n')
