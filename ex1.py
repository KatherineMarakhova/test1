""" 1. Напишите на любом языке программирования программу,
    печатающую в стандартный вывод все простые числа,
    не превосходящие заданного числа
"""
from math import sqrt

n = int(input())

if n<2:
    print('There are no prime numbers')

else:
    lst=[]
    for i in range(2, n+1):
        for j in lst:
            if j > int((sqrt(i)) + 1):
                lst.append(i)
                break
            if (i % j == 0): # непростое число будет обязательно делиться на простое
                break
        else:
            lst.append(i)
    print(lst)
