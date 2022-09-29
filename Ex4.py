# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся
# в файле file.txt в одной строке одно число.

from random import randint

n = int(input('Enter the quantity of numbers in list N: '))
list = []
for i in range(n):
    list.append(randint(-n, n))
print(list)
print()
multiplication = 1

with open('file.txt', 'r') as f:
    for string in f:
        multiplication *= list[int(string) - 1]
print(f'The multiplication equals to {multiplication}')
f.close()