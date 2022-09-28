# Задайте список из n чисел последовательности (1+1/n)^n и выведите на
# экран их сумму.

n = int(input('Enter the quantity of numbers in list n: '))
sum = 0
number_of_sequence = 0
for i in range(1, n+1):
    number_of_sequence = (1 + 1/i)**i
    print(f'The {i} number of sequence is {round(number_of_sequence, 2)}')
    sum += (1 + 1/i)**i
print()
print(f'The sum of the numbers of the sequence (1+1/n)^n is {round(sum, 2)}')
