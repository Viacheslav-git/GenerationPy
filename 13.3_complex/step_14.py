"""Сопряженные числа"""

n, z1, z2 = 1, 2+3j, 1+4j  # int(input()), complex(input()), complex(input())
result = z1**n + z2**n + z1.conjugate()**n + z2.conjugate()**(n+1)
print(result)
