# Задайте список из n чисел последовательности (1+1/n)^n и выведите на
# экран их сумму.

n = int(input('Enter the quantity of numbers in list n: '))
sum = 0
j = 0
for i in range(1, n+1):
    j = (1 + 1/i)**i
    print(round(j, 2))
    sum += (1 + 1/i)**i
print()
print(f'The sum of the numbers of the sequence (1+1/n)^n is {round(sum, 2)}')
