# Реализуйте алгоритм перемешивания списка.

from random import randint

n = int(input('Enter the quantity of numbers in list N: '))
list = []
for i in range(n):
    list.append(randint(-100, 100))
print(list)
print()

for i in range(len(list)):
    random_index = randint(0, len(list) - 1)
    temp = list[i]
    list[i] = list[random_index]
    list[random_index] = temp
print(list)