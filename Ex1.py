# Напишите программу, которая принимает на вход вещественное число и
# показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

number = input('Enter any number: ')
sum_of_digits = 0
for i in number:
    if i not in {'.', ',', '-'}:
        sum_of_digits += int(i)
print()
print(f'The sum of the digits in {number} is {sum_of_digits}')